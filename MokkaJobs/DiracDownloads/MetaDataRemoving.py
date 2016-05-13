import os

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

evtType = 'Z_uds'
jobDescription = 'OptimisationStudies'
detNumbers = range(84,104) 
recoStages = range(71,72) 

fc = FileCatalogClient()
for detNumber in detNumbers:
#    path = '/ilc/user/s/sgreen/' + jobDescription + '/MokkaJobs/Detector_Model_' + str(detNumber) + '/Z_uds/91GeV'
#    metadata = ['Energy','EvtType','JobDescription','MokkaJobNumber','Type']
#    metaDict = {path:metadata}
#    result = fc.removeMetadata(metaDict)
#
#    path = '/ilc/user/s/sgreen/' + jobDescription + '/MokkaJobs/Detector_Model_' + str(detNumber) + '/Z_uds/200GeV'
#    metadata = ['Energy','EvtType','JobDescription','MokkaJobNumber','Type']
#    metaDict = {path:metadata}
#    result = fc.removeMetadata(metaDict)

#    path = '/ilc/user/s/sgreen/' + jobDescription + '/MokkaJobs/Detector_Model_' + str(detNumber) + '/Z_uds/360GeV'
#    metadata = ['Energy','EvtType','JobDescription','MokkaJobNumber','Type']
#    metaDict = {path:metadata}
#    result = fc.removeMetadata(metaDict)

#    path = '/ilc/user/s/sgreen/' + jobDescription + '/MokkaJobs/Detector_Model_' + str(detNumber) + '/Z_uds/500GeV'
#    metadata = ['Energy','EvtType','JobDescription','MokkaJobNumber','Type']
#    metaDict = {path:metadata}
#    result = fc.removeMetadata(metaDict)
#
    path = '/ilc/user/s/sgreen/' + jobDescription + '/MokkaJobs/Detector_Model_' + str(detNumber) + '/Photon/100GeV'
    metadata = ['Energy','EvtType','JobDescription','MokkaJobNumber','Type']
    metaDict = {path:metadata}
    result = fc.removeMetadata(metaDict)

#    path = '/ilc/user/s/sgreen/' + jobDescription + '/MokkaJobs/Detector_Model_' + str(detNumber) + '/Kaon0L/20GeV'
#    metadata = ['Energy','EvtType','JobDescription','MokkaJobNumber','Type']
#    metaDict = {path:metadata}
#    result = fc.removeMetadata(metaDict)

#    path = '/ilc/user/s/sgreen/' + jobDescription + '/MokkaJobs/Detector_Model_' + str(detNumber) + '/Muon/10GeV'
#    metadata = ['Energy','EvtType','JobDescription','MokkaJobNumber','Type']
#    metaDict = {path:metadata}
#    result = fc.removeMetadata(metaDict)
