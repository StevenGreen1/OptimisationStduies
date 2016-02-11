# Example to submit Marlin job: MarlinExample.py
import os
import sys

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from ILCDIRAC.Interfaces.API.DiracILC import  DiracILC
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import *
from ILCDIRAC.Interfaces.API.NewInterface.Applications import *

from XmlGenerationLogic import * 

### ----------------------------------------------------------------------------------------------------
### Start of getSlcioFiles function
### ----------------------------------------------------------------------------------------------------

def getSlcioFiles(jobDescription, detModel, energy, eventType):
    slcioFiles = []
    os.system('dirac-ilc-find-in-FC /ilc JobDescription=' + jobDescription + ' Type=Sim_PhotonLikelihoodTraining MokkaJobNumber=' + str(detModel) + ' Energy=' + str(energy) + ' EvtType=' + eventType + ' > tmp.txt')
    with open('tmp.txt') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            line = line.strip()
            slcioFiles.append(line)
    os.system('rm tmp.txt')
    return slcioFiles

### ----------------------------------------------------------------------------------------------------
### End of getSlcioFiles function
### ----------------------------------------------------------------------------------------------------
### Start of ECal detector information
### ----------------------------------------------------------------------------------------------------

numberECalLayersDict = {}

for detModel in range(1,96):
    numberECalLayersDict[detModel] = 30

numberECalLayersDict[96] = 30
numberECalLayersDict[97] = 26
numberECalLayersDict[98] = 20
numberECalLayersDict[99] = 16
numberECalLayersDict[100] = 30
numberECalLayersDict[101] = 26
numberECalLayersDict[102] = 20
numberECalLayersDict[103] = 16

### ----------------------------------------------------------------------------------------------------
### End of ECal detector information
### ----------------------------------------------------------------------------------------------------

#===== User Input =====

jobDescription = 'OptimisationStudies'
detModel = sys.argv[1] 
recoVar = sys.argv[2]

eventsToSimulate = [ { 'EventType': "Z_uds", 'Energies': [500] } ]

pandoraSettingsFile = 'PandoraSettingsDefaultForTraining.xml' 

#===== Second level user input =====

gearFile = '/r04/lc/sg568/HCAL_Optimisation_Studies/GridSandboxes/GJN' + str(detModel) + '_OutputSandbox/ILD_o1_v06_Detector_Model_' + str(detModel) + '.gear'
calibConfigFile = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudies/PhotonLikelihoodTraining/CalibrationInfo/CalibrationConfigMuon/CalibConfig_DetModel' + str(detModel) + '_RecoStage' + str(recoVar) + '.py'

#===== Begin =====

# Edit Pandora Settings File
numberECalLayers = numberECalLayersDict[(int)(detModel)] 
photonLikelihoodFileName = 'PandoraLikelihoodData_DetModel_' + str(detModel) + '_RecoStage_' + str(recoVar) + '.xml'

os.system('cp PandoraSettings/' + pandoraSettingsFile + ' .')

pandoraBase = open(pandoraSettingsFile,'r')
pandoraContentBase = pandoraBase.read()
pandoraBase.close()

pandoraContent = re.sub('NumberOfECalLayers',str(numberECalLayers),pandoraContentBase)
pandoraContent = re.sub('PandoraPhotonLikelihoodDataFileName',photonLikelihoodFileName,pandoraContent)

pandoraActive = open(pandoraSettingsFile,'w')
pandoraActive.write(pandoraContent)
pandoraActive.close()

# Copy gear file to local directory
os.system('cp ' + gearFile + ' .')
gearFileLocal = os.path.basename(gearFile)

# Start submission
JobIdentificationString = jobDescription + '_Detector_Model_' + str(detModel) + '_Reco_' + str(recoVar)
diracInstance = DiracILC(withRepo=True,repoLocation="%s.cfg" %( JobIdentificationString))

for eventSelection in eventsToSimulate:
    eventType = eventSelection['EventType']
    for energy in eventSelection['Energies']:
        slcioFilesToProcess = getSlcioFiles(jobDescription,detModel,energy,eventType)
        slcioFilesInputSteeringFileString = ''
        slcioFilesGridFilesString = []

        for slcioFile in slcioFilesToProcess:
            slcioFileNoPath = os.path.basename(slcioFile)
            slcioFilesInputSteeringFileString += slcioFileNoPath + '\n'
            slcioFilesGridFilesString.append('lfn:' + slcioFile)

        print 'Submitting ' + eventType + ' ' + str(energy) + 'GeV jobs.  Detector model ' + str(detModel) + '.  Reconstruction stage ' + str(recoVar) + '.'  
        xmlGeneration = XmlGeneration(calibConfigFile,'Si',True,pandoraSettingsFile,gearFileLocal,slcioFilesInputSteeringFileString)
        xmlTemplate = xmlGeneration.produceXml()

        with open("MarlinSteering.steer" ,"w") as SteeringFile:
            SteeringFile.write(xmlTemplate)

        ma = Marlin()
        ma.setVersion('ILCSoft-01-17-07')
        ma.setSteeringFile('MarlinSteering.steer')
        ma.setGearFile(gearFileLocal)
        ma.setInputFile(slcioFilesGridFilesString)

        outputFiles = []
        outputFiles.append(photonLikelihoodFileName)

        inputSandbox = [pandoraSettingsFile]
        job = UserJob()
        job.setJobGroup(jobDescription)
        job.setInputSandbox(inputSandbox) # Local files
        job.setOutputSandbox(['*.log','*.gear','*.mac','*.steer'])
        job.setOutputData(outputFiles,OutputPath='/' + jobDescription + '/TrainingPhotonLikelihoodData/Detector_Model_' + str(detModel) + '/Reco_Stage_' + str(recoVar) + '/' + eventType + '/' + str(energy) + 'GeV') # On grid
        job.setName(jobDescription + '_Detector_Model_' + str(detModel) + '_Reco_' + str(recoVar))
        job.setBannedSites(['LCG.IN2P3-CC.fr','LCG.IN2P3-IRES.fr','LCG.KEK.jp','OSG.PNNL.us'])
        job.dontPromptMe()
        res = job.append(ma)

        if not res['OK']:
            print res['Message']
            exit()
        job.submit(diracInstance)
        os.system('rm *.cfg')

# Tidy Up
os.system('rm MarlinSteering.steer')
os.system('rm ' + pandoraSettingsFile)
os.system('rm ' + gearFileLocal)
