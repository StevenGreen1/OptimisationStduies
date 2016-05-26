#!/bin/bash

source ../../env.sh

jobDescription=OptimisationStudies_ECalStudies

for evtType in "Kaon0L" "Photon"
do
    for detModel in {84..103}
    do
        for recoStage in 71 38 63
        do
            echo "Downloading: ${jobDescription}, ${evtType}, Detector Model ${detModel}, Reco Stage ${recoStage}"
            cd /r06/lc/sg568/HCAL_Optimisation_Studies/EnergyResolutionResults/Detector_Model_${detModel}/Reco_Stage_${recoStage}/${evtType}
            dirac-ilc-find-in-FC /ilc/user/s/sgreen JobDescription=${jobDescription} EvtType=${evtType} Type=EResResults MokkaJobNumber=${detModel} ReconstructionVariant=${recoStage} > "tmp.txt"
            while read line
            do
                if [[ $line == *'.root'* ]] && [[ $line == *'Default'* ]]
                then
                    if [ ! -f "${line##*/}" ];
                    then
                        echo "Downloading file: $line"
                        dirac-dms-get-file $line
                    fi
                fi
            done < "tmp.txt"
        done
    done
done

