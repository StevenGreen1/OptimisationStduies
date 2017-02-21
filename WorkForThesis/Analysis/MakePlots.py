#!/usr/bin/python/Results

# -*- coding: utf-8 -*-

import sys
import re
import math
import os

from MakePlotsLogic import *

#===== User Input =====#
jetEnergyList = [91,200,360,500]

# Number Of HCal Layers Of Fixed Depth
resultsName = 'Number Of HCal Layers Of Fixed Depth'
detectorModelList = [116,117,85,118,119]
reconstructionVariantList = [71,71,71,71,71]
xAxisPlottingList = [36,42,48,54,60]
xAxisTitle = 'Number Of HCal Layers Of Fixed Depth'

hcalCellSizeResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
hcalCellSizeResults.readData()
hcalCellSizeResults.optimiseData()
hcalCellSizeResults.plotData()
hcalCellSizeResults.generateConfusionTerms()
hcalCellSizeResults.plotConfusionData(500)
hcalCellSizeResults.plotConfusionData(360)
hcalCellSizeResults.plotConfusionData(200)
hcalCellSizeResults.plotConfusionData(91)

# HCal Cell Size
resultsName = 'HCal Cell Size'
reconstructionVariantList = [69,70,71,72,73,74]
detectorModelList = [39,40,85,41,42,43]
xAxisPlottingList = [10,20,30,40,50,100]
xAxisTitle = 'HCal Cell Size [mm^{2}]'

hcalCellSizeResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, True, 0)
hcalCellSizeResults.readData()
hcalCellSizeResults.optimiseData()
hcalCellSizeResults.plotData()
hcalCellSizeResults.generateConfusionTerms()
hcalCellSizeResults.plotConfusionData(500)
hcalCellSizeResults.plotConfusionData(360)
hcalCellSizeResults.plotConfusionData(200)
hcalCellSizeResults.plotConfusionData(91)

# Material
resultsName = 'HCal Absorber Material'
detectorModelList = [85,46,47,48]
reconstructionVariantList = [71,71,71,71]
xAxisPlottingList = [1,2,3,4]
xAxisTitle = 'HCal Absorber Material'

hcalMaterialResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
hcalMaterialResults.readData()
hcalMaterialResults.optimiseData()
hcalMaterialResults.plotDataVsJetEnergy()
hcalMaterialResults.generateConfusionTerms()
hcalMaterialResults.plotConfusionData(500)
hcalMaterialResults.plotConfusionData(360)
hcalMaterialResults.plotConfusionData(200)
hcalMaterialResults.plotConfusionData(91)

# Number of HCal Layers
resultsName = 'Number Of Layers In The HCal'
detectorModelList = [49,50,51,52,53,85,54,55]
reconstructionVariantList = [71,71,71,71,71,71,71,71]
xAxisPlottingList = [18,24,30,36,42,48,54,60]
xAxisTitle = 'Number Of Layers In The HCal'

layerResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
layerResults.readData()
layerResults.optimiseData()
layerResults.plotData()
layerResults.generateConfusionTerms()
layerResults.plotConfusionData(500)
layerResults.plotConfusionData(360)
layerResults.plotConfusionData(200)
layerResults.plotConfusionData(91)

# Number of HCal Interation Lengths
resultsName = 'Number Of Nuclear Interation Lengths In The HCal'
detectorModelList = [56,57,85,58,59]
reconstructionVariantList = [71,71,71,71,71]
xAxisPlottingList = [4.576,5.148,5.72,6.292,6.864]
xAxisTitle = 'Number Of Nuclear Interation Lengths In The HCal [#lambda_{I}]'

lengthResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
lengthResults.readData()
lengthResults.optimiseData()
lengthResults.plotData()
lengthResults.generateConfusionTerms()
lengthResults.plotConfusionData(500)
lengthResults.plotConfusionData(360)
lengthResults.plotConfusionData(200)
lengthResults.plotConfusionData(91)

# Sampling Fraction in HCal
resultsName = 'Sampling Fraction In The HCal'
detectorModelList = [60,61,85,62,63]
reconstructionVariantList = [71,71,71,71,71]
xAxisPlottingList = [0.05,0.10,0.15,0.20,0.25]
xAxisTitle = 'Sampling Fraction In The HCal'

sampFraclengthResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
sampFraclengthResults.readData()
sampFraclengthResults.optimiseData()
sampFraclengthResults.plotData()
sampFraclengthResults.generateConfusionTerms()
sampFraclengthResults.plotConfusionData(500)
sampFraclengthResults.plotConfusionData(360)
sampFraclengthResults.plotConfusionData(200)
sampFraclengthResults.plotConfusionData(91)

# B Field
resultsName = 'Magnetic Field Strength'
detectorModelList = [64,65,66,67,68,85,70,71,72]
reconstructionVariantList = [71,71,71,71,71,71,71,71,71]
xAxisPlottingList = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
xAxisTitle = 'Magentic Field Strength [T]'

bFieldResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
bFieldResults.readData()
bFieldResults.optimiseData()
bFieldResults.plotData()
bFieldResults.generateConfusionTerms()
bFieldResults.plotConfusionData(500)
bFieldResults.plotConfusionData(360)
bFieldResults.plotConfusionData(200)
bFieldResults.plotConfusionData(91)

# ECal Inner Radius
resultsName = 'ECal Inner Radius'
detectorModelList = [73,74,75,85,77]
reconstructionVariantList = [71,71,71,71,71]
xAxisPlottingList = [1208,1408,1608,1808,2008]
xAxisTitle = 'ECal Inner Radius [mm]'

ecalInnerRadResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
ecalInnerRadResults.readData()
ecalInnerRadResults.optimiseData()
ecalInnerRadResults.plotData()
ecalInnerRadResults.generateConfusionTerms()
ecalInnerRadResults.plotConfusionData(500)
ecalInnerRadResults.plotConfusionData(360)
ecalInnerRadResults.plotConfusionData(200)
ecalInnerRadResults.plotConfusionData(91)

