#!/bin/bash

# Done : 38-77 excluding 44

for detModel in {84..89}
do
   for recoVar in {69..76}
    do
         python MarlinSubmit.py ${detModel} ${recoVar}
    done
done

