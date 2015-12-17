# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 42.9512111599

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 49.4884539605
CalibrHCalEndcap = 55.6766966696
CalibrHCalOther = 30.0859163637

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
ECalToMIPCalibration = 153.846
HCalToMIPCalibration = 38.61
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.00246328146
HCalToEMGeVCalibration = 1.11505419659
ECalToHadGeVCalibration = 1.13414028532
HCalToHadGeVCalibration = 1.11505419659

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
