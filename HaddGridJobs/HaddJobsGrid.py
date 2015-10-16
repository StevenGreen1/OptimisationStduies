# Example to submit Marlin job: MarlinExample.py
import os
import sys

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from ILCDIRAC.Interfaces.API.DiracILC import  DiracILC
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import *
from ILCDIRAC.Interfaces.API.NewInterface.Applications import *

#from MarlinGridJobs import *

#===== User Input =====

#jobDescription = 'OptimisationStudies'
#detModel = sys.argv[1] 
#recoVar = sys.argv[2] # Ranges from 69 to 76, all using realistic ECal and HCal

#eventsToSimulate = [ { 'EventType': "Z_uds", 'Energies': [91, 200, 360, 500] } ]

#baseXmlFile = 'TemplateRepository/MarlinSteeringFileTemplate_Jets_1.xml'
# Notes: 
# Turned off the slcio outpuf processor to speed up job processing in xml file.

#pandoraSettingsFiles = {}
#pandoraSettingsFiles['Default'] = 'PandoraSettings/PandoraSettingsDefault.xml' 
#pandoraSettingsFiles['Default_LikelihoodData'] = 'PandoraSettings/PandoraLikelihoodData9EBin.xml' 
#pandoraSettingsFiles['Muon'] = 'PandoraSettings/PandoraSettingsMuon.xml'
#pandoraSettingsFiles['PerfectPhoton'] = 'PandoraSettings/PandoraSettingsPerfectPhoton.xml'
#pandoraSettingsFiles['PerfectPhotonNK0L'] = 'PandoraSettings/PandoraSettingsPerfectPhotonNeutronK0L.xml'
#pandoraSettingsFiles['PerfectPFA'] = 'PandoraSettings/PandoraSettingsPerfectPFA.xml'

#===== Second level user input =====
# If using naming scheme doesn't need changing 

#gearFile = '/r04/lc/sg568/HCAL_Optimisation_Studies/GridSandboxes/GJN' + str(detModel) + '_OutputSandbox/ILD_o1_v06_GJN' + str(detModel) + '.gear'
#calibConfigFile = '/r04/lc/sg568/HCAL_Optimisation_Studies/CalibrationResults/Detector_Model_' + str(detModel) + '/Reco_Stage_' + str(recoVar) + '/CalibConfig_DetModel' + str(detModel) + '_RecoStage' + str(recoVar) + '.py'

#=====

# Copy gear file and pandora settings files to local directory as is needed for submission.
#os.system('cp ' + gearFile + ' .')
#gearFileLocal = os.path.basename(gearFile)

#pandoraSettingsFilesLocal = {}
#for key, value in pandoraSettingsFiles.iteritems():
#    os.system('cp ' + value + ' .')
#    pandoraSettingsFilesLocal[key] = os.path.basename(value)

# Start submission
JobIdentificationString = 'TestingHadd'
diracInstance = DiracILC(withRepo=True,repoLocation="%s.cfg" %( JobIdentificationString))

#for eventSelection in eventsToSimulate:
#    eventType = eventSelection['EventType']
#    for energy in eventSelection['Energies']:
#        slcioFilesToProcess = getSlcioFiles(jobDescription,detModel,energy,eventType)
#        for slcioFile in slcioFilesToProcess:
#            print 'Submitting ' + eventType + ' ' + str(energy) + 'GeV jobs.  Detector model ' + str(detModel) + '.  Reconstruction stage ' + str(recoVar) + '.'  
#            marlinSteeringTemplate = ''
#            marlinSteeringTemplate = getMarlinSteeringFileTemplate(baseXmlFile,calibConfigFile)
#            marlinSteeringTemplate = setPandoraSettingsFile(marlinSteeringTemplate,pandoraSettingsFilesLocal)
#            marlinSteeringTemplate = setGearFile(marlinSteeringTemplate,gearFileLocal)

#            slcioFileNoPath = os.path.basename(slcioFile)
#            marlinSteeringTemplate = setInputSlcioFile(marlinSteeringTemplate,slcioFileNoPath)
#            marlinSteeringTemplate = setOutputFiles(marlinSteeringTemplate,'MarlinReco_' + slcioFileNoPath[:-6])

#            with open("MarlinSteering.steer" ,"w") as SteeringFile:
#                SteeringFile.write(marlinSteeringTemplate)

#ILCDIRAC.Interfaces.API.NewInterface.Applications._Root._Root
arguements = ['HaddTest.root','/ilc/user/s/sgreen/OptimisationStudies/MarlinJobs/Detector_Model_38/Reco_Stage_75/Z_uds/91GeV/MarlinReco_ILD_o1_v06_GJN38_uds91_02_200_Default.root','/ilc/user/s/sgreen/OptimisationStudies/MarlinJobs/Detector_Model_38/Reco_Stage_75/Z_uds/91GeV/MarlinReco_ILD_o1_v06_GJN38_uds91_02_300_Default.root']

files = []

for arg in arguements:
    head, tail = os.path.split(arg)
    files.append(tail)

from ILCDIRAC.Interfaces.API.NewInterface.Applications import GenericApplication
genericApplication = GenericApplication()
genericApplication.setScript('Hadd.sh')
genericApplication.setArguments(" ".join(files))
genericApplication.setDependency({"marlin":"ILCSoft-01-17-07"})

#            ma = Marlin()
#            ma.setVersion('ILCSoft-01-17-07')
#            ma.setSteeringFile('MarlinSteering.steer')
#            ma.setGearFile(gearFileLocal)
#            ma.setInputFile('lfn:' + slcioFile)

#            outputFiles = []
#            outputFiles.append('MarlinReco_' + slcioFileNoPath[:-6] + '_Default.root')
            #outputFiles.append('MarlinReco_' + slcioFileNoPath[:-6] + '.slcio') # Not saving the output collections to speed up processing.
#            if eventType == 'Z_uds':
#                outputFiles.append('MarlinReco_' + slcioFileNoPath[:-6] + '_Muon.root')
#                outputFiles.append('MarlinReco_' + slcioFileNoPath[:-6] + '_PerfectPhoton.root')
#                outputFiles.append('MarlinReco_' + slcioFileNoPath[:-6] + '_PerfectPhotonNK0L.root')
#                outputFiles.append('MarlinReco_' + slcioFileNoPath[:-6] + '_PerfectPFA.root')

job = UserJob()
job.setJobGroup('TestingHadd')
#job.setInputSandbox(['hadd.C']) # Local files
#            job.setOutputSandbox(['*.log','*.gear','*.mac','*.steer','*.xml'])

job.setInputData(arguements[1:])
job.setOutputData('HaddTest.root',OutputPath='/Testing') # On grid
job.setName('TestingHadd')
job.setBannedSites(['LCG.IN2P3-CC.fr','LCG.IN2P3-IRES.fr','LCG.KEK.jp'])
job.dontPromptMe()
job.setCPUTime(1000)
res = job.append(genericApplication)

if not res['OK']:
    print res['Message']
    exit()
job.submit(diracInstance)
os.system('rm *.cfg')

# Tidy Up
#os.system('rm MarlinSteering.steer')
#os.system('rm ' + gearFileLocal)
#for key, value in pandoraSettingsFilesLocal.iteritems():
#    os.system('rm ' + value)

