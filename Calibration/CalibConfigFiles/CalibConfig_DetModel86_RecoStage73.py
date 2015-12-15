# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 42.477753059

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 49.2809057236
CalibrHCalEndcap = 55.4960595368
CalibrHCalOther = 30.1944053655

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
ECalToMIPCalibration = 153.846
HCalToMIPCalibration = 39.2157
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.01265964757
HCalToEMGeVCalibration = 1.06698653757
ECalToHadGeVCalibration = 1.16316862669
HCalToHadGeVCalibration = 1.06698653757

# Pandora Threshold Cuts
ECalMIPThresholdPandora = 0.5
HCalMIPThresholdPandora = 0.3

# Hadronic Energy Truncation in HCal PandoraPFA
MaxHCalHitHadronicEnergy = 2.0

# Timing ECal
ECalBarrelTimeWindowMax = 100.0
ECalEndcapTimeWindowMax = 100.0

# Timing HCal
HCalBarrelTimeWindowMax = 100.0
HCalEndcapTimeWindowMax = 100.0
