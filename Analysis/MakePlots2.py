#!/usr/bin/python/Results

# -*- coding: utf-8 -*-

import sys
import re
import math
import os

from MakePlotsLogic2 import *

#===== User Input =====#
jetEnergyList = [91,200,360,500,750,1000,2000,3000]
reconstructionVariantList = range(0,1)

# Material
resultsName = 'High Energy Jets'
detectorModelList = [38]
xAxisPlottingList = [1]
xAxisTitle = 'High Energy Jets'

hcalMaterialResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False, 71)
hcalMaterialResults.readData()
hcalMaterialResults.optimiseData()
hcalMaterialResults.printData()
hcalMaterialResults.plotDataVsJetEnergy()

