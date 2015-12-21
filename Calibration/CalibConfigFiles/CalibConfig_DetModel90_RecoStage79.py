# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 31.6559067331

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 48.8185662081
CalibrHCalEndcap = 53.9798844822
CalibrHCalOther = 29.1104933598

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
ECalToMIPCalibration = 103.093
HCalToMIPCalibration = 39.8406
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.04249506111
HCalToEMGeVCalibration = 1.11783271956
ECalToHadGeVCalibration = 0.972246627334
HCalToHadGeVCalibration = 1.11783271956

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
