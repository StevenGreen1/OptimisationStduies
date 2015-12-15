# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 43.248982481

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 49.270834535
CalibrHCalEndcap = 56.4056313096
CalibrHCalOther = 31.3817825379

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
ECalToMIPCalibration = 149.254
HCalToMIPCalibration = 38.0228
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.00195679807
HCalToEMGeVCalibration = 1.05398292107
ECalToHadGeVCalibration = 1.16637028964
HCalToHadGeVCalibration = 1.05398292107

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
