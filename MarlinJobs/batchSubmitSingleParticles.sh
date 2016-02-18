#!/bin/bash

for detModel in {96..99}
do
   for recoVar in 71 
    do
         python MarlinSubmitSingleParticles.py ${detModel} ${recoVar}
    done
done



