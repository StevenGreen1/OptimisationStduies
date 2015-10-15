import os

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

evtType = 'Z_uds'
jobDescription = 'OptimisationStudies'
detNumbers = [38, 39] #, 40, 41, 42, 49, 50, 51, 60, 61, 62, 63]
recoStages = [69, 70, 71, 72, 73, 74, 75, 76]
fileType = 'Rec'

energies = [91,200,360,500]

fc = FileCatalogClient()
for detNumber in detNumbers:
    for recoStage in recoStages:
        for energy in energies:
            path = '/ilc/user/s/sgreen/' + jobDescription + '/MarlinJobs/Detector_Model_' + str(detNumber) + '/Reco_Stage_' + str(recoStage) + '/' + evtType + '/' + str(energy) + 'GeV'
            pathdict = {'path':path, 'meta':{'Energy':energy, 'EvtType':evtType, 'JobDescription':jobDescription, 'MokkaJobNumber':detNumber, 'ReconstructionVariant':recoStage, 'Type':fileType}}
            res = fc.setMetadata(pathdict['path'], pathdict['meta'])
