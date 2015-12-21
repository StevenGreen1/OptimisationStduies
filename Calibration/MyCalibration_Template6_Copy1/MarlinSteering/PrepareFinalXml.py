# -*- coding: utf-8 -*-
import os
import re
import random
import dircache
import sys

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ''

#======================
# Calibration Constants
#======================
CalibrECal_Input = sys.argv[2]
CalibrECal_Input2 = 2 * float(CalibrECal_Input)
CalibrECal = str(CalibrECal_Input) + ' ' + str(CalibrECal_Input2)
CalibrHCalBarrel = sys.argv[3]
CalibrHCalEndcap = sys.argv[4]
CalibrHCalOther = sys.argv[5]
ECalBarrelTimeWindowMax = sys.argv[6]
HCalBarrelTimeWindowMax = sys.argv[7]
ECalEndcapTimeWindowMax = sys.argv[8]
HCalEndcapTimeWindowMax = sys.argv[9]
CalibrMuon = '56.7'
ECalGeVToMIP = sys.argv[10]
HCalGeVToMIP = sys.argv[11]
MuonGeVToMIP = sys.argv[12]
MHHHE = sys.argv[13]
ECalToEm = sys.argv[14]
HCalToEm = sys.argv[15]
ECalToHad = sys.argv[16]
HCalToHad = sys.argv[17]
ECalMipThresholdPandora = '0.5'
HCalMipThresholdPandora = '0.3'

#======================
# Output Path
#======================

outputPath = sys.argv[1]

#======================

baseFileName = 'ILD_o1_v06_XX_YY.xml'

jobList = ''

base = open(baseFileName,'r')
baseContent = base.read()
base.close()

newContent = baseContent

newContent = re.sub('CALIBR_ECAL_XXXX',CalibrECal,newContent)
newContent = re.sub('CALIBR_HCAL_BARREL_XXXX',CalibrHCalBarrel,newContent)
newContent = re.sub('CALIBR_HCAL_ENDCAP_XXXX',CalibrHCalEndcap,newContent)
newContent = re.sub('CALIBR_HCAL_OTHER_XXXX',CalibrHCalOther,newContent)
newContent = re.sub('ECALBARRELTIMEWINDOWMAX_XXXX',ECalBarrelTimeWindowMax,newContent)
newContent = re.sub('HCALBARRELTIMEWINDOWMAX_XXXX',HCalBarrelTimeWindowMax,newContent)
newContent = re.sub('ECALENDCAPTIMEWINDOWMAX_XXXX',ECalEndcapTimeWindowMax,newContent)
newContent = re.sub('HCALENDCAPTIMEWINDOWMAX_XXXX',HCalEndcapTimeWindowMax,newContent)
newContent = re.sub('CALIBR_MUON_XXXX',CalibrMuon,newContent)
newContent = re.sub('ECALTOMIPCALIBRATION_XXXX',ECalGeVToMIP,newContent)
newContent = re.sub('HCALTOMIPCALIBRATION_XXXX',HCalGeVToMIP,newContent)
newContent = re.sub('MUONTOMIPCALIBRATION_XXXX',MuonGeVToMIP,newContent)
newContent = re.sub('MAXHCALHITHADRONICENERGY_XXXX',MHHHE,newContent)
newContent = re.sub('ECALTOEMGEVCALIBRATION_XXXX',ECalToEm,newContent)
newContent = re.sub('HCALTOEMGEVCALIBRATION_XXXX',HCalToEm,newContent)
newContent = re.sub('ECALTOHADGEVCALIBRATION_XXXX',ECalToHad,newContent)
newContent = re.sub('HCALTOHADGEVCALIBRATION_XXXX',HCalToHad,newContent)
newContent = re.sub('ECALMIPTHRESHOLD_XXXX',ECalMipThresholdPandora,newContent)
newContent = re.sub('HCALMIPTHRESHOLD_XXXX',HCalMipThresholdPandora,newContent)

fullPath = os.path.join(outputPath, 'ILD_o1_v06_AAxAA_BBxBB_XX_YY.xml')

file = open(fullPath,'w')
file.write(newContent)
file.close()


