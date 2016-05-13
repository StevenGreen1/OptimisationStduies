# Example to submit Marlin job: MarlinExample.py
import os
import sys

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from ILCDIRAC.Interfaces.API.DiracILC import  DiracILC
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import *
from ILCDIRAC.Interfaces.API.NewInterface.Applications import *

from Logic.XmlGenerationLogic import * 
from Logic.DiracTools import *
from Logic.DetectorInfo import *

#===== User Input =====

jobDescription = 'OptimisationStudies_ECalStudies'
detModel = int(sys.argv[1])
recoVar = int(sys.argv[2])

eventsToSimulate = [ { 'EventType': "Z_uds", 'Energies': [500] } ]

pandoraSettingsFile = '../../PandoraSettings/PandoraSettingsDefaultForTraining.xml' 

#===== Second level user input =====

gearFile = '/r04/lc/sg568/HCAL_Optimisation_Studies/GridSandboxes/GJN' + str(detModel) + '_OutputSandbox/ILD_o1_v06_Detector_Model_' + str(detModel) + '.gear'
calibConfigFile = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudies/Calibration/CalibConfigFiles/MuonCalibration/CalibConfig_DetModel' + str(detModel) + '_RecoStage' + str(recoVar) + '.py'

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

# Tidy Up?
idyUp = True

# Start submission
JobIdentificationString = jobDescription + '_Detector_Model_' + str(detModel) + '_Reco_' + str(recoVar)
diracInstance = DiracILC(withRepo=True,repoLocation="%s.cfg" %( JobIdentificationString))

for eventSelection in eventsToSimulate:
    eventType = eventSelection['EventType']
    for energy in eventSelection['Energies']:
        outputPath = '/' + jobDescription + '/TrainingPhotonLikelihoodData/Detector_Model_' + str(detModel) + '/Reco_Stage_' + str(recoVar) + '/' + eventType + '/' + str(energy) + 'GeV'
        outputFiles = []
        outputFiles.append(photonLikelihoodFileName)

        lfn = '/ilc/user/s/sgreen/' + outputPath + '/' + outputFiles[0]
        if doesFileExist(lfn):
            tidyUp = False
            continue

        slcioFilesToProcess = getSlcioFiles(jobDescription,detModel,energy,eventType)
        slcioFilesToProcess = slcioFilesToProcess[:15] # Photons trained on 3000 zuds events, each file has 200 events
        slcioFilesString = ''
        slcioFilesGridFilesString = []
        inputDataString = []

        for slcioFile in slcioFilesToProcess:
            slcioFileNoPath = os.path.basename(slcioFile)
            slcioFilesString += slcioFileNoPath + '\n'
            slcioFilesGridFilesString.append('lfn:' + slcioFile)
            inputDataString.append(slcioFile)

        print 'Submitting ' + eventType + ' ' + str(energy) + 'GeV jobs.  Detector model ' + str(detModel) + '.  Reconstruction stage ' + str(recoVar) + '.'  
        xmlGeneration = XmlGeneration(calibConfigFile,ecalAbsMatType[detModel],realisticDigi[recoVar],pandoraSettingsFile,gearFileLocal,slcioFilesString)
        xmlTemplate = xmlGeneration.produceXml()

        with open("MarlinSteering.steer" ,"w") as SteeringFile:
            SteeringFile.write(xmlTemplate)

        ma = Marlin()
        ma.setVersion('ILCSoft-01-17-07')
        ma.setSteeringFile('MarlinSteering.steer')
        ma.setGearFile(gearFileLocal)
        ma.setInputFile(slcioFilesGridFilesString)

        inputSandbox = [pandoraSettingsFile]
        job = UserJob()
        job.setJobGroup(jobDescription)
        job.setInputSandbox(inputSandbox) # Local files
        job.setInputData(inputDataString)
        job.setOutputSandbox(['*.log','*.gear','*.mac','*.steer'])
        job.setOutputData(outputFiles,OutputPath=outputPath) # On grid
        job.setName(jobDescription + '_Detector_Model_' + str(detModel) + '_Reco_' + str(recoVar))
        job.setBannedSites(['LCG.IN2P3-CC.fr','LCG.IN2P3-IRES.fr','LCG.KEK.jp','OSG.PNNL.us','OSG.CIT.us'])
        job.dontPromptMe()
        res = job.append(ma)

        if not res['OK']:
            print res['Message']
            exit()
        job.submit(diracInstance)
        os.system('rm *.cfg')

# Tidy Up
if tidyUp:
    os.system('rm MarlinSteering.steer')

os.system('rm ' + pandoraSettingsFile)
os.system('rm ' + gearFileLocal)
