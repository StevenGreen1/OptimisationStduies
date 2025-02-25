# Submit Mokka jobs to the grid: MokkaGridJobs.py 
import re
import os
import sys

### ----------------------------------------------------------------------------------------------------

def setGearFile(mokkaSteeringTemplate,gearFile):
    mokkaSteeringTemplate = re.sub('GEAR_FILE_XXXX',gearFile,mokkaSteeringTemplate)
    return mokkaSteeringTemplate

### ----------------------------------------------------------------------------------------------------

def setStartNumber(mokkaSteeringTemplate,startNumber):
    mokkaSteeringTemplate = re.sub('START_EVENT_NUMBER_XXXX',str(startNumber),mokkaSteeringTemplate)
    return mokkaSteeringTemplate

### ----------------------------------------------------------------------------------------------------

def setOutputFile(mokkaSteeringTemplate,outputFile):
    mokkaSteeringTemplate = re.sub('OUTPUT_FILE_NAME_XXXX',outputFile,mokkaSteeringTemplate)
    return mokkaSteeringTemplate

### ----------------------------------------------------------------------------------------------------

def getMokkaVersion(detectorConfigFile):
    config = {}
    execfile(detectorConfigFile, config)
    return config['MokkaVersion']

### ----------------------------------------------------------------------------------------------------

def getMokkaSteeringFileTemplate(baseFileName,detectorConfigFile):
    config = {}
    execfile(detectorConfigFile, config)

    baseFile = open(baseFileName,'r')
    mokkaSteeringTemplate = baseFile.read()
    baseFile.close()

    # Detector Model
    mokkaSteeringTemplate = re.sub('DETECTOR_MODEL_XXXX',config['DetectorModel'],mokkaSteeringTemplate)

    # Physics List
    mokkaSteeringTemplate = re.sub('PHYSICS_LIST_XXXX',config['PhysicsList'],mokkaSteeringTemplate)

    # HCal absorber material
    mokkaSteeringTemplate = re.sub('HCAL_ABSORBER_MATERIAL_XXXX',str(config['HCalAbsorberMaterial']),mokkaSteeringTemplate)

    # HCal cell size
    mokkaSteeringTemplate = re.sub('HCAL_CELL_SIZE_XXXX',str(config['HCalCellSize']),mokkaSteeringTemplate)

    # Thickness of absorber layers in the HCal
    mokkaSteeringTemplate = re.sub('HCAL_ABSORBER_LAYER_THICKNESS_XXXX',str(config['HCalAbsorberLayerThickness']),mokkaSteeringTemplate)

    # Thickenss of scintillator layers in the HCal
    mokkaSteeringTemplate = re.sub('HCAL_SCINTILLATOR_LAYER_THICKNESS_XXXX',str(config['HCalScintillatorThickness']),mokkaSteeringTemplate)

    # Number of layers in the HCal
    mokkaSteeringTemplate = re.sub('HCAL_NUMBER_OF_LAYERS_XXXX',str(config['NumberHCalLayers']),mokkaSteeringTemplate)

    # Coil extra size, has to be varied if expanding HCal
    mokkaSteeringTemplate = re.sub('COIL_EXTRA_SIZE_XXXX',str(config['CoilExtraSize']),mokkaSteeringTemplate)

    # Strength of B field in tracker
    mokkaSteeringTemplate = re.sub('BFIELD_XXXX',str(config['BField']),mokkaSteeringTemplate)

    # Outer radius of the tracker/ inner radius of the ECal
    mokkaSteeringTemplate = re.sub('TPC_OUTER_RADIUS_XXXX',str(config['TPCOuterRadius']),mokkaSteeringTemplate)

    # Detailed shower mode
    mokkaSteeringTemplate = re.sub('DETAILED_SHOWER_MODE_XXXX',config['DetailedShowerMode'],mokkaSteeringTemplate)

    # ECal cell size
    mokkaSteeringTemplate = re.sub('ECAL_CELL_SIZE_XXXX',str(config['ECalCellSize']),mokkaSteeringTemplate)

    # ECal Number of Layers 
    mokkaSteeringTemplate = re.sub('ECAL_NLAYERS1_XXXX',str(config['NumberECalLayers1']),mokkaSteeringTemplate)
    mokkaSteeringTemplate = re.sub('ECAL_NLAYERS2_XXXX',str(config['NumberECalLayers2']),mokkaSteeringTemplate)
    mokkaSteeringTemplate = re.sub('ECAL_NLAYERS3_XXXX',str(config['NumberECalLayers3']),mokkaSteeringTemplate)

    # LCal Number of Layers
    mokkaSteeringTemplate = re.sub('LCAL_NLAYERS_XXXX',str(config['NumberLCalLayers']),mokkaSteeringTemplate)

    # Thickness of absorber layers in the ECal
    mokkaSteeringTemplate = re.sub('ECAL_RADIATOR_LAYERS_SET1_THICKNESS_XXXX',str(config['ECalAbsorberLayerThickness1']),mokkaSteeringTemplate)
    mokkaSteeringTemplate = re.sub('ECAL_RADIATOR_LAYERS_SET2_THICKNESS_XXXX',str(config['ECalAbsorberLayerThickness2']),mokkaSteeringTemplate)
    mokkaSteeringTemplate = re.sub('ECAL_RADIATOR_LAYERS_SET3_THICKNESS_XXXX',str(config['ECalAbsorberLayerThickness3']),mokkaSteeringTemplate)

    # Thickenss of scintillator layers in the ECal
    mokkaSteeringTemplate = re.sub('ECAL_SC_THICKNESS_XXXX',str(config['ECalScintillatorThickness']),mokkaSteeringTemplate)

    # Thickenss of silicon layers in the ECal
    mokkaSteeringTemplate = re.sub('ECAL_SI_THICKNESS_XXXX',str(config['ECalSiliconThickness']),mokkaSteeringTemplate)

    # Ecal Sc N strips across module
    mokkaSteeringTemplate = re.sub('ECAL_SC_NSTRIPS_ACROSS_MODULE_XXXX',str(config['ECalScNStripsAcrossModule']),mokkaSteeringTemplate)

    # ECal Sc and Si Mix
    mokkaSteeringTemplate = re.sub('ECAL_SC_SI_MIX_XXXX',str(config['ECalScSiMix']),mokkaSteeringTemplate)

    # ECal Sc Cell Dimensions
    if config['ECalScCellDim'] != '':
        mokkaSteeringTemplate = re.sub('ECAL_SC_CELLDIM_XXXX',str(config['ECalScCellDim']),mokkaSteeringTemplate)
    else:
        mokkaSteeringTemplate = re.sub('/Mokka/init/userInitString Ecal_Sc_cellDim1_string ECAL_SC_CELLDIM_XXXX','',mokkaSteeringTemplate)
        mokkaSteeringTemplate = re.sub('/Mokka/init/userInitString Ecal_Sc_cellDim2_string ECAL_SC_CELLDIM_XXXX','',mokkaSteeringTemplate)

    # HCal Cell size as Function of Depth
    if config['HCalNLayersLowGran'] != '':
        mokkaSteeringTemplate = re.sub('HCAL_NLAYERS_LOWGRAN_XXXX',str(config['HCalNLayersLowGran']),mokkaSteeringTemplate)
    else:
        mokkaSteeringTemplate = re.sub('/Mokka/init/userInitInt Hcal_nlayers_lowgran HCAL_NLAYERS_LOWGRAN_XXXX','',mokkaSteeringTemplate)

    # HCal Cell size as Function of Depth
    if config['HCalCellSizeLowGran'] != '':
        mokkaSteeringTemplate = re.sub('HCAL_CELL_SIZE_LOWGRAN_XXXX',str(config['HCalCellSizeLowGran']),mokkaSteeringTemplate)
    else:
        mokkaSteeringTemplate = re.sub('/Mokka/init/userInitDouble Hcal_cell_size_lowgran HCAL_CELL_SIZE_LOWGRAN_XXXX','',mokkaSteeringTemplate)

    return mokkaSteeringTemplate

### ----------------------------------------------------------------------------------------------------

def getHEPEvtFiles(eventType, energy):
    jobDescription = 'HEPEvt'

    if eventType == 'Z_uds':
        jobDescription = 'StdHep'

    hepevtFiles = []
    os.system('dirac-ilc-find-in-FC /ilc JobDescription="' + jobDescription + '" Energy=' + str(energy) + ' EvtType="' + eventType + '" > tmp.txt')
    with open('tmp.txt') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            line = line.strip()
            print line
            hepevtFiles.append(line)
    os.system('rm tmp.txt')
    return hepevtFiles

### ----------------------------------------------------------------------------------------------------

def doesFileExist(lfn):
    from DIRAC.DataManagementSystem.Client.DataManager import DataManager
    dm = DataManager()
    result = dm.getActiveReplicas(lfn)
    if result[('Value')][('Successful')]:
        return True
#        print 'File exists.'
    else:
        return False
#        print 'File does notexists.'

### ----------------------------------------------------------------------------------------------------

