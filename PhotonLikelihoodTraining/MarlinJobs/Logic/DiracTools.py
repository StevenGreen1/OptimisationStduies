# Example to submit Marlin job: MarlinExample.py
import os
import sys

### ----------------------------------------------------------------------------------------------------
### Start of getSlcioFiles function
### ----------------------------------------------------------------------------------------------------

def getSlcioFiles(jobDescription, detModel, energy, eventType):
    slcioFiles = []
    os.system('dirac-ilc-find-in-FC /ilc JobDescription=' + jobDescription + ' Type=Sim_PhotonLikelihoodTraining MokkaJobNumber=' + str(detModel) + ' Energy=' + str(energy) + ' EvtType=' + eventType + ' > tmp.txt')
    with open('tmp.txt') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            line = line.strip()
            slcioFiles.append(line)
    os.system('rm tmp.txt')
    return slcioFiles

### ----------------------------------------------------------------------------------------------------
### End of getSlcioFiles function
### ----------------------------------------------------------------------------------------------------
### Start of doesFileExist function
### ----------------------------------------------------------------------------------------------------

def doesFileExist(lfn):
    from DIRAC.DataManagementSystem.Client.DataManager import DataManager
    dm = DataManager()
    result = dm.getActiveReplicas(lfn)
    if result[('Value')][('Successful')]:
        return True
    else:
        return False

### ----------------------------------------------------------------------------------------------------
### End of doesFileExist function
### ----------------------------------------------------------------------------------------------------
