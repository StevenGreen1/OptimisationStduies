import os

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

evtType = 'Z_uds'
jobDescription = 'OptimisationStudies'
detNumbers = range(90,96) 
recoStages = [63,79] 
fileType = 'Results'

energies = [91,200,360,500]

fc = FileCatalogClient()
for detNumber in detNumbers:
    for recoStage in recoStages:
        for energy in energies:
            path = '/ilc/user/s/sgreen/' + jobDescription + '/AnalysePerformance/Detector_Model_' + str(detNumber) + '_Run4/Reco_Stage_' + str(recoStage) + '/' + evtType + '/' + str(energy) + 'GeV'
            pathdict = {'path':path, 'meta':{'Energy':energy, 'EvtType':evtType, 'JobDescription':jobDescription, 'MokkaJobNumber':detNumber, 'ReconstructionVariant':recoStage, 'Type':fileType}}
            res = fc.setMetadata(pathdict['path'], pathdict['meta'])

