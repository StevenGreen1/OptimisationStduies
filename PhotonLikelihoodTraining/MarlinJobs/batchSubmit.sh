#!/bin/bash

# 1 is silicon ECal, realistic options
# 5 is scintillator ECal, realistic options 

for detModel in {96..99}
do
    for recoVar in 71 
    do
         python MarlinTrainingSubmit.py ${detModel} ${recoVar} ${templateNumber}
    done
done

