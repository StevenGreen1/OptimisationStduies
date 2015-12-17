#!/usr/bin/python/Results

# -*- coding: utf-8 -*-

import sys
import re
import math
import os

from MakePlotsLogic import *

#===== User Input =====#
jetEnergyList = [91,200,360,500]
reconstructionVariantList = range(69,77)

# Optimised HCal Cell Size
#resultsName = 'Optimised HCal Cell Size'
#detectorModelList = [39,40,38,41,42,43]
#xAxisPlottingList = [10,20,30,40,50,100]
#xAxisTitle = 'Optimised HCal Cell Size [mm^{2}]'

#hcalCellSizeResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, True)
#hcalCellSizeResults.readData()
#hcalCellSizeResults.optimiseData()
#hcalCellSizeResults.analyseOptimalData()
#hcalCellSizeResults.plotData()

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

#sys.exit()

# ECal Cell Size Silicon
resultsName = 'Silicon ECal Cell Size'
detectorModelList = [84,85,86,87,88,89]
xAxisPlottingList = [3,5,7,10,15,20]
xAxisTitle = 'Silicon ECal Cell Size [mm^{2}]'

ecalCellSizeResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False)
ecalCellSizeResults.readData()
ecalCellSizeResults.optimiseData()
ecalCellSizeResults.plotData()
#ecalCellSizeResults.analyseOptimalData()
ecalCellSizeResults.generateConfusionTerms()
ecalCellSizeResults.plotConfusionData(500)
ecalCellSizeResults.plotConfusionData(91)

# ECal Cell Size Scintillator
resultsName = 'Scintillator ECal Cell Size'
detectorModelList = [90,91,92,93,94,95]
xAxisPlottingList = [3,5,7,10,15,20]
xAxisTitle = 'Scintillator ECal Cell Size [mm^{2}]'

ecalCellSize2Results = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False)
ecalCellSize2Results.readData()
ecalCellSize2Results.optimiseData()
ecalCellSize2Results.plotData()
#ecalCellSize2Results.analyseOptimalData()
ecalCellSize2Results.generateConfusionTerms()
ecalCellSize2Results.plotConfusionData(500)
ecalCellSize2Results.plotConfusionData(91)

sys.exit()

# Material
resultsName = 'HCal Absorber Material'
detectorModelList = [45,46,47,48]
xAxisPlottingList = [1,2,3,4]
xAxisTitle = 'HCal Absorber Material'

hcalMaterialResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False)
hcalMaterialResults.readData()
hcalMaterialResults.optimiseData()
hcalMaterialResults.plotData()

# HCal Cell Size
resultsName = 'HCal Cell Size'
detectorModelList = [39,40,38,41,42,43]
xAxisPlottingList = [10,20,30,40,50,100]
xAxisTitle = 'HCal Cell Size [mm^{2}]'

hcalCellSizeResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, True)
hcalCellSizeResults.readData()
hcalCellSizeResults.optimiseData()
hcalCellSizeResults.analyseOptimalData()
hcalCellSizeResults.plotData()
hcalCellSizeResults.fancyPlot()

# Number of HCal Layers
resultsName = 'Number Of Layers In The HCal'
detectorModelList = [49,50,51,52,53,38,54,55]
xAxisPlottingList = [18,24,30,36,42,48,54,60]
xAxisTitle = 'Number Of Layers In The HCal'

layerResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False)
layerResults.readData()
layerResults.optimiseData()
layerResults.plotData()
layerResults.fancyPlot()

# Number of HCal Interation Lengths
resultsName = 'Number Of Nuclear Interation Lengths In The HCal'
detectorModelList = [56,57,38,58,59]
xAxisPlottingList = [4.576,5.148,5.72,6.292,6.864]
xAxisTitle = 'Number Of Nuclear Interation Lengths In The HCal [#lambda_{I}]'

lengthResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False)
lengthResults.readData()
lengthResults.optimiseData()
lengthResults.plotData()
lengthResults.fancyPlot()

# Sampling Fraction in HCal
resultsName = 'Sampling Fraction In The HCal'
detectorModelList = [60,61,38,62,63]
xAxisPlottingList = [0.05,0.10,0.15,0.20,0.25]
xAxisTitle = 'Sampling Fraction In The HCal'

sampFraclengthResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False)
sampFraclengthResults.readData()
sampFraclengthResults.optimiseData()
sampFraclengthResults.plotData()
sampFraclengthResults.fancyPlot()

# B Field
resultsName = 'Magnetic Field Strength'
detectorModelList = [64,65,66,67,68,69,70,71,72]
xAxisPlottingList = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
xAxisTitle = 'Magentic Field Strength [T]'

bFieldResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False)
bFieldResults.readData()
bFieldResults.optimiseData()
bFieldResults.plotData()
bFieldResults.fancyPlot()

# Sampling Fraction in HCal
resultsName = 'ECal Inner Radius'
detectorModelList = [73,74,75,76,77]
xAxisPlottingList = [1208,1408,1608,1808,2008]
xAxisTitle = 'ECal Inner Radius [mm]'

ecalInnerRadResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False)
ecalInnerRadResults.readData()
ecalInnerRadResults.optimiseData()
ecalInnerRadResults.plotData()
ecalInnerRadResults.fancyPlot()


