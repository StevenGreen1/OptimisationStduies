import os

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

jobDescription = 'OptimisationStudies_ECalStudies'
fileType = 'Sim'

detModelList = range(84,104) 

eventsToSimulate = [ { 'EventType': 'Z_uds', 'Energies': [91, 200, 360, 500] },
                     { 'EventType': 'Photon', 'Energies': [10, 20, 50, 100, 200, 500] },
                     { 'EventType': 'Muon', 'Energies': [10] },
                     { 'EventType': 'Kaon0L', 'Energies': [10, 20, 50, 100, 200, 500] } 
                   ]

for detModel in detModelList:
    for eventSelection in eventsToSimulate:
        eventType = eventSelection['EventType']
        fc = FileCatalogClient()
        for energy in eventSelection['Energies']:
            path = '/ilc/user/s/sgreen/' + jobDescription + '/MokkaJobs/Detector_Model_' + str(detModel) + '/' + eventType + '/' + str(energy) + 'GeV' 
            pathdict = {'path':path, 'meta':{'Energy':energy, 'EvtType':eventType, 'JobDescription':jobDescription, 'MokkaJobNumber':detModel, 'Type':fileType}}
            res = fc.setMetadata(pathdict['path'], pathdict['meta'])
