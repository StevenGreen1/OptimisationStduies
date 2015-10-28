#!/bin/bash

for detModel in {39..43}
do
    for recoVar in {69..76}
    do
        python SubmitAnalysePerformance.py ${detModel} ${recoVar} 
    done
done

