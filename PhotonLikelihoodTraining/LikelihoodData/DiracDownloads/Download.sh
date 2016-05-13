#!/bin/bash

source ../../../env.sh

evtType=Z_uds
jobDescription=OptimisationStudies

for detModel in {84..89} {96..99}
do
    for recoStage in 38 71 
    do
        for energy in 500
        do
            cd /usera/sg568/ilcsoft_v01_17_07/${jobDescription}/PhotonLikelihoodTraining/LikelihoodData/Detector_Model_${detModel}/Reco_Stage_${recoStage}/${evtType}/${energy}GeV
            fileToDownload="PandoraLikelihoodData_DetModel_${detModel}_RecoStage_${recoStage}.xml"
            gridPath="/ilc/user/s/sgreen/${jobDescription}/TrainingPhotonLikelihoodData/Detector_Model_${detModel}/Reco_Stage_${recoStage}/${evtType}/${energy}GeV"
            file="${gridPath}/${fileToDownload}"
            if [[ ! -f "${file##*/}" ]];
            then
                echo "Downloading file: $file"
                dirac-dms-get-file $file
            fi
        done
    done
done
