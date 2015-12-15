# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 20.9308039326

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 48.94113166
CalibrHCalEndcap = 55.3183025809
CalibrHCalOther = 30.7562142458

# Digitisation Constants NewLDCCaloDigi - HCal
CalibrHCal = -1

# Digitisation Constants - Muon Chamber
CalibrMuon = 56.7

# MIP Peak position in directed corrected SimCaloHit energy distributions
# used for realistic ECal and HCal digitisation options
CalibrECalMIP = 0.0003175
CalibrHCalMIP = 0.0004875

# MIP Peak position in directed corrected CaloHit energy distributions
# used for MIP definition in PandoraPFA
ECalToMIPCalibration = 153.846
HCalToMIPCalibration = 39.5257
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.02408251409
HCalToEMGeVCalibration = 1.06182645387
ECalToHadGeVCalibration = 0.795887956902
HCalToHadGeVCalibration = 1.06182645387

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
