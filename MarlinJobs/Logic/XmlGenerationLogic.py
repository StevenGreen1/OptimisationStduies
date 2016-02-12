#!/usr/bin/python

import os, sys, getopt, re, subprocess, math, dircache, logging, time, random, string

class XmlGeneration:
    'Common base class for generating xml steering files.'

### ----------------------------------------------------------------------------------------------------
### Start of constructor
### ----------------------------------------------------------------------------------------------------

    def __init__(self, configFileName, ecalType, realisticDigitisation, pandoraSettings, gearFile, lcioFile):

        'Logger'
        calibrationLogFullPath = os.path.join('PhotonLikelihoodGridJobs.log')
        if os.path.isfile(calibrationLogFullPath):
            os.remove(calibrationLogFullPath)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(calibrationLogFullPath)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        'Config File'
        self.configFileName = configFileName
        config = {}
        execfile(self.configFileName, config)

        'Pandora Settings, Gear File, Input Lcio File'
        self._PandoraSettingsFiles = {}
        self._PandoraSettings = []
        for key, value in pandoraSettings.iteritems():
            if 'LikelihoodData' not in key:
                self._PandoraSettingsFiles[key] = value
                self._PandoraSettings.append(key)
        self._GearFile = gearFile
        self._LcioInputFile = lcioFile

        'Si or Sw ECal'
        self._ECalType = ecalType

        'Realistic Digitisation'
        self._RealisticDigitisation = realisticDigitisation
        self.ApplyECalRealisticDigi = 0
        self.ApplyHCalRealisticDigi = 0
        self.ECalMaxDynamicRangeMIP = 0.0 # Set to 0 to avoid accidental truncation if not using realistic digitisation options
        self.HCalMaxDynamicRangeMIP = 0.0 # Set to 0 to avoid accidental truncation if not using realistic digitisation options

        if self._RealisticDigitisation:
            self.ECalMaxDynamicRangeMIP = 2500       # Realistic Values
            self.HCalMaxDynamicRangeMIP = 99999999   # Realistic Values
            self.ApplyHCalRealisticDigi = 1
            if self._ECalType.lower() in ['si']:
                self.ApplyECalRealisticDigi = 1
            if self._ECalType.lower() in ['sc']:
                self.ApplyECalRealisticDigi = 2

        self.logger.info('Realistic digitsation setting : ' + str(self._RealisticDigitisation))
        self.logger.info('self.ApplyECalRealisticDigi   : ' + str(self.ApplyECalRealisticDigi))
        self.logger.info('self.ApplyHCalRealisticDigi   : ' + str(self.ApplyHCalRealisticDigi))

        'ECal Calibration Variables - Digitisation'
        self._CalibrECal = config['CalibrECal'] 
        self._CalibrECalMIP = config['CalibrECalMIP']
        self._ECalGapCorrectionFactor = 1
        self._ECalBarrelTimeWindowMax = config['ECalBarrelTimeWindowMax']
        self._ECalEndCapTimeWindowMax = config['ECalEndcapTimeWindowMax']

        'ECal Calibration Variables - Pandora'
        self._ECalGeVToMIP = config['ECalToMIPCalibration']
        self._ECalMIPThresholdPandora = config['ECalMIPThresholdPandora']
        self._ECalToEm = config['ECalToEMGeVCalibration']
        self._ECalToHad = config['ECalToHadGeVCalibration']

        'HCal Calibration Variables - Digitisation'
        self._CalibrHCalBarrel = config['CalibrHCalBarrel']
        self._CalibrHCalEndCap = config['CalibrHCalEndcap']
        self._CalibrHCalOther = config['CalibrHCalOther']
        self._CalibrHCalMIP = config['CalibrHCalMIP']
        self._HCalBarrelTimeWindowMax = config['HCalBarrelTimeWindowMax']
        self._HCalEndCapTimeWindowMax = config['HCalEndcapTimeWindowMax']

        'HCal Calibration Variables - Pandora'
        self._HCalGeVToMIP = config['HCalToMIPCalibration']
        self._HCalMIPThresholdPandora = config['HCalMIPThresholdPandora']
        self._MHHHE = config['MaxHCalHitHadronicEnergy']
        self._HCalToEm = config['HCalToEMGeVCalibration']
        self._HCalToHad = config['HCalToHadGeVCalibration']

        'Muon Chamber Calibration Variables'
        self._CalibrMuon = config['CalibrMuon']
        self._MuonGeVToMIP = config['MuonToMIPCalibration']

### ----------------------------------------------------------------------------------------------------
### End of constructor
### ----------------------------------------------------------------------------------------------------

### ====================================================================================================
### MARLIN XML GNERATION 
### ====================================================================================================

    def produceXml(self):
        baseSteeringFile = os.path.join(os.getcwd(), 'ILD_o1_v06_XX_YY.xml')
        base = open(baseSteeringFile,'r')
        xmlTemplate = base.read()
        base.close()

        xmlTemplate = self.generateXml(xmlTemplate)
        xmlTemplate = self.setGearFile(xmlTemplate)
        xmlTemplate = self.setLcioFile(xmlTemplate)
        return xmlTemplate

### ----------------------------------------------------------------------------------------------------
### Start of writeXmlFile function
### ----------------------------------------------------------------------------------------------------

    def generateXml(self, xmlTemplate):
        if self._ECalType.lower() in ['si']:
            self.logger.debug('Writing xml file.  Si ECal')
            digitiserHeader = self.writeILDCaloDigiSiECalXmlHeader()
            xmlTemplate = re.sub('DigitiserHeader',digitiserHeader,xmlTemplate)

            simpleMuonDigiHeader = self.writeSimpleMuonDigiXmlHeader()
            xmlTemplate = re.sub('SimpleMuonDigiHeader',simpleMuonDigiHeader,xmlTemplate)

            pandoraHeader = self.writePandoraXmlHeader()
            xmlTemplate = re.sub('PandoraHeader',pandoraHeader,xmlTemplate)

            digitiserImplementation = self.writeILDCaloDigiSiECalXml()
            xmlTemplate = re.sub('DigitiserImplementation',digitiserImplementation,xmlTemplate)

            simpleMuonDigiImplementation = self.writeSimpleMuonDigiXml()
            xmlTemplate = re.sub('SimpleMuonDigiImplementation',simpleMuonDigiImplementation,xmlTemplate)

            pandoraImplementation = self.writeMarlinPandoraSiECalXml()
            pandoraImplementation += '\n'
            pandoraImplementation += self.writePandoraAnalsisSiECalXml()
            xmlTemplate = re.sub('PandoraImplementation',pandoraImplementation,xmlTemplate)
            return xmlTemplate

        elif self._ECalType.lower() in ['sc']:
            self.logger.debug('Writing xml file.  Sc ECal')
            digitiserHeader = self.writeILDCaloDigiScECalXmlHeader()
            xmlTemplate = re.sub('DigitiserHeader',digitiserHeader,xmlTemplate)

            simpleMuonDigiHeader = self.writeSimpleMuonDigiXmlHeader()
            xmlTemplate = re.sub('SimpleMuonDigiHeader',simpleMuonDigiHeader,xmlTemplate)

            pandoraHeader = self.writePandoraXmlHeader()
            xmlTemplate = re.sub('PandoraHeader',pandoraHeader,xmlTemplate)

            digitiserImplementation = self.writeILDCaloDigiScECalXml()
            xmlTemplate = re.sub('DigitiserImplementation',digitiserImplementation,xmlTemplate)

            simpleMuonDigiImplementation = self.writeSimpleMuonDigiXml()
            xmlTemplate = re.sub('SimpleMuonDigiImplementation',simpleMuonDigiImplementation,xmlTemplate)

            pandoraImplementation = self.writeMarlinPandoraScECalXml()
            pandoraImplementation += '\n'
            pandoraImplementation += self.writePandoraAnalsisScECalXml()
            xmlTemplate = re.sub('PandoraImplementation',pandoraImplementation,xmlTemplate)
            return xmlTemplate

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
  <parameter name="ECALLayers" type="IntVec">20 100 </parameter>
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
  <parameter name="ECAL_apply_realistic_digi" type="int">""" + str(self.ApplyECalRealisticDigi) + """</parameter>
  <parameter name="CalibECALMIP" type="float">""" + str(self._CalibrECalMIP) + """</parameter>
  <parameter name="ECAL_maxDynamicRange_MIP" type="float">""" + str(self.ECalMaxDynamicRangeMIP) + """</parameter>
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
  <parameter name="HCAL_apply_realistic_digi" type="int">""" + str(self.ApplyHCalRealisticDigi) + """</parameter>
  <parameter name="HCALThresholdUnit" type="string">MIP</parameter>
  <parameter name="CalibHCALMIP" type="float">""" + str(self._CalibrHCalMIP) + """</parameter>
  <parameter name="HCAL_maxDynamicRange_MIP" type="float">""" + str(self.HCalMaxDynamicRangeMIP) + """</parameter>
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
  <parameter name="ECALLayers" type="IntVec">20 100  </parameter>
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
  <parameter name="ECAL_apply_realistic_digi" type="int">""" + str(self.ApplyECalRealisticDigi) + """</parameter>
  <parameter name="CalibECALMIP" type="float">""" + str(self._CalibrECalMIP) + """</parameter>
  <parameter name="ECAL_maxDynamicRange_MIP" type="float">""" + str(self.ECalMaxDynamicRangeMIP) + """</parameter>
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
  <parameter name="HCAL_apply_realistic_digi" type="int">""" + str(self.ApplyHCalRealisticDigi) + """</parameter>
  <parameter name="HCALThresholdUnit" type="string">MIP</parameter>
  <parameter name="CalibHCALMIP" type="float">""" + str(self._CalibrHCalMIP) + """</parameter>
  <parameter name="HCAL_maxDynamicRange_MIP" type="float">""" + str(self.HCalMaxDynamicRangeMIP) + """</parameter>
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
  <parameter name="ECALLayers" type="IntVec">20 100  </parameter>
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
  <parameter name="ECAL_apply_realistic_digi" type="int">""" + str(self.ApplyECalRealisticDigi) + """</parameter>
  <parameter name="CalibECALMIP" type="float">""" + str(self._CalibrECalMIP) + """</parameter>
  <parameter name="ECAL_maxDynamicRange_MIP" type="float">""" + str(self.ECalMaxDynamicRangeMIP) + """</parameter>
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
  <parameter name="HCAL_apply_realistic_digi" type="int">""" + str(self.ApplyHCalRealisticDigi) + """</parameter>
  <parameter name="HCALThresholdUnit" type="string">MIP</parameter>
  <parameter name="CalibHCALMIP" type="float">""" + str(self._CalibrHCalMIP) + """</parameter>
  <parameter name="HCAL_maxDynamicRange_MIP" type="float">""" + str(self.HCalMaxDynamicRangeMIP) + """</parameter>
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
  <parameter name="ECALLayers" type="IntVec">20 100  </parameter>
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
  <parameter name="ECAL_apply_realistic_digi" type="int">""" + str(self.ApplyECalRealisticDigi) + """</parameter>
  <parameter name="CalibECALMIP" type="float">""" + str(self._CalibrECalMIP) + """</parameter>
  <parameter name="ECAL_maxDynamicRange_MIP" type="float">""" + str(self.ECalMaxDynamicRangeMIP) + """</parameter>
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
  <parameter name="HCAL_apply_realistic_digi" type="int">""" + str(self.ApplyHCalRealisticDigi) + """</parameter>
  <parameter name="HCALThresholdUnit" type="string">MIP</parameter>
  <parameter name="CalibHCALMIP" type="float">""" + str(self._CalibrHCalMIP) + """</parameter>
  <parameter name="HCAL_maxDynamicRange_MIP" type="float">""" + str(self.HCalMaxDynamicRangeMIP) + """</parameter>
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
        headerString = ''
        for setting in self._PandoraSettings:
            headerString += """
<processor name="MyMarlinPandora""" + setting + """"/>
<processor name="MyPfoAnalysis""" + setting + """"/>"""
        return headerString

### ----------------------------------------------------------------------------------------------------
### End of writeMarlinPandoraXmlHeader function
### ----------------------------------------------------------------------------------------------------
### Start of writeMarlinPandoraSiECalXml function
### ----------------------------------------------------------------------------------------------------

    def writeMarlinPandoraSiECalXml(self):
        self.logger.debug('Writing MarlinPandora xml block for Si ECal.')
        marlinPandoraTemplate = ''
        for setting in self._PandoraSettings:
            marlinPandoraTemplate += """
<processor name="MyMarlinPandora""" + setting + """" type="PandoraPFANewProcessor">
  <parameter name="PandoraSettingsXmlFile" type="String">""" + self._PandoraSettingsFiles[setting] + """</parameter>
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
  <parameter name="ClusterCollectionName" type="String">PandoraClusters""" + setting + """</parameter>
  <parameter name="PFOCollectionName" type="String">PandoraPFOs""" + setting + """</parameter>
  <parameter name="StartVertexCollectionName" type="String">StartVertices""" + setting + """</parameter>
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
        marlinPandoraTemplate = ''
        for setting in self._PandoraSettings:
            marlinPandoraTemplate += """
<processor name="MyMarlinPandora""" + setting + """" type="PandoraPFANewProcessor">
  <parameter name="StripSplittingOn" type="bool">0</parameter>
  <parameter name="UseEcalScLayers" type="bool">1</parameter>
  <parameter name="PandoraSettingsXmlFile" type="String">""" + self._PandoraSettingsFiles[setting] + """</parameter>
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
  <parameter name="ClusterCollectionName" type="String">PandoraClusters""" + setting + """</parameter>
  <parameter name="PFOCollectionName" type="String">PandoraPFOs""" + setting + """</parameter>
  <parameter name="StartVertexCollectionName" type="String">StartVertices""" + setting + """</parameter>
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
        pandoraAnalysis = ''
        for setting in self._PandoraSettings:
            pandoraAnalysis += """ 
<processor name="MyPfoAnalysis""" + setting + """" type="PfoAnalysis">
  <!--PfoAnalysis analyses output of PandoraPFANew, Modified for calibration-->
  <!--Names of input pfo collection-->
  <parameter name="PfoCollection" type="string" lcioInType="ReconstructedParticle">PandoraPFOs""" + setting + """</parameter>
  <!--Names of mc particle collection-->
  <parameter name="MCParticleCollection" type="string" lcioInType="MCParticle">MCParticle </parameter>
  <!--Set the debug print level-->
  <parameter name="Printing" type="int"> 0 </parameter>
  <!--Output root file name-->
  <parameter name="RootFile" type="string">MarlinReco_""" + self._LcioInputFile[:-6] + '_' + setting + """.root</parameter>
</processor>"""
        return pandoraAnalysis

### ----------------------------------------------------------------------------------------------------
### End of writePandoraAnalsisSiECalXml function
### ----------------------------------------------------------------------------------------------------
### Start of writePandoraAnalsisScECalXml function
### ----------------------------------------------------------------------------------------------------

    def writePandoraAnalsisScECalXml(self):
        self.logger.debug('Writing PandoraAnalysis xml block for Sc ECal.')
        pandoraAnalysis = ''
        for setting in self._PandoraSettings:
            pandoraAnalysis += """
<processor name="MyPfoAnalysis""" + setting + """" type="PfoAnalysis">
  <!--PfoAnalysis analyses output of PandoraPFANew, Modified for calibration-->
  <!--Names of input pfo collection-->
  <parameter name="PfoCollection" type="string" lcioInType="ReconstructedParticle">PandoraPFOs""" + setting + """</parameter>
  <!--Names of mc particle collection-->
  <parameter name="MCParticleCollection" type="string" lcioInType="MCParticle">MCParticle </parameter>
  <!--Set the debug print level-->
  <parameter name="Printing" type="int"> 0 </parameter>
  <!--Output root file name-->
  <parameter name="RootFile" type="string">MarlinReco_""" + self._LcioInputFile[:-6] + '_' + setting + """.root</parameter>
</processor>"""
        return pandoraAnalysis

### ----------------------------------------------------------------------------------------------------
### End of writePandoraAnalsisScECalXml function
### ----------------------------------------------------------------------------------------------------
### Start of setGearFile function
### ----------------------------------------------------------------------------------------------------

    def setGearFile(self,xmlTemplate):
        xmlTemplate = re.sub('GearFile',self._GearFile,xmlTemplate)
        return xmlTemplate

### ----------------------------------------------------------------------------------------------------
### End of setGearFile function
### ----------------------------------------------------------------------------------------------------
### Start of setLcioFile function
### ----------------------------------------------------------------------------------------------------

    def setLcioFile(self,xmlTemplate):
        xmlTemplate = re.sub('LcioInputFile',self._LcioInputFile,xmlTemplate)
        return xmlTemplate

### ----------------------------------------------------------------------------------------------------
### End of setLcioFile function
### ----------------------------------------------------------------------------------------------------
### Start of listOutputFiles function
### ----------------------------------------------------------------------------------------------------

    def listOutputFiles(self):
        outputFiles = []
        for setting in self._PandoraSettings:
            outputFiles.append('MarlinReco_' + self._LcioInputFile[:-6] + '_' + setting + '.root')
        return outputFiles

### ----------------------------------------------------------------------------------------------------
### End of listOutputFiles function
### ----------------------------------------------------------------------------------------------------


