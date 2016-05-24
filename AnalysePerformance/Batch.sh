#!/bin/bash

for detModel in {84..103}
do
    for recoVar in 63
    do
        for pandora in "Default"
        do
            python SubmitAnalysePerformance.py ${detModel} ${recoVar} ${pandora}
        done
    done
done

for detModel in {90..95} {100..103}
do
    for recoVar in 38 71
    do
        for pandora in "Default"
        do
            python SubmitAnalysePerformance.py ${detModel} ${recoVar} ${pandora}
        done
    done
done

for detModel in {84..103}
do
    for recoVar in 63 
    do
        for pandora in "PerfectPFA" "PerfectPhoton" "PerfectPhotonNK0L" "Muon"
        do
            python SubmitAnalysePerformance.py ${detModel} ${recoVar} ${pandora}
        done
    done
done

for detModel in {90..95} {100..103}
do
    for recoVar in 38 71
    do
        for pandora in "PerfectPFA" "PerfectPhoton" "PerfectPhotonNK0L" "Muon"
        do
            python SubmitAnalysePerformance.py ${detModel} ${recoVar} ${pandora}
        done
    done
done

