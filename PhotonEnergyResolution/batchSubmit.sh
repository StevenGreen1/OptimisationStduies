#!/bin/bash

#for detModel in {38..44}
#do
#   for recoVar in {69..76}
#    do
#        python SubmitEnergyResolutionAnalysis.py ${detModel} ${recoVar}
#    done
#done

for detModel in {45..77}
do
    for recoVar in 71
    do
        python SubmitEnergyResolutionAnalysis.py ${detModel} ${recoVar}
    done
done
