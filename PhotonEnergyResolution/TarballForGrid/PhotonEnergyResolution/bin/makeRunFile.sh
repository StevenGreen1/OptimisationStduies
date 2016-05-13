for i in 1000 2000 3000 4000 5000 6000 7000 8000 9000 10000
do
    for j in 96 97 98 99
    do
        echo "/r04/lc/sg568/HCAL_Optimisation_Studies/Calibration/Detector_Model_${j}/Reco_Stage_71/DefaultCalibration/RootFiles/ILD_o1_v06_10_GeV_Photon_SN_1000_${i}.root $j" >> runfile.txt
    done
done
