#!/bin/bash

source ../env.sh

evtType=Kaon0L
jobDescription=OptimisationStudies

for detModel in {38..43}
do
    for recoStage in {69..76}
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


#for detModel in {45..77}
#do
#    for recoVar in 71
#    do
#        python SubmitEnergyResolutionAnalysis.py ${detModel} ${recoVar}
#    done
#done
