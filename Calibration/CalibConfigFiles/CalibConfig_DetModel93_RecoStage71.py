# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 20.9308039326

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 48.936584313
CalibrHCalEndcap = 55.3876823641
CalibrHCalOther = 30.8184918421

# Digitisation Constants NewLDCCaloDigi - HCal
CalibrHCal = -1

# Digitisation Constants - Muon Chamber
CalibrMuon = 56.7

# MIP Peak position in directed corrected SimCaloHit energy distributions
# used for realistic ECal and HCal digitisation options
CalibrECalMIP = 0.0003175
CalibrHCalMIP = 0.0004875

# MIP Peak position in directed corrected CaloHit energy distributions
# used for MIP definition in PandoraPFA
ECalToMIPCalibration = 153.846
HCalToMIPCalibration = 39.5257
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 0.980958710673
HCalToEMGeVCalibration = 1.11491749914
ECalToHadGeVCalibration = 0.788625804343
HCalToHadGeVCalibration = 1.11491749914

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
