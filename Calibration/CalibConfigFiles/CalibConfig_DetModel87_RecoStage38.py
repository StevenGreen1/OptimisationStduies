# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 42.8005167685

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 46.3793232051
CalibrHCalEndcap = 52.3031066843
CalibrHCalOther = 27.7937918743

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
HCalToMIPCalibration = 40.8163
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.01645999776
HCalToEMGeVCalibration = 1.12394735226
ECalToHadGeVCalibration = 1.06268256563
HCalToHadGeVCalibration = 1.12394735226

# Pandora Threshold Cuts
ECalMIPThresholdPandora = 0.5
HCalMIPThresholdPandora = 0.3

# Hadronic Energy Truncation in HCal PandoraPFA
MaxHCalHitHadronicEnergy = 1.0

# Timing ECal
ECalBarrelTimeWindowMax = 1000000.0
ECalEndcapTimeWindowMax = 1000000.0

# Timing HCal
HCalBarrelTimeWindowMax = 1000000.0
HCalEndcapTimeWindowMax = 1000000.0
