#!/bin/bash

# Done : 38-77 excluding 44

for detModel in 43
do
   for recoVar in {71..76}
    do
         python MarlinSubmitHCalCellSize.py ${detModel} ${recoVar}
    done
done

