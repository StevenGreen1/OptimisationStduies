#!/bin/bash

# Done : 38-77 excluding 44

for detModel in 38 
do
   for recoVar in 38 43 46 51 54 59
    do
         python MarlinSubmitSingleParticles.py ${detModel} ${recoVar}
    done
done

