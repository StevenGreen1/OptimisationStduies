#!/usr/bin/python

import os, sys, getopt, re, subprocess, math, dircache

class Calibration:
    'Common base class for all calibration process'

### ----------------------------------------------------------------------------------------------------
### Start of constructor
### ----------------------------------------------------------------------------------------------------

    def __init__(self, slcioFormat, slcioPath, gearFile, pandoraSettings, outputPath, timingCut, hadronicEnergyTrunc):
        'Calibration File'
        self._OutputPath = outputPath
        self._CalibrationFile = os.path.join(outputPath, '/Calibration.txt')

        'Default Energies Of Calibration Particles'
        self._Kaon0LEnergyCalibration = 20
        self._MuonEnergyCalibration = 10
        self._PhotonEnergyCalibration = 10

        'Root File Info'
        self._RootFileFolder = os.path.join(os.getcwd(), '/RootFiles') 

        self._Kaon0LRootFiles = os.path.join(self._RootFileFolder, '/ILD_o1_v06_' + str(self._Kaon0LEnergyCalibration) + '_GeV_Kaon0L_SN_*.root')
        self._PhotonRootFiles = os.path.join(self._RootFileFolder, '/ILD_o1_v06_' + str(self._PhotonEnergyCalibration) + '_GeV_Photon_SN_*.root')
        self._MuonRootFiles = os.path.join(self._RootFileFolder, '/ILD_o1_v06_' + str(self._MuonEnergyCalibration) + '_GeV_Muon_SN_*.root')

        'Slcio Path Information'
        self._SlcioFormat = slcioFormat
        self._SlcioPath = slcioPath

        'Gear File'
        self._GearFile = gearFile

        'Detector Info'
        self._NumberHCalLayers = 48

        'Pandora Settings File'
        self._PandoraSettingsFile = pandoraSettings

        'ECal Calibration Variables'
        self._CalibrECal = 42.77
        self._ECalBarrelTimeWindowMax = timingCut
        self._ECalEndCapTimeWindowMax = timingCut
        self._ECalGeVToMIP = 160.0
        self._ECalMIPMPV = 0.00015
        self._ECalToEm = 0.9995
        self._ECalToHad = 1.076

        'HCal Calibration Variables'
        self._CalibrHCalBarrel = 43.58
        self._CalibrHCalEndCap = 50.26
        self._CalibrHCalOther = 26.76
        self._HCalBarrelTimeWindowMax = timingCut
        self._HCalEndCapTimeWindowMax = timingCut
        self._HCalGeVToMIP = 34.8
        self._HCalMIPMPV = 0.00004
        self._MHHHE = hadronicEnergyTrunc
        self._HCalToEm = 1.075
        self._HCalToHad = 1.075

        self._CalibrHCalBarrel = self._CalibrHCalBarrel * 48 / self._NumberHCalLayers
        self._CalibrHCalEndCap = self._CalibrHCalEndCap * 48 / self._NumberHCalLayers

        'Muon Chamber Calibration Variables'
        self._MuonGeVToMIP = 10.0

        'Condor'
        self._UseCondor = True
        self._CondorRunList = []
        self._CondorMaxRuns = 500 

        'Pandora Analysis'
        self._PandoraAnalysisPath = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudies/PandoraAnalysis_OptimisationStudies/LCPandoraAnalysis/bin'
        self._HadronicScaleSettingPandora = 'CSM' # or 'TEM'

        'Precision of Calibration'
        self._DigitisationPrecision = 0.05 # 5%
        self._PandoraPFAPrecision = 0.005 # 0.5%

        'Physical Constants'
        self._Kaon0LMass = 0.497614

        self._Kaon0LKineticEnergy = math.sqrt(self._Kaon0LEnergyCalibration * self._Kaon0LEnergyCalibration - self._Kaon0LMass * self._Kaon0LMass)

        self.calibrationProcess()

### ----------------------------------------------------------------------------------------------------
### End of constructor
### ----------------------------------------------------------------------------------------------------
### Start of calibration process function
### ----------------------------------------------------------------------------------------------------

    def calibrationProcess(self):
        rootDirectory = os.path.join(os.getcwd(), 'RootFiles')
        if not os.path.exists(rootDirectory):
            os.makedirs(rootDirectory)

        marlinDirectory = os.path.join(os.getcwd(), 'MarlinXml')
        if not os.path.exists(marlinDirectory):
            os.makedirs(marlinDirectory)

        if os.path.isfile(self._CalibrationFile):
            os.remove(self._CalibrationFile)

        self.prepareSteeringFiles('Muon',self._MuonEnergyCalibration)
        self.runCondorJobs()
        executable = os.path.join(self._PandoraAnalysisPath,'SimCaloHitEnergyDistribution')
        subprocess.Popen([executable, '-a', self._MuonRootFiles, '-b', str(self._MuonEnergyCalibration), '-c', self._OutputPath])

### ----------------------------------------------------------------------------------------------------
### End of calibration process function
### ----------------------------------------------------------------------------------------------------
### Start of prepareSteeringFiles function
### ----------------------------------------------------------------------------------------------------

    def prepareSteeringFiles(self,particle,activeParticleEnergy):
        jobName = str(activeParticleEnergy) + '_GeV_' + particle

        activeSlcioFormat = self._SlcioFormat
        activeSlcioFormat = re.sub('ENERGY',str(activeParticleEnergy),activeSlcioFormat)
        activeSlcioFormat = re.sub('PARTICLE',particle,activeSlcioFormat)

        currentDirectory = os.getcwd()
        oneUpDirectory = os.path.dirname(currentDirectory)

        baseFileName = 'ILD_o1_v06_Calibration_XX_YY.xml'
        baseSteeringFile = os.path.join(currentDirectory, 'ILD_o1_v06_XX_YY.xml')
        marlinPath = os.path.join(oneUpDirectory,'MarlinXml')
        rootFilePath = os.path.join(oneUpDirectory,'RootFiles')

        jobList = [] # runFileText = ''

        # Get Template Steering Files
        base = open(baseSteeringFile,'r')
        baseContent = base.read()
        base.close()

        # Read All Files in Slcio Directory
        fileDirectory = self._SlcioPath
        allFilesInDirectory = dircache.listdir(fileDirectory)
        inputFileExt = 'slcio'

        allFiles = []
        allFiles.extend(allFilesInDirectory)
        # $ is end of line character, either end of string or new line
        # * means match any number of times
        # '.' matches anything except new line
        # \. means search for a . before inputFileExt
        allFiles[:] = [ item for item in allFiles if re.match('.*\.' + inputFileExt + '$', item.lower()) ]
        allFiles.sort()

        # Check there are slcio files
        if not allFiles:
            print 'No files in input slcio folder.'
            return

        array_size=len(allFiles)
        for nfiles in range(array_size):
            newContent = baseContent
            nextFile = allFiles.pop(0)
            matchObj = re.match(self._SlcioFormat, nextFile, re.M|re.I)

            # Check files match
            if not matchObj:
                continue

            SN = matchObj.group(1)

            # Marlin Xml and Root File Name
            newFileName = re.sub('XX_YY',jobName + '_SN_' + SN,baseFileName)
            marlinFullPath = os.path.join(marlinPath, newFileName)
            rootFileFullPath = os.path.join(rootFilePath, 'ILD_o1_v06_' + jobName + '_SN_' + SN + '.root')

            # Root Files
            newContent = re.sub('PANDORA_SETTINGS_DEFAULT_ROOT_FILE',self._RootFileFolder,newContent)

            # Pandora Settings Files
            newContent = re.sub('PANDORA_SETTINGS_DEFAULT_FILE',self._PandoraSettingsFile,newContent)

            # Slcio File
            slcioFileName = self._SlcioFormat + nextFile
            newContent = re.sub('LCIO_INPUT_FILE',slcioFileName,newContent)

            # Gear File
            newContent = re.sub('GEAR_FILE',self._GearFile,newContent)

            # ECal
            newContent = re.sub('CALIBRECAL_XXXX',self._CalibrECal,newContent)
            newContent = re.sub('ECALBARRELTIMEWINDOWMAX_XXXX',self._ECalBarrelTimeWindowMax,newContent)
            newContent = re.sub('ECALENDCAPTIMEWINDOWMAX_XXXX',self._ECalEndCapTimeWindowMax,newContent)
            newContent = re.sub('ECALTOMIP_XXXX',self._ECalGeVToMIP,newContent)
            newContent = re.sub('ECALMIPMPV_XXXX',self._ECalMIPMPV,newContent)
            newContent = re.sub('ECALTOEM_XXXX',self._ECalToEm,newContent)
            newContent = re.sub('ECALTOHAD_XXXX',self._ECalToHad,newContent)

            # HCal
            newContent = re.sub('CALIBRHCALBARREL_XXXX',self._CalibrHCalBarrel,newContent)
            newContent = re.sub('CALIBRHCALENDCAP_XXXX',self._CalibrHCalEndCap,newContent)
            newContent = re.sub('CALIBRHCALOTHER_XXXX',self._CalibrHCalOther,newContent)
            newContent = re.sub('HCALBARRELTIMEWINDOWMAX_XXXX',self._HCalBarrelTimeWindowMax,newContent)
            newContent = re.sub('HCALENDCAPTIMEWINDOWMAX_XXXX',self._HCalEndCapTimeWindowMax,newContent)
            newContent = re.sub('HCALTOMIP_XXXX',self._HCalGeVToMIP,newContent)
            newContent = re.sub('HCALMIPMPV_XXXX',self._HCalMIPMPV,newContent)
            newContent = re.sub('MHHHE_XXXX',self._MHHHE,newContent)
            newContent = re.sub('HCALTOEM_XXXX',self._HCalToEm,newContent)
            newContent = re.sub('HCALTOHAD_XXXX',self._HCalToHad,newContent)

            # Muon Chamber
            newContent = re.sub('CALIBRMUON_XXXX','56.7',newContent)
            newContent = re.sub('MUONTOMIP_XXXX',self._MuonGeVToMIP,newContent)

            file = open(marlinFullPath,'w')
            file.write(newContent)
            file.close()

            jobList.append(marlinFullPath)

        self._CondorRunList = jobList

### ----------------------------------------------------------------------------------------------------
### End of prepareSteeringFiles function
### ----------------------------------------------------------------------------------------------------
### Start of getCondorJobString function
### ----------------------------------------------------------------------------------------------------

    def getCondorJobString(self):
        jobString  = 'executable              = ' + os.getcwd() + '/MarlinCalibration.sh                             \n'
        jobString += 'initial_dir             = ' + os.getcwd() + '                                                  \n'
        jobString += 'notification            = never                                                                \n'
        jobString += 'Requirements            = (memory > 2048) && (OSTYPE == \"SLC6\")                              \n'
        jobString += 'Rank                    = memory                                                               \n'
        jobString += 'output                  = ' + os.environ['HOME'] + '/CondorLogs/Marlin.out                     \n'
        jobString += 'error                   = ' + os.environ['HOME'] + '/CondorLogs/Marlin.err                     \n'
        jobString += 'log                     = ' + os.environ['HOME'] + '/CondorLogs/Marlin.log                     \n'
        jobString += 'environment             = CONDOR_JOB=true                                                      \n'
        jobString += 'Universe                = vanilla                                                              \n'
        jobString += 'getenv                  = false                                                                \n'
        jobString += 'copy_to_spool           = true                                                                 \n'
        jobString += 'should_transfer_files   = yes                                                                  \n'
        jobString += 'when_to_transfer_output = on_exit_or_evict                                                     \n'
        return jobString

### ----------------------------------------------------------------------------------------------------
### End of getCondorJobString function
### ----------------------------------------------------------------------------------------------------
### Start of runCondorJobs function
### ----------------------------------------------------------------------------------------------------

    def runCondorJobs(self):
        # Do condor_q and pipe output to queueOutput
        queueProcess = subprocess.Popen(['condor_q','-w'], stdout=subprocess.PIPE)
        queueOutput = queueProcess.communicate()[0]

        regex = re.compile('Calibration|Marlin')
        queueList = regex.findall(queueOutput)
        nQueued = len(queueList)

        # Sleep for 0.5s if too many jobs queued
        if nQueued >= self._CondorMaxRuns:
            subprocess.call(["usleep", "500000"])

        else:
            for idx, fileToRun in enumerate(self._CondorRunList):
                nRemaining = len(self._CondorRunList) - idx

                with open('tempCalibJob.job', 'w') as jobFile:
                    jobString = getCondorJobString()
                    jobString += 'arguments = ' + fileToRun + '\n'
                    jobString += 'queue 1 \n'
                    jobFile.write(jobString)

                subprocess.call(['condor_submit', 'tempCalibJob.job'])
                print 'Submitted job as there were only ' + str(nQueued) + ' jobs in the queue and ' + str(nRemaining) + ' jobs remaining.'
                subprocess.call(["usleep", "500000"])
                os.remove('tempCalibJob.job')

                if 0 == nRemaining:
                    print 'Runlist empty'
                    return

### ----------------------------------------------------------------------------------------------------
### End of runCondorJobs function
### ----------------------------------------------------------------------------------------------------
