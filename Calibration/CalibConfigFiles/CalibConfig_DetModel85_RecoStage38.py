# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 42.8542514584

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 46.6207226265
CalibrHCalEndcap = 51.6336240806
CalibrHCalOther = 28.1869229812

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
ECalToMIPCalibration = 153.846
HCalToMIPCalibration = 41.841
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.0047628667
HCalToEMGeVCalibration = 1.11833532829
ECalToHadGeVCalibration = 1.08478198605
HCalToHadGeVCalibration = 1.11833532829

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
