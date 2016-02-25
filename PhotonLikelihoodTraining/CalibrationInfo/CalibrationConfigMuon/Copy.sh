#!/bin/bash

for detModel in {84..103}
do
    for recoVar in 38 71
    do
        cp /r04/lc/sg568/HCAL_Optimisation_Studies/Calibration/Detector_Model_${detModel}/Reco_Stage_${recoVar}/MuonCalibration/Validation/CalibConfig_DetModel${detModel}_RecoStage${recoVar}.py .
    done
done
