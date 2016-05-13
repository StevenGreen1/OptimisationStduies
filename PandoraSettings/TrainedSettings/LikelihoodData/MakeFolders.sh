#!/bin/bash

currentDirectory=$(pwd)

for detModel in {84..103}
do
    for recoVar in 38 63 71 
    do
        cd ${currentDirectory}
        mkdir Detector_Model_${detModel}
        cd Detector_Model_${detModel}
        mkdir Reco_Stage_${recoVar}
        cd Reco_Stage_${recoVar}
        mkdir Z_uds
        cd Z_uds
        mkdir 500GeV
    done
done
