import re
import os
import sys

### ----------------------------------------------------------------------------------------------------

def getRootFiles(jobDescription, detModel, recoVar, energy, eventType, pandoraSettings):
    rootFiles = []
    os.system('dirac-ilc-find-in-FC /ilc Energy=' + str(energy) + ' EvtType=' + eventType + ' JobDescription=' + jobDescription + ' MokkaJobNumber=' + str(detModel) + ' ReconstructionVariant=' + str(recoVar) + ' Type=Rec > tmp.txt')
    with open('tmp.txt') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            line = line.strip()
            matchString = pandoraSettings + '.root'
            if matchString in line:
                rootFiles.append(line)
    os.system('rm tmp.txt')
    return rootFiles

### ----------------------------------------------------------------------------------------------------

