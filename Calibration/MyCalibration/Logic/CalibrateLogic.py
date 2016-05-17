#!/usr/bin/python

import os, sys, getopt, re, subprocess, math, dircache, logging, time, random, string

class Calibration:
    'Common base class for all calibration process'

### ----------------------------------------------------------------------------------------------------
### Start of constructor
### ----------------------------------------------------------------------------------------------------

    def __init__(self, detModelNumber, recoVariant, slcioFormat, slcioPath, gearFile, pandoraSettings, outputPath, timingCut, hadronicEnergyTrunc, ecalType, realisticDigitisation):

        'Detector Model Number'
        self._DetectorModelNumber = detModelNumber

        'Reconstruction Variant Number'
        self._ReconstructionVariant = recoVariant

        'Calibration File'
        self._OutputPath = outputPath

        'Root File Info'
        self._RootFileFolder = os.path.join(self._OutputPath, 'RootFiles') 
        if not os.path.exists(self._RootFileFolder):
            os.makedirs(self._RootFileFolder)

        'Marlin Xml Path'
        self._MarlinXmlPath = os.path.join(self._OutputPath, 'MarlinXml')
        if not os.path.exists(self._MarlinXmlPath):
            os.makedirs(self._MarlinXmlPath)

        'Validation Plots Path'
        self._ResultsPath = os.path.join(self._OutputPath, 'Validation/')
        if not os.path.exists(self._ResultsPath):
            os.makedirs(self._ResultsPath)

        self._CalibrationFile = os.path.join(self._ResultsPath, 'Calibration.txt')
        if os.path.isfile(self._CalibrationFile):
            os.remove(self._CalibrationFile)
        calibrationFile = open(self._CalibrationFile, 'w')
        calibrationFile.close()

        'Logger'
        calibrationLogFullPath = os.path.join(self._ResultsPath, 'calibration.log') 
        if os.path.isfile(calibrationLogFullPath):
            os.remove(calibrationLogFullPath)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(calibrationLogFullPath)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        self.logger.info('Output path : ' + self._OutputPath)

        'Slcio Path Information'
        self._SlcioFormat = slcioFormat
        self._SlcioPath = slcioPath
        self._SlcioFiles = self.getSlcioFiles()

        'Gear File'
        if not os.path.isfile(gearFile):
            self.logger.error('Gear file does not exist!  Exiting calibration.')
            self.logger.error('Gear file : ' + gearFile)
            sys.exit()

        self._GearFile = gearFile

        'Detector Info'
        self._NumberHCalLayers = 48

        'Pandora Settings File'
        if not os.path.isfile(pandoraSettings):
            self.logger.error('Pandora settings file does not exist!  Exiting calibration.')
            self.logger.error('Pandora settings file : ' + pandoraSettings)
            sys.exit()

        self._PandoraSettingsFile = pandoraSettings

        'Si or Sw ECal'
        self._ECalType = ecalType

        'Realistic Digitisation'
        self._RealisticDigitisation = realisticDigitisation
        self._ApplyECalRealisticDigi = 0
        self._ApplyHCalRealisticDigi = 0
        self._ECalMaxDynamicRangeMIP = 0.0 # Set to 0 to avoid accidental truncation if not using realistic digitisation options
        self._HCalMaxDynamicRangeMIP = 0.0 # Set to 0 to avoid accidental truncation if not using realistic digitisation options

        if self._RealisticDigitisation:
            self._ECalMaxDynamicRangeMIP = 2500       # Realistic Values
            self._HCalMaxDynamicRangeMIP = 99999999   # Realistic Values
            self._ApplyHCalRealisticDigi = 1
            if self._ECalType.lower() in ['si']:
                self._ApplyECalRealisticDigi = 1
            if self._ECalType.lower() in ['sc']:
                self._ApplyECalRealisticDigi = 2

        self.logger.info('Realistic digitsation setting : ' + str(self._RealisticDigitisation))
        self.logger.info('self._ApplyECalRealisticDigi   : ' + str(self._ApplyECalRealisticDigi))
        self.logger.info('self._ApplyHCalRealisticDigi   : ' + str(self._ApplyHCalRealisticDigi))

        'Default Energies Of Calibration Particles'
        self._Kaon0LEnergyCalibration = 20
        self._MuonEnergyCalibration = 10
        self._PhotonEnergyCalibration = 10

        self._Kaon0LRootFiles = os.path.join(self._RootFileFolder, 'ILD_o1_v06_' + str(self._Kaon0LEnergyCalibration) + '_GeV_Kaon0L_SN_*.root')
        self._PhotonRootFiles = os.path.join(self._RootFileFolder, 'ILD_o1_v06_' + str(self._PhotonEnergyCalibration) + '_GeV_Photon_SN_*.root')
        self._MuonRootFiles = os.path.join(self._RootFileFolder, 'ILD_o1_v06_' + str(self._MuonEnergyCalibration) + '_GeV_Muon_SN_*.root')

        'ECal Calibration Variables - Digitisation'
        self._CalibrECal = 42.77
        self._CalibrECalMIP = 0.00015
        self._ECalGapCorrectionFactor = 1.0

        if self._ECalType.lower() in ['si']:
            self._ECalGapCorrectionFactor = 1.012314 # Default of 1.025 slightly too large based on ECal cell size scan.
        if self._ECalType.lower() in ['sc']:
            self._ECalGapCorrectionFactor = 1.052675 # Needed scaling up by 1.027, but default 1.025 so new value is.

        self._ECalBarrelTimeWindowMax = timingCut
        self._ECalEndCapTimeWindowMax = timingCut
        self._ECalLayerChange = 0

        if detModelNumber in range(1,96):
            self._ECalLayerChange = 20
        elif detModelNumber in [96, 100]
            self._ECalLayerChange = 20
        elif detModelNumber in [97, 101]
            self._ECalLayerChange = 17
        elif detModelNumber in [98, 102]
            self._ECalLayerChange = 13
        elif detModelNumber in [99, 103]
            self._ECalLayerChange = 10

        'ECal Calibration Variables - Pandora'
        self._ECalGeVToMIP = 160.0
        self._ECalMIPThresholdPandora = 0.5
        self._ECalToEm = 0.9995
        self._ECalToHad = 1.076

        'HCal Calibration Variables - Digitisation'
        self._CalibrHCalBarrel = 43.58
        self._CalibrHCalEndCap = 50.26
        self._CalibrHCalOther = 26.76
        self._CalibrHCalMIP = 0.00004
        self._HCalBarrelTimeWindowMax = timingCut
        self._HCalEndCapTimeWindowMax = timingCut
        self._CalibrHCalBarrel = self._CalibrHCalBarrel * 48 / self._NumberHCalLayers
        self._CalibrHCalEndCap = self._CalibrHCalEndCap * 48 / self._NumberHCalLayers

        'HCal Calibration Variables - Pandora'
        self._HCalGeVToMIP = 34.8
        self._HCalMIPThresholdPandora = 0.3
        self._MHHHE = hadronicEnergyTrunc
        self._HCalToEm = 1.075
        self._HCalToHad = 1.075

        self._AbsorberThicknessHCalRing = -1         # Inactive material
        self._AbsorberThicknessHCalEndCap = -1       # Inactive material
        self._ScintillatorThicknessHCalRing = -1     # Active material 
        self._ScintillatorThicknessHCalEndCap = -1   # Active material

        'Muon Chamber Calibration Variables'
        self._CalibrMuon = 56.7
        self._MuonGeVToMIP = 10.0

        'Parameters used in Calibration'
        self._HCalRingMIPPeakSimCaloHit = -1
        self._HCalEndCapMIPPeakSimCaloHit = -1
        self._MeanDirectionCorrectionHCalRing = -1
        self._MeanDirectionCorrectionHCalEndCap = -1
        self._GaussianFitKaon0LEndCapMean = -1
        self._GaussianFitKaon0LBarrelMean = -1
        self._ActiveAbsorberThicknessRatio = -1

        'Pandora Analysis'
        self._PandoraAnalysisPath = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudies/PandoraAnalysis_OptimisationStudies/LCPandoraAnalysis/bin'
        self._HadronicScaleSettingPandora = 'CSM' # or 'TEM'

        'Precision of Calibration'
        self._DigitisationPrecision = 0.05 # 5%
        self._PandoraPFAPrecision = 0.005 # 0.5%

        'Physical Constants'
        self._Kaon0LMass = 0.497614
        self._Kaon0LKineticEnergy = math.sqrt(self._Kaon0LEnergyCalibration * self._Kaon0LEnergyCalibration - self._Kaon0LMass * self._Kaon0LMass)

        'Condor'
        self._UseCondor = True
        self._CondorRunList = []
        self._CondorMaxRuns = 500

        'Random String For Job Submission'
        self._RandomString = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        self._MarlinExecutable = 'MarlinCalibration_' + self._RandomString + '.sh'

        os.system('cp Logic/MarlinCalibration.sh ' + self._MarlinExecutable)
        if not os.path.isfile(self._MarlinExecutable):
            self.logger.error('Marlin executable missing.  Exiting calibration.')
            self.logger.error('Marlin executable : ' + self._MarlinExecutable)
            sys.exit()

        self.calibrationProcess()
        os.system('rm ' + self._MarlinExecutable)

### ----------------------------------------------------------------------------------------------------
### End of constructor
### ----------------------------------------------------------------------------------------------------
### Start of calibration process function
### ----------------------------------------------------------------------------------------------------

    def calibrationProcess(self):
        self.logger.info('Checking that calibration text document, root folder and marlin folder exists and if not make them')

        # Set MIP scale in digitisers
        self.prepareSteeringFiles('Muon',self._MuonEnergyCalibration)
        self.runCondorJobs()
        self.checkCondorJobs()

        executable = os.path.join(self._PandoraAnalysisPath,'SimCaloHitEnergyDistribution')
        runExecutable = subprocess.Popen([executable, '-a', self._MuonRootFiles, '-b', str(self._MuonEnergyCalibration), '-c', self._ResultsPath])
        runExecutable.wait()
        self.setMIPScaleDigitser()

        # ECal Digitsation
        ecalDigitsationOk = False
        while not ecalDigitsationOk:
            self.prepareSteeringFiles('Photon',self._PhotonEnergyCalibration)
            self.runCondorJobs()
            self.checkCondorJobs()

            executable = os.path.join(self._PandoraAnalysisPath,'ECalDigitisation_ContainedEvents')
            runExecutable = subprocess.Popen([executable, '-a', self._PhotonRootFiles, '-b', str(self._PhotonEnergyCalibration), '-c', str(self._DigitisationPrecision), '-d', self._ResultsPath, '-e', '90'])
            runExecutable.wait()
            ecalDigitsationOk = self.setCalibrECal()
            
        # HCal Digitsation
        hcalDigitsationOk = False
        while not hcalDigitsationOk:
            self.prepareSteeringFiles('Kaon0L',self._Kaon0LEnergyCalibration)
            self.runCondorJobs()
            self.checkCondorJobs()

            executable = os.path.join(self._PandoraAnalysisPath,'HCalDigitisation_ContainedEvents')
            runExecutable = subprocess.Popen([executable, '-a', self._Kaon0LRootFiles, '-b', str(self._Kaon0LEnergyCalibration), '-c', str(self._DigitisationPrecision), '-d', self._ResultsPath, '-e', '90', '-f', str(self._NumberHCalLayers), '-g', 'Barrel', '-i', '0.2', '-j', '0.6'])
            runExecutable.wait()
            runExecutable = subprocess.Popen([executable, '-a', self._Kaon0LRootFiles, '-b', str(self._Kaon0LEnergyCalibration), '-c', str(self._DigitisationPrecision), '-d', self._ResultsPath, '-e', '90', '-f', str(self._NumberHCalLayers), '-g', 'EndCap', '-i', '0.8', '-j', '0.9'])
            runExecutable.wait()
            hcalDigitsationOk = self.setCalibrHCal()

        # HCal Ring Digitsation
        self.prepareSteeringFiles('Muon',self._MuonEnergyCalibration)
        self.runCondorJobs()
        self.checkCondorJobs()

        executable = os.path.join(self._PandoraAnalysisPath,'HCalDigitisation_DirectionCorrectionDistribution')
        runExecutable = subprocess.Popen([executable, '-a', self._Kaon0LRootFiles, '-b', str(self._Kaon0LEnergyCalibration), '-c', self._ResultsPath])
        runExecutable.wait()
        executable = os.path.join(self._PandoraAnalysisPath,'SimCaloHitEnergyDistribution')
        runExecutable = subprocess.Popen([executable, '-a', self._MuonRootFiles, '-b', str(self._MuonEnergyCalibration), '-c', self._ResultsPath])
        runExecutable.wait()
        self.setCalibrHCalOther()

        # Set MIP scale in Pandora
        executable = os.path.join(self._PandoraAnalysisPath,'PandoraPFACalibrate_MipResponse')
        runExecutable = subprocess.Popen([executable, '-a', self._MuonRootFiles, '-b', str(self._MuonEnergyCalibration), '-c', self._ResultsPath])
        runExecutable.wait()
        self.setPandoraMIPScale()

        # Set Electromagentic Energy Scale Pandora
        pandoraEMScaleOk = False
        while not pandoraEMScaleOk:
            self.prepareSteeringFiles('Photon',self._PhotonEnergyCalibration)
            self.runCondorJobs()
            self.checkCondorJobs()

            executable = os.path.join(self._PandoraAnalysisPath,'PandoraPFACalibrate_EMScale')
            runExecutable = subprocess.Popen([executable, '-a', self._PhotonRootFiles, '-b', str(self._PhotonEnergyCalibration), '-c', str(self._PandoraPFAPrecision), '-d', self._ResultsPath, '-e', '90'])
            runExecutable.wait()
            pandoraEMScaleOk = self.setPandoraEMScale()

        # Set Hadronic Energy Scale Pandora
        pandoraHadScaleOk = False
        while not pandoraHadScaleOk:
            self.prepareSteeringFiles('Kaon0L',self._Kaon0LEnergyCalibration)
            self.runCondorJobs()
            self.checkCondorJobs()

            if self._HadronicScaleSettingPandora == 'CSM':
                executable = os.path.join(self._PandoraAnalysisPath,'PandoraPFACalibrate_HadronicScale_ChiSquareMethod')
                runExecutable = subprocess.Popen([executable, '-a', self._Kaon0LRootFiles, '-b', str(self._Kaon0LEnergyCalibration), '-c', str(self._PandoraPFAPrecision), '-d', self._ResultsPath, '-e', str(self._NumberHCalLayers)])
                runExecutable.wait()
                pandoraHadScaleOk = self.setPandoraHadScaleCSM()

            elif self._HadronicScaleSettingPandora == 'TEM':
                executable = os.path.join(self._PandoraAnalysisPath,'PandoraPFACalibrate_HadronicScale_TotalEnergyMethod')
                runExecutable = subprocess.Popen([executable, '-a', self._Kaon0LRootFiles, '-b', str(self._Kaon0LEnergyCalibration), '-c', str(self._PandoraPFAPrecision), '-d', self._ResultsPath, '-e', '90', '-f', str(self._NumberHCalLayers)])
                runExecutable.wait()
                pandoraHadScaleOk = self.setPandoraHadScaleTEM()

            else:
                self.logger.warning('Problem in specifying hadronic scale calibration method.')
                sys.exit()

        self.writeCalibrationConfigFile()

        print '===== Calibration done ====='

### ----------------------------------------------------------------------------------------------------
### End of calibration process function
### ----------------------------------------------------------------------------------------------------
### ====================================================================================================
### READ CALIBRATION NUMBERS FROM TEXT FILE
### ====================================================================================================
### ----------------------------------------------------------------------------------------------------
### Start of writeCalibrationConfigFile function
### ----------------------------------------------------------------------------------------------------

    def writeCalibrationConfigFile(self):
        self.logger.info('Writing out the config file.')

        configText = '# Digitisation Constants - ECal                                             \n'
        configText += 'CalibrECal = ' + str(self._CalibrECal) + '                                 \n'
        configText += '                                                                           \n'
        configText += '# Digitisation Constants ILDCaloDigi - HCal                                \n'
        configText += 'CalibrHCalBarrel = ' + str(self._CalibrHCalBarrel) + '                     \n'
        configText += 'CalibrHCalEndcap = ' + str(self._CalibrHCalEndCap) + '                     \n'
        configText += 'CalibrHCalOther = ' + str(self._CalibrHCalOther) + '                       \n'
        configText += '                                                                           \n'
        configText += '# Digitisation Constants NewLDCCaloDigi - HCal                             \n'
        configText += 'CalibrHCal = -1                                                            \n'
        configText += '                                                                           \n'
        configText += '# Digitisation Constants - Muon Chamber                                    \n'
        configText += 'CalibrMuon = ' + str(self._CalibrMuon) + '                                 \n'
        configText += '                                                                           \n'
        configText += '# MIP Peak position in directed corrected SimCaloHit energy distributions  \n'
        configText += '# used for realistic ECal and HCal digitisation options                    \n'
        configText += 'CalibrECalMIP = ' + str(self._CalibrECalMIP) + '                           \n'
        configText += 'CalibrHCalMIP = ' + str(self._CalibrHCalMIP) + '                           \n'
        configText += '                                                                           \n'
        configText += '# MIP Peak position in directed corrected CaloHit energy distributions     \n'
        configText += '# used for MIP definition in PandoraPFA                                    \n'
        configText += 'ECalToMIPCalibration = ' + str(self._ECalGeVToMIP) + '                     \n'
        configText += 'HCalToMIPCalibration = ' + str(self._HCalGeVToMIP) + '                     \n'
        configText += 'MuonToMIPCalibration = ' + str(self._MuonGeVToMIP) + '                     \n'
        configText += '                                                                           \n'
        configText += '# EM and Had Scale Settings                                                \n'
        configText += 'ECalToEMGeVCalibration = ' + str(self._ECalToEm) + '                       \n'
        configText += 'HCalToEMGeVCalibration = ' + str(self._HCalToEm) + '                       \n'
        configText += 'ECalToHadGeVCalibration = ' + str(self._ECalToHad) + '                     \n'
        configText += 'HCalToHadGeVCalibration = ' + str(self._HCalToHad) + '                     \n'
        configText += '                                                                           \n'
        configText += '# Pandora Threshold Cuts                                                   \n'
        configText += 'ECalMIPThresholdPandora = ' + str(self._ECalMIPThresholdPandora) + '       \n'
        configText += 'HCalMIPThresholdPandora = ' + str(self._HCalMIPThresholdPandora) + '       \n'
        configText += '                                                                           \n'
        configText += '# Hadronic Energy Truncation in HCal PandoraPFA                            \n'
        configText += 'MaxHCalHitHadronicEnergy = ' + str(self._MHHHE) + '                        \n'
        configText += '                                                                           \n'
        configText += '# Timing ECal                                                              \n'
        configText += 'ECalBarrelTimeWindowMax = ' + str(self._ECalBarrelTimeWindowMax) + '       \n'
        configText += 'ECalEndcapTimeWindowMax = ' + str(self._ECalEndCapTimeWindowMax) + '       \n'
        configText += '                                                                           \n'
        configText += '# Timing HCal                                                              \n'
        configText += 'HCalBarrelTimeWindowMax = ' + str(self._HCalBarrelTimeWindowMax) + '       \n'
        configText += 'HCalEndcapTimeWindowMax = ' + str(self._HCalEndCapTimeWindowMax) + '       \n'

        configFileName = 'CalibConfig_DetModel' + str(self._DetectorModelNumber) + '_RecoStage' + str(self._ReconstructionVariant) + '.py'
        configFileFullPath = os.path.join(self._ResultsPath, configFileName)

        with open(configFileFullPath, 'w') as configFile:
            configFile.write(configText)
        return

### ----------------------------------------------------------------------------------------------------
### End of writeCalibrationConfigFile function
### ----------------------------------------------------------------------------------------------------
### ----------------------------------------------------------------------------------------------------
### Start of setPandoraHadScaleCSM function
### ----------------------------------------------------------------------------------------------------

    def setPandoraHadScaleCSM(self):
        self.logger.info('Setting hadronic scale in Pandora via chi squred method.')

        csmECalToHadIntercept = -1
        csmHCalToHadIntercept = -1
        with open(self._CalibrationFile, 'r') as calibrationFile:
            searchlines = calibrationFile.readlines()
            for line in searchlines:
                if 'm_eCalToHadInterceptMinChi2' in line:
                    csmECalToHadIntercept = float(findBetween( line, ' : ', ' : '))
                elif 'm_hCalToHadInterceptMinChi2' in line:
                    csmHCalToHadIntercept = float(findBetween( line, ' : ', ' : '))

        newECalToHad = self._Kaon0LKineticEnergy * self._ECalToHad / csmECalToHadIntercept
        newHCalToHad = self._Kaon0LKineticEnergy * self._HCalToHad / csmHCalToHadIntercept

        self.logger.info('_____________________________________________________________________________________')
        self.logger.info('Kinetic Energy To Calibrate                        : ' + str(self._Kaon0LKineticEnergy))
        self.logger.info('ECalToHad.')
        self.logger.info('Initial ECalToHad                                  : ' + str(self._ECalToHad))
        self.logger.info('CSM_Intercept                                      : ' + str(csmECalToHadIntercept))
        self.logger.info('New ECalToHad                                      : ' + str(newECalToHad))
        self.logger.info('HCalToHad.')
        self.logger.info('Initial HCalToHad                                  : ' + str(self._HCalToHad))
        self.logger.info('CSM_Intercept                                      : ' + str(csmHCalToHadIntercept))
        self.logger.info('New HCalToHad                                      : ' + str(newHCalToHad))

        self._ECalToHad = newECalToHad
        self._HCalToHad = newHCalToHad
        self._HCalToEm = newHCalToHad

        errorECalToHadScale = math.fabs(self._Kaon0LKineticEnergy - csmECalToHadIntercept) / self._Kaon0LKineticEnergy 
        errorHCalToHadScale = math.fabs(self._Kaon0LKineticEnergy - csmHCalToHadIntercept) / self._Kaon0LKineticEnergy 

        if errorECalToHadScale < self._PandoraPFAPrecision and errorHCalToHadScale < self._PandoraPFAPrecision:
            return True
        else:
            return False

### ----------------------------------------------------------------------------------------------------
### End of setPandoraHadScaleCSM function
### ----------------------------------------------------------------------------------------------------
### ----------------------------------------------------------------------------------------------------
### Start of setPandoraHadScaleTEM function
### ----------------------------------------------------------------------------------------------------

    def setPandoraHadScaleTEM(self):
        self.logger.info('Setting hadronic scale in Pandora via total energy method.')

        temECalToHadMultiplier = -1
        temHCalToHadMultiplier = -1
        with open(self._CalibrationFile, 'r') as calibrationFile:
            searchlines = calibrationFile.readlines()
            for line in searchlines:
                if 'Minimum_RMS_ECal_Multiplier' in line:
                    temECalToHadMultiplier = float(findBetween( line, ' : ', ' :'))
                if 'Minimum_RMS_HCal_Multiplier' in line:
                    temHCalToHadMultiplier = float(findBetween( line, ' : ', ' :'))

        newECalToHad = temECalToHadMultiplier * self._ECalToHad
        newHCalToHad = temHCalToHadMultiplier * self._HCalToHad

        self.logger.info('_____________________________________________________________________________________')
        self.logger.info('Kinetic Energy To Calibrate                        : ' + str(self._Kaon0LKineticEnergy))
        self.logger.info('ECalToHad.')
        self.logger.info('Initial ECalToHad                                  : ' + str(self._ECalToHad))
        self.logger.info('TEM_Multiplier                                     : ' + str(temECalToHadMultiplier))
        self.logger.info('New ECalToHad                                      : ' + str(newECalToHad))
        self.logger.info('HCalToHad.')
        self.logger.info('Initial HCalToHad                                  : ' + str(self._HCalToHad))
        self.logger.info('TEM_Multiplier                                     : ' + str(temHCalToHadMultiplier))
        self.logger.info('New HCalToHad                                      : ' + str(newHCalToHad))
        self.logger.info('New HCalToEm                                       : ' + str(newHCalToHad))

        self._ECalToHad = newECalToHad
        self._HCalToHad = newHCalToHad
        self._HCalToEm = newHCalToHad

        errorECalToHadScale = temECalToHadMultiplier 
        errorHCalToHadScale = temHCalToHadMultiplier

        if errorECalToHadScale < self._PandoraPFAPrecision and errorHCalToHadScale < self._PandoraPFAPrecision:
            return True
        else:
            return False

### ----------------------------------------------------------------------------------------------------
### End of setPandoraHadScaleTEM function
### ----------------------------------------------------------------------------------------------------
### ----------------------------------------------------------------------------------------------------
### Start of setPandoraEMScale function
### ----------------------------------------------------------------------------------------------------

    def setPandoraEMScale(self):
        self.logger.info('Setting electromagnetic scale in Pandora.')

        with open(self._CalibrationFile, 'r') as calibrationFile:
            searchlines = calibrationFile.readlines()
            for line in searchlines:
                if 'ECalToEM Mean' in line:
                    gaussianFitPhotonMean = float(findBetween( line, ' : ', ' : '))
        newECalToEM = self._PhotonEnergyCalibration * self._ECalToEm / gaussianFitPhotonMean

        self.logger.info('_____________________________________________________________________________________')
        self.logger.info('ECal/HCalToEM.')
        self.logger.info('Photon Energy To Calibrate                         : ' + str(self._PhotonEnergyCalibration))
        self.logger.info('Initial ECalToEM                                   : ' + str(self._ECalToEm))
        self.logger.info('Mean                                               : ' + str(gaussianFitPhotonMean))
        self.logger.info('Updated => ECalToEM =                              : ' + str(newECalToEM))

        self._ECalToEm = newECalToEM

        errorECalEMScale = math.fabs(self._PhotonEnergyCalibration - gaussianFitPhotonMean) / self._PhotonEnergyCalibration
        if errorECalEMScale < self._PandoraPFAPrecision:
            return True
        else:
            return False

### ----------------------------------------------------------------------------------------------------
### End of setPandoraEMScale function
### ----------------------------------------------------------------------------------------------------
### ----------------------------------------------------------------------------------------------------
### Start of setPandoraMIPScale function
### ----------------------------------------------------------------------------------------------------

    def setPandoraMIPScale(self):
        self.logger.info('Setting MIP scale in Pandora.')

        with open(self._CalibrationFile, 'r') as calibrationFile:
            searchlines = calibrationFile.readlines()
            for line in searchlines:
                if 'ECalGeVToMIP' in line:
                    self._ECalGeVToMIP = findBetween( line, ' : ', ' :')
                elif 'HCalGeVToMIP' in line:
                    self._HCalGeVToMIP = findBetween( line, ' : ', ' :')
                elif 'MuonGeVToMIP' in line:
                    self._MuonGeVToMIP = findBetween( line, ' : ', ' :')
        self.logger.info('_____________________________________________________________________________________')
        self.logger.info('ECalGeVToMIP                                       : ' + str(self._ECalGeVToMIP))
        self.logger.info('HCalGeVToMIP                                       : ' + str(self._HCalGeVToMIP))
        self.logger.info('MuonGeVToMIP                                       : ' + str(self._MuonGeVToMIP))
        self.setMIPScaleDigitser()
        return

### ----------------------------------------------------------------------------------------------------
### End of setPandoraMIPScale function
### ----------------------------------------------------------------------------------------------------
### ----------------------------------------------------------------------------------------------------
### Start of readGearFile function
### ----------------------------------------------------------------------------------------------------

    def readGearFile(self):
        self.logger.info('Reading detector geometry information relevant to calibration procedure from gear file.')
        with open(self._GearFile, 'r') as gearFile:
            searchlines = gearFile.readlines()
            detectorName = ''
            for line in searchlines:
                detRegex = re.compile("(.*?)detector name=\"(.*?)\"(.*?)")
                detResults = detRegex.search(line)
                if detResults is not None:
                    detectorName = detResults.group(2)

                if 'HcalRing' in detectorName:
                    absRegex = re.compile("(.*?)absorberThickness=\"(.*?)e+(.*?)\" cellSize0=(.*?)")
                    absResults = absRegex.search(line)
                    if absResults is not None:
                        self._AbsorberThicknessHCalRing = float(absResults.group(2)) * pow(10,float(absResults.group(3)))

                    actRegex = re.compile("(.*?)Hcal_scintillator_thickness(.*?)value=\"(.*?)e+(.*?)\"(.*?)")
                    actResults = actRegex.search(line)
                    if actResults is not None:
                        self._ScintillatorThicknessHCalRing = float(actResults.group(3)) * pow(10,float(actResults.group(4)))

                if 'HcalEndcap' in detectorName:
                    absRegex = re.compile("(.*?)absorberThickness=\"(.*?)e+(.*?)\" cellSize0=(.*?)")
                    absResults = absRegex.search(line)
                    if absResults is not None:
                        self._AbsorberThicknessHCalEndCap = float(absResults.group(2)) * pow(10,float(absResults.group(3)))

                    actRegex = re.compile("(.*?)Hcal_scintillator_thickness(.*?)value=\"(.*?)e+(.*?)\"(.*?)")
                    actResults = actRegex.search(line)
                    if actResults is not None:
                        self._ScintillatorThicknessHCalEndCap = float(actResults.group(3)) * pow(10,float(actResults.group(4)))

        self._ActiveAbsorberThicknessRatio = (self._AbsorberThicknessHCalEndCap * self._ScintillatorThicknessHCalRing) / (self._AbsorberThicknessHCalRing * self._ScintillatorThicknessHCalEndCap)


### ----------------------------------------------------------------------------------------------------
### End of readGearFile function
### ----------------------------------------------------------------------------------------------------
### Start of setCalibrHCalOther process function
### ----------------------------------------------------------------------------------------------------

    def setCalibrHCalOther(self):
        self.logger.info('Setting digitsation in HCal ring.')
        self.readGearFile()

        with open(self._CalibrationFile, 'r') as calibrationFile:
            searchlines = calibrationFile.readlines()
            for line in searchlines:
                if 'HCal Ring MIP Peak' in line:
                    self._HCalRingMIPPeakSimCaloHit = float(findBetween( line, ' : ', ' :'))
                elif 'HCal EndCap MIP Peak' in line:
                    self._HCalEndCapMIPPeakSimCaloHit = float(findBetween( line, ' : ', ' :'))
                elif 'Mean Direction Correction HCalOther:' in line:
                    self._MeanDirectionCorrectionHCalRing = float(findBetween( line, ' : ', ' :'))
                elif 'Mean Direction Correction HCalEndCap:' in line:
                    self._MeanDirectionCorrectionHCalEndCap = float(findBetween( line, ' : ', ' :'))

        self._CalibrHCalOther = (self._CalibrHCalEndCap * self._Kaon0LEnergyCalibration / self._GaussianFitKaon0LEndCapMean) * (self._MeanDirectionCorrectionHCalEndCap / self._MeanDirectionCorrectionHCalRing) * (self._HCalEndCapMIPPeakSimCaloHit / self._HCalRingMIPPeakSimCaloHit) * self._ActiveAbsorberThicknessRatio 

        self.writeCalibrHCalOtherInfo()
        return

### ----------------------------------------------------------------------------------------------------
### End of setCalibrHCalOther function
### ----------------------------------------------------------------------------------------------------
### Start of writeCalibrHCalOtherInfo function
### ----------------------------------------------------------------------------------------------------

    def writeCalibrHCalOtherInfo(self):
        self.logger.info('Writing CalibrHCalOther info to calibration file.')
        self.logger.info('_____________________________________________________________________________________')
        self.logger.info('Retrieving GEAR information for HCal Ring Digitisation')
        self.logger.info('AbsorberThicknessHCalRing                          : ' + str(self._AbsorberThicknessHCalRing) + ' /mm')
        self.logger.info('ScintillatorThicknessHCalRing                      : ' + str(self._ScintillatorThicknessHCalRing) + ' /mm')
        self.logger.info('AbsorberThicknessHCalEndCap                        : ' + str(self._AbsorberThicknessHCalEndCap) + ' /mm')
        self.logger.info('ScintillatorThicknessHCalEndCap                    : ' + str(self._ScintillatorThicknessHCalEndCap) + ' /mm')
        self.logger.info('Ratio used for HCal Ring Digitisation is           : ')
        self.logger.info('AbsorberThicknessHCalEndCap x ScintillatorThicknessHCalRing')
        self.logger.info('-----------------------------------------------------------     = ' + str(self._ActiveAbsorberThicknessRatio))
        self.logger.info('ScintillatorThicknessHCalEndCap x AbsorberThicknessHCalRing')
        self.logger.info('_____________________________________________________________________________________')
        self.logger.info('Finding MIP peak ratios (Ring/Other to EndCap) for HCal SimCaloHits')
        self.logger.info('For Muons with energy                              :' + str(self._MuonEnergyCalibration) + ' /GeV')
        self.logger.info('Ring SimCaloHit MIP Peak                           :' + str(self._HCalRingMIPPeakSimCaloHit))
        self.logger.info('EndCap SimCaloHit MIP Peak                         :' + str(self._HCalEndCapMIPPeakSimCaloHit))
        self.logger.info('_____________________________________________________________________________________')
        self.logger.info('Finding ratio of mean direction corrections for SimCaloHits in HCalEndCap and HCalOther')
        self.logger.info('(Ring/Other to EndCap) for HCal.')
        self.logger.info('For KaonL events with energy                       :' + str(self._Kaon0LEnergyCalibration) + ' /GeV')
        self.logger.info('Ring Mean Direction Correction                     :' + str(self._MeanDirectionCorrectionHCalRing))
        self.logger.info('EndCap Mean Direction Correction                   :' + str(self._MeanDirectionCorrectionHCalEndCap))
        self.logger.info('_____________________________________________________________________________________')
        self.logger.info('CalibrHCALOther                                    :' + str(self._CalibrHCalOther))
        return

### ----------------------------------------------------------------------------------------------------
### End of writeCalibrHCalOtherInfo function
### ----------------------------------------------------------------------------------------------------
### Start of setCalibrHCal process function
### ----------------------------------------------------------------------------------------------------

    def setCalibrHCal(self):
        self.logger.info('Setting digitsation in HCal.')
        with open(self._CalibrationFile, 'r') as calibrationFile:
            searchlines = calibrationFile.readlines()
            for line in searchlines:
                if 'HCal Barrel Digi Mean' in line:
                    self._GaussianFitKaon0LBarrelMean = float(findBetween( line, ' : ', ' :'))
                elif 'HCal EndCap Digi Mean' in line:
                    self._GaussianFitKaon0LEndCapMean = float(findBetween( line, ' : ', ' :'))

        newCalibrHCalBarrel = self._Kaon0LEnergyCalibration * self._CalibrHCalBarrel / self._GaussianFitKaon0LBarrelMean
        newCalibrHCalEndCap = self._Kaon0LEnergyCalibration * self._CalibrHCalEndCap / self._GaussianFitKaon0LEndCapMean

        self.logger.info('_____________________________________________________________________________________')
        self.logger.info('CalibrHCalBarrel and CalibrHCalEndCap. ')
        self.logger.info('_____________________________________________________________________________________')
        self.logger.info('KaonL Energy To Calibrate                          : ' + str(self._Kaon0LEnergyCalibration) + ' /GeV')
        self.logger.info('Initial Calibration Constant - Barrel              : ' + str(self._CalibrHCalBarrel))
        self.logger.info('CalibrHCalBarrel Mean                              : ' + str(self._GaussianFitKaon0LBarrelMean) + ' /GeV')
        self.logger.info('New CalibrHCalBarrel                               : ' + str(newCalibrHCalBarrel))
        self.logger.info('Initial Calibration Constant - EndCap              : ' + str(self._CalibrHCalEndCap))
        self.logger.info('CalibrHCalEndCap Mean                              : ' + str(self._GaussianFitKaon0LEndCapMean) + ' /GeV')
        self.logger.info('New CalibrHCalEndCap                               : ' + str(newCalibrHCalEndCap))

        self._CalibrHCalBarrel = newCalibrHCalBarrel
        self._CalibrHCalEndCap = newCalibrHCalEndCap

        errorHCalBarrelDigitsation = math.fabs(self._Kaon0LEnergyCalibration - self._GaussianFitKaon0LBarrelMean) / self._Kaon0LEnergyCalibration
        errorHCalEndCapDigitsation = math.fabs(self._Kaon0LEnergyCalibration - self._GaussianFitKaon0LEndCapMean) / self._Kaon0LEnergyCalibration

        if errorHCalBarrelDigitsation < self._DigitisationPrecision and errorHCalEndCapDigitsation < self._DigitisationPrecision:
            return True
        else:
            return False

### ----------------------------------------------------------------------------------------------------
### End of setCalibrHCal process function
### ----------------------------------------------------------------------------------------------------
### Start of setCalibrECal process function
### ----------------------------------------------------------------------------------------------------

    def setCalibrECal(self):
        self.logger.info('Setting digitsation in ECal.')
        gaussianFitPhotonsMean = -1
        with open(self._CalibrationFile, 'r') as calibrationFile:
            searchlines = calibrationFile.readlines()
            for line in searchlines:
                if 'ECal Digi Mean' in line:
                    gaussianFitPhotonsMean = float(findBetween( line, ' : ', ' :'))

        newCalibrECal = self._PhotonEnergyCalibration * self._CalibrECal / gaussianFitPhotonsMean

        self.logger.info('_____________________________________________________________________________________')
        self.logger.info('CalibrECal. ')
        self.logger.info('_____________________________________________________________________________________')
        self.logger.info('Photon Energy To Calibrate                         : ' + str(self._PhotonEnergyCalibration) + ' /GeV')
        self.logger.info('Initial Calibration Constant                       : ' + str(self._CalibrECal))
        self.logger.info('CalibrECal Mean                                    : ' + str(gaussianFitPhotonsMean) + ' /GeV')
        self.logger.info('New CalibrECal                                     : ' + str(newCalibrECal))

        self._CalibrECal = newCalibrECal

        errorECalDigitsation = math.fabs(self._PhotonEnergyCalibration - gaussianFitPhotonsMean) / self._PhotonEnergyCalibration
        if errorECalDigitsation < self._DigitisationPrecision:
            return True
        else:
            return False

### ----------------------------------------------------------------------------------------------------
### End of setCalibrECal process function
### ----------------------------------------------------------------------------------------------------
### Start of setMIPScaleDigitser process function
### ----------------------------------------------------------------------------------------------------

    def setMIPScaleDigitser(self):
        self.logger.info('Setting MIP scale at ECal and HCal digitisation stage.')
        with open(self._CalibrationFile, 'r') as calibrationFile:
            searchlines = calibrationFile.readlines()
            for line in searchlines:
                if 'HCal Barrel MIP Peak' in line:
                    self._CalibrHCalMIP = float(findBetween( line, ' : ', ' :'))
                if 'ECal MIP Peak' in line:
                    self._CalibrECalMIP = float(findBetween( line, ' : ', ' :'))
        self.logger.info('_____________________________________________________________________________________')
        self.logger.info('Muon Energy To Calibrate                           : ' + str(self._MuonEnergyCalibration) + ' /GeV')
        self.logger.info('CalibrECalMIP                                      : ' + str(self._CalibrECalMIP))
        self.logger.info('CalibrHCalMIP                                      : ' + str(self._CalibrHCalMIP))
        return

### ----------------------------------------------------------------------------------------------------
### End of setMIPScaleDigitser process function
### ----------------------------------------------------------------------------------------------------

### ====================================================================================================
### MARLIN XML GNERATION 
### ====================================================================================================

### ----------------------------------------------------------------------------------------------------
### Start of getSlcioFiles function
### ----------------------------------------------------------------------------------------------------

    def getSlcioFiles(self):
        fileDirectory = self._SlcioPath
        allFilesInDirectory = dircache.listdir(fileDirectory)
        allFiles = []
        allFiles.extend(allFilesInDirectory)
        allFiles[:] = [ item for item in allFiles if re.match('.*\.slcio$', item.lower()) ]
        allFiles.sort()
        return allFiles

### ----------------------------------------------------------------------------------------------------
### End of getSlcioFiles function
### ----------------------------------------------------------------------------------------------------
### Start of prepareSteeringFiles function
### ----------------------------------------------------------------------------------------------------

    def prepareSteeringFiles(self,particle,activeParticleEnergy):
        self.logger.debug('Preparing ' + particle + ' steering files.')
        jobName = str(activeParticleEnergy) + '_GeV_' + particle

        activeSlcioFormat = self._SlcioFormat
        activeSlcioFormat = re.sub('ENERGY',str(activeParticleEnergy),activeSlcioFormat)
        activeSlcioFormat = re.sub('PARTICLE',particle,activeSlcioFormat)

        baseFileName = 'ILD_o1_v06_Calibration_XX_YY.xml'
        baseSteeringFile = os.path.join(os.getcwd(), 'Logic/ILD_o1_v06_XX_YY.xml')

        jobList = []

        base = open(baseSteeringFile,'r')
        baseContent = base.read()
        base.close()

        slcioFiles = []
        slcioFiles = list(self._SlcioFiles)

        if not slcioFiles:
            self.logger.debug('No files in input slcio folder.')
            self.logger.debug('Slcio Folder : ' + self._SlcioPath)
            self.logger.debug('Slcio Format : ' + activeSlcioFormat)
            sys.exit()

        for nfiles in range(len(slcioFiles)):
            marlinTemplate = baseContent
            nextFile = slcioFiles.pop(0)
            matchObj = re.match(activeSlcioFormat, nextFile, re.M|re.I)

            # Check files match
            if not matchObj:
                continue

            info = matchObj.group(1)

            slcioFileName = os.path.join(self._SlcioPath,nextFile)
            newFileName = 'ILD_o1_v06_Calibration_' + jobName + '_SN_' + info + '.xml'
            xmlFullPath = os.path.join(self._MarlinXmlPath, newFileName)
            rootFileFullPath = os.path.join(self._RootFileFolder, 'ILD_o1_v06_' + jobName + '_SN_' + info + '.root')

            marlinTemplate = re.sub('LcioInputFile',slcioFileName,marlinTemplate)           # Slcio File
            marlinTemplate = re.sub('GearFile',self._GearFile,marlinTemplate)               # Gear File
            marlinTemplate = self.writeXmlFile(marlinTemplate)                              # Calibration Parameters
            marlinTemplate = re.sub('PfoAnalysisRootFile',rootFileFullPath,marlinTemplate)  # PfoAnalysis Root File

            file = open(xmlFullPath,'w')
            file.write(marlinTemplate)
            file.close()

            jobList.append(xmlFullPath)

        self._CondorRunList = jobList

        self.logger.debug('The current list of xml files to process is: ')
        self.logger.debug(jobList)

### ----------------------------------------------------------------------------------------------------
### End of prepareSteeringFiles function
### ----------------------------------------------------------------------------------------------------
### Start of writeXmlFile function
### ----------------------------------------------------------------------------------------------------

    def writeXmlFile(self, template):
        if self._ECalType.lower() in ['si']:
            self.logger.debug('Writing xml file.  Si ECal')
            digitiserHeader = self.writeILDCaloDigiSiECalXmlHeader()
            template = re.sub('DigitiserHeader',digitiserHeader,template)

            simpleMuonDigiHeader = self.writeSimpleMuonDigiXmlHeader()
            template = re.sub('SimpleMuonDigiHeader',simpleMuonDigiHeader,template)

            pandoraHeader = self.writePandoraXmlHeader()
            template = re.sub('PandoraHeader',pandoraHeader,template)

            digitiserImplementation = self.writeILDCaloDigiSiECalXml()
            template = re.sub('DigitiserImplementation',digitiserImplementation,template)

            simpleMuonDigiImplementation = self.writeSimpleMuonDigiXml()
            template = re.sub('SimpleMuonDigiImplementation',simpleMuonDigiImplementation,template)

            pandoraImplementation = self.writeMarlinPandoraSiECalXml()
            pandoraImplementation += '\n'
            pandoraImplementation += self.writePandoraAnalsisSiECalXml()
            template = re.sub('PandoraImplementation',pandoraImplementation,template)
            return template

        elif self._ECalType.lower() in ['sc']:
            self.logger.debug('Writing xml file.  Sc ECal')
            digitiserHeader = self.writeILDCaloDigiScECalXmlHeader()
            template = re.sub('DigitiserHeader',digitiserHeader,template)

            simpleMuonDigiHeader = self.writeSimpleMuonDigiXmlHeader()
            template = re.sub('SimpleMuonDigiHeader',simpleMuonDigiHeader,template)

            pandoraHeader = self.writePandoraXmlHeader()
            template = re.sub('PandoraHeader',pandoraHeader,template)

            digitiserImplementation = self.writeILDCaloDigiScECalXml()
            template = re.sub('DigitiserImplementation',digitiserImplementation,template)

            simpleMuonDigiImplementation = self.writeSimpleMuonDigiXml()
            template = re.sub('SimpleMuonDigiImplementation',simpleMuonDigiImplementation,template)

            pandoraImplementation = self.writeMarlinPandoraScECalXml()
            pandoraImplementation += '\n'
            pandoraImplementation += self.writePandoraAnalsisScECalXml()
            template = re.sub('PandoraImplementation',pandoraImplementation,template)
            return template

        else:
            self.logger.warning('Please select a valid ECal type (Si/Sc)')
            sys.exit()

### ----------------------------------------------------------------------------------------------------
### End of writeXmlFile function
### ----------------------------------------------------------------------------------------------------
### Start of writeILDCaloDigiSiECalXmlHeader function
### ----------------------------------------------------------------------------------------------------

    def writeILDCaloDigiSiECalXmlHeader(self):
        self.logger.debug('Writing ILDCaloDigi xml header block for Si ECal.')
        ildCaloDigiHeader = """<processor name="MyILDCaloDigi"/>"""
        return ildCaloDigiHeader

### ----------------------------------------------------------------------------------------------------
### End of writeILDCaloDigiSiECalXmlHeader function
### ----------------------------------------------------------------------------------------------------
### Start of writeILDCaloDigiScECalXmlHeader function
### ----------------------------------------------------------------------------------------------------

    def writeILDCaloDigiScECalXmlHeader(self):
        self.logger.debug('Writing ILDCaloDigi xml header block for Sc ECal.')
        ildCaloDigiHeader = """
<processor name="MyILDCaloDigi_ScTrans"/>
<processor name="MyILDCaloDigi_ScLong"/>
<processor name="MyILDCaloDigi"/>"""
        return ildCaloDigiHeader

### ----------------------------------------------------------------------------------------------------
### End of writeILDCaloDigiScECalXmlHeader function
### ----------------------------------------------------------------------------------------------------
### Start of writeILDCaloDigiSiECalXml function
### ----------------------------------------------------------------------------------------------------

    def writeILDCaloDigiSiECalXml(self):
        self.logger.debug('Writing ILDCaloDigi xml block for Si ECal.')
        ildCaloDigi  = """
<processor name="MyILDCaloDigi" type="ILDCaloDigi">
  <!--ILD digitizer...-->
  <!--Calibration coefficients for ECAL-->
  <parameter name="CalibrECAL" type="FloatVec">""" + str(self._CalibrECal) + ' ' + str(2*self._CalibrECal) + """</parameter>
  <!--Calibration coefficients for HCAL barrel, endcap, other-->
  <parameter name="CalibrHCALBarrel" type="FloatVec">""" + str(self._CalibrHCalBarrel) + """</parameter>
  <parameter name="CalibrHCALEndcap" type="FloatVec">""" + str(self._CalibrHCalEndCap) + """</parameter>
  <parameter name="CalibrHCALOther" type="FloatVec">""" + str(self._CalibrHCalOther) + """</parameter>
  <!--ECAL Collection Names-->
  <parameter name="ECALCollections" type="StringVec">EcalBarrelSiliconCollection EcalEndcapSiliconCollection  EcalEndcapRingCollection </parameter>
  <!--Index of ECal Layers-->
  <parameter name="ECALLayers" type="IntVec">""" + str(self._ECalLayerChange) + """ 100 </parameter>
  <!--Threshold for ECAL Hits in GeV-->
  <parameter name="ECALThreshold" type="float">5e-05 </parameter>
  <!--HCAL Collection Names-->
  <parameter name="HCALCollections" type="StringVec">HcalBarrelRegCollection  HcalEndCapsCollection HcalEndCapRingsCollection</parameter>
  <!--Index of HCal Layers-->
  <parameter name="HCALLayers" type="IntVec">100  </parameter>
  <!--Threshold for HCAL Hits in MIPs - given HCALThresholdUnit is specified-->
  <parameter name="HCALThreshold" type="float">0.5 </parameter>
  <!--Digital Ecal-->
  <parameter name="IfDigitalEcal" type="int">0 </parameter>
  <!--Digital Hcal-->
  <parameter name="IfDigitalHcal" type="int">0 </parameter>
  <!--name for the new collection -->
  <parameter name="ECALOutputCollection0" type="stringVec">ECALBarrel </parameter>
  <parameter name="ECALOutputCollection1" type="stringVec">ECALEndcap </parameter>
  <parameter name="ECALOutputCollection2" type="stringVec">ECALOther </parameter>
  <parameter name="HCALOutputCollection0" type="stringVec">HCALBarrel </parameter>
  <parameter name="HCALOutputCollection1" type="stringVec">HCALEndcap </parameter>
  <parameter name="HCALOutputCollection2" type="stringVec">HCALOther </parameter>
  <!--CaloHit Relation Collection-->
  <parameter name="RelationOutputCollection" type="string"> RelationCaloHit</parameter>
  <!--Gap Correction-->
  <parameter name="ECALGapCorrection" type="int"> 1 </parameter>
  <!--Gap Correction Fudge Factor-->
  <parameter name="ECALGapCorrectionFactor" type="float">""" + str(self._ECalGapCorrectionFactor) + """</parameter>
  <parameter name="ECALModuleGapCorrectionFactor" type="int"> 0.0 </parameter>
  <!-- Timing -->
  <parameter name="UseEcalTiming" type="int">1</parameter>
  <parameter name="UseHcalTiming" type="int">1</parameter>
  <parameter name="ECALBarrelTimeWindowMax" type="float">""" + str(self._ECalBarrelTimeWindowMax) + """</parameter>
  <parameter name="HCALBarrelTimeWindowMax" type="float">""" + str(self._HCalBarrelTimeWindowMax) + """</parameter>
  <parameter name="ECALEndcapTimeWindowMax" type="float">""" + str(self._ECalEndCapTimeWindowMax) + """</parameter>
  <parameter name="HCALEndcapTimeWindowMax" type="float">""" + str(self._HCalEndCapTimeWindowMax) + """</parameter>
  <parameter name="ECALTimeWindowMin" type="float"> -1.0 </parameter>
  <parameter name="HCALTimeWindowMin" type="float"> -1.0 </parameter>
  <parameter name="ECALCorrectTimesForPropagation" type="int">1</parameter>
  <parameter name="HCALCorrectTimesForPropagation" type="int">1</parameter>
  <parameter name="ECALDeltaTimeHitResolution" type="float"> 20.0 </parameter>
  <parameter name="HCALDeltaTimeHitResolution" type="float"> 20.0 </parameter>
  <!-- Realistic ECal -->
  <parameter name="ECAL_apply_realistic_digi" type="int">""" + str(self._ApplyECalRealisticDigi) + """</parameter>
  <parameter name="CalibECALMIP" type="float">""" + str(self._CalibrECalMIP) + """</parameter>
  <parameter name="ECAL_maxDynamicRange_MIP" type="float">""" + str(self._ECalMaxDynamicRangeMIP) + """</parameter>
  <parameter name="ECAL_elec_noise_mips" type="float">0.07</parameter>
  <parameter name="ECAL_deadCellRate" type="float">0</parameter>
  <parameter name="ECAL_miscalibration_uncorrel" type="float">0</parameter>
  <parameter name="ECAL_miscalibration_uncorrel_memorise" type="bool">false</parameter>
  <parameter name="ECAL_miscalibration_correl" type="float">0</parameter>
  <parameter name="energyPerEHpair" type="float">3.6</parameter>
  <parameter name="ECAL_PPD_PE_per_MIP" type="float">7</parameter>
  <parameter name="ECAL_PPD_N_Pixels" type="int">10000</parameter>
  <parameter name="ECAL_PPD_N_Pixels_uncertainty" type="float">0.05</parameter>
  <parameter name="ECAL_pixel_spread" type="float">0.05</parameter>
  <!-- Realistic HCal -->
  <parameter name="HCAL_apply_realistic_digi" type="int">""" + str(self._ApplyHCalRealisticDigi) + """</parameter>
  <parameter name="HCALThresholdUnit" type="string">MIP</parameter>
  <parameter name="CalibHCALMIP" type="float">""" + str(self._CalibrHCalMIP) + """</parameter>
  <parameter name="HCAL_maxDynamicRange_MIP" type="float">""" + str(self._HCalMaxDynamicRangeMIP) + """</parameter>
  <parameter name="HCAL_elec_noise_mips" type="float">0.06</parameter>
  <parameter name="HCAL_deadCellRate" type="float">0</parameter>
  <parameter name="HCAL_PPD_N_Pixels" type="int">2000</parameter>
  <parameter name="HCAL_PPD_PE_per_MIP" type="float">15</parameter>
  <parameter name="HCAL_pixel_spread" type="float">0.05</parameter>
  <parameter name="HCAL_PPD_N_Pixels_uncertainty" type="float">0</parameter>
  <parameter name="HCAL_miscalibration_uncorrel" type="float">0</parameter>
  <parameter name="HCAL_miscalibration_correl" type="float">0</parameter>
  <!-- Histograms-->
  <parameter name="Histograms" type="int"> 0 </parameter>
</processor>"""
        return ildCaloDigi

### ----------------------------------------------------------------------------------------------------
### End of writeILDCaloDigiSiECalXml function
### ----------------------------------------------------------------------------------------------------
### Start of writeILDCaloDigiScECalXml function
### ----------------------------------------------------------------------------------------------------

    def writeILDCaloDigiScECalXml(self):
        self.logger.debug('Writing ILDCaloDigi xml block for Sc ECal.')

        ecalOtherRealisticDigi = 0
        if self._ApplyECalRealisticDigi != 0:
            ecalOtherRealisticDigi = 1 # ECal other is always silicon, not scintillator according to digitiser

        ildCaloDigi  = """
<processor name="MyILDCaloDigi_ScTrans" type="ILDCaloDigi">
  <!--ILD digitizer...-->
  <!--Calibration coefficients for ECAL-->
  <parameter name="CalibrECAL" type="FloatVec">""" + str(self._CalibrECal) + ' ' + str(2*self._CalibrECal) + """</parameter>
  <!--Calibration coefficients for HCAL barrel, endcap, other-->
  <parameter name="CalibrHCALBarrel" type="FloatVec">""" + str(self._CalibrHCalBarrel) + """</parameter>
  <parameter name="CalibrHCALEndcap" type="FloatVec">""" + str(self._CalibrHCalEndCap) + """</parameter>
  <parameter name="CalibrHCALOther" type="FloatVec">""" + str(self._CalibrHCalOther) + """</parameter>
  <!--ECAL Collection Names-->
  <parameter name="ECALCollections" type="StringVec">EcalBarrelScintillatorTransverseStrips EcalEndcapScintillatorTransverseStrips dummy1</parameter>
  <!--Index of ECal Layers-->
  <parameter name="ECALLayers" type="IntVec">""" + str(self._ECalLayerChange) + """ 100  </parameter>
  <!--Threshold for ECAL Hits in GeV-->
  <parameter name="ECALThreshold" type="float">5e-05 </parameter>
  <!--HCAL Collection Names-->
  <parameter name="HCALCollections" type="StringVec">dummy2 dummy3 dummy4</parameter>
  <!--Index of HCal Layers-->
  <parameter name="HCALLayers" type="IntVec">100 </parameter>
  <!--Threshold for HCAL Hits in MIPs - given HCALThresholdUnit is specified-->
  <parameter name="HCALThreshold" type="float">0.5 </parameter>
  <!--Digital Ecal-->
  <parameter name="IfDigitalEcal" type="int">0 </parameter>
  <!--Digital Hcal-->
  <parameter name="IfDigitalHcal" type="int">0 </parameter>
  <!--name for the new collection -->
  <parameter name="ECALOutputCollection0" type="stringVec">ECALScTransverseBarrel </parameter>
  <parameter name="ECALOutputCollection1" type="stringVec">ECALScTransverseEndcap </parameter>
  <parameter name="ECALOutputCollection2" type="stringVec">blah1 </parameter>
  <parameter name="HCALOutputCollection0" type="stringVec">blah2 </parameter>
  <parameter name="HCALOutputCollection1" type="stringVec">blah3 </parameter>
  <parameter name="HCALOutputCollection2" type="stringVec">blah4 </parameter>
  <!--CaloHit Relation Collection-->
  <parameter name="RelationOutputCollection" type="string">RelationECALScTransverseCaloHit</parameter>
  <!--Gap Correction-->
  <parameter name="ECALGapCorrection" type="int"> 0 </parameter>
  <!--Gap Correction Fudge Factor-->
  <parameter name="ECALGapCorrectionFactor" type="int">""" + str(self._ECalGapCorrectionFactor) + """</parameter>
  <parameter name="ECALModuleGapCorrectionFactor" type="int"> 0.0 </parameter>
  <!-- Timing -->
  <parameter name="UseEcalTiming" type="int">1</parameter>
  <parameter name="UseHcalTiming" type="int">1</parameter>
  <parameter name="ECALBarrelTimeWindowMax" type="float">""" + str(self._ECalBarrelTimeWindowMax) + """</parameter>
  <parameter name="HCALBarrelTimeWindowMax" type="float">""" + str(self._HCalBarrelTimeWindowMax) + """</parameter>
  <parameter name="ECALEndcapTimeWindowMax" type="float">""" + str(self._ECalEndCapTimeWindowMax) + """</parameter>
  <parameter name="HCALEndcapTimeWindowMax" type="float">""" + str(self._HCalEndCapTimeWindowMax) + """</parameter>
  <parameter name="ECALTimeWindowMin" type="float"> -1.0 </parameter>
  <parameter name="HCALTimeWindowMin" type="float"> -1.0 </parameter>
  <parameter name="ECALCorrectTimesForPropagation" type="int">1</parameter>
  <parameter name="HCALCorrectTimesForPropagation" type="int">1</parameter>
  <parameter name="ECALDeltaTimeHitResolution" type="float"> 20.0 </parameter>
  <parameter name="HCALDeltaTimeHitResolution" type="float"> 20.0 </parameter>
  <!-- Realistic ECal -->
  <parameter name="ECAL_apply_realistic_digi" type="int">""" + str(self._ApplyECalRealisticDigi) + """</parameter>
  <parameter name="CalibECALMIP" type="float">""" + str(self._CalibrECalMIP) + """</parameter>
  <parameter name="ECAL_maxDynamicRange_MIP" type="float">""" + str(self._ECalMaxDynamicRangeMIP) + """</parameter>
  <parameter name="ECAL_elec_noise_mips" type="float">0.07</parameter>
  <parameter name="ECAL_deadCellRate" type="float">0</parameter>
  <parameter name="ECAL_miscalibration_uncorrel" type="float">0</parameter>
  <parameter name="ECAL_miscalibration_uncorrel_memorise" type="bool">false</parameter>
  <parameter name="ECAL_miscalibration_correl" type="float">0</parameter>
  <parameter name="energyPerEHpair" type="float">3.6</parameter>
  <parameter name="ECAL_PPD_PE_per_MIP" type="float">7</parameter>
  <parameter name="ECAL_PPD_N_Pixels" type="int">10000</parameter>
  <parameter name="ECAL_PPD_N_Pixels_uncertainty" type="float">0.05</parameter>
  <parameter name="ECAL_pixel_spread" type="float">0.05</parameter>
  <!-- Realistic HCal -->
  <parameter name="HCAL_apply_realistic_digi" type="int">""" + str(self._ApplyHCalRealisticDigi) + """</parameter>
  <parameter name="HCALThresholdUnit" type="string">MIP</parameter>
  <parameter name="CalibHCALMIP" type="float">""" + str(self._CalibrHCalMIP) + """</parameter>
  <parameter name="HCAL_maxDynamicRange_MIP" type="float">""" + str(self._HCalMaxDynamicRangeMIP) + """</parameter>
  <parameter name="HCAL_elec_noise_mips" type="float">0.06</parameter>
  <parameter name="HCAL_deadCellRate" type="float">0</parameter>
  <parameter name="HCAL_PPD_N_Pixels" type="int">2000</parameter>
  <parameter name="HCAL_PPD_PE_per_MIP" type="float">15</parameter>
  <parameter name="HCAL_pixel_spread" type="float">0.05</parameter>
  <parameter name="HCAL_PPD_N_Pixels_uncertainty" type="float">0</parameter>
  <parameter name="HCAL_miscalibration_uncorrel" type="float">0</parameter>
  <parameter name="HCAL_miscalibration_correl" type="float">0</parameter>
</processor>

<processor name="MyILDCaloDigi_ScLong" type="ILDCaloDigi">
  <!--ILD digitizer...-->
  <!--Calibration coefficients for ECAL-->
  <parameter name="CalibrECAL" type="FloatVec">""" + str(self._CalibrECal) + ' ' + str(2*self._CalibrECal) + """</parameter>
  <!--Calibration coefficients for HCAL barrel, endcap, other-->
  <parameter name="CalibrHCALBarrel" type="FloatVec">""" + str(self._CalibrHCalBarrel) + """</parameter>
  <parameter name="CalibrHCALEndcap" type="FloatVec">""" + str(self._CalibrHCalEndCap) + """</parameter>
  <parameter name="CalibrHCALOther" type="FloatVec">""" + str(self._CalibrHCalOther) + """</parameter>
  <!--ECAL Collection Names-->
  <parameter name="ECALCollections" type="StringVec">EcalBarrelScintillatorLongitudinalStrips EcalEndcapScintillatorLongitudinalStrips dummy5 </parameter>
  <!--Index of ECal Layers-->
  <parameter name="ECALLayers" type="IntVec">""" + str(self._ECalLayerChange) + """ 100  </parameter>
  <!--Threshold for ECAL Hits in GeV-->
  <parameter name="ECALThreshold" type="float">5e-05 </parameter>
  <!--HCAL Collection Names-->
  <parameter name="HCALCollections" type="StringVec">dummy6 dummy7 dummy8</parameter>
  <!--Index of HCal Layers-->
  <parameter name="HCALLayers" type="IntVec">100 </parameter>
  <!--Threshold for HCAL Hits in MIPs - given HCALThresholdUnit is specified-->
  <parameter name="HCALThreshold" type="float">0.5 </parameter>
  <!--Digital Ecal-->
  <parameter name="IfDigitalEcal" type="int">0 </parameter>
  <!--Digital Hcal-->
  <parameter name="IfDigitalHcal" type="int">0 </parameter>
  <!--name for the new collection -->
  <parameter name="ECALOutputCollection0" type="stringVec">ECALScLongitudinalBarrel </parameter>
  <parameter name="ECALOutputCollection1" type="stringVec">ECALScLongitudinalEndcap </parameter>
  <parameter name="ECALOutputCollection2" type="stringVec">blah5 </parameter>
  <parameter name="HCALOutputCollection0" type="stringVec">blah6 </parameter>
  <parameter name="HCALOutputCollection1" type="stringVec">blah7 </parameter>
  <parameter name="HCALOutputCollection2" type="stringVec">blah8 </parameter>
  <!--CaloHit Relation Collection-->
  <parameter name="RelationOutputCollection" type="string">RelationECALScLongitudinalCaloHit</parameter>
  <!--Gap Correction-->
  <parameter name="ECALGapCorrection" type="int"> 0 </parameter>
  <!--Gap Correction Fudge Factor-->
  <parameter name="ECALGapCorrectionFactor" type="float">""" + str(self._ECalGapCorrectionFactor) + """</parameter>
  <parameter name="ECALModuleGapCorrectionFactor" type="int"> 0.0 </parameter>
  <!-- Timing -->
  <parameter name="UseEcalTiming" type="int">1</parameter>
  <parameter name="UseHcalTiming" type="int">1</parameter>
  <parameter name="ECALBarrelTimeWindowMax" type="float">""" + str(self._ECalBarrelTimeWindowMax) + """</parameter>
  <parameter name="HCALBarrelTimeWindowMax" type="float">""" + str(self._HCalBarrelTimeWindowMax) + """</parameter>
  <parameter name="ECALEndcapTimeWindowMax" type="float">""" + str(self._ECalEndCapTimeWindowMax) + """</parameter>
  <parameter name="HCALEndcapTimeWindowMax" type="float">""" + str(self._HCalEndCapTimeWindowMax) + """</parameter>
  <parameter name="ECALTimeWindowMin" type="float"> -1.0 </parameter>
  <parameter name="HCALTimeWindowMin" type="float"> -1.0 </parameter>
  <parameter name="ECALCorrectTimesForPropagation" type="int">1</parameter>
  <parameter name="HCALCorrectTimesForPropagation" type="int">1</parameter>
  <parameter name="ECALDeltaTimeHitResolution" type="float"> 20.0 </parameter>
  <parameter name="HCALDeltaTimeHitResolution" type="float"> 20.0 </parameter>
  <!-- Realistic ECal -->
  <parameter name="ECAL_apply_realistic_digi" type="int">""" + str(self._ApplyECalRealisticDigi) + """</parameter>
  <parameter name="CalibECALMIP" type="float">""" + str(self._CalibrECalMIP) + """</parameter>
  <parameter name="ECAL_maxDynamicRange_MIP" type="float">""" + str(self._ECalMaxDynamicRangeMIP) + """</parameter>
  <parameter name="ECAL_elec_noise_mips" type="float">0.07</parameter>
  <parameter name="ECAL_deadCellRate" type="float">0</parameter>
  <parameter name="ECAL_miscalibration_uncorrel" type="float">0</parameter>
  <parameter name="ECAL_miscalibration_uncorrel_memorise" type="bool">false</parameter>
  <parameter name="ECAL_miscalibration_correl" type="float">0</parameter>
  <parameter name="energyPerEHpair" type="float">3.6</parameter>
  <parameter name="ECAL_PPD_PE_per_MIP" type="float">7</parameter>
  <parameter name="ECAL_PPD_N_Pixels" type="int">10000</parameter>
  <parameter name="ECAL_PPD_N_Pixels_uncertainty" type="float">0.05</parameter>
  <parameter name="ECAL_pixel_spread" type="float">0.05</parameter>
  <!-- Realistic HCal -->
  <parameter name="HCAL_apply_realistic_digi" type="int">""" + str(self._ApplyHCalRealisticDigi) + """</parameter>
  <parameter name="HCALThresholdUnit" type="string">MIP</parameter>
  <parameter name="CalibHCALMIP" type="float">""" + str(self._CalibrHCalMIP) + """</parameter>
  <parameter name="HCAL_maxDynamicRange_MIP" type="float">""" + str(self._HCalMaxDynamicRangeMIP) + """</parameter>
  <parameter name="HCAL_elec_noise_mips" type="float">0.06</parameter>
  <parameter name="HCAL_deadCellRate" type="float">0</parameter>
  <parameter name="HCAL_PPD_N_Pixels" type="int">2000</parameter>
  <parameter name="HCAL_PPD_PE_per_MIP" type="float">15</parameter>
  <parameter name="HCAL_pixel_spread" type="float">0.05</parameter>
  <parameter name="HCAL_PPD_N_Pixels_uncertainty" type="float">0</parameter>
  <parameter name="HCAL_miscalibration_uncorrel" type="float">0</parameter>
  <parameter name="HCAL_miscalibration_correl" type="float">0</parameter>
</processor>

<processor name="MyILDCaloDigi" type="ILDCaloDigi">
  <!--ILD digitizer...-->
  <!--Calibration coefficients for ECAL-->
  <parameter name="CalibrECAL" type="FloatVec">""" + str(self._CalibrECal) + ' ' + str(2*self._CalibrECal)  + """</parameter>
  <!--Calibration coefficients for HCAL barrel, endcap, other-->
  <parameter name="CalibrHCALBarrel" type="FloatVec">""" + str(self._CalibrHCalBarrel) + """</parameter>
  <parameter name="CalibrHCALEndcap" type="FloatVec">""" + str(self._CalibrHCalEndCap) + """</parameter>
  <parameter name="CalibrHCALOther" type="FloatVec">""" + str(self._CalibrHCalOther) + """</parameter>
  <!--ECAL Collection Names-->
  <parameter name="ECALCollections" type="StringVec">EcalBarrelSiliconCollection EcalEndcapSiliconCollection EcalEndcapRingCollection </parameter>
  <!--Index of ECal Layers-->
  <parameter name="ECALLayers" type="IntVec">""" + str(self._ECalLayerChange) + """ 100  </parameter>
  <!--Threshold for ECAL Hits in GeV-->
  <parameter name="ECALThreshold" type="float">5e-05 </parameter>
  <!--HCAL Collection Names-->
  <parameter name="HCALCollections" type="StringVec">HcalBarrelRegCollection HcalEndCapsCollection HcalEndCapRingsCollection</parameter>
  <!--Index of HCal Layers-->
  <parameter name="HCALLayers" type="IntVec">100 </parameter>
  <!--Threshold for HCAL Hits in MIPs - given HCALThresholdUnit is specified-->
  <parameter name="HCALThreshold" type="float">0.5 </parameter>
  <!--Digital Ecal-->
  <parameter name="IfDigitalEcal" type="int">0 </parameter>
  <!--Digital Hcal-->
  <parameter name="IfDigitalHcal" type="int">0 </parameter>
  <!--name for the new collection -->
  <parameter name="ECALOutputCollection0" type="stringVec">ECALBarrel </parameter>
  <parameter name="ECALOutputCollection1" type="stringVec">ECALEndcap </parameter>
  <parameter name="ECALOutputCollection2" type="stringVec">ECALOther </parameter>
  <parameter name="HCALOutputCollection0" type="stringVec">HCALBarrel </parameter>
  <parameter name="HCALOutputCollection1" type="stringVec">HCALEndcap </parameter>
  <parameter name="HCALOutputCollection2" type="stringVec">HCALOther </parameter>
  <!--CaloHit Relation Collection-->
  <parameter name="RelationOutputCollection" type="string"> RelationCaloHit</parameter>
  <!--Gap Correction-->
  <parameter name="ECALGapCorrection" type="int"> 0 </parameter>
  <!--Gap Correction Fudge Factor-->
  <parameter name="ECALGapCorrectionFactor" type="float">""" + str(self._ECalGapCorrectionFactor) + """</parameter>
  <parameter name="ECALModuleGapCorrectionFactor" type="int"> 0.0 </parameter>
  <!-- Timing -->
  <parameter name="UseEcalTiming" type="int">1</parameter>
  <parameter name="UseHcalTiming" type="int">1</parameter>
  <parameter name="ECALBarrelTimeWindowMax" type="float">""" + str(self._ECalBarrelTimeWindowMax) + """</parameter>
  <parameter name="HCALBarrelTimeWindowMax" type="float">""" + str(self._HCalBarrelTimeWindowMax) + """</parameter>
  <parameter name="ECALEndcapTimeWindowMax" type="float">""" + str(self._ECalEndCapTimeWindowMax) + """</parameter>
  <parameter name="HCALEndcapTimeWindowMax" type="float">""" + str(self._HCalEndCapTimeWindowMax) + """</parameter>
  <parameter name="ECALTimeWindowMin" type="float"> -1.0 </parameter>
  <parameter name="HCALTimeWindowMin" type="float"> -1.0 </parameter>
  <parameter name="ECALCorrectTimesForPropagation" type="int">1</parameter>
  <parameter name="HCALCorrectTimesForPropagation" type="int">1</parameter>
  <parameter name="ECALDeltaTimeHitResolution" type="float"> 20.0 </parameter>
  <parameter name="HCALDeltaTimeHitResolution" type="float"> 20.0 </parameter>
  <!-- Realistic ECal -->
  <parameter name="ECAL_apply_realistic_digi" type="int">""" + str(ecalOtherRealisticDigi) + """</parameter>
  <parameter name="CalibECALMIP" type="float">""" + str(self._CalibrECalMIP) + """</parameter>
  <parameter name="ECAL_maxDynamicRange_MIP" type="float">""" + str(self._ECalMaxDynamicRangeMIP) + """</parameter>
  <parameter name="ECAL_elec_noise_mips" type="float">0.07</parameter>
  <parameter name="ECAL_deadCellRate" type="float">0</parameter>
  <parameter name="ECAL_miscalibration_uncorrel" type="float">0</parameter>
  <parameter name="ECAL_miscalibration_uncorrel_memorise" type="bool">false</parameter>
  <parameter name="ECAL_miscalibration_correl" type="float">0</parameter>
  <parameter name="energyPerEHpair" type="float">3.6</parameter>
  <parameter name="ECAL_PPD_PE_per_MIP" type="float">7</parameter>
  <parameter name="ECAL_PPD_N_Pixels" type="int">10000</parameter>
  <parameter name="ECAL_PPD_N_Pixels_uncertainty" type="float">0.05</parameter>
  <parameter name="ECAL_pixel_spread" type="float">0.05</parameter>
  <!-- Realistic HCal -->
  <parameter name="HCAL_apply_realistic_digi" type="int">""" + str(self._ApplyHCalRealisticDigi) + """</parameter>
  <parameter name="HCALThresholdUnit" type="string">MIP</parameter>
  <parameter name="CalibHCALMIP" type="float">""" + str(self._CalibrHCalMIP) + """</parameter>
  <parameter name="HCAL_maxDynamicRange_MIP" type="float">""" + str(self._HCalMaxDynamicRangeMIP) + """</parameter>
  <parameter name="HCAL_elec_noise_mips" type="float">0.06</parameter>
  <parameter name="HCAL_deadCellRate" type="float">0</parameter>
  <parameter name="HCAL_PPD_N_Pixels" type="int">2000</parameter>
  <parameter name="HCAL_PPD_PE_per_MIP" type="float">15</parameter>
  <parameter name="HCAL_pixel_spread" type="float">0.05</parameter>
  <parameter name="HCAL_PPD_N_Pixels_uncertainty" type="float">0</parameter>
  <parameter name="HCAL_miscalibration_uncorrel" type="float">0</parameter>
  <parameter name="HCAL_miscalibration_correl" type="float">0</parameter>
</processor>
"""
        return ildCaloDigi

### ----------------------------------------------------------------------------------------------------
### End of writeILDCaloDigiScECalXml function
### ----------------------------------------------------------------------------------------------------
### Start of writeSimpleMuonDigiXmlHeader function
### ----------------------------------------------------------------------------------------------------

    def writeSimpleMuonDigiXmlHeader(self):
        self.logger.debug('Writing SimpleMuonDigi xml header block.')
        simpleMuonDigiHeader = """<processor name="MySimpleMuonDigi"/>"""
        return simpleMuonDigiHeader

### ----------------------------------------------------------------------------------------------------
### End of writeSimpleMuonDigiXmlHeader function
### ----------------------------------------------------------------------------------------------------
### Start of writeSimpleMuonDigiXml function
### ----------------------------------------------------------------------------------------------------

    def writeSimpleMuonDigiXml(self):
        self.logger.debug('Writing SimpleMuonDigi xml block.')
        simpleMuonDigi = """
<processor name="MySimpleMuonDigi" type="SimpleMuonDigi">
  <!--Performs simple digitization of sim calo hits...-->
  <!--Calibration coefficients for MUON-->
  <parameter name="CalibrMUON" type="FloatVec">""" + str(self._CalibrMuon) + """</parameter>
  <!-- maximum hit energy for a MUON hit -->
  <parameter name="MaxHitEnergyMUON" type="float">2.0</parameter>
  <!--MUON Collection Names-->
  <parameter name="MUONCollections" type="StringVec">
   MuonBarrelCollection MuonEndCapCollection</parameter>
  <!--MUON Collection of real Hits-->
  <parameter name="MUONOutputCollection" type="string">MUON </parameter>
  <!--Threshold for MUON Hits in GeV-->
  <parameter name="MUONThreshold" type="float">1e-06 </parameter>
  <!--MuonHit Relation Collection-->
  <parameter name="RelationOutputCollection" type="string">RelationMuonHit </parameter>
</processor>"""
        return simpleMuonDigi

### ----------------------------------------------------------------------------------------------------
### End of writeSimpleMuonDigiXml function
### ----------------------------------------------------------------------------------------------------
### Start of writeMarlinPandoraXmlHeader function
### ----------------------------------------------------------------------------------------------------

    def writePandoraXmlHeader(self):
        self.logger.debug('Writing MarlinPandora and PfoAnalysis xml header block.')
        headerString = """
<processor name="MyMarlinPandoraDefault"/>
<processor name="MyPfoAnalysisDefault"/>"""
        return headerString

### ----------------------------------------------------------------------------------------------------
### End of writeMarlinPandoraXmlHeader function
### ----------------------------------------------------------------------------------------------------
### Start of writeMarlinPandoraSiECalXml function
### ----------------------------------------------------------------------------------------------------

    def writeMarlinPandoraSiECalXml(self):
        self.logger.debug('Writing MarlinPandora xml block for Si ECal.')
        marlinPandoraTemplate  = """
<processor name="MyMarlinPandoraDefault" type="PandoraPFANewProcessor">
  <parameter name="PandoraSettingsXmlFile" type="String">""" + self._PandoraSettingsFile + """</parameter>
  <!-- Collection names -->
  <parameter name="TrackCollections" type="StringVec">MarlinTrkTracks</parameter>
  <parameter name="ECalCaloHitCollections" type="StringVec">ECALBarrel ECALEndcap ECALOther</parameter>
  <parameter name="HCalCaloHitCollections" type="StringVec">HCALBarrel HCALEndcap HCALOther</parameter>
  <parameter name="LCalCaloHitCollections" type="StringVec">LCAL</parameter>
  <parameter name="LHCalCaloHitCollections" type="StringVec">LHCAL</parameter>
  <parameter name="MuonCaloHitCollections" type="StringVec">MUON</parameter>
  <parameter name="MCParticleCollections" type="StringVec">MCParticle</parameter>
  <parameter name="RelCaloHitCollections" type="StringVec">RelationCaloHit RelationMuonHit</parameter>
  <parameter name="RelTrackCollections" type="StringVec">MarlinTrkTracksMCTruthLink</parameter>
  <parameter name="KinkVertexCollections" type="StringVec">KinkVertices</parameter>
  <parameter name="ProngVertexCollections" type="StringVec">ProngVertices</parameter>
  <parameter name="SplitVertexCollections" type="StringVec">SplitVertices</parameter>
  <parameter name="V0VertexCollections" type="StringVec">V0Vertices</parameter>
  <parameter name="ClusterCollectionName" type="String">PandoraClustersDefault</parameter>
  <parameter name="PFOCollectionName" type="String">PandoraPFOsDefault</parameter>
  <parameter name="StartVertexCollectionName" type="String">StartVerticesDefault</parameter>
  <!-- Calibration constants -->
  <parameter name="ECalToMipCalibration" type="float">""" + str(self._ECalGeVToMIP) + """</parameter>
  <parameter name="HCalToMipCalibration" type="float">""" + str(self._HCalGeVToMIP) + """</parameter>
  <parameter name="ECalMipThreshold" type="float">""" + str(self._ECalMIPThresholdPandora) + """</parameter>
  <parameter name="HCalMipThreshold" type="float">""" + str(self._HCalMIPThresholdPandora) + """</parameter>
  <parameter name="ECalToEMGeVCalibration" type="float">""" + str(self._ECalToEm) + """</parameter>
  <parameter name="HCalToEMGeVCalibration" type="float">""" + str(self._HCalToEm) + """</parameter>
  <parameter name="ECalToHadGeVCalibrationBarrel" type="float">""" + str(self._ECalToHad) + """</parameter>
  <parameter name="ECalToHadGeVCalibrationEndCap" type="float">""" + str(self._ECalToHad) + """</parameter>
  <parameter name="HCalToHadGeVCalibration" type="float">""" + str(self._HCalToHad) + """</parameter>
  <parameter name="MuonToMipCalibration" type="float">""" + str(self._MuonGeVToMIP) + """</parameter>
  <parameter name="DigitalMuonHits" type="int">0</parameter>
  <parameter name="MaxHCalHitHadronicEnergy" type="float">""" + str(self._MHHHE) + """</parameter>
  <parameter name="AbsorberRadLengthECal" type="float">0.2854</parameter>
  <parameter name="AbsorberIntLengthECal" type="float">0.0101</parameter>
  <parameter name="AbsorberRadLengthHCal" type="float">0.0569</parameter>
  <parameter name="AbsorberIntLengthHCal" type="float">0.0060</parameter>
  <parameter name="AbsorberRadLengthOther" type="float">0.0569</parameter>
  <parameter name="AbsorberIntLengthOther" type="float">0.0060</parameter>
  <!--Whether to calculate track states manually, rather than copy stored fitter values-->
  <parameter name="UseOldTrackStateCalculation" type="int">0 </parameter>
</processor> """
        return marlinPandoraTemplate

### ----------------------------------------------------------------------------------------------------
### End of writeMarlinPandoraSiECalXml function
### ----------------------------------------------------------------------------------------------------
### Start of writeMarlinPandoraScECalXml function
### ----------------------------------------------------------------------------------------------------

    def writeMarlinPandoraScECalXml(self):
        self.logger.debug('Writing MarlinPandora xml block for Sc ECal.')
        marlinPandoraTemplate  = """
<processor name="MyMarlinPandoraDefault" type="PandoraPFANewProcessor">
  <parameter name="StripSplittingOn" type="bool">0</parameter>
  <parameter name="UseEcalScLayers" type="bool">1</parameter>
  <parameter name="PandoraSettingsXmlFile" type="String">""" + self._PandoraSettingsFile + """</parameter>
  <!-- Collection names -->
  <parameter name="TrackCollections" type="StringVec">MarlinTrkTracks</parameter>
  <parameter name="ECalCaloHitCollections" type="StringVec">ECALScLongitudinalBarrel ECALScTransverseBarrel ECALScLongitudinalEndcap ECALScTransverseEndcap ECALOther</parameter>
  <parameter name="HCalCaloHitCollections" type="StringVec">HCALBarrel HCALEndcap HCALOther</parameter>
  <parameter name="LCalCaloHitCollections" type="StringVec">LCAL</parameter>
  <parameter name="LHCalCaloHitCollections" type="StringVec">LHCAL</parameter>
  <parameter name="MuonCaloHitCollections" type="StringVec">MUON</parameter>
  <parameter name="MCParticleCollections" type="StringVec">MCParticle</parameter>
  <parameter name="RelCaloHitCollections" type="StringVec">RelationECALScTransverseCaloHit RelationECALScLongitudinalCaloHit RelationCaloHit RelationMuonHit</parameter>
  <parameter name="RelTrackCollections" type="StringVec">MarlinTrkTracksMCTruthLink</parameter>
  <parameter name="KinkVertexCollections" type="StringVec">KinkVertices</parameter>
  <parameter name="ProngVertexCollections" type="StringVec">ProngVertices</parameter>
  <parameter name="SplitVertexCollections" type="StringVec">SplitVertices</parameter>
  <parameter name="V0VertexCollections" type="StringVec">V0Vertices</parameter>
  <parameter name="ClusterCollectionName" type="String">PandoraClustersDefault</parameter>
  <parameter name="PFOCollectionName" type="String">PandoraPFOsDefault</parameter>
  <parameter name="StartVertexCollectionName" type="String">StartVerticesDefault</parameter>
  <!-- Calibration constants, ECalSc -->
  <parameter name="ECalScToMipCalibration" type="float">""" + str(self._ECalGeVToMIP) + """</parameter>
  <parameter name="ECalScMipThreshold" type="float">""" + str(self._ECalMIPThresholdPandora) + """</parameter>
  <parameter name="ECalScToEMGeVCalibration" type="float">""" + str(self._ECalToEm) + """</parameter>
  <parameter name="ECalScToHadGeVCalibrationBarrel" type="float">""" + str(self._ECalToHad) + """</parameter>
  <parameter name="ECalScToHadGeVCalibrationEndCap" type="float">""" + str(self._ECalToHad) + """</parameter>
  <!-- ECal other -->
  <!-- Fixed taken from DetModel 38, Default Model, and Reco Var 71, 1 GeV Truncation, 100ns Timing Cuts, Realisitic Options -->
  <parameter name="ECalToMipCalibration" type="float">153.846</parameter>
  <parameter name="ECalMipThreshold" type="float">0.5</parameter>
  <parameter name="ECalToEMGeVCalibration" type="float">1.00356141304</parameter>
  <parameter name="ECalToHadGeVCalibrationBarrel" type="float">1.14127910463</parameter>
  <parameter name="ECalToHadGeVCalibrationEndCap" type="float">1.14127910463</parameter>
  <!-- HCal -->
  <parameter name="HCalToMipCalibration" type="float">""" + str(self._HCalGeVToMIP) + """</parameter>
  <parameter name="HCalMipThreshold" type="float">""" + str(self._HCalMIPThresholdPandora) + """</parameter>
  <parameter name="HCalToEMGeVCalibration" type="float">""" + str(self._HCalToEm) + """</parameter>
  <parameter name="HCalToHadGeVCalibration" type="float">""" + str(self._HCalToHad) + """</parameter>
  <parameter name="MaxHCalHitHadronicEnergy" type="float">""" + str(self._MHHHE) + """</parameter>
  <!-- Muon -->
  <parameter name="MuonToMipCalibration" type="float">""" + str(self._MuonGeVToMIP) + """</parameter>
  <parameter name="DigitalMuonHits" type="int">0</parameter>
  <parameter name="AbsorberRadLengthECal" type="float">0.2854</parameter>
  <parameter name="AbsorberIntLengthECal" type="float">0.0101</parameter>
  <parameter name="AbsorberRadLengthHCal" type="float">0.0569</parameter>
  <parameter name="AbsorberIntLengthHCal" type="float">0.0060</parameter>
  <parameter name="AbsorberRadLengthOther" type="float">0.0569</parameter>
  <parameter name="AbsorberIntLengthOther" type="float">0.0060</parameter>
  <!--Whether to calculate track states manually, rather than copy stored fitter values-->
  <parameter name="UseOldTrackStateCalculation" type="int">0 </parameter>
</processor> """
        return marlinPandoraTemplate

### ----------------------------------------------------------------------------------------------------
### End of writeMarlinPandoraScECalXml function
### ----------------------------------------------------------------------------------------------------
### Start of writePandoraAnalsisSiECalXml function
### ----------------------------------------------------------------------------------------------------

    def writePandoraAnalsisSiECalXml(self):
        self.logger.debug('Writing PandoraAnalysis xml block for Si ECal.')
        pandoraAnalysis  = """
<processor name="MyPfoAnalysisDefault" type="PfoAnalysis">
  <!--PfoAnalysis analyses output of PandoraPFANew, Modified for calibration-->
  <!--Names of input pfo collection-->
  <parameter name="PfoCollection" type="string" lcioInType="ReconstructedParticle">PandoraPFOsDefault </parameter>
  <!--Names of mc particle collection-->
  <parameter name="MCParticleCollection" type="string" lcioInType="MCParticle">MCParticle </parameter>
  <!--Collect Calibration Details-->
  <parameter name="CollectCalibrationDetails" type="int">1</parameter>
  <!--Detector Geometry Missing From Gear-->
  <parameter name="HCalRingOuterSymmetryOrder" type="int">8</parameter>
  <parameter name="HCalRingOuterPhi0" type="int">0</parameter>
  <!--Name of the ECAL collection used to form clusters-->
  <parameter name="ECalCollections" type="StringVec" lcioInType="CalorimeterHit">ECALBarrel ECALEndcap ECALOther</parameter>
  <!--Name of the HCAL collection used to form clusters-->
  <parameter name="HCalCollections" type="StringVec" lcioInType="CalorimeterHit">HCALBarrel HCALEndcap HCALOther </parameter>
  <!--Name of the MUON collection used to form clusters-->
  <parameter name="MuonCollections" type="StringVec" lcioInType="CalorimeterHit">MUON </parameter>
  <!--Name of the BCAL collection used to form clusters-->
  <parameter name="BCalCollections" type="StringVec" lcioInType="CalorimeterHit">BCAL</parameter>
  <!--Name of the LHCAL collection used to form clusters-->
  <parameter name="LHCalCollections" type="StringVec" lcioInType="CalorimeterHit">LHCAL </parameter>
  <!--Name of the LCAL collection used to form clusters-->
  <parameter name="LCalCollections" type="StringVec" lcioInType="CalorimeterHit">LCAL </parameter>
  <!--ECal Collection SimCaloHit Names-->
  <parameter name="ECalCollectionsSimCaloHit" type="StringVec">EcalBarrelSiliconCollection EcalEndcapSiliconCollection  EcalEndcapRingCollection </parameter>
  <!--HCal Barrel Collection SimCaloHit Names-->
  <parameter name="HCalBarrelCollectionsSimCaloHit" type="StringVec"> HcalBarrelRegCollection </parameter>
  <!--HCal Endcap Collection SimCaloHit Names-->
  <parameter name="HCalEndCapCollectionsSimCaloHit" type="StringVec"> HcalEndCapsCollection </parameter>
  <!--HCal Other/Ring Collection SimCaloHit Names-->
  <parameter name="HCalOtherCollectionsSimCaloHit" type="StringVec"> HcalEndCapRingsCollection</parameter>
  <!--Set the debug print level-->
  <parameter name="Printing" type="int"> 0 </parameter>
  <!--Output root file name-->
  <parameter name="RootFile" type="string">PfoAnalysisRootFile</parameter>
</processor>"""
        return pandoraAnalysis

### ----------------------------------------------------------------------------------------------------
### End of writePandoraAnalsisSiECalXml function
### ----------------------------------------------------------------------------------------------------
### Start of writePandoraAnalsisScECalXml function
### ----------------------------------------------------------------------------------------------------

    def writePandoraAnalsisScECalXml(self):
        self.logger.debug('Writing PandoraAnalysis xml block for Sc ECal.')
        pandoraAnalysis  = """
<processor name="MyPfoAnalysisDefault" type="PfoAnalysis">
  <!--PfoAnalysis analyses output of PandoraPFANew, Modified for calibration-->
  <!--Names of input pfo collection-->
  <parameter name="PfoCollection" type="string" lcioInType="ReconstructedParticle">PandoraPFOsDefault </parameter>
  <!--Names of mc particle collection-->
  <parameter name="MCParticleCollection" type="string" lcioInType="MCParticle">MCParticle </parameter>
  <!--Collect Calibration Details-->^M
  <parameter name="CollectCalibrationDetails" type="int">1</parameter>^M
  <!--Detector Geometry Missing From Gear-->^M
  <parameter name="HCalRingOuterSymmetryOrder" type="int">8</parameter>^M
  <parameter name="HCalRingOuterPhi0" type="int">0</parameter>^M
  <!--Name of the ECAL collection used to form clusters-->^M
  <parameter name="ECalCollections" type="StringVec" lcioInType="CalorimeterHit">ECALScLongitudinalBarrel ECALScTransverseBarrel ECALScLongitudinalEndcap ECALScTransverseEndcap ECALOther</parameter>^M
  <!--Name of the HCAL collection used to form clusters-->^M
  <parameter name="HCalCollections" type="StringVec" lcioInType="CalorimeterHit">HCALBarrel HCALEndcap HCALOther </parameter>^M
  <!--Name of the MUON collection used to form clusters-->^M
  <parameter name="MuonCollections" type="StringVec" lcioInType="CalorimeterHit">MUON </parameter>^M
  <!--Name of the BCAL collection used to form clusters-->^M
  <parameter name="BCalCollections" type="StringVec" lcioInType="CalorimeterHit">BCAL</parameter>^M
  <!--Name of the LHCAL collection used to form clusters-->^M
  <parameter name="LHCalCollections" type="StringVec" lcioInType="CalorimeterHit">LHCAL </parameter>^M
  <!--Name of the LCAL collection used to form clusters-->^M
  <parameter name="LCalCollections" type="StringVec" lcioInType="CalorimeterHit">LCAL </parameter>^M
  <!--ECal Collection SimCaloHit Names-->^M
  <parameter name="ECalCollectionsSimCaloHit" type="StringVec">EcalBarrelScintillatorLongitudinalStrips EcalEndcapScintillatorLongitudinalStrips EcalBarrelScintillatorTransverseStrips EcalEndcapScintillatorTransverseStrips EcalEndcapRingCollection</parameter>^M
  <!--HCal Barrel Collection SimCaloHit Names-->^M
  <parameter name="HCalBarrelCollectionsSimCaloHit" type="StringVec"> HcalBarrelRegCollection </parameter>^M
  <!--HCal Endcap Collection SimCaloHit Names-->^M
  <parameter name="HCalEndCapCollectionsSimCaloHit" type="StringVec"> HcalEndCapsCollection </parameter>^M
  <!--HCal Other/Ring Collection SimCaloHit Names-->^M
  <parameter name="HCalOtherCollectionsSimCaloHit" type="StringVec"> HcalEndCapRingsCollection</parameter>^M
  <!--Set the debug print level-->
  <parameter name="Printing" type="int"> 0 </parameter>
  <!--Output root file name-->^M
  <parameter name="RootFile" type="string">PfoAnalysisRootFile</parameter>^M
</processor>"""
        return pandoraAnalysis

### ----------------------------------------------------------------------------------------------------
### End of writePandoraAnalsisScECalXml function
### ----------------------------------------------------------------------------------------------------
### Start of runCondorJobs function
### ----------------------------------------------------------------------------------------------------

    def runCondorJobs(self):
        self.logger.debug('Running condor jobs.')
        nQueued = self.nQueuedCondorJobs()
        condorJobFile = 'CalibrationJob_' + self._RandomString + '.job'

        while True:
            if nQueued >= self._CondorMaxRuns:
                subprocess.call(["usleep", "500000"])

            else:
                for idx, fileToRun in enumerate(self._CondorRunList):
                    nRemaining = len(self._CondorRunList) - idx - 1
                    nQueued = self.nQueuedCondorJobs()

                    with open(condorJobFile, 'w') as jobFile:
                        jobString = self.getCondorJobString()
                        jobString += 'arguments = ' + fileToRun + '\n'
                        jobString += 'queue 1 \n'
                        jobFile.write(jobString)

                    subprocess.call(['condor_submit', condorJobFile])
                    print 'Submitted job as there were only ' + str(nQueued) + ' jobs in the queue and ' + str(nRemaining) + ' jobs remaining.'
                    subprocess.call(["usleep", "500000"])
                    os.remove(condorJobFile)

                    if 0 == nRemaining:
                        print 'All condor jobs submitted.'
                        return

### ----------------------------------------------------------------------------------------------------
### End of runCondorJobs function
### ----------------------------------------------------------------------------------------------------
### Start of getCondorJobString function
### ----------------------------------------------------------------------------------------------------

    def getCondorJobString(self):
        jobString  = 'executable              = ' + os.getcwd() + '/' + self._MarlinExecutable + '                   \n'
        jobString += 'initial_dir             = ' + os.getcwd() + '                                                  \n'
        jobString += 'notification            = never                                                                \n'
        jobString += 'Requirements            = (OSTYPE == \"SLC6\")                                                 \n'
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
### Start of checkCondorJobs function
### ----------------------------------------------------------------------------------------------------

    def checkCondorJobs(self):
        self.logger.debug('Checking on the running condor jobs.')
        while True: 
            nActiveJobs = self.nQueuedCondorJobs()
            if (nActiveJobs > 0):
                time.sleep(10)
            else:
                self.logger.debug('There are no more active condor jobs.')
                return

### ----------------------------------------------------------------------------------------------------
### End of checkCondorJobs function
### ----------------------------------------------------------------------------------------------------
### Start of checkCondorJobs function
### ----------------------------------------------------------------------------------------------------

    def nQueuedCondorJobs(self):
        self.logger.debug('Checking on the number of running condor jobs.')
        queueProcess = subprocess.Popen(['condor_q','-w'], stdout=subprocess.PIPE)
        queueOutput = queueProcess.communicate()[0]
        regex = re.compile(self._MarlinExecutable)
        queueList = regex.findall(queueOutput)
        return int(len(queueList))

### ----------------------------------------------------------------------------------------------------
### End of checkCondorJobs function
### ----------------------------------------------------------------------------------------------------

### ====================================================================================================
### GENERAL TOOLS 
### ====================================================================================================

### ----------------------------------------------------------------------------------------------------
### Start of findBetween function
### ----------------------------------------------------------------------------------------------------

def findBetween( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ''

### ----------------------------------------------------------------------------------------------------
### End of findBetween function
### ----------------------------------------------------------------------------------------------------
