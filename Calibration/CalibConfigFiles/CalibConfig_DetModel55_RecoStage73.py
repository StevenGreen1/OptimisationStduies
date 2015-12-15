# Calibration config file for testing
# Digitisation Constants - ECal 
CalibrECal = 42.9326718938

# Digitisation Constants ILDCaloDigi - HCal
CalibrHCalBarrel = 49.0893576418
CalibrHCalEndcap = 55.2575742809
CalibrHCalOther = 26.3659381868

# Digitisation Constants NewLDCCaloDigi - HCal
CalibrHCal = -1

# Digitisation Constants - Muon Chamber
CalibrMuon = 56.7

# MIP Peak position in directed corrected SimCaloHit energy distributions
# used for realistic ECal and HCal digitisation options
CalibrECalMIP = 0.0001475
CalibrHCalMIP = 0.0003925

# MIP Peak position in directed corrected CaloHit energy distributions
# used for MIP definition in PandoraPFA
ECalToMIPCalibration = 149.254
HCalToMIPCalibration = 48.3092
MuonToMIPCalibration = 10.3093

# EM and Had Scale Settings
ECalToEMGeVCalibration = 1.00377810227
HCalToEMGeVCalibration = 1.06698653757
ECalToHadGeVCalibration = 1.14919234164
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
