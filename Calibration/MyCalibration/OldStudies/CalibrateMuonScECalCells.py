#!/usr/bin/python

import sys 
from Logic.CalibrateLogic import *

# No timing cut, 1 GeV truncation, realistic digi
for detectorModel in range(90,96):
    recoStage = 38
    calibraitonStage = 'Muon'
    outputPath = '/r04/lc/sg568/HCAL_Optimisation_Studies/Calibration/Detector_Model_' + str(detectorModel) + '/Reco_Stage_' + str(recoStage) + '/' + calibraitonStage + 'Calibration'
    slcioFormat = 'MokkaSim_Detector_Model_' + str(detectorModel) + '_PARTICLE_ENERGYGeV_(.*?).slcio'
    slcioPath = '/r04/lc/sg568/HCAL_Optimisation_Studies/Slcio/GJN'+ str(detectorModel)  
    gearFile = '/r04/lc/sg568/HCAL_Optimisation_Studies/GridSandboxes/GJN' + str(detectorModel) + '_OutputSandbox/ILD_o1_v06_Detector_Model_' + str(detectorModel) + '.gear'
    timingCut = 1000000
    hadronicEnergyTrunc = 1
    pandoraSettings = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudies/PandoraSettings/PandoraSettingsMuon.xml'
    Calibration(detectorModel, recoStage, slcioFormat, slcioPath, gearFile, pandoraSettings, outputPath, timingCut, hadronicEnergyTrunc, 'Sc', True)

# No timing cut, 1 GeV truncation, no realistic digi
for detectorModel in range(90,96):
    recoStage = 63
    calibraitonStage = 'Muon'
    outputPath = '/r04/lc/sg568/HCAL_Optimisation_Studies/Calibration/Detector_Model_' + str(detectorModel) + '/Reco_Stage_' + str(recoStage) + '/' + calibraitonStage + 'Calibration'
    slcioFormat = 'MokkaSim_Detector_Model_' + str(detectorModel) + '_PARTICLE_ENERGYGeV_(.*?).slcio'
    slcioPath = '/r04/lc/sg568/HCAL_Optimisation_Studies/Slcio/GJN'+ str(detectorModel)
    gearFile = '/r04/lc/sg568/HCAL_Optimisation_Studies/GridSandboxes/GJN' + str(detectorModel) + '_OutputSandbox/ILD_o1_v06_Detector_Model_' + str(detectorModel) + '.gear'
    timingCut = 1000000
    hadronicEnergyTrunc = 1
    pandoraSettings = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudies/PandoraSettings/PandoraSettingsMuon.xml'
    Calibration(detectorModel, recoStage, slcioFormat, slcioPath, gearFile, pandoraSettings, outputPath, timingCut, hadronicEnergyTrunc, 'Sc', False)

# 100ns timing cut, 1 GeV truncation, realistic digi
for detectorModel in range(90,96):
    recoStage = 71
    calibraitonStage = 'Muon'
    outputPath = '/r04/lc/sg568/HCAL_Optimisation_Studies/Calibration/Detector_Model_' + str(detectorModel) + '/Reco_Stage_' + str(recoStage) + '/' + calibraitonStage + 'Calibration'
    slcioFormat = 'MokkaSim_Detector_Model_' + str(detectorModel) + '_PARTICLE_ENERGYGeV_(.*?).slcio'
    slcioPath = '/r04/lc/sg568/HCAL_Optimisation_Studies/Slcio/GJN'+ str(detectorModel)
    gearFile = '/r04/lc/sg568/HCAL_Optimisation_Studies/GridSandboxes/GJN' + str(detectorModel) + '_OutputSandbox/ILD_o1_v06_Detector_Model_' + str(detectorModel) + '.gear'
    timingCut = 100
    hadronicEnergyTrunc = 1
    pandoraSettings = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudies/PandoraSettings/PandoraSettingsMuon.xml'
    Calibration(detectorModel, recoStage, slcioFormat, slcioPath, gearFile, pandoraSettings, outputPath, timingCut, hadronicEnergyTrunc, 'Sc', True)


