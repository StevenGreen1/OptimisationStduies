#!/bin/bash

#for detModel in {84..89}
#do
#    for recoVar in 38 71 
#    do
#         python MarlinTrainingSubmit.py ${detModel} ${recoVar}
#    done
#done

for detModel in 98 #{96..99}
do
    for recoVar in 71 #38 71
    do
         python MarlinTrainingSubmit.py ${detModel} ${recoVar}
    done
done


