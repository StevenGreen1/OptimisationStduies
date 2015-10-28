# Example to submit Marlin job: MarlinExample.py
import os
import sys

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from ILCDIRAC.Interfaces.API.DiracILC import  DiracILC
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import *
from ILCDIRAC.Interfaces.API.NewInterface.Applications import *

from EnergyResolutionAnalysisGridJobs import *

#===== User Input =====

jobDescription = 'OptimisationStudies'
detModel = sys.argv[1] 
recoVar = sys.argv[2]
#eventsToSimulate = [ { 'EventType': "Kaon0L", 'Energies': [1,2,3,4,5,6,7,8,9,10,15,20,25,30,35,40,45,50] } ]
eventsToSimulate = [ { 'EventType': "Kaon0L", 'Energies': [1,2,5,10,15,20,25,30,40,50] } ]
pandoraSettings = 'Default'

#===== Second level user input =====

#=====

# Start submission
JobIdentificationString = jobDescription + '_AnalysePerformance'
diracInstance = DiracILC(withRepo=True,repoLocation="%s.cfg" %( JobIdentificationString))

for eventSelection in eventsToSimulate:
    eventType = eventSelection['EventType']
    allRootFilesToUse = []
    runFile = open("RunFile.txt", "a")

    for energy in eventSelection['Energies']:
        runFile.write('Kaon0L_Energy_' + str(energy) + '\n')
        rootFilesToProcess = getRootFiles(jobDescription,detModel,recoVar,energy,eventType,pandoraSettings)
        
        allRootFilesToUse.extend(rootFilesToProcess[:10])
        for rootFile in rootFilesToProcess[:10]:
            path, fileName = os.path.split(rootFile)
            runFile.write("%s\n" % fileName)
        runFile.write('===End_Entry===' + '\n')
    runFile.close()

    arguements = [
                   str(recoVar),
                   'RunFile.txt',
                   'EnergyResolution_PandoraSettings' + pandoraSettings + '_DetectorModel_' + str(detModel) + '_Reco_Stage_' + str(recoVar) + '_' + eventType + '.root'
                 ]
    outputFiles = arguements[2:]

    genericApplication = GenericApplication()
    genericApplication.setScript('SingleParticleResolution.exe')
    genericApplication.setArguments(' '.join(arguements))
    genericApplication.setDependency({'Marlin':'ILCSoft-01-17-07'})

    job = UserJob()
    job.setJobGroup(JobIdentificationString)
    job.setInputSandbox(['LFN:/ilc/user/s/sgreen/EnergyResolutionTarBall/lib.tar.gz', 'RunFile.txt']) 
    job.setInputData(allRootFilesToUse)
    job.setOutputData(outputFiles,OutputPath='/OptimisationStudies/EnergyResolution/Detector_Model_' + str(detModel) + '/Reco_Stage_' + str(recoVar) + '/' + eventType)
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
