# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 42.1221611613

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 49.3319103895
CalibrHCalEndcap = 55.5230147535
CalibrHCalOther = 30.8490764585

# Digitisation Constants NewLDCCaloDigi - HCal
CalibrHCal = -1

# Digitisation Constants - Muon Chamber
CalibrMuon = 56.7

# MIP Peak position in directed corrected SimCaloHit energy distributions
# used for realistic ECal and HCal digitisation options
CalibrECalMIP = 0.0001475
CalibrHCalMIP = 0.0005025

# MIP Peak position in directed corrected CaloHit energy distributions
# used for MIP definition in PandoraPFA
ECalToMIPCalibration = 153.846
HCalToMIPCalibration = 38.9105
MuonToMIPCalibration = 10.101

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.01550920655
HCalToEMGeVCalibration = 1.27841777285
ECalToHadGeVCalibration = 1.09880019652
HCalToHadGeVCalibration = 1.27841777285

# Pandora Threshold Cuts
ECalMIPThresholdPandora = 0.5
HCalMIPThresholdPandora = 0.3

# Hadronic Energy Truncation in HCal PandoraPFA
MaxHCalHitHadronicEnergy = 0.5

# Timing ECal
ECalBarrelTimeWindowMax = 100.0
ECalEndcapTimeWindowMax = 100.0

# Timing HCal
HCalBarrelTimeWindowMax = 100.0
HCalEndcapTimeWindowMax = 100.0
