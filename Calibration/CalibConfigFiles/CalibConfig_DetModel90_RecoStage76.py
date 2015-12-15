# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 31.7117786893

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 49.3842179855
CalibrHCalEndcap = 55.0406972668
CalibrHCalOther = 29.4544130498

# Digitisation Constants NewLDCCaloDigi - HCal
CalibrHCal = -1

# Digitisation Constants - Muon Chamber
CalibrMuon = 56.7

# MIP Peak position in directed corrected SimCaloHit energy distributions
# used for realistic ECal and HCal digitisation options
CalibrECalMIP = 0.0003075
CalibrHCalMIP = 0.0004925

# MIP Peak position in directed corrected CaloHit energy distributions
# used for MIP definition in PandoraPFA
ECalToMIPCalibration = 232.558
HCalToMIPCalibration = 38.61
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.00342640753
HCalToEMGeVCalibration = 1.05880131472
ECalToHadGeVCalibration = 0.966784755835
HCalToHadGeVCalibration = 1.05880131472

# Pandora Threshold Cuts
ECalMIPThresholdPandora = 0.5
HCalMIPThresholdPandora = 0.3

# Hadronic Energy Truncation in HCal PandoraPFA
MaxHCalHitHadronicEnergy = 1000000.0

# Timing ECal
ECalBarrelTimeWindowMax = 100.0
ECalEndcapTimeWindowMax = 100.0

# Timing HCal
HCalBarrelTimeWindowMax = 100.0
HCalEndcapTimeWindowMax = 100.0
