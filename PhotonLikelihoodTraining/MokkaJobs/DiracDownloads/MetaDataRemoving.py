import os

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

jobDescription = 'OptimisationStudies'
detModelList = range(84,104)
eventsToSimulate = [ { 'EventType': 'Z_uds', 'Energies': [500] } ]

for detModel in detModelList:
    for eventSelection in eventsToSimulate:
        eventType = eventSelection['EventType']
        fc = FileCatalogClient()
        for energy in eventSelection['Energies']:
            path = '/ilc/user/s/sgreen/' + jobDescription + '/PhotonLikelihoodTraining/MokkaJobs/Detector_Model_' + str(detModel) + '/' + eventType + '/' + str(energy) + 'GeV'
            metadata = ['Energy','EvtType','JobDescription','MokkaJobNumber','Type']
            metaDict = {path:metadata}
            result = fc.removeMetadata(metaDict)

