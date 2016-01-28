# Submit Mokka jobs to the grid: MokkaSubmit.py
import os
import sys

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from ILCDIRAC.Interfaces.API.DiracILC import  DiracILC
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import *
from ILCDIRAC.Interfaces.API.NewInterface.Applications import *

from MokkaGridJobs import *

#===== User Input =====

detectorModelNumber = sys.argv[1] 

eventsToSimulate = [ { 'EventType': "Z_uds"  , 'EventsPerFile' : 200 , 'Energies':  ['500'] } ]

baseXmlFile  = 'TemplateRepository/MokkaSteer.steer'
eventsPerJob = 100

jobName = 'OptimisationStudies'

#===== Second level user input =====
# If using naming scheme doesn't need changing 

detModelConfigFile = 'DetectorModelConfigFiles/Detector_Model_' + str(detectorModelNumber) + '_Config.py'
gearFile     = 'ILD_o1_v06_Detector_Model_' + str(detectorModelNumber) + '.gear'

#=====

# Start submission
JobIdentificationString = jobName + '_Default_Detector_Model_Reco_' + str(detectorModelNumber)
diracInstance = DiracILC(withRepo=True,repoLocation="%s.cfg" %( JobIdentificationString))

for eventSelection in eventsToSimulate:
    eventType = eventSelection['EventType']
    eventsPerFile = eventSelection['EventsPerFile']
    for energy in eventSelection['Energies']:
        hepevtFilesToProcess = getHEPEvtFiles(eventType,energy)
        jobNumber = 0
        for hepevtFile in hepevtFilesToProcess:
            for startEvent in xrange(0, eventsPerFile, eventsPerJob):
                print 'Submitting ' + eventType + ' ' + energy + 'GeV jobs.  Detector model ' + str(detectorModelNumber) + '.  Start event number ' + str(startEvent) + ' out of ' + str(eventsPerFile) + '.'  

                jobNumber += eventsPerJob
                description = eventType + '_' + str(energy) + 'GeV'
                outputFile = 'MokkaSim_Detector_Model_' + str(detectorModelNumber) + '_' + description + '_' + str(eventsPerJob) + '_' + str(jobNumber) + '.slcio'
                outputPath = '/' + jobName + '/PhotonLikelihoodTraining/MokkaJobs/Detector_Model_' + str(detectorModelNumber) + '/' + eventType + '/' + str(energy) + 'GeV' 

                lfn = '/ilc/user/s/sgreen/' + outputPath + '/' + outputFile
                if doesFileExist(lfn):
                    continue

                mokkaSteeringTemplate = ''
                mokkaSteeringTemplate = getMokkaSteeringFileTemplate(baseXmlFile,detModelConfigFile)
                mokkaSteeringTemplate = setGearFile(mokkaSteeringTemplate,gearFile)
                mokkaSteeringTemplate = setOutputFile(mokkaSteeringTemplate,outputFile)
                mokkaSteeringTemplate = setStartNumber(mokkaSteeringTemplate,startEvent)

                with open("MokkaSteering.steer" ,"w") as steeringFile:
                    steeringFile.write(mokkaSteeringTemplate)

                MokkaApplication = Mokka()
                MokkaApplication.setVersion(getMokkaVersion(detModelConfigFile))
                MokkaApplication.setSteeringFile('MokkaSteering.steer')
                MokkaApplication.setNumberOfEvents(eventsPerJob)
                MokkaApplication.setStartFrom(startEvent)

                job = UserJob()
                job.setJobGroup(jobName)
                job.setOutputSandbox( ["*.log", "*.gear", "*.mac", "*.steer", "*.xml" ] )
                job.setOutputData(outputFile, OutputPath=outputPath)
                job.setInputData(hepevtFile)
                job.setName(jobName + '_Detector_Model_' + str(detectorModelNumber))
                job.setBannedSites(['LCG.IN2P3-CC.fr','LCG.IN2P3-IRES.fr','LCG.KEK.jp'])

                res = job.append(MokkaApplication)
                if not res['OK']:
                    print res['Message']
                    exit()
                job.dontPromptMe()
                job.submit(diracInstance)
                os.system('rm *.cfg')

# Tidy Up
os.system('rm MokkaSteering.steer')

