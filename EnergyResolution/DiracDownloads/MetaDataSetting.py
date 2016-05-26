import os

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

jobDescription = 'OptimisationStudies_ECalStudies'
evtTypeList = ['Kaon0L','Photon']
detModelList = range(84,104)
recoStageList = [71, 38, 63]
fileType = 'EResResults'

fc = FileCatalogClient()
for detNumber in detModelList:
    for recoStage in recoStageList:
        for evtType in evtTypeList:
            path = '/ilc/user/s/sgreen/' + jobDescription + '/EnergyResolution/Detector_Model_' + str(detNumber) + '/Reco_Stage_' + str(recoStage) + '/' + evtType
            pathdict = {'path':path, 'meta':{'EvtType':evtType, 'JobDescription':jobDescription, 'MokkaJobNumber':detNumber, 'ReconstructionVariant':recoStage, 'Type':fileType}}
            res = fc.setMetadata(pathdict['path'], pathdict['meta'])

