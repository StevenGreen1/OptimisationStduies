#!/bin/bash

for detModel in 38 39 40 41 42 49 50 51 60 61 62
do
   for recoVar in {69..76}
    do
         python MarlinSubmit.py ${detModel} ${recoVar}
    done
done
