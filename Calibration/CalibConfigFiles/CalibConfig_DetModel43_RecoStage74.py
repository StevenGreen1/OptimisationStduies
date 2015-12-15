# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 43.3441364312

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 49.1831633764
CalibrHCalEndcap = 53.9330688884
CalibrHCalOther = 29.2791298855

# Digitisation Constants NewLDCCaloDigi - HCal
CalibrHCal = -1

# Digitisation Constants - Muon Chamber
CalibrMuon = 56.7

# MIP Peak position in directed corrected SimCaloHit energy distributions
# used for realistic ECal and HCal digitisation options
CalibrECalMIP = 0.0001475
CalibrHCalMIP = 0.0004875

# MIP Peak position in directed corrected CaloHit energy distributions
# used for MIP definition in PandoraPFA
ECalToMIPCalibration = 149.254
HCalToMIPCalibration = 38.0228
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 0.9953791304
HCalToEMGeVCalibration = 1.07247199111
ECalToHadGeVCalibration = 1.14954466993
HCalToHadGeVCalibration = 1.07247199111

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
