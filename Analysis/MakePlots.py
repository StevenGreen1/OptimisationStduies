#!/usr/bin/python/Results

# -*- coding: utf-8 -*-

import sys
import re
import math
import os

from MakePlotsLogic import *

#===== User Input =====#
jetEnergyList = [91,200,360,500]
reconstructionVariantList = [71] #range(69,77)

# ECal Cell Size Silicon
resultsName = 'Silicon ECal Number of Layers'
detectorModelList = [99,98,97,96]
xAxisPlottingList = [16,20,26,30]
xAxisTitle = 'Silicon ECal Number of Layers'

ecalLayersResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
ecalLayersResults.readData()
ecalLayersResults.optimiseData()
ecalLayersResults.plotData()
#ecalLayersResults.analyseOptimalData()
ecalLayersResults.generateConfusionTerms()
ecalLayersResults.plotConfusionData(500)
ecalLayersResults.plotConfusionData(91)

sys.exit()

# Optimised HCal Cell Size
resultsName = 'Optimised HCal Cell Size'
detectorModelList = [39,40,38,41,42,43]
xAxisPlottingList = [10,20,30,40,50,100]
xAxisTitle = 'Optimised HCal Cell Size [mm^{2}]'

hcalCellSizeResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, True, 0)
hcalCellSizeResults.readData()
hcalCellSizeResults.optimiseData()
hcalCellSizeResults.analyseOptimalData()
#hcalCellSizeResults.plotData()

sys.exit()

# No Truncation HCal Cell Size
#resultsName = 'No Truncation HCal Cell Size'
#detectorModelList = [39,40,38,41,42,43]
#xAxisPlottingList = [10,20,30,40,50,100]
#xAxisTitle = 'No Truncation HCal Cell Size [mm^{2}]'

#hcalCellSizeResults2 = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False)
#hcalCellSizeResults2.readData()
#hcalCellSizeResults2.optimiseData()
#hcalCellSizeResults2.analyseOptimalData()
#hcalCellSizeResults2.plotData()

# Material
resultsName = 'HCal Absorber Material'
detectorModelList = [45,46,47,48]
xAxisPlottingList = [1,2,3,4]
xAxisTitle = 'HCal Absorber Material'

hcalMaterialResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
hcalMaterialResults.readData()
hcalMaterialResults.optimiseData()
#hcalMaterialResults.analyseOptimalData()
#hcalMaterialResults.plotData()
hcalMaterialResults.plotDataVsJetEnergy()

#sys.exit()

# ECal Cell Size Silicon
resultsName = 'Silicon ECal Cell Size'
detectorModelList = [84,85,86,87,88,89]
xAxisPlottingList = [3,5,7,10,15,20]
xAxisTitle = 'Silicon ECal Cell Size [mm^{2}]'

ecalCellSizeResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
ecalCellSizeResults.readData()
ecalCellSizeResults.optimiseData()
ecalCellSizeResults.plotData()
#ecalCellSizeResults.analyseOptimalData()
ecalCellSizeResults.generateConfusionTerms()
ecalCellSizeResults.plotConfusionData(500)
ecalCellSizeResults.plotConfusionData(91)

#sys.exit()

# ECal Cell Size Silicon 2
reconstructionVariantList2 = [79]

resultsName = 'Silicon ECal Cell Size No Realistic Digitisation Effects'
detectorModelList = [84,85,86,87,88,89]
xAxisPlottingList = [3,5,7,10,15,20]
xAxisTitle = 'Silicon ECal Cell Size [mm^{2}]'

ecalCellSizeResults2 = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList2,jetEnergyList, False, 79)
ecalCellSizeResults2.readData()
ecalCellSizeResults2.optimiseData()
ecalCellSizeResults2.plotData()
ecalCellSizeResults2.analyseOptimalData()
#ecalCellSizeResults2.generateConfusionTerms()
#ecalCellSizeResults2.plotConfusionData(500)
#ecalCellSizeResults2.plotConfusionData(91)

# ECal Cell Size Silicon 3
reconstructionVariantList2 = [38]

resultsName = 'Silicon ECal Cell Size Realistic Digitisation Effects No Timing Cuts'
detectorModelList = [84,85,86,87,88,89]
xAxisPlottingList = [3,5,7,10,15,20]
xAxisTitle = 'Silicon ECal Cell Size [mm^{2}]'

ecalCellSizeResults3 = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList2,jetEnergyList, False, 38)
ecalCellSizeResults3.readData()
ecalCellSizeResults3.optimiseData()
ecalCellSizeResults3.plotData()
ecalCellSizeResults3.analyseOptimalData()
#ecalCellSizeResults3.generateConfusionTerms()
#ecalCellSizeResults3.plotConfusionData(500)
#ecalCellSizeResults3.plotConfusionData(91)

# ECal Cell Size Scintillator
resultsName = 'Scintillator ECal Cell Size'
detectorModelList = [90,91,92,93,94,95]
xAxisPlottingList = [3,5,7,10,15,20]
xAxisTitle = 'Scintillator ECal Cell Size [mm^{2}]'

ecalCellSize2Results = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
ecalCellSize2Results.readData()
ecalCellSize2Results.optimiseData()
ecalCellSize2Results.plotData()
#ecalCellSize2Results.analyseOptimalData()
#ecalCellSize2Results.generateConfusionTerms()
#ecalCellSize2Results.plotConfusionData(500)
#ecalCellSize2Results.plotConfusionData(91)

# ECal Cell Size Scintillator 2
reconstructionVariantList2 = [79]

resultsName = 'Scintillator ECal Cell Size Basic ILD'
detectorModelList = [90,91,92,93,94,95]
xAxisPlottingList = [3,5,7,10,15,20]
xAxisTitle = 'Scintillator ECal Cell Size [mm^{2}]'

ecalCellSize2Results2 = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList2,jetEnergyList, False, 79)
ecalCellSize2Results2.readData()
ecalCellSize2Results2.optimiseData()
ecalCellSize2Results2.plotData()
#ecalCellSize2Results2.analyseOptimalData()
#ecalCellSize2Results2.generateConfusionTerms()
#ecalCellSize2Results2.plotConfusionData(500)
#ecalCellSize2Results2.plotConfusionData(91)

# ECal Cell Size Scintillator 3
reconstructionVariantList2 = [63]

resultsName = 'Scintillator ECal Cell Size Basic ILD No Timing Cuts'
detectorModelList = [90,91,92,93,94,95]
xAxisPlottingList = [3,5,7,10,15,20]
xAxisTitle = 'Scintillator ECal Cell Size [mm^{2}]'

ecalCellSize2Results3 = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList2,jetEnergyList, False, 63)
ecalCellSize2Results3.readData()
ecalCellSize2Results3.optimiseData()
ecalCellSize2Results3.plotData()
#ecalCellSize2Results3.analyseOptimalData()
#ecalCellSize2Results3.generateConfusionTerms()
#ecalCellSize2Results3.plotConfusionData(500)
#ecalCellSize2Results3.plotConfusionData(91)

sys.exit()

# Material
resultsName = 'HCal Absorber Material'
detectorModelList = [45,46,47,48]
xAxisPlottingList = [1,2,3,4]
xAxisTitle = 'HCal Absorber Material'

hcalMaterialResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
hcalMaterialResults.readData()
hcalMaterialResults.optimiseData()
#hcalMaterialResults.analyseOptimalData()
#hcalMaterialResults.plotData()
hcalMaterialResults.plotDataVsJetEnergy()

#sys.exit()

# HCal Cell Size
resultsName = 'HCal Cell Size'
detectorModelList = [39,40,38,41,42,43]
xAxisPlottingList = [10,20,30,40,50,100]
xAxisTitle = 'HCal Cell Size [mm^{2}]'

hcalCellSizeResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, True, 0)
hcalCellSizeResults.readData()
hcalCellSizeResults.optimiseData()
hcalCellSizeResults.analyseOptimalData()
hcalCellSizeResults.plotData()
hcalCellSizeResults.plotConfusionData(500)

# Number of HCal Layers
resultsName = 'Number Of Layers In The HCal'
detectorModelList = [49,50,51,52,53,38,54,55]
xAxisPlottingList = [18,24,30,36,42,48,54,60]
xAxisTitle = 'Number Of Layers In The HCal'

layerResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
layerResults.readData()
layerResults.optimiseData()
layerResults.plotData()

# Number of HCal Interation Lengths
resultsName = 'Number Of Nuclear Interation Lengths In The HCal'
detectorModelList = [56,57,38,58,59]
xAxisPlottingList = [4.576,5.148,5.72,6.292,6.864]
xAxisTitle = 'Number Of Nuclear Interation Lengths In The HCal [#lambda_{I}]'

lengthResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
lengthResults.readData()
lengthResults.optimiseData()
lengthResults.plotData()

# Sampling Fraction in HCal
resultsName = 'Sampling Fraction In The HCal'
detectorModelList = [60,61,38,62,63]
xAxisPlottingList = [0.05,0.10,0.15,0.20,0.25]
xAxisTitle = 'Sampling Fraction In The HCal'

sampFraclengthResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
sampFraclengthResults.readData()
sampFraclengthResults.optimiseData()
sampFraclengthResults.plotData()

# B Field
resultsName = 'Magnetic Field Strength'
detectorModelList = [64,65,66,67,68,69,70,71,72]
xAxisPlottingList = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
xAxisTitle = 'Magentic Field Strength [T]'

bFieldResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
bFieldResults.readData()
bFieldResults.optimiseData()
bFieldResults.plotData()

# Sampling Fraction in HCal
resultsName = 'ECal Inner Radius'
detectorModelList = [73,74,75,76,77]
xAxisPlottingList = [1208,1408,1608,1808,2008]
xAxisTitle = 'ECal Inner Radius [mm]'

ecalInnerRadResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
ecalInnerRadResults.readData()
ecalInnerRadResults.optimiseData()
ecalInnerRadResults.plotData()


