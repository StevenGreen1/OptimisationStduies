#!/bin/bash

energy=100
particle="Photon" #Kaon0L Muon Photon
pdg="22"

cd HEPEvtFiles

for entry in *
do
    if [[ $entry == *"${energy}_GeV_Energy_${pdg}"* ]]
    then
        echo "Uploading file : $entry"
        dirac-dms-add-file /ilc/user/s/sgreen/HEPEvtFiles/${particle}/${energy}GeV/${entry} ${entry} DESY-SRM
        mv $entry UploadedFiles
    fi
done

