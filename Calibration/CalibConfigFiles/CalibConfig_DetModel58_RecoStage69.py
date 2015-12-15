# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 42.5182917131

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 49.9478530053
CalibrHCalEndcap = 56.1588168155
CalibrHCalOther = 32.9041893421

# Digitisation Constants NewLDCCaloDigi - HCal
CalibrHCal = -1

# Digitisation Constants - Muon Chamber
CalibrMuon = 56.7

# MIP Peak position in directed corrected SimCaloHit energy distributions
# used for realistic ECal and HCal digitisation options
CalibrECalMIP = 0.0001525
CalibrHCalMIP = 0.0005475

# MIP Peak position in directed corrected CaloHit energy distributions
# used for MIP definition in PandoraPFA
ECalToMIPCalibration = 153.846
HCalToMIPCalibration = 33.8983
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.013805932
HCalToEMGeVCalibration = 1.31428691857
ECalToHadGeVCalibration = 1.08884011307
HCalToHadGeVCalibration = 1.31428691857

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
