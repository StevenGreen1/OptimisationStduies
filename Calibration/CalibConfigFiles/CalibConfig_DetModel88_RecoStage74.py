# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 42.7571728481

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 49.1251081364
CalibrHCalEndcap = 55.0421310226
CalibrHCalOther = 30.4820093043

# Digitisation Constants NewLDCCaloDigi - HCal
CalibrHCal = -1

# Digitisation Constants - Muon Chamber
CalibrMuon = 56.7

# MIP Peak position in directed corrected SimCaloHit energy distributions
# used for realistic ECal and HCal digitisation options
CalibrECalMIP = 0.0001475
CalibrHCalMIP = 0.0004975

# MIP Peak position in directed corrected CaloHit energy distributions
# used for MIP definition in PandoraPFA
ECalToMIPCalibration = 153.846
HCalToMIPCalibration = 38.61
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.02621144934
HCalToEMGeVCalibration = 1.06966036021
ECalToHadGeVCalibration = 1.17258504222
HCalToHadGeVCalibration = 1.06966036021

# Pandora Threshold Cuts
ECalMIPThresholdPandora = 0.5
HCalMIPThresholdPandora = 0.3

# Hadronic Energy Truncation in HCal PandoraPFA
MaxHCalHitHadronicEnergy = 5.0

# Timing ECal
ECalBarrelTimeWindowMax = 100.0
ECalEndcapTimeWindowMax = 100.0

# Timing HCal
HCalBarrelTimeWindowMax = 100.0
HCalEndcapTimeWindowMax = 100.0
