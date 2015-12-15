# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 24.1018329349

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 48.9321077445
CalibrHCalEndcap = 55.1495475418
CalibrHCalOther = 30.2576250742

# Digitisation Constants NewLDCCaloDigi - HCal
CalibrHCal = -1

# Digitisation Constants - Muon Chamber
CalibrMuon = 56.7

# MIP Peak position in directed corrected SimCaloHit energy distributions
# used for realistic ECal and HCal digitisation options
CalibrECalMIP = 0.0003125
CalibrHCalMIP = 0.0004925

# MIP Peak position in directed corrected CaloHit energy distributions
# used for MIP definition in PandoraPFA
ECalToMIPCalibration = 158.73
HCalToMIPCalibration = 40.1606
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.00805234875
HCalToEMGeVCalibration = 1.06166688118
ECalToHadGeVCalibration = 0.850651814519
HCalToHadGeVCalibration = 1.06166688118

# Pandora Threshold Cuts
ECalMIPThresholdPandora = 0.5
HCalMIPThresholdPandora = 0.3

# Hadronic Energy Truncation in HCal PandoraPFA
MaxHCalHitHadronicEnergy = 1000000.0

# Timing ECal
ECalBarrelTimeWindowMax = 100.0
ECalEndcapTimeWindowMax = 100.0

# Timing HCal
HCalBarrelTimeWindowMax = 100.0
HCalEndcapTimeWindowMax = 100.0
