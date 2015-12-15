# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 42.3662496409

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 50.3504586994
CalibrHCalEndcap = 55.6419000329
CalibrHCalOther = 30.5873671511

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
ECalToMIPCalibration = 153.846
HCalToMIPCalibration = 36.1011
MuonToMIPCalibration = 10.101

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.00203414435
HCalToEMGeVCalibration = 1.00203414435
ECalToHadGeVCalibration = 1.09290139114
HCalToHadGeVCalibration = 1.09770494916

# Pandora Threshold Cuts
ECalMIPThresholdPandora = 0.5
HCalMIPThresholdPandora = 0.3

# Hadronic Energy Truncation in HCal PandoraPFA
MaxHCalHitHadronicEnergy = 1.0

# Timing ECal
ECalBarrelTimeWindowMax = 300.0
ECalEndcapTimeWindowMax = 300.0

# Timing HCal
HCalBarrelTimeWindowMax = 300.0
HCalEndcapTimeWindowMax = 300.0
