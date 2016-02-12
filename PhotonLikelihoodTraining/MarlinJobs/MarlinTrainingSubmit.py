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
        slcioFilesString = ''
        slcioFilesGridFilesString = []

        for slcioFile in slcioFilesToProcess:
            slcioFileNoPath = os.path.basename(slcioFile)
            slcioFilesString += slcioFileNoPath + '\n'
            slcioFilesGridFilesString.append('lfn:' + slcioFile)

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
