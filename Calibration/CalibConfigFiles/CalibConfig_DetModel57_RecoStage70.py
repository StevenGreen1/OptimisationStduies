# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 43.0732355785

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 49.3325005885
CalibrHCalEndcap = 55.6086055538
CalibrHCalOther = 28.5575812766

# Digitisation Constants NewLDCCaloDigi - HCal
CalibrHCal = -1

# Digitisation Constants - Muon Chamber
CalibrMuon = 56.7

# MIP Peak position in directed corrected SimCaloHit energy distributions
# used for realistic ECal and HCal digitisation options
CalibrECalMIP = 0.0001475
CalibrHCalMIP = 0.0004425

# MIP Peak position in directed corrected CaloHit energy distributions
# used for MIP definition in PandoraPFA
ECalToMIPCalibration = 149.254
HCalToMIPCalibration = 44.0529
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.0010395989
HCalToEMGeVCalibration = 1.15438071815
ECalToHadGeVCalibration = 1.10760728251
HCalToHadGeVCalibration = 1.15438071815

# Pandora Threshold Cuts
ECalMIPThresholdPandora = 0.5
HCalMIPThresholdPandora = 0.3

# Hadronic Energy Truncation in HCal PandoraPFA
MaxHCalHitHadronicEnergy = 0.75

# Timing ECal
ECalBarrelTimeWindowMax = 100.0
ECalEndcapTimeWindowMax = 100.0

# Timing HCal
HCalBarrelTimeWindowMax = 100.0
HCalEndcapTimeWindowMax = 100.0
