# Example to submit AnalysePerformance job: SubmitAnalysePerformance.py
import os
import sys

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from ILCDIRAC.Interfaces.API.DiracILC import  DiracILC
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import *
from ILCDIRAC.Interfaces.API.NewInterface.Applications import *

from Logic.AnalysePerformanceGridJobs import *

#===== User Input =====

jobDescription = 'OptimisationStudies_ECalStudies'
detModel = sys.argv[1] 
recoVar = sys.argv[2]
eventsToSimulate = [ { 'EventType': "Z_uds", 'Energies': [91, 200, 360, 500] } ]
pandoraSettings = sys.argv[3]

#===== Second level user input =====

#=====

# Start submission
JobIdentificationString = jobDescription + '_AnalysePerformance_DetectorModel_' + str(detModel) + '_ReconstructionVariant_' + str(recoVar) + '_PandoraSettings' + pandoraSettings
diracInstance = DiracILC(withRepo=True,repoLocation="%s.cfg" %( JobIdentificationString))

for eventSelection in eventsToSimulate:
    eventType = eventSelection['EventType']
    for energy in eventSelection['Energies']:
        rootFilesToProcess = getRootFiles(jobDescription,detModel,recoVar,energy,eventType,pandoraSettings)

#        rootFilesToProcess = rootFilesToProcess[:1] # Testing with one file.

        runFileName = 'runfile.txt'
        runFile = open(runFileName,'w')
        for rootFile in rootFilesToProcess:
            path, fileName = os.path.split(rootFile)
            runFile.write("%s\n" % fileName)
        runFile.close()

        arguements = [
                       'runfile.txt',
                       'AnalysePerformance_PandoraSettings' + pandoraSettings + '_DetectorModel_' + str(detModel) + '_Reco_Stage_' + str(recoVar) + '_' + eventType + '_' + str(energy) + 'GeV.root',
                       'AnalysePerformance_PandoraSettings' + pandoraSettings + '_DetectorModel_' + str(detModel) + '_Reco_Stage_' + str(recoVar) + '_' + eventType + '_' + str(energy) + 'GeV.txt'
                     ]

        outputFiles = arguements[1:]
        outputPath = '/' + jobDescription + '/AnalysePerformance/Detector_Model_' + str(detModel) + '/Reco_Stage_' + str(recoVar) + '/' + eventType + '/' + str(energy) + 'GeV'

        lfn = '/ilc/user/s/sgreen/' + outputPath + '/' + arguements[1]
        if doesFileExist(lfn):
            continue

        genericApplication = GenericApplication()
        genericApplication.setScript('AnalysePerformance')
        genericApplication.setArguments(' '.join(arguements))
        genericApplication.setDependency({'ROOT':'5.34'})

        job = UserJob()
        job.setJobGroup(JobIdentificationString)
        job.setInputSandbox(['LFN:/ilc/user/s/sgreen/AnalysePerformanceTarBall/lib.tar.gz', 'runfile.txt']) 
        job.setInputData(rootFilesToProcess)
        job.setOutputData(outputFiles,OutputPath=outputPath)

        job.setName(JobIdentificationString)
        job.setBannedSites(['LCG.IN2P3-CC.fr','LCG.IN2P3-IRES.fr','LCG.KEK.jp','OSG.PNNL.us','OSG.CIT.us','LCG.LAPP.fr'])
        job.dontPromptMe()
        #job.setCPUTime(1000)
        res = job.append(genericApplication)

        if not res['OK']:
            print res['Message']
            exit()
        print 'Submitting job. (' + str(detModel) + ', ' + str(recoVar) + ', ' + eventType + ', ' + str(energy) + ')'
        job.submit(diracInstance)
        os.system('rm *.cfg')
        os.system('rm runfile.txt')

# Tidy Up
