# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 24.102478222

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 44.9433118578
CalibrHCalEndcap = 50.2066741634
CalibrHCalOther = 27.4142420861

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
ECalToMIPCalibration = 129.87
HCalToMIPCalibration = 42.5532
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.01493134548
HCalToEMGeVCalibration = 1.12997349189
ECalToHadGeVCalibration = 0.79383335793
HCalToHadGeVCalibration = 1.12997349189

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
