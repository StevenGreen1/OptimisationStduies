import os

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

evtType = 'Kaon0L'
jobDescription = 'OptimisationStudies'
detNumbers = range(45,78) #range(38,44)
recoStages = [71] #range(69,77)
fileType = 'EResResults'

fc = FileCatalogClient()
for detNumber in detNumbers:
    for recoStage in recoStages:
        path = '/ilc/user/s/sgreen/' + jobDescription + '/EnergyResolution/Detector_Model_' + str(detNumber) + '/Reco_Stage_' + str(recoStage) + '/' + evtType
        pathdict = {'path':path, 'meta':{'EvtType':evtType, 'JobDescription':jobDescription, 'MokkaJobNumber':detNumber, 'ReconstructionVariant':recoStage, 'Type':fileType}}
        res = fc.setMetadata(pathdict['path'], pathdict['meta'])

#for detModel in {45..77}
#do
#    for recoVar in 71
#    do
#        python SubmitEnergyResolutionAnalysis.py ${detModel} ${recoVar}
#    done
#done
