#!/bin/bash

#===== Batch calibration for optimisation studies =====#

#!!! This is for Scintillator ECal options only !!! 

#===================================#
#===== Detector Model Settings =====#

numberOfHCalLayers[90]="48"
numberOfHCalLayers[91]="48"
numberOfHCalLayers[92]="48"
numberOfHCalLayers[93]="48"
numberOfHCalLayers[94]="48"
numberOfHCalLayers[95]="48"
numberOfHCalLayers[96]="48"
numberOfHCalLayers[97]="48"
numberOfHCalLayers[98]="48"
numberOfHCalLayers[99]="48"
numberOfHCalLayers[100]="48"
numberOfHCalLayers[101]="48"
numberOfHCalLayers[102]="48"
numberOfHCalLayers[103]="48"

#===== Reconstruction Settings =====#
MHHHE[69]="0.5"
MHHHE[70]="0.75"
MHHHE[71]="1.0"
MHHHE[72]="1.5"
MHHHE[73]="2.0"
MHHHE[74]="5.0"
MHHHE[75]="10.0"
MHHHE[76]="1000000.0"

ECalBarrelTimeWindowMax="100.0"
HCalBarrelTimeWindowMax="100.0"
ECalEndcapTimeWindowMax="100.0"
HCalEndcapTimeWindowMax="100.0"

#===== End Settings =====#

for detModel in {100..103}
do
    slcioPath="/r04/lc/sg568/HCAL_Optimisation_Studies/Slcio/GJN${detModel}/"
    gearFile="/r04/lc/sg568/HCAL_Optimisation_Studies/GridSandboxes/GJN${detModel}_OutputSandbox/ILD_o1_v06_Detector_Model_${detModel}.gear"
    pandoraSettingsFile="/var/clus/usera/sg568/ilcsoft_v01_17_07/OptimisationStudiesScECal/Calibration/PandoraSettings_MarlinPandora_v02-00-00/PandoraSettingsMuon.xml"
    currentNumberOfHCalLayers=${numberOfHCalLayers[${detModel}]}
    slcioFormat="MokkaSim_Detector_Model_${detModel}_PARTICLE_ENERGYGeV_(.*?).slcio"

    for recoStage in 71 
    do
        calibrationResultsPath="/r04/lc/sg568/HCAL_Optimisation_Studies/CalibrationResults/Detector_Model_${detModel}/Reco_Stage_${recoStage}/MuonCalibration/"
        calibrationFilePath="/r04/lc/sg568/HCAL_Optimisation_Studies/Calibration/Detector_Model_${detModel}/Reco_Stage_${recoStage}/MuonCalibration/"
        currentMHHHE="${MHHHE[${recoStage}]}"
        cd MyCalibration_Template5_Copy2
        ./Calibrate.sh "${slcioPath}" "${slcioFormat}" "${gearFile}" "${calibrationResultsPath}" "${pandoraSettingsFile}" "${currentMHHHE}" "${currentNumberOfHCalLayers}" "${ECalBarrelTimeWindowMax}" "${HCalBarrelTimeWindowMax}" "${ECalEndcapTimeWindowMax}" "${HCalEndcapTimeWindowMax}" "${calibrationFilePath}" 
        cd -
    done
done

