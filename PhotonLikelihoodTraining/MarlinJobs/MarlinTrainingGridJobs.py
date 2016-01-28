# Example to submit Marlin job: MarlinExample.py
import re
import os
import sys

### ----------------------------------------------------------------------------------------------------

def generatePandoraSettingsActive(photonLikelihoodFileName,numberOfECalLayers):
    baseFileName = 'PandoraSettings/PandoraSettingsDefault.xml'

    baseFile = open(baseFileName,'r')
    pandoraSettingsTemplate = baseFile.read()
    baseFile.close()

    pandoraSettingsTemplate = re.sub('PANDORATRAININGXMLFILENAME_XXXX',photonLikelihoodFileName,pandoraSettingsTemplate)
    pandoraSettingsTemplate = re.sub('NUMBEROFECALLAYERS_XXXX',str(numberOfECalLayers),pandoraSettingsTemplate)

    with open("PandoraSettingsActive.xml" ,"w") as pandoraSettingsFile:
        pandoraSettingsFile.write(pandoraSettingsTemplate)

### ----------------------------------------------------------------------------------------------------

def setPandoraSettingsFile(marlinSteeringTemplate,pandoraSettingsFiles):
    marlinSteeringTemplate = re.sub('PANDORASETTINGSDEFAULT_XXXX',pandoraSettingsFiles['Active'],marlinSteeringTemplate)
    return marlinSteeringTemplate

### ----------------------------------------------------------------------------------------------------

def setGearFile(marlinSteeringTemplate,gearFile):
    marlinSteeringTemplate = re.sub('GEAR_FILE_XXXX',gearFile,marlinSteeringTemplate)
    return marlinSteeringTemplate

### ----------------------------------------------------------------------------------------------------

def setInputSlcioFile(marlinSteeringTemplate,inputSlcioFile):
    marlinSteeringTemplate = re.sub('INPUT_SLCIO_FILE_XXXX',inputSlcioFile,marlinSteeringTemplate)
    return marlinSteeringTemplate

### ----------------------------------------------------------------------------------------------------

def getMarlinSteeringFileTemplate(baseFileName,calibrationFileName):
    config = {}
    execfile(calibrationFileName, config)

    baseFile = open(baseFileName,'r')
    marlinSteeringTemplate = baseFile.read()
    baseFile.close()

    # Digitisation Constants
    ECalString = str(config['CalibrECal']) + ' ' + str(2 * config['CalibrECal'])
    marlinSteeringTemplate = re.sub('CALIBR_ECAL_XXXX',ECalString,marlinSteeringTemplate)
    marlinSteeringTemplate = re.sub('CALIBR_HCAL_XXXX',str(config['CalibrHCal']),marlinSteeringTemplate) # Only for NewLDCCaloDigi
    marlinSteeringTemplate = re.sub('CALIBR_HCAL_BARREL_XXXX',str(config['CalibrHCalBarrel']),marlinSteeringTemplate)
    marlinSteeringTemplate = re.sub('CALIBR_HCAL_ENDCAP_XXXX',str(config['CalibrHCalEndcap']),marlinSteeringTemplate)
    marlinSteeringTemplate = re.sub('CALIBR_HCAL_OTHER_XXXX',str(config['CalibrHCalOther']),marlinSteeringTemplate)
    marlinSteeringTemplate = re.sub('CALIBR_MUON_XXXX',str(config['CalibrMuon']),marlinSteeringTemplate)

    # Timing Cuts in HCal
    marlinSteeringTemplate = re.sub('HCALBARRELTIMEWINDOWMAX_XXXX',str(config['HCalBarrelTimeWindowMax']),marlinSteeringTemplate)
    marlinSteeringTemplate = re.sub('HCALENDCAPTIMEWINDOWMAX_XXXX',str(config['HCalEndcapTimeWindowMax']),marlinSteeringTemplate)

    # Timing Cuts in ECal
    marlinSteeringTemplate = re.sub('ECALBARRELTIMEWINDOWMAX_XXXX',str(config['ECalBarrelTimeWindowMax']),marlinSteeringTemplate)
    marlinSteeringTemplate = re.sub('ECALENDCAPTIMEWINDOWMAX_XXXX',str(config['ECalEndcapTimeWindowMax']),marlinSteeringTemplate)

    # MIP definition pre digitisation
    marlinSteeringTemplate = re.sub('CALIBR_ECAL_MIP_XXXX',str(config['CalibrECalMIP']),marlinSteeringTemplate)
    marlinSteeringTemplate = re.sub('CALIBR_HCAL_MIP_XXXX',str(config['CalibrHCalMIP']),marlinSteeringTemplate)

    # MIP defintion post digitisation
    marlinSteeringTemplate = re.sub('ECALTOMIPCALIBRATION_XXXX',str(config['ECalToMIPCalibration']),marlinSteeringTemplate)
    marlinSteeringTemplate = re.sub('HCALTOMIPCALIBRATION_XXXX',str(config['HCalToMIPCalibration']),marlinSteeringTemplate)
    marlinSteeringTemplate = re.sub('MUONTOMIPCALIBRATION_XXXX',str(config['MuonToMIPCalibration']),marlinSteeringTemplate)

    # MIP Threshold Cuts applied in Pandora
    marlinSteeringTemplate = re.sub('ECALMIPTHRESHOLD_XXXX',str(config['ECalMIPThresholdPandora']),marlinSteeringTemplate)
    marlinSteeringTemplate = re.sub('HCALMIPTHRESHOLD_XXXX',str(config['HCalMIPThresholdPandora']),marlinSteeringTemplate)

    # Pandora PFA Calibration Constants
    # Electromagnetic
    marlinSteeringTemplate = re.sub('ECALTOEMGEVCALIBRATION_XXXX',str(config['ECalToEMGeVCalibration']),marlinSteeringTemplate)
    marlinSteeringTemplate = re.sub('HCALTOEMGEVCALIBRATION_XXXX',str(config['HCalToEMGeVCalibration']),marlinSteeringTemplate)
    # Hadronic
    marlinSteeringTemplate = re.sub('ECALTOHADGEVCALIBRATION_XXXX',str(config['ECalToHadGeVCalibration']),marlinSteeringTemplate)
    marlinSteeringTemplate = re.sub('HCALTOHADGEVCALIBRATION_XXXX',str(config['HCalToHadGeVCalibration']),marlinSteeringTemplate)

    # Hadronic Corrections
    marlinSteeringTemplate = re.sub('MAXHCALHITHADRONICENERGY_XXXX',str(config['MaxHCalHitHadronicEnergy']),marlinSteeringTemplate)

    return marlinSteeringTemplate

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

def getPhotonFiles(energy):
    fileFormat = '/ilc/user/b/bxu/20150401/0804/DoubleClosePhotonRecoXu20150401/PhotonSingle/1GeV/22PDG_' + str(energy) + 'GeV_10000Events'
    slcioFiles = []
    os.system('dirac-dms-user-lfns -b /ilc/user/b/bxu/20150401/0804/DoubleClosePhotonRecoXu20150401/PhotonSingle/1GeV/22PDG_' + str(energy) + 'GeV_10000Events > /dev/null')
    os.system('mv ilc-user-b-bxu-20150401-0804-DoubleClosePhotonRecoXu20150401-PhotonSingle-1GeV-22PDG_' + str(energy) + 'GeV_10000Events.lfns tmp.txt')
    with open('tmp.txt') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            line = line.strip()
            slcioFiles.append(line)
    os.system('rm tmp.txt')
    return slcioFiles

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


