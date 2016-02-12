# Example to submit Marlin job: MarlinExample.py
import os
import sys

### ----------------------------------------------------------------------------------------------------
### Start of number of ECal layers information
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

### ----------------------------------------------------------------------------------------------------
### End of number of ECal layers information
### ----------------------------------------------------------------------------------------------------
### Start of ECal absorber info type - Keyed On Detector Model
### ----------------------------------------------------------------------------------------------------

ecalAbsMatType = {}
for detModel in range(1,90):
    ecalAbsMatType[detModel] = 'Si'

ecalAbsMatType[90] = 'Sc'
ecalAbsMatType[91] = 'Sc'
ecalAbsMatType[92] = 'Sc'
ecalAbsMatType[93] = 'Sc'
ecalAbsMatType[94] = 'Sc'
ecalAbsMatType[95] = 'Sc'
ecalAbsMatType[96] = 'Si'
ecalAbsMatType[97] = 'Si'
ecalAbsMatType[98] = 'Si'
ecalAbsMatType[99] = 'Si'
ecalAbsMatType[100] = 'Sc'
ecalAbsMatType[101] = 'Sc'
ecalAbsMatType[102] = 'Sc'
ecalAbsMatType[103] = 'Sc'

### ----------------------------------------------------------------------------------------------------
### End of ECal absorber info type
### ----------------------------------------------------------------------------------------------------
### Start of Realistic Digitisation Options - Keyed On Reconstruction Variant
### ----------------------------------------------------------------------------------------------------

realisticDigi = {}
for recoVar in range(36,61):
    realisticDigi[recoVar] = True

for recoVar in range(61,69):
    realisticDigi[recoVar] = False

for recoVar in range(69,77):
    realisticDigi[recoVar] = True

for recoVar in range(77,85):
    realisticDigi[recoVar] = False

### ----------------------------------------------------------------------------------------------------
### End of Realistic Digitisation Options
### ----------------------------------------------------------------------------------------------------


