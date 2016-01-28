#!/usr/bin/python

from CalibrateLogic import *

outputPath = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudiesScECal/Calibration/MyCalibration_Development/TestCalibration'
slcioFormat = 'MokkaSim_Detector_Model_38_PARTILCE_ENERGYGeV_(.*?).slcio'
slcioPath = '/r04/lc/sg568/HCAL_Optimisation_Studies/Slcio/GJN38' 
gearFile = '/r04/lc/sg568/HCAL_Optimisation_Studies/GridSandboxes/GJN38_OutputSandbox/ILD_o1_v06_Detector_Model_38.gear'
pandoraSettings = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudiesScECal/Calibration/MyCalibration_Development/PandoraSettingsDefault.xml'
timingCut = 100
hadronicEnergyTrunc = 1

Calibration(slcioFormat, slcioPath, gearFile, pandoraSettings, outputPath, timingCut, hadronicEnergyTrunc)

