#!/bin/bash

# 1 is silicon ECal, realistic options
# 5 is scintillator ECal, realistic options 

templateNumber=2

for detModel in {84..89}
do
   for recoVar in 79 #{77..76}
    do
         python MarlinSubmit.py ${detModel} ${recoVar} ${templateNumber}
    done
done

