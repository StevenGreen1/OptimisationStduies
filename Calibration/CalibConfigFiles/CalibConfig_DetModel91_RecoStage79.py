# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 24.1010031453

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 47.9050946631
CalibrHCalEndcap = 53.8090640699
CalibrHCalOther = 29.5451376684

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
ECalToMIPCalibration = 129.87
HCalToMIPCalibration = 39.8406
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.01519385412
HCalToEMGeVCalibration = 1.12394735226
ECalToHadGeVCalibration = 0.83812869432
HCalToHadGeVCalibration = 1.12394735226

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
