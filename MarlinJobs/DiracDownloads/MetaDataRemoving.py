import os

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

jobDescription = 'OptimisationStudies_ECalStudies'
#detNumbers = range(84,104)
detNumbers = range(90,96) + range(100,104)
#recoStages = [63]
recoStages = [38, 63, 71]
fileType = 'Rec'

eventsToSimulate = [ { 'EventType': 'Z_uds', 'Energies': [91, 200, 360, 500] } ,
                     { 'EventType': 'Kaon0L', 'Energies': [10, 20, 50, 100, 200, 500] },
                     { 'EventType': 'Photon', 'Energies': [10, 20, 50, 100, 200, 500] }
                   ]

fc = FileCatalogClient()

for detNumber in detNumbers:
    for recoStage in recoStages:
        for eventSelection in eventsToSimulate:
            eventType = eventSelection['EventType']
            for energy in eventSelection['Energies']:
                path = '/ilc/user/s/sgreen/' + jobDescription + '/MarlinJobs/Detector_Model_' + str(detNumber) + '/Reco_Stage_' + str(recoStage) + '/' + eventType + '/' + str(energy) + 'GeV'
                metadata = ['Energy','EvtType','JobDescription','MokkaJobNumber','ReconstructionVariant','Type']
                metaDict = {path:metadata}
                result = fc.removeMetadata(metaDict)

