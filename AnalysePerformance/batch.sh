#!/bin/bash

for detModel in 95 #{84..94}
do
    for recoVar in {69..76}
    do
        for pandora in "PerfectPFA" "PerfectPhoton" "PerfectPhotonNK0L" "Default"
        do
            python SubmitAnalysePerformance.py ${detModel} ${recoVar} ${pandora}
        done
    done
done

