import os
import sys
import re
import time
import threading

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from DIRAC.DataManagementSystem.Client.DataManager import DataManager
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient
from DIRAC.Core.Utilities.ReturnValues import returnSingleResult

#=================================

jobDescription = 'OptimisationStudies'

eventsToDownload = [
#                       { 'DetectorModel' : 38, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 39, 'ReconstructionVariant' : 69, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 40, 'ReconstructionVariant' : 70, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 41, 'ReconstructionVariant' : 72, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 42, 'ReconstructionVariant' : 73, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
                       { 'DetectorModel' : 43, 'ReconstructionVariant' : 74, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 45, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 46, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 47, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 48, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 49, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 50, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 51, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 52, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 53, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 54, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 55, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 56, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 57, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 58, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 59, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 60, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 61, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 62, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 63, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 64, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 65, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 66, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 67, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 68, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 69, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 70, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 71, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 72, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 73, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 74, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 75, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 76, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 77, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] }
                   ]

maxThread = 100

#=================================

def downloadFile(dm, lfn, localFolder):
    res = returnSingleResult(dm.getFile(lfn, localFolder))
    if not res or not res['OK']:
        print "Error with file %s"%lfn
        print res
    else:
        print "Downloaded %s"%lfn

class ActivePool(object):
    def __init__(self):
        super(ActivePool, self).__init__()
        self.active = []
        self.lock = threading.Lock()
    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)

def worker(threadingSemaphore, pool, dm, lfn, localFolder):
    with threadingSemaphore:
        name = threading.currentThread().getName()
        pool.makeActive(name)
        downloadFile(dm, lfn, localFolder)
        pool.makeInactive(name)

#=================================

fc = FileCatalogClient()
dm = DataManager()

pool = ActivePool()
threadingSemaphore = threading.Semaphore(maxThread)

for eventSelection in eventsToDownload:
    detectorModel = eventSelection['DetectorModel']
    reconstructionVariant = eventSelection['ReconstructionVariant']
    eventType = eventSelection['EventType']
    for energy in eventSelection['Energies']:
        for settings in eventSelection['ReconstructionSettings']:
            localPath = '/r02/lc/sg568/' + jobDescription + '/MarlinJobs/Detector_Model_' + str(detectorModel) + '/Reconstruction_Variant_' + str(reconstructionVariant) + '/' + eventType + '/' + str(energy) + 'GeV/PandoraSettings' + settings
            if not os.path.exists(localPath):
                os.makedirs(localPath)

            gridPath = '/ilc/user/s/sgreen/' + jobDescription + '/MarlinJobs/Detector_Model_' + str(detectorModel) + '_Run2/Reco_Stage_' + str(reconstructionVariant) + '/' + eventType + '/' + str(energy) + 'GeV'
            meta = {}
            meta['Owner'] = 'sgreen'

            res = fc.findFilesByMetadata(meta, gridPath)
            if not res['OK']:
                print res['Message']

            lfns = res['Value']
            fileFormat = 'MarlinReco_ILD_o1_v06_GJN' + str(detectorModel) + '_uds' + str(energy) + '_(.*?)_' + settings + '.root'

            for lfn in lfns:
                localFile = os.path.basename(lfn)
                matchObj = re.match(fileFormat, localFile, re.M|re.I)
                if not matchObj:
                    continue

                localFileNameAndPath = os.path.join(localPath, localFile)
                #print localFileNameAndPath

                if os.path.isfile(localFileNameAndPath):
                    #print 'File exists'
                    continue
                else: 
                    #print 'File does not exist'
                    while threading.activeCount() > (maxThread * 2):
                        time.sleep(5)

                    downloadThread = threading.Thread(target=worker, name=str(localFileNameAndPath), args=(threadingSemaphore, pool, dm, lfn, localPath))
                    downloadThread.start()

currentThread = threading.currentThread()

for thread in threading.enumerate():
    if thread is currentThread:
        continue
    thread.join(500)

print 'Download script has finished.'
