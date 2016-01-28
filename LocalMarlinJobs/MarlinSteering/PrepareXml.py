# -*- coding: utf-8 -*-
import os
import re
import random
import dircache
import sys
from LocalMarlinJobs import *

#===========================
# Input Variables
#===========================

detectorModel = 90
recoStage = 63
templateNumber = 5

jobName = 'Detector_Model_' + str(detectorModel) + '_Reco_Stage_' + str(recoStage) + '_Template_Number_' + str(templateNumber)

#eventsToSimulate = [ { 'EventType': 'Z_uds', 'Energies': [91, 200, 360, 500] } ]
eventsToSimulate = [ { 'EventType': 'Photon', 'Energies': [10] } ]

gearFile = '/r04/lc/sg568/HCAL_Optimisation_Studies/GridSandboxes/GJN' + str(detectorModel) + '_OutputSandbox/ILD_o1_v06_Detector_Model_' + str(detectorModel) + '.gear'

pandoraSettingsFiles = {}
pandoraSettingsFiles['Default'] =                os.path.join(os.getcwd(),'PandoraSettings/PandoraSettingsDefault.xml')
pandoraSettingsFiles['Default_LikelihoodData'] = os.path.join(os.getcwd(),'PandoraSettings/PandoraLikelihoodData9EBin.xml')
pandoraSettingsFiles['Muon'] =                   os.path.join(os.getcwd(),'PandoraSettings/PandoraSettingsMuon.xml')
pandoraSettingsFiles['PerfectPhoton'] =          os.path.join(os.getcwd(),'PandoraSettings/PandoraSettingsPerfectPhoton.xml')
pandoraSettingsFiles['PerfectPhotonNK0L'] =      os.path.join(os.getcwd(),'PandoraSettings/PandoraSettingsPerfectPhotonNeutronK0L.xml')
pandoraSettingsFiles['PerfectPFA'] =             os.path.join(os.getcwd(),'PandoraSettings/PandoraSettingsPerfectPFA.xml')

#===========================

# Make Folders
marlinXmlFolder = '/r04/lc/sg568/HCAL_Optimisation_Studies/MarlinXml/Detector_Model_' + str(detectorModel) + '/Reco_Stage_' + str(recoStage) + '/' + eventType + '/' + str(energy) + 'GeV'
makeFolder(marlinXmlFolder)

rootFolder = '/r04/lc/sg568/HCAL_Optimisation_Studies/MarlinXml/Detector_Model_' + str(detectorModel) + '/Reco_Stage_' + str(recoStage) + '/' + eventType + '/' + str(energy) + 'GeV'
makeFolder(rootFolder)

# Get Template Xml File
baseXmlFile = os.path.join(os.getcwd(), 'TemplateRepository/MarlinSteeringFileTemplate_' + str(templateNumber) + '.xml')

# Set Calibration Numbers
calibConfigFile = '/r04/lc/sg568/HCAL_Optimisation_Studies/CalibrationResults/Detector_Model_' + str(detectorModel) + '/Reco_Stage_' + str(recoStage) + '/CalibConfig_DetModel' + str(detectorModel) + '_RecoStage' + str(recoStage) + '.py'

jobList = ''

for eventSelection in eventsToSimulate:
    eventType = eventSelection['EventType']
    for energy in eventSelection['Energies']:
        slcioFilesToProcess = getSlcioFiles(detectorModel,energy,eventType)
        for idx, slcioFile in enumerate(slcioFilesToProcess):
            print 'Creating ' + eventType + ' ' + str(energy) + 'GeV jobs.  Detector model ' + str(detModel) + '.  Reconstruction stage ' + str(recoVar) + '.'
            marlinSteeringTemplate = getMarlinSteeringFileTemplate(baseXmlFile,calibConfigFile)
            marlinSteeringTemplate = setPandoraSettingsFile(marlinSteeringTemplate,pandoraSettingsFiles)
            marlinSteeringTemplate = setGearFile(marlinSteeringTemplate,gearFile)
            marlinSteeringTemplate = setInputSlcioFile(marlinSteeringTemplate,slcioFile)

            marlinXmlFileName = 'MarlinReco_MokkaSim_Detector_Model_' + str(detModel) + '_' + eventType + '_' + energy + 'GeV_' + str(idx) + '.xml' 
            marlinXmlPath = os.path.join(marlinXmlFolder,marlinXmlFileName)

            marlinSteeringTemplate = setOutputFiles(marlinSteeringTemplate,marlinXmlFileName[:-4])

            with open(marlinXmlPath ,"w") as SteeringFile:
                SteeringFile.write(marlinSteeringTemplate)

            jobList += marlinXmlPath
            jobList += '\n'

runFilePath = os.getcwd() + '/Condor'
file = open(runFilePath + '/MarlinRunFile_' + jobName + '.txt','w')
file.write(jobList)
file.close()

