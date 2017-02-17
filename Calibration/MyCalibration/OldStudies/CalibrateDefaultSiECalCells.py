#!/usr/bin/python

import sys 
import os
from Logic.CalibrateLogic import *

# No timing cut, 1 GeV truncation, realistic digi
for detectorModel in range(84,90):
    recoStage = 38
    calibraitonStage = 'Default'
    outputPath = '/r04/lc/sg568/HCAL_Optimisation_Studies/Calibration/Detector_Model_' + str(detectorModel) + '/Reco_Stage_' + str(recoStage) + '/' + calibraitonStage + 'Calibration'
    slcioFormat = 'MokkaSim_Detector_Model_' + str(detectorModel) + '_PARTICLE_ENERGYGeV_(.*?).slcio'
    slcioPath = '/r04/lc/sg568/HCAL_Optimisation_Studies/Slcio/GJN'+ str(detectorModel)
    gearFile = '/r04/lc/sg568/HCAL_Optimisation_Studies/GridSandboxes/GJN' + str(detectorModel) + '_OutputSandbox/ILD_o1_v06_Detector_Model_' + str(detectorModel) + '.gear'
    timingCut = 1000000
    hadronicEnergyTrunc = 1
    basePath = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudies/PandoraSettings/TrainedSettings/LikelihoodData/Detector_Model_' + str(detectorModel) + '/Reco_Stage_' + str(recoStage) + '/Z_uds/500GeV'
    pandoraSettings = os.path.join(basePath,'PandoraSettingsDefault.xml')
    photonLikelihoodData = os.path.join(basePath,'PandoraLikelihoodData_DetModel_' + str(detectorModel) + '_RecoStage_' + str(recoStage) + '.xml')

    if not os.path.isfile(photonLikelihoodData):
        continue

    Calibration(detectorModel, recoStage, slcioFormat, slcioPath, gearFile, pandoraSettings, outputPath, timingCut, hadronicEnergyTrunc, 'Si', True)

# No timing cut, 1 GeV truncation, no realistic digi
for detectorModel in range(84,90):
    recoStage = 63
    calibraitonStage = 'Default'
    outputPath = '/r04/lc/sg568/HCAL_Optimisation_Studies/Calibration/Detector_Model_' + str(detectorModel) + '/Reco_Stage_' + str(recoStage) + '/' + calibraitonStage + 'Calibration'
    slcioFormat = 'MokkaSim_Detector_Model_' + str(detectorModel) + '_PARTICLE_ENERGYGeV_(.*?).slcio'
    slcioPath = '/r04/lc/sg568/HCAL_Optimisation_Studies/Slcio/GJN'+ str(detectorModel)
    gearFile = '/r04/lc/sg568/HCAL_Optimisation_Studies/GridSandboxes/GJN' + str(detectorModel) + '_OutputSandbox/ILD_o1_v06_Detector_Model_' + str(detectorModel) + '.gear'
    timingCut = 1000000
    hadronicEnergyTrunc = 1
    basePath = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudies/PandoraSettings/TrainedSettings/LikelihoodData/Detector_Model_' + str(detectorModel) + '/Reco_Stage_' + str(recoStage) + '/Z_uds/500GeV'
    pandoraSettings = os.path.join(basePath,'PandoraSettingsDefault.xml')
    photonLikelihoodData = os.path.join(basePath,'PandoraLikelihoodData_DetModel_' + str(detectorModel) + '_RecoStage_' + str(recoStage) + '.xml')

    if not os.path.isfile(photonLikelihoodData):
        continue

    Calibration(detectorModel, recoStage, slcioFormat, slcioPath, gearFile, pandoraSettings, outputPath, timingCut, hadronicEnergyTrunc, 'Si', False)

# 100ns timing cut, 1 GeV truncation, realistic digi
for detectorModel in range(84,90):
    recoStage = 71
    calibraitonStage = 'Default'
    outputPath = '/r04/lc/sg568/HCAL_Optimisation_Studies/Calibration/Detector_Model_' + str(detectorModel) + '/Reco_Stage_' + str(recoStage) + '/' + calibraitonStage + 'Calibration'
    slcioFormat = 'MokkaSim_Detector_Model_' + str(detectorModel) + '_PARTICLE_ENERGYGeV_(.*?).slcio'
    slcioPath = '/r04/lc/sg568/HCAL_Optimisation_Studies/Slcio/GJN'+ str(detectorModel)
    gearFile = '/r04/lc/sg568/HCAL_Optimisation_Studies/GridSandboxes/GJN' + str(detectorModel) + '_OutputSandbox/ILD_o1_v06_Detector_Model_' + str(detectorModel) + '.gear'
    timingCut = 100
    hadronicEnergyTrunc = 1
    basePath = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudies/PandoraSettings/TrainedSettings/LikelihoodData/Detector_Model_' + str(detectorModel) + '/Reco_Stage_' + str(recoStage) + '/Z_uds/500GeV'
    pandoraSettings = os.path.join(basePath,'PandoraSettingsDefault.xml')
    photonLikelihoodData = os.path.join(basePath,'PandoraLikelihoodData_DetModel_' + str(detectorModel) + '_RecoStage_' + str(recoStage) + '.xml')

    if not os.path.isfile(photonLikelihoodData):
        continue

    Calibration(detectorModel, recoStage, slcioFormat, slcioPath, gearFile, pandoraSettings, outputPath, timingCut, hadronicEnergyTrunc, 'Si', True)

