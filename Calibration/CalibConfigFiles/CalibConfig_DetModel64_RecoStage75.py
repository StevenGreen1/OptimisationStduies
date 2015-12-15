# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 43.4253316804

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 53.1946762869
CalibrHCalEndcap = 56.0843582549
CalibrHCalOther = 31.4700505386

# Digitisation Constants NewLDCCaloDigi - HCal
CalibrHCal = -1

# Digitisation Constants - Muon Chamber
CalibrMuon = 56.7

# MIP Peak position in directed corrected SimCaloHit energy distributions
# used for realistic ECal and HCal digitisation options
CalibrECalMIP = 0.0001475
CalibrHCalMIP = 0.0004925

# MIP Peak position in directed corrected CaloHit energy distributions
# used for MIP definition in PandoraPFA
ECalToMIPCalibration = 149.254
HCalToMIPCalibration = 38.0228
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.00404934759
HCalToEMGeVCalibration = 1.0696323769
ECalToHadGeVCalibration = 1.14650067903
HCalToHadGeVCalibration = 1.0696323769

# Pandora Threshold Cuts
ECalMIPThresholdPandora = 0.5
HCalMIPThresholdPandora = 0.3

# Hadronic Energy Truncation in HCal PandoraPFA
MaxHCalHitHadronicEnergy = 10.0

# Timing ECal
ECalBarrelTimeWindowMax = 100.0
ECalEndcapTimeWindowMax = 100.0

# Timing HCal
HCalBarrelTimeWindowMax = 100.0
HCalEndcapTimeWindowMax = 100.0
