# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 42.429292779

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 50.0843766428
CalibrHCalEndcap = 55.4568843
CalibrHCalOther = 30.5482022194

# Digitisation Constants NewLDCCaloDigi - HCal
CalibrHCal = -1

# Digitisation Constants - Muon Chamber
CalibrMuon = 56.7

# MIP Peak position in directed corrected SimCaloHit energy distributions
# used for realistic ECal and HCal digitisation options
CalibrECalMIP = -1
CalibrHCalMIP = -1

# MIP Peak position in directed corrected CaloHit energy distributions
# used for MIP definition in PandoraPFA
ECalToMIPCalibration = 158.73
HCalToMIPCalibration = 38.61
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.01489494714
HCalToEMGeVCalibration = 1.11196520089
ECalToHadGeVCalibration = 1.14446839564
HCalToHadGeVCalibration = 1.11196520089

# Pandora Threshold Cuts
ECalMIPThresholdPandora = 0.5
HCalMIPThresholdPandora = 0.3

# Hadronic Energy Truncation in HCal PandoraPFA
MaxHCalHitHadronicEnergy = 1.0

# Timing ECal
ECalBarrelTimeWindowMax = 100.0
ECalEndcapTimeWindowMax = 100.0

# Timing HCal
HCalBarrelTimeWindowMax = 100.0
HCalEndcapTimeWindowMax = 100.0
