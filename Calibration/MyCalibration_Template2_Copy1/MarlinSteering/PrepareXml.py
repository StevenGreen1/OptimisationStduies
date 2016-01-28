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


#===========================
# Input Variables
#===========================

print sys.argv

particle = sys.argv[1]
energy = sys.argv[2]
slcioPath = sys.argv[3] 
slcioFormat = sys.argv[4] #ILD_o1_v06_GJN${detModel}_ENERGY_GeV_Energy_PARTICLE_pdg_SN_(.*?).slcio
gearFile = sys.argv[5]
pandoraSettingsDefault = sys.argv[6]

#===========================

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#particleNumber = 0

#if 'Photon' in particle:
#    particleNumber = 22
#elif 'Muon' in particle:
#    particleNumber = 13
#elif 'Kaon0L' in particle:
#    particleNumber = 130

jobName = energy + '_GeV_' + particle

slcioFormat = re.sub('ENERGY',energy,slcioFormat)
slcioFormat = re.sub('PARTICLE',particle,slcioFormat)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#===========================
# Calibration Numbers
#===========================
CalibrECal = sys.argv[7]
CalibrECal2 = 2 * float(CalibrECal)
CalibrECal = str(CalibrECal) + ' ' + str(CalibrECal2)
CalibrHCalBarrel = sys.argv[8]
CalibrHCalEndcap = sys.argv[9]
CalibrHCalOther = sys.argv[10]
ECalBarrelTimeWindowMax = sys.argv[11]
HCalBarrelTimeWindowMax = sys.argv[12]
ECalEndcapTimeWindowMax = sys.argv[13]
HCalEndcapTimeWindowMax = sys.argv[14]
ECalToMIP = sys.argv[15]
HCalToMIP = sys.argv[16]
MuonToMIP = sys.argv[17]
MHHHE = sys.argv[18]
ECalToEm = sys.argv[19]
HCalToEm = sys.argv[20]
ECalToHad = sys.argv[21]
HCalToHad = sys.argv[22]
#===========================

calibrationFilePath = sys.argv[23]

#===========================

baseFile = os.path.join(os.getcwd(), 'ILD_o1_v06_XX_YY.xml')
baseFileName = 'ILD_o1_v06_XX_YY.xml'
marlinPath = calibrationFilePath + 'MarlinXml'
rootFilePath = calibrationFilePath + 'RootFiles'

jobList = ''

base = open(baseFile,'r')
baseContent = base.read()
base.close()

fileDirectory = slcioPath
allFilesInDirectory = dircache.listdir(fileDirectory)
inputFileExt = 'slcio'

allFiles = []
allFiles.extend(allFilesInDirectory)
allFiles[:] = [ item for item in allFiles if re.match('.*\.'+inputFileExt+'$',item.lower()) ]
allFiles.sort()

if allFiles:
    array_size=len(allFiles)
    
    for nfiles in range (array_size):
        newContent = baseContent
        nextFile = allFiles.pop(0)
        matchObj = re.match(slcioFormat, nextFile, re.M|re.I)
        
        if matchObj:
            SN = matchObj.group(1)
            
            # Marlin Xml and Root File Name
            newFileName = re.sub('XX_YY',jobName + '_SN_' + SN,baseFileName)
            marlinFullPath = os.path.join(marlinPath, newFileName)
            rootFileFullPath = os.path.join(rootFilePath, 'ILD_o1_v06_' + jobName + '_SN_' + SN + '.root')

            # Root Files
            newContent = re.sub('ROOTFILEDEFAULT_XXXX',rootFileFullPath,newContent)

            # Pandora Settings Files
            newContent = re.sub('PANDORASETTINGSDEFAULT_XXXX',pandoraSettingsDefault,newContent)

            # Slcio File
            newContent = re.sub('LCIO_INPUT_FILE',slcioPath + nextFile,newContent)

            # Gear File
            newContent = re.sub('GEAR_FILE',gearFile,newContent)
            
            # Digitisation Constants
            newContent = re.sub('CALIBR_ECAL_XXXX',CalibrECal,newContent)
            newContent = re.sub('CALIBR_HCAL_BARREL_XXXX',CalibrHCalBarrel,newContent)
            newContent = re.sub('CALIBR_HCAL_ENDCAP_XXXX',CalibrHCalEndcap,newContent)
            newContent = re.sub('CALIBR_HCAL_OTHER_XXXX',CalibrHCalOther,newContent)
            newContent = re.sub('CALIBR_MUON_XXXX','56.7',newContent)
            newContent = re.sub('ECALBARRELTIMEWINDOWMAX_XXXX',ECalBarrelTimeWindowMax,newContent)
            newContent = re.sub('HCALBARRELTIMEWINDOWMAX_XXXX',HCalBarrelTimeWindowMax,newContent)
            newContent = re.sub('ECALENDCAPTIMEWINDOWMAX_XXXX',ECalEndcapTimeWindowMax,newContent)
            newContent = re.sub('HCALENDCAPTIMEWINDOWMAX_XXXX',HCalEndcapTimeWindowMax,newContent)

            # Pandora Thresholds
            newContent = re.sub('ECALMIPTHRESHOLD_XXXX','0.5',newContent)
            newContent = re.sub('HCALMIPTHRESHOLD_XXXX','0.3',newContent)

            # Pandora Settings  
            newContent = re.sub('ECALTOMIPCALIBRATION_XXXX',ECalToMIP,newContent)
            newContent = re.sub('HCALTOMIPCALIBRATION_XXXX',HCalToMIP,newContent)
            newContent = re.sub('MUONTOMIPCALIBRATION_XXXX',MuonToMIP,newContent)

            newContent = re.sub('MAXHCALHITHADRONICENERGY_XXXX',MHHHE,newContent)

            newContent = re.sub('ECALTOEMGEVCALIBRATION_XXXX',ECalToEm,newContent)
            newContent = re.sub('HCALTOEMGEVCALIBRATION_XXXX',HCalToEm,newContent)
            newContent = re.sub('ECALTOHADGEVCALIBRATION_XXXX',ECalToHad,newContent)
            newContent = re.sub('HCALTOHADGEVCALIBRATION_XXXX',HCalToHad,newContent)

            file = open(marlinFullPath,'w')
            file.write(newContent)
            file.close()
            
            jobList += marlinFullPath
            jobList += '\n'
            del newContent

runFilePath = os.getcwd() + '/Condor'
file = open(runFilePath + '/MarlinRunFile_' + jobName + '.txt','w')
file.write(jobList)
file.close()
