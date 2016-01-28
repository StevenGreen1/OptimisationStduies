# Submit Mokka jobs to the grid: MokkaSubmit.py
import os
import sys

/Mokka/init/globalModelParameter Ecal_nlayers1 20
/Mokka/init/globalModelParameter Ecal_nlayers2 9
/Mokka/init/globalModelParameter Ecal_nlayers3 0
/Mokka/init/globalModelParameter Ecal_radiator_layers_set1_thickness 2.1
/Mokka/init/globalModelParameter Ecal_radiator_layers_set2_thickness 4.2
/Mokka/init/globalModelParameter Ecal_radiator_layers_set3_thickness 0
/Mokka/init/globalModelParameter Ecal_Si_thickness 0.5
/Mokka/init/globalModelParameter Ecal_Sc_thickness 2.0


/Mokka/init/globalModelParameter Ecal_nlayers1 ECAL_NLAYERS1_XXXX
/Mokka/init/globalModelParameter Ecal_nlayers2 ECAL_NLAYERS2_XXXX
/Mokka/init/globalModelParameter Ecal_nlayers3 ECAL_NLAYERS3_XXXX
/Mokka/init/globalModelParameter Ecal_radiator_layers_set1_thickness ECAL_RADIATOR_LAYERS_SET1_THICKNESS_XXXX
/Mokka/init/globalModelParameter Ecal_radiator_layers_set2_thickness ECAL_RADIATOR_LAYERS_SET2_THICKNESS_XXXX
/Mokka/init/globalModelParameter Ecal_radiator_layers_set3_thickness ECAL_RADIATOR_LAYERS_SET3_THICKNESS_XXXX
/Mokka/init/globalModelParameter Ecal_Si_thickness ECAL_SI_THICKNESS_XXXX
/Mokka/init/globalModelParameter Ecal_Sc_thickness ECAL_SC_THICKNESS_XXXX


    mokkaSteeringTemplate = re.sub('ECAL_NLAYERS1_XXXX',str(config['NumberECalLayers1']),mokkaSteeringTemplate)
    mokkaSteeringTemplate = re.sub('ECAL_NLAYERS2_XXXX',str(config['NumberECalLayers2']),mokkaSteeringTemplate)
    mokkaSteeringTemplate = re.sub('ECAL_NLAYERS3_XXXX',str(config['NumberECalLayers3']),mokkaSteeringTemplate)

    # Thickness of absorber layers in the ECal
    mokkaSteeringTemplate = re.sub('ECAL_RADIATOR_LAYERS_SET1_THICKNESS_XXXX',str(config['ECalAbsorberLayerThickness1']),mokkaSteeringTemplate)
    mokkaSteeringTemplate = re.sub('ECAL_RADIATOR_LAYERS_SET2_THICKNESS_XXXX',str(config['ECalAbsorberLayerThickness2']),mokkaSteeringTemplate)
    mokkaSteeringTemplate = re.sub('ECAL_RADIATOR_LAYERS_SET3_THICKNESS_XXXX',str(config['ECalAbsorberLayerThickness3']),mokkaSteeringTemplate)

    # Thickenss of scintillator layers in the ECal
    mokkaSteeringTemplate = re.sub('ECAL_SC_THICKNESS_XXXX',str(config['ECalSiliconThickness']),mokkaSteeringTemplate)

    # Thickenss of silicon layers in the ECal
    mokkaSteeringTemplate = re.sub('ECAL_SI_THICKNESS_XXXX',str(config['ECalScintillatorThickness']),mokkaSteeringTemplate)


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
ECalCellSize                 = 3                   # ECal cell size
ECalScNStripsAcrossModule    = 60                  # Number of scintillator strips across module

#===========================================================================
# Silicon is 0, scintillator is 3.  Each number represents a pair of layers
#===========================================================================

ECalScSiMix                  = '000000000000000'   # All silicon

#===========================================================================
# Cell size for each layer number.  Total number of layers set here too.
# Only defined for scintillator. 5_5_5 is three layers of 5x5 cells.
# Leave as '' if not using scintillator
#===========================================================================

ECalScCellDim                = ''                  # Cell dimenstion for scintillator ECal



