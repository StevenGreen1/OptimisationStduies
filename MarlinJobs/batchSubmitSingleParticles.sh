#!/bin/bash

# 1 is silicon ECal, realistic options
# 5 is scintillator ECal, realistic options

templateNumber=5

for detModel in 90
do
   for recoVar in 69 #{69..76}
    do
         python MarlinSubmitSingleParticles.py ${detModel} ${recoVar} ${templateNumber}
    done
done



