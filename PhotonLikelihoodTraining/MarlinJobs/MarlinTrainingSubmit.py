# Example to submit Marlin job: MarlinExample.py
import os
import sys

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from ILCDIRAC.Interfaces.API.DiracILC import  DiracILC
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import *
from ILCDIRAC.Interfaces.API.NewInterface.Applications import *

from MarlinTrainingGridJobs import *

#===== User Input =====

jobDescription = 'OptimisationStudies'
detModel = sys.argv[1] 
recoVar = sys.argv[2]
templateNumber = sys.argv[3]

eventsToSimulate = [ { 'EventType': "Z_uds", 'Energies': [500] } ]

baseXmlFile = 'TemplateRepository/MarlinSteeringFileTemplate_Jets_' + str(templateNumber) + '.xml'

# Notes: 
# Turned off the slcio output processor to speed up job processing in xml file.

pandoraSettingsFiles = {}
pandoraSettingsFiles['Active'] = 'PandoraSettingsActive.xml' 

#===== Second level user input =====
# If using naming scheme doesn't need changing 

gearFile = '/r04/lc/sg568/HCAL_Optimisation_Studies/GridSandboxes/GJN' + str(detModel) + '_OutputSandbox/ILD_o1_v06_Detector_Model_' + str(detModel) + '.gear'
calibConfigFile = '/r04/lc/sg568/HCAL_Optimisation_Studies/CalibrationResults/Detector_Model_' + str(detModel) + '/Reco_Stage_' + str(recoVar) + '/CalibConfig_DetModel' + str(detModel) + '_RecoStage' + str(recoVar) + '.py'

# Edit pandora settings file used for training

numberECalLayers = numberECalLayersDict[(int)(detModel)] 
photonLikelihoodFileName = 'PandoraLikelihoodData_DetModel_' + str(detModel) + '_RecoStage_' + str(recoVar) + '.xml'
generatePandoraSettingsActive(photonLikelihoodFileName,numberECalLayers)

#=====

# Copy gear file and pandora settings files to local directory as is needed for submission.
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
        marlinSteeringTemplate = ''
        marlinSteeringTemplate = getMarlinSteeringFileTemplate(baseXmlFile,calibConfigFile)
        marlinSteeringTemplate = setPandoraSettingsFile(marlinSteeringTemplate,pandoraSettingsFiles)
        marlinSteeringTemplate = setGearFile(marlinSteeringTemplate,gearFileLocal)
        marlinSteeringTemplate = setInputSlcioFile(marlinSteeringTemplate,slcioFilesInputSteeringFileString)

        with open("MarlinSteering.steer" ,"w") as SteeringFile:
            SteeringFile.write(marlinSteeringTemplate)

        ma = Marlin()
        ma.setVersion('ILCSoft-01-17-07')
        ma.setSteeringFile('MarlinSteering.steer')
        ma.setGearFile(gearFileLocal)
        ma.setInputFile(slcioFilesGridFilesString)

        outputFiles = []
        outputFiles.append(photonLikelihoodFileName)

        job = UserJob()
        job.setJobGroup(jobDescription)
        job.setInputSandbox(pandoraSettingsFiles.values()) # Local files
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
os.system('rm ' + gearFileLocal)
for key, value in pandoraSettingsFiles.iteritems():
    os.system('rm ' + value)

