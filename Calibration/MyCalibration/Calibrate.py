#!/usr/bin/python

from CalibrateLogic import *

for detectorModel in [96, 97]:
    for recoStage in [71]:
        outputPath = '/r04/lc/sg568/HCAL_Optimisation_Studies/Calibration/Detector_Model_' + str(detectorModel) + '/Reco_Stage_' + str(recoStage) + '/MuonCalibration'
        slcioFormat = 'MokkaSim_Detector_Model_' + str(detectorModel) + '_PARTICLE_ENERGYGeV_(.*?).slcio'
        slcioPath = '/r04/lc/sg568/HCAL_Optimisation_Studies/Slcio/GJN'+ str(detectorModel)  
        gearFile = '/r04/lc/sg568/HCAL_Optimisation_Studies/GridSandboxes/GJN' + str(detectorModel) + '_OutputSandbox/ILD_o1_v06_Detector_Model_' + str(detectorModel) + '.gear'
        pandoraSettings = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudiesScECal/Calibration/PandoraSettings_MarlinPandora_v02-00-00/PandoraSettingsMuon.xml'
        timingCut = 100
        hadronicEnergyTrunc = 1
        Calibration(detectorModel, recoStage, slcioFormat, slcioPath, gearFile, pandoraSettings, outputPath, timingCut, hadronicEnergyTrunc, 'Si', True)
