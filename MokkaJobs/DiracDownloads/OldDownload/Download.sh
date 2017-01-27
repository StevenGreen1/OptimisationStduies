#!/bin/bash

source ../../env.sh

#            !EvtType : Photon
#     !MokkaJobNumber : 44
#             !Energy : 10
#              *Owner : sgreen

for detectorNumber in {84..103}
do 
    cd /r04/lc/sg568/HCAL_Optimisation_Studies/Slcio/GJN${detectorNumber}
    dirac-ilc-find-in-FC /ilc/user/s/sgreen Energy=20 EvtType="Kaon0L" JobDescription=OptimisationStudies_ECalStudies MokkaJobNumber=${detectorNumber} Type="Sim" > "tmp.txt"
    while read line 
    do
        echo "Considering : $line"
        if [[ $line == *'.slcio'* ]]
        then
            if [ ! -f "${line##*/}" ] && [ ! -f "/r04/lc/sg568/HCAL_Optimisation_Studies/Slcio/GJN${detectorNumber}/${line##*/}" ];
            then
                echo "Downloading : $line "
                dirac-dms-get-file $line
            fi
        fi
    done < "tmp.txt"
    rm "tmp.txt"

    dirac-ilc-find-in-FC /ilc/user/s/sgreen Energy=10 EvtType="Photon" JobDescription=OptimisationStudies_ECalStudies MokkaJobNumber=${detectorNumber} Type="Sim" > "tmp.txt"
    while read line
    do
        echo "Considering : $line"
        if [[ $line == *'.slcio'* ]]
        then
            if [ ! -f "${line##*/}" ] && [ ! -f "/r04/lc/sg568/HCAL_Optimisation_Studies/Slcio/GJN${detectorNumber}/${line##*/}" ];
            then
                echo "Downloading : $line "
                dirac-dms-get-file $line
            fi
        fi
    done < "tmp.txt"
    rm "tmp.txt"

    dirac-ilc-find-in-FC /ilc/user/s/sgreen Energy=10 EvtType="Muon" JobDescription=OptimisationStudies_ECalStudies MokkaJobNumber=${detectorNumber} Type="Sim" > "tmp.txt"
    while read line
    do
        echo "Considering : $line"
        if [[ $line == *'.slcio'* ]]
        then
            if [ ! -f "${line##*/}" ] && [ ! -f "/r04/lc/sg568/HCAL_Optimisation_Studies/Slcio/GJN${detectorNumber}/${line##*/}" ];
            then
                echo "Downloading : $line "
                dirac-dms-get-file $line
            fi
        fi
    done < "tmp.txt"
    rm "tmp.txt"
done
