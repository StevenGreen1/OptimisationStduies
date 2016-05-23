# Example to submit Marlin job
import os
import sys

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from ILCDIRAC.Interfaces.API.DiracILC import  DiracILC
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import *
from ILCDIRAC.Interfaces.API.NewInterface.Applications import *

from Logic.XmlGenerationLogic import *
from Logic.DiracTools import *

#===== User Input =====

jobDescription = 'OptimisationStudies_ECalStudies'
detModel = sys.argv[1] 
recoVar = sys.argv[2]

eventsToSimulate = [ 
                     { 'EventType': "Kaon0L", 'Energies': [10, 20, 50, 100, 200, 500] }, 
                     { 'EventType': "Photon", 'Energies': [10, 20, 50, 100, 200, 500] }
                   ]

#===== Second level user input =====

# All keys are given separate MarlinPandora processor, unless the word Likelihood appears as a substring of the key
basePath = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudies/PandoraSettings/TrainedSettings/LikelihoodData/Detector_Model_' + str(detModel) + '/Reco_Stage_' + str(recoVar) + '/Z_uds/500GeV'
pandoraSettingsFiles = {}
pandoraSettingsFiles['Default'] = os.path.join(basePath,'PandoraSettingsDefault.xml')  
pandoraSettingsFiles['Default_LikelihoodData'] = os.path.join(basePath,'PandoraLikelihoodData_DetModel_' + str(detModel) + '_RecoStage_' + str(recoVar) + '.xml')
#pandoraSettingsFiles['Muon'] = '../PandoraSettings/PandoraSettingsMuon.xml'
#pandoraSettingsFiles['PerfectPhoton'] = '../PandoraSettings/PandoraSettingsPerfectPhoton.xml'
#pandoraSettingsFiles['PerfectPhotonNK0L'] = '../PandoraSettings/PandoraSettingsPerfectPhotonNeutronK0L.xml'
pandoraSettingsFiles['PerfectPFA'] = '../PandoraSettings/PandoraSettingsPerfectPFA.xml'

gearFile = '/r04/lc/sg568/HCAL_Optimisation_Studies/GridSandboxes/GJN' + str(detModel) + '_OutputSandbox/ILD_o1_v06_Detector_Model_' + str(detModel) + '.gear'

calibConfigPath = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudies/Calibration/CalibConfigFiles/DefaultCalibration'
calibConfigFile = os.path.join(calibConfigPath,'CalibConfig_DetModel' + str(detModel) + '_RecoStage' + str(recoVar) + '.py')

#=====

# Copy gear file and pandora settings files to local directory as is needed for submission.
os.system('cp ' + gearFile + ' .')
gearFileLocal = os.path.basename(gearFile)

pandoraSettingsFilesLocal = {}
for key, value in pandoraSettingsFiles.iteritems():
    os.system('cp ' + value + ' .')
    pandoraSettingsFilesLocal[key] = os.path.basename(value)

# Edit local Pandora settings default to remove likelihood data path
pandoraSettingsDefaultContent = ''
with open(pandoraSettingsFilesLocal['Default'], 'r') as localPandoraSettingsDefault:
    pandoraSettingsDefaultContent = localPandoraSettingsDefault.read()
pandoraSettingsDefaultContent = re.sub('<HistogramFile>(.*?)</HistogramFile>','<HistogramFile>' + pandoraSettingsFilesLocal['Default_LikelihoodData'] + '</HistogramFile>',pandoraSettingsDefaultContent)
with open(pandoraSettingsFilesLocal['Default'] ,'w') as localPandoraSettingsDefault:
    localPandoraSettingsDefault.write(pandoraSettingsDefaultContent)

# Start submission
JobIdentificationString = jobDescription + '_Detector_Model_' + str(detModel) + '_Reco_' + str(recoVar)
diracInstance = DiracILC(withRepo=True,repoLocation="%s.cfg" %( JobIdentificationString))

for eventSelection in eventsToSimulate:
    eventType = eventSelection['EventType']
    for energy in eventSelection['Energies']:
        slcioFilesToProcess = getSlcioFiles(jobDescription,detModel,energy,eventType)

        if not slcioFilesToProcess:
            print 'No slcio files found.  Exiting job submission.'
            sys.exit()

        for slcioFile in slcioFilesToProcess:
            print 'Checking ' + eventType + ' ' + str(energy) + 'GeV jobs.  Detector model ' + str(detModel) + '.  Reconstruction stage ' + str(recoVar) + '.  Slcio file ' + slcioFile + '.'  

            slcioFileNoPath = os.path.basename(slcioFile)
            xmlGeneration = XmlGeneration(calibConfigFile,'Si',True,pandoraSettingsFilesLocal,gearFileLocal,slcioFileNoPath)
            xmlTemplate = xmlGeneration.produceXml()
            outputFiles = xmlGeneration.listOutputFiles()

            with open("MarlinSteering.steer" ,"w") as SteeringFile:
                SteeringFile.write(xmlTemplate)

            outputPath = '/' + jobDescription + '/MarlinJobs/Detector_Model_' + str(detModel) + '/Reco_Stage_' + str(recoVar) + '/' + eventType + '/' + str(energy) + 'GeV'

            lfn = '/ilc/user/s/sgreen/' + outputPath + '/' + outputFiles[0]
            if doesFileExist(lfn):
                continue

            print 'Submitting ' + eventType + ' ' + str(energy) + 'GeV jobs.  Detector model ' + str(detModel) + '.  Reconstruction stage ' + str(recoVar) + '.  Slcio file ' + slcioFile + '.'  

            ma = Marlin()
            ma.setVersion('ILCSoft-01-17-07')
            ma.setSteeringFile('MarlinSteering.steer')
            ma.setGearFile(gearFileLocal)
            ma.setInputFile('lfn:' + slcioFile)

            job = UserJob()
            job.setJobGroup(jobDescription)
            job.setInputSandbox(pandoraSettingsFilesLocal.values()) # Local files
            job.setOutputSandbox(['*.log','*.gear','*.mac','*.steer','*.xml'])
            job.setOutputData(outputFiles,OutputPath=outputPath) # On grid
            job.setName(jobDescription + '_Detector_Model_' + str(detModel) + '_Reco_' + str(recoVar))
            job.setBannedSites(['LCG.IN2P3-CC.fr','LCG.IN2P3-IRES.fr','LCG.KEK.jp','OSG.PNNL.us','OSG.CIT.us','LCG.LAPP.fr'])
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
for key, value in pandoraSettingsFilesLocal.iteritems():
    os.system('rm ' + value)

