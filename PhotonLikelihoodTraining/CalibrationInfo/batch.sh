#!/bin/bash
# Batch making of calibration config files for optimisation studies

for detModel in {84..95}
do 
    for recoStage in 71
    do 
        cd /r04/lc/sg568/HCAL_Optimisation_Studies/CalibrationResults/Detector_Model_${detModel}/Reco_Stage_${recoStage}/MuonCalibration
        python /usera/sg568/ilcsoft_v01_17_07/OptimisationStudiesScECal/PhotonLikelihoodTraining/CalibrationInfo/MakeConfigFile.py ILD_o1_v06_AAxAA_BBxBB_XX_YY.xml CalibConfig_DetModel${detModel}_RecoStage${recoStage}_Muon.py 
        cp CalibConfig_DetModel${detModel}_RecoStage${recoStage}_Muon.py /usera/sg568/ilcsoft_v01_17_07/OptimisationStudiesScECal/PhotonLikelihoodTraining/CalibrationInfo/CalibrationConfigMuon/ 
    done
done
