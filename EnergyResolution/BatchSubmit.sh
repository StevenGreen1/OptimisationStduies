#!/bin/bash

for detModel in 84 #{84..103}
do
    for recoVar in 71 #38 63 
    do
        python SubmitEnergyResolutionAnalysis.py ${detModel} ${recoVar}
    done
done
