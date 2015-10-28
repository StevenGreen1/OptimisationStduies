#!/bin/bash

source ../env.sh

evtType=Z_uds
jobDescription=OptimisationStudies

for detModel in {60..77} #{38..77}
do
    for recoStage in {69..76}
    do
        for energy in 91 200 360 500
        do
            echo "Downloading: ${jobDescription}, ${evtType}, Detector Model ${detModel}, Reco Stage ${recoStage}, ${energy}GeV"
            cd /r06/lc/sg568/HCAL_Optimisation_Studies/RootFilesBatch/Detector_Model_${detModel}/Reco_Stage_${recoStage}/${evtType}/${energy}GeV
            dirac-ilc-find-in-FC /ilc/user/s/sgreen JobDescription=${jobDescription} Energy=${energy} EvtType=${evtType} Type=Rec MokkaJobNumber=${detModel} ReconstructionVariant=${recoStage} > "tmp.txt"
            while read line
            do
                if [[ $line == *'.root'* ]] && [[ $line == *'Default'* ]]
                then
                    if [ ! -f "${line##*/}" ] && [ ! -f "/r06/lc/sg568/${jobDescription}/Detector_Model_${detModel}/Reco_Stage_${recoVar}/${i}GeV/${line##*/}" ];
                    then
                        echo "Downloading file: $line"
                        dirac-dms-get-file $line
                    fi
                fi
            done < "tmp.txt"
        done
    done
done
