# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 42.6863347838

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 49.9354331436
CalibrHCalEndcap = 56.2948073458
CalibrHCalOther = 31.0695799707

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
HCalToMIPCalibration = 38.3142
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.01988591448
HCalToEMGeVCalibration = 1.10615895792
ECalToHadGeVCalibration = 1.13743661982
HCalToHadGeVCalibration = 1.10615895792

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
