#!/bin/bash

for detModel in {84..89} {96..99}
do
    for recoVar in 63 # Done 38 71
    do
         python MarlinSubmitSingleParticles.py ${detModel} ${recoVar}
    done
done

for detModel in {90..95} {100..103}
do
    for recoVar in 38 63 71
    do
         python MarlinSubmitSingleParticles.py ${detModel} ${recoVar}
    done
done


