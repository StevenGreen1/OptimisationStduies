# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 42.7593101725

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 46.3943207727
CalibrHCalEndcap = 51.5011146371
CalibrHCalOther = 28.4179490447

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
HCalToMIPCalibration = 41.1523
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.02555920504
HCalToEMGeVCalibration = 1.11819861381
ECalToHadGeVCalibration = 1.08511243953
HCalToHadGeVCalibration = 1.11819861381

# Pandora Threshold Cuts
ECalMIPThresholdPandora = 0.5
HCalMIPThresholdPandora = 0.3

# Hadronic Energy Truncation in HCal PandoraPFA
MaxHCalHitHadronicEnergy = 1.0

# Timing ECal
ECalBarrelTimeWindowMax = 1000000.0
ECalEndcapTimeWindowMax = 1000000.0

# Timing HCal
HCalBarrelTimeWindowMax = 1000000.0
HCalEndcapTimeWindowMax = 1000000.0
