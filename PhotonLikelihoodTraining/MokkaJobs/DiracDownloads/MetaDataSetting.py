import os

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

jobDescription = 'OptimisationStudies'
fileType = 'Sim_PhotonLikelihoodTraining'

detModelList = range(84,104)

#detModelList = [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]

#eventsToSimulate = [ { 'EventType': 'Z_uds', 'Energies': [91, 200, 360, 500] },
#                     { 'EventType': 'Photon', 'Energies': [10] },
#                     { 'EventType': 'Muon', 'Energies': [10] },
#                     { 'EventType': 'Kaon0L', 'Energies': [20] } ]

eventsToSimulate = [ { 'EventType': 'Z_uds', 'Energies': [500] } ]

for detModel in detModelList:
    for eventSelection in eventsToSimulate:
        eventType = eventSelection['EventType']
        fc = FileCatalogClient()
        for energy in eventSelection['Energies']:
            path = '/ilc/user/s/sgreen/' + jobDescription + '/PhotonLikelihoodTraining/MokkaJobs/Detector_Model_' + str(detModel) + '/' + eventType + '/' + str(energy) + 'GeV' 
            pathdict = {'path':path, 'meta':{'Energy':energy, 'EvtType':eventType, 'JobDescription':jobDescription, 'MokkaJobNumber':detModel, 'Type':fileType}}
            res = fc.setMetadata(pathdict['path'], pathdict['meta'])

# Removing Meta Data
#metadata = ['Energy','EvtType','JobDescription','MokkaJobNumber','Type']
#metaDict = {path:metadata}
#result = fc.removeMetadata(metaDict)
