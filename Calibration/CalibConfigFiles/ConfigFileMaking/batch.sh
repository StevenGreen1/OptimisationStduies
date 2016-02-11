#!/bin/bash
# Batch making of calibration config files for optimisation studies

for detModel in 38 39 40 41 42 49 50 51 60 61 62
do 
    for recoStage in {69..76}
    do 
        cd /r04/lc/sg568/HCAL_Optimisation_Studies/CalibrationResults/Detector_Model_${detModel}/Reco_Stage_${recoStage}
        python /r04/lc/sg568/HCAL_Optimisation_Studies/CalibrationResults/MakeConfigFile.py ILD_o1_v06_AAxAA_BBxBB_XX_YY.xml CalibConfig_DetModel${detModel}_RecoStage${recoStage}.py 
    done
done
