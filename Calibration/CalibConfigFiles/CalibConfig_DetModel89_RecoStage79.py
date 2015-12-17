# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 43.541955326

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 49.8638117252
CalibrHCalEndcap = 55.5535748781
CalibrHCalOther = 30.5629735630

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
ECalToMIPCalibration = 153.846
HCalToMIPCalibration = 38.9105
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.01444841742
HCalToEMGeVCalibration = 1.1063977926
ECalToHadGeVCalibration = 1.15551595832
HCalToHadGeVCalibration = 1.1063977926

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
