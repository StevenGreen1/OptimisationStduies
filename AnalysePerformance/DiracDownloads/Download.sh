#!/bin/bash

source ../../env.sh

evtType=Z_uds
jobDescription=OptimisationStudies_ECalStudies

for detModel in {84..103}
do
    for recoStage in 38 63 71
    do
        for energy in 91 200 360 500
        do
            echo "Downloading: ${jobDescription}, ${evtType}, Detector Model ${detModel}, Reco Stage ${recoStage}, ${energy}GeV"
            cd /r06/lc/sg568/HCAL_Optimisation_Studies/AnalysePerformanceResults/Detector_Model_${detModel}/Reco_Stage_${recoStage}/${evtType}/${energy}GeV
            dirac-ilc-find-in-FC /ilc/user/s/sgreen JobDescription=${jobDescription} Energy=${energy} EvtType=${evtType} Type=Results MokkaJobNumber=${detModel} ReconstructionVariant=${recoStage} > "tmp.txt"
            while read line
            do
                if [[ ! -f "${line##*/}" ]] && [[ $line == *"Default"* ]];
                then
                    echo "Downloading file: $line"
                    dirac-dms-get-file $line
                fi
            done < "tmp.txt"
            rm "tmp.txt"
        done
    done
done

for detModel in {84..103}
do
    for recoStage in 38 63 71
    do
        for energy in 91 200 360 500
        do
            echo "Downloading: ${jobDescription}, ${evtType}, Detector Model ${detModel}, Reco Stage ${recoStage}, ${energy}GeV"
            cd /r06/lc/sg568/HCAL_Optimisation_Studies/AnalysePerformanceResults/Detector_Model_${detModel}/Reco_Stage_${recoStage}/${evtType}/${energy}GeV
            dirac-ilc-find-in-FC /ilc/user/s/sgreen JobDescription=${jobDescription} Energy=${energy} EvtType=${evtType} Type=Results MokkaJobNumber=${detModel} ReconstructionVariant=${recoStage} > "tmp.txt"
            while read line
            do
                if [[ ! -f "${line##*/}" ]];
                then
                    echo "Downloading file: $line"
                    dirac-dms-get-file $line
                fi
            done < "tmp.txt"
            rm "tmp.txt"
        done
    done
done

