#!/bin/bash

for detModel in {1..95}
do
    for recoVar in {1..84}
    do
        file="/r04/lc/sg568/HCAL_Optimisation_Studies/CalibrationResults/Detector_Model_${detModel}/Reco_Stage_${recoVar}/CalibConfig_DetModel${detModel}_RecoStage${recoVar}.py"
        if [[ -a ${file} ]]
        then
            cp ${file} .
        fi
    done
done
