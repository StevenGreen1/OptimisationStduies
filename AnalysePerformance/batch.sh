#!/bin/bash

for detModel in {84..89}
do
    for recoVar in 79 #{69..76}
    do
        for pandora in "PerfectPFA" "PerfectPhoton" "PerfectPhotonNK0L" "Default"
        do
            python SubmitAnalysePerformance.py ${detModel} ${recoVar} ${pandora}
        done
    done
done

