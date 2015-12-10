#!/bin/bash

MC1=0
MC2=0
MC3=0

UnFin1=0
UnFin2=0
UnFin3=0

MC1Array=()
MC2Array=()
MC3Array=()

while read line; 
do
    IFS=' ' read -r -a array <<< "$line"
    jobID=${array[0]}
    running=${array[5]}

    IFS=':' read -r -a timeArray <<< "${array[4]}"
    runTimeMinutes=${timeArray[1]}
    runTimeSeconds=${timeArray[2]}

    echo "Job ${jobID} has been running for ${runTimeMinutes} minutes and ${runTimeSeconds} seconds."

    if [[ "${runTimeMinutes}" > 30 ]];
    then 
        echo "Job ${jobID} is taking a long time (${runTimeMinutes} min, ${runTimeSeconds} sec) and will be killed."
        condor_rm ${jobID}
    fi
done < <(condor_q -wide | grep Marlin)

