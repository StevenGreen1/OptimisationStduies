#!/bin/bash

for detModel in {84..89}
do
    for recoVar in 38 
    do
        for pandora in "PerfectPFA" "PerfectPhoton" "PerfectPhotonNK0L" "Default"
        do
            python SubmitAnalysePerformance.py ${detModel} ${recoVar} ${pandora}
        done
    done
done

for detModel in {90..95}
do
    for recoVar in 79 63
    do
        for pandora in "PerfectPFA" "PerfectPhoton" "PerfectPhotonNK0L" "Default"
        do
            python SubmitAnalysePerformance.py ${detModel} ${recoVar} ${pandora}
        done
    done
done

