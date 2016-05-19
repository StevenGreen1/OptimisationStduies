#!/bin/bash

for detModel in {84..103}
do
    for recoVar in 38 63 71
    do
        file="/r04/lc/sg568/HCAL_Optimisation_Studies/Calibration/Detector_Model_${detModel}/Reco_Stage_${recoVar}/MuonCalibration/Validation/CalibConfig_DetModel${detModel}_RecoStage${recoVar}.py"
        if [[ -a ${file} ]] && [[ ! -a "CalibConfig_DetModel${detModel}_RecoStage${recoVar}.py" ]]
        then
            echo "Copying over file : ${file}"
            cp ${file} .
        fi
    done
done
