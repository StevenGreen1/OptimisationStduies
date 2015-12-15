# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 42.8074993694

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 50.0225823686
CalibrHCalEndcap = 55.7555017204
CalibrHCalOther = 29.8651612339

# Digitisation Constants NewLDCCaloDigi - HCal
CalibrHCal = -1

# Digitisation Constants - Muon Chamber
CalibrMuon = 56.7

# MIP Peak position in directed corrected SimCaloHit energy distributions
# used for realistic ECal and HCal digitisation options
CalibrECalMIP = 0.0001525
CalibrHCalMIP = 0.0004975

# MIP Peak position in directed corrected CaloHit energy distributions
# used for MIP definition in PandoraPFA
ECalToMIPCalibration = 153.846
HCalToMIPCalibration = 39.2157
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.00761127073
HCalToEMGeVCalibration = 1.28359946948
ECalToHadGeVCalibration = 1.08216986742
HCalToHadGeVCalibration = 1.28359946948

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
