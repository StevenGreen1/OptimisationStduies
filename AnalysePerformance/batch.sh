#!/bin/bash

for detModel in {38..43}
do
    for recoVar in {69..76}
    do
        python SubmitAnalysePerformance.py ${detModel} ${recoVar} 
    done
done

for detModel in {45..77}
do
    for recoVar in {69..76}
    do
        python SubmitAnalysePerformance.py ${detModel} ${recoVar}
    done
done

