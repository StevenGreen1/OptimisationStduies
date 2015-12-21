# Calibration config file for detector model 84
MokkaVersion                 = '0804'              # Mokka version
DetectorModel                = 'ILD_o1_v06'        # Detector model
PhysicsList                  = 'QGSP_BERT'         # Physics list
HCalAbsorberMaterial         = 'Iron'              # HCal absorber material Iron/WMod
NumberHCalLayers             = 48                  # Number of layers in the HCal
HCalCellSize                 = 30                  # HCal cell size
HCalAbsorberLayerThickness   = 20                  # Thickness of absorber layers in the HCal
HCalScintillatorThickness    = 3                   # Thickenss of scintillator layers in the HCal
CoilExtraSize                = 1522                # Coil extra size, has to be varied if expanding HCal 
BField                       = 3.5                 # Strength of B field in tracker
TPCOuterRadius               = 1808                # Outer radius of the tracker/ inner radius of the ECal
DetailedShowerMode           = 'true'              # Detailed shower mode
ECalCellSize                 = 5                   # ECal cell size
ECalScNStripsAcrossModule    = 36                  # Number of scintillator strips across module

NumberECalLayers1            = 10                  # Number of Layers ECal Longitudinal Granularity 1
NumberECalLayers2            = 5                   # Number of Layers ECal Longitudinal Granularity 2
NumberECalLayers3            = 0                   # Number of Layers ECal Longitudinal Granularity 3

NumberLCalLayers             = 16                  # Number of Layers LCal

ECalAbsorberLayerThickness1  = 4.0                 # Absorber Thickness ECal Longitudinal Granularity 1
ECalAbsorberLayerThickness2  = 8.0                 # Absorber Thickness ECal Longitudinal Granularity 2
ECalAbsorberLayerThickness3  = 0.0                 # Absorber Thickness ECal Longitudinal Granularity 3

ECalSiliconThickness         = 0.5                 # Silicon Thickness ECal
ECalScintillatorThickness    = 2.0                 # Scintillator Thickenss ECal

#===========================================================================
# Silicon is 0, scintillator is 3.  Each number represents a pair of layers
#===========================================================================

ECalScSiMix                  = '33333333'   # All scintillator

#===========================================================================
# Cell size for each layer number.  Total number of layers set here too.  
# Only defined for scintillator. 5_5_5 is three layers of 5x5 cells.
# Leave as '' if not using scintillator
#===========================================================================

ECalScCellDim                = '5_5_5_5_5_5_5_5_5_5_5_5_5_5_5_5'                  # Cell dimenstion for scintillator ECal

