# Example to submit Marlin job: MarlinExample.py
import os
import sys

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from ILCDIRAC.Interfaces.API.DiracILC import  DiracILC
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import *
from ILCDIRAC.Interfaces.API.NewInterface.Applications import *

from PhotonEnergyResolutionGridJobs import *

#===== User Input =====

jobDescription = 'OptimisationStudies'
recoVar = 71
eventsToSimulate = [ { 'EventType': 'Photon', 'Energies': [100], 'DetectorModels': [96, 97, 98, 99] } ]

#===== Second level user input =====

#=====

# Start submission
JobIdentificationString = jobDescription + '_PhotonEnergyResolution'
diracInstance = DiracILC(withRepo=True,repoLocation="%s.cfg" %( JobIdentificationString))

for eventSelection in eventsToSimulate:
    eventType = eventSelection['EventType']
    for energy in eventSelection['Energies']:
        allRootFilesToUse = []
        for detModel in eventSelection['DetectorModels']:
            runFile = open('RunFile.txt', 'a')
            rootFilesToProcess = getRootFiles(jobDescription,detModel,recoVar,energy,eventType)
            #allRootFilesToUse.extend(rootFilesToProcess[:10]) <- Only look at 10 elements here
            allRootFilesToUse.extend(rootFilesToProcess)
            for rootFile in rootFilesToProcess:
                path, fileName = os.path.split(rootFile)
                runFile.write("%s %s\n" % (fileName, detModel))
            runFile.close()

        sys.exit()

        arguements = [
                       'RunFile.txt',
                       'PhotonEnergyResolution_' + str(energy) + 'GeV_RecoVar' + str(recoVar) + '.root'
                     ]
        outputFiles = arguements[1:]

        genericApplication = GenericApplication()
        genericApplication.setScript('PhotonResolution.exe')
        genericApplication.setArguments(' '.join(arguements))
        genericApplication.setDependency({'Marlin':'ILCSoft-01-17-07'})

        job = UserJob()
        job.setJobGroup(JobIdentificationString)
        job.setInputSandbox(['LFN:/ilc/user/s/sgreen/PhotonEnergyResolutionTarBall/lib.tar.gz', 'RunFile.txt']) 
        job.setInputData(allRootFilesToUse)
        job.setOutputData(outputFiles,OutputPath='/OptimisationStudies/PhotonEnergyResolution/SiECalLayers/Reco_Stage_' + str(recoVar) + '/' + eventType + '/' + str(energy))
        job.setName(JobIdentificationString)
        job.setBannedSites(['LCG.IN2P3-CC.fr','LCG.IN2P3-IRES.fr','LCG.KEK.jp','OSG.CIT.us'])
        job.dontPromptMe()
        res = job.append(genericApplication)

        if not res['OK']:
            print res['Message']
            exit()
        job.submit(diracInstance)

        # Tidy Up
        os.system('rm *.cfg')
        os.system('rm RunFile.txt')
