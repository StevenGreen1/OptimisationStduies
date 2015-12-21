# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 42.3851429024

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 46.9729543347
CalibrHCalEndcap = 52.1603853641
CalibrHCalOther = 28.2220640718

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
HCalToMIPCalibration = 39.2157
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.01425025343
HCalToEMGeVCalibration = 1.11196520089
ECalToHadGeVCalibration = 1.07896019576
HCalToHadGeVCalibration = 1.11196520089

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
