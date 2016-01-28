#!/bin/bash

# 1 is silicon ECal, realistic options
# 5 is scintillator ECal, realistic options 

templateNumber=5

for detModel in {90..95}
do
    for recoVar in 71 #{77..76}
    do
         python MarlinSubmit.py ${detModel} ${recoVar} ${templateNumber}
    done
done

