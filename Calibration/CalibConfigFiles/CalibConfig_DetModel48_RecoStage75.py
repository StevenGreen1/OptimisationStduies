# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 42.9415514982

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 60.2367869284
CalibrHCalEndcap = 66.8896438832
CalibrHCalOther = 24.9410044460

# Digitisation Constants NewLDCCaloDigi - HCal
CalibrHCal = -1

# Digitisation Constants - Muon Chamber
CalibrMuon = 56.7

# MIP Peak position in directed corrected SimCaloHit energy distributions
# used for realistic ECal and HCal digitisation options
CalibrECalMIP = 0.0001525
CalibrHCalMIP = 0.0002875

# MIP Peak position in directed corrected CaloHit energy distributions
# used for MIP definition in PandoraPFA
ECalToMIPCalibration = 153.846
HCalToMIPCalibration = 54.6448
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.00410078982
HCalToEMGeVCalibration = 1.0723128299
ECalToHadGeVCalibration = 1.07331033021
HCalToHadGeVCalibration = 1.0723128299

# Pandora Threshold Cuts
ECalMIPThresholdPandora = 0.5
HCalMIPThresholdPandora = 0.3

# Hadronic Energy Truncation in HCal PandoraPFA
MaxHCalHitHadronicEnergy = 10.0

# Timing ECal
ECalBarrelTimeWindowMax = 100.0
ECalEndcapTimeWindowMax = 100.0

# Timing HCal
HCalBarrelTimeWindowMax = 100.0
HCalEndcapTimeWindowMax = 100.0
