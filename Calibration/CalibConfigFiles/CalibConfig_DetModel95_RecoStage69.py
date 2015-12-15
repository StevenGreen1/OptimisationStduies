# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 20.2177834211

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 49.2644861408
CalibrHCalEndcap = 55.3928670686
CalibrHCalOther = 30.5575558720

# Digitisation Constants NewLDCCaloDigi - HCal
CalibrHCal = -1

# Digitisation Constants - Muon Chamber
CalibrMuon = 56.7

# MIP Peak position in directed corrected SimCaloHit energy distributions
# used for realistic ECal and HCal digitisation options
CalibrECalMIP = 0.0003175
CalibrHCalMIP = 0.0004925

# MIP Peak position in directed corrected CaloHit energy distributions
# used for MIP definition in PandoraPFA
ECalToMIPCalibration = 153.846
HCalToMIPCalibration = 38.0228
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.04511445618
HCalToEMGeVCalibration = 1.30106448956
ECalToHadGeVCalibration = 0.699452064082
HCalToHadGeVCalibration = 1.30106448956

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
