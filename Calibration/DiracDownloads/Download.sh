#!/bin/bash

source env.sh

jobDescription=OptimisationStudies

for detModel in {85..95}
do
    for evtType in "Muon" "Photon"
    do
        energy="10"
        echo "Downloading: ${jobDescription}, ${evtType}, Detector Model ${detModel}, ${energy} GeV"

        cd /r04/lc/sg568/HCAL_Optimisation_Studies/Slcio/GJN${detModel}
        dirac-ilc-find-in-FC /ilc/user/s/sgreen JobDescription=${jobDescription} Energy=${energy} EvtType=${evtType} Type=Sim MokkaJobNumber=${detModel} > "tmp.txt"

        while read line
        do
            if [[ $line == *'.slcio'* ]] 
            then
                if [ ! -f "${line##*/}" ] && [ ! -f "/r04/lc/sg568/HCAL_Optimisation_Studies/Slcio/GJN${detModel}/${line##*/}" ];
                then
                    echo "Downloading file: $line"
                    dirac-dms-get-file $line
                fi
            fi
        done < "tmp.txt"
    done

    for evtType in "Kaon0L" 
    do
        energy="20"
        echo "Downloading: ${jobDescription}, ${evtType}, Detector Model ${detModel}, ${energy} GeV"

        cd /r04/lc/sg568/HCAL_Optimisation_Studies/Slcio/GJN${detModel}
        dirac-ilc-find-in-FC /ilc/user/s/sgreen JobDescription=${jobDescription} Energy=${energy} EvtType=${evtType} Type=Sim MokkaJobNumber=${detModel} > "tmp.txt"

        while read line
        do
            if [[ $line == *'.slcio'* ]]
            then
                if [ ! -f "${line##*/}" ] && [ ! -f "/r04/lc/sg568/HCAL_Optimisation_Studies/Slcio/GJN${detModel}/${line##*/}" ];
                then
                    echo "Downloading file: $line"
                    dirac-dms-get-file $line
                fi
            fi
        done < "tmp.txt"
    done
done
