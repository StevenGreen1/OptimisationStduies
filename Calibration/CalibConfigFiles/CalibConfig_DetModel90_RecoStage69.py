# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 31.7126615394

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 49.3346577108
CalibrHCalEndcap = 54.7937216147
CalibrHCalOther = 29.1041722134

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
HCalToMIPCalibration = 37.7359
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.00314744411
HCalToEMGeVCalibration = 1.29215905206
ECalToHadGeVCalibration = 0.903557228154
HCalToHadGeVCalibration = 1.29215905206

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
