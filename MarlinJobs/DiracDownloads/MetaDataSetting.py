import os

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

evtType = 'Kaon0L'
jobDescription = 'OptimisationStudies'
detNumbers = [38] #range(44,78) 
recoStages = [38,43,46,51,54,59]
fileType = 'Rec'

energies = [1,2,3,4,5,6,7,8,9,10,15,20,25,30,35,40,45,50]

fc = FileCatalogClient()
for detNumber in detNumbers:
    for recoStage in recoStages:
        for energy in energies:
            path = '/ilc/user/s/sgreen/' + jobDescription + '/MarlinJobs/Detector_Model_' + str(detNumber) + '/Reco_Stage_' + str(recoStage) + '/' + evtType + '/' + str(energy) + 'GeV'
            pathdict = {'path':path, 'meta':{'Energy':energy, 'EvtType':evtType, 'JobDescription':jobDescription, 'MokkaJobNumber':detNumber, 'ReconstructionVariant':recoStage, 'Type':fileType}}
            res = fc.setMetadata(pathdict['path'], pathdict['meta'])

