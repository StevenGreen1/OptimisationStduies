# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 42.4170898128

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 49.9202851313
CalibrHCalEndcap = 55.0298978901
CalibrHCalOther = 30.4257421263

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
ECalToMIPCalibration = 158.73
HCalToMIPCalibration = 38.9105
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.03348111871
HCalToEMGeVCalibration = 1.10917037816
ECalToHadGeVCalibration = 1.14688623792
HCalToHadGeVCalibration = 1.10917037816

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
