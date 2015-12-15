# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 44.8694882235

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 49.5583131638
CalibrHCalEndcap = 56.4086351378
CalibrHCalOther = 31.2211246402

# Digitisation Constants NewLDCCaloDigi - HCal
CalibrHCal = -1

# Digitisation Constants - Muon Chamber
CalibrMuon = 56.7

# MIP Peak position in directed corrected SimCaloHit energy distributions
# used for realistic ECal and HCal digitisation options
CalibrECalMIP = 0.0001475
CalibrHCalMIP = 0.0004925

# MIP Peak position in directed corrected CaloHit energy distributions
# used for MIP definition in PandoraPFA
ECalToMIPCalibration = 144.928
HCalToMIPCalibration = 38.9105
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 0.97313814693
HCalToEMGeVCalibration = 1.15794582487
ECalToHadGeVCalibration = 1.10461343539
HCalToHadGeVCalibration = 1.15794582487

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
