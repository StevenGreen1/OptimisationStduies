void Draw_ER_vs_HCalCellSize() 
{
    const int recoVar(71);
    const int energy(50);

    std::vector<int> detectorModels;
    detectorModels.push_back(39);
    detectorModels.push_back(40);
    detectorModels.push_back(85);
    detectorModels.push_back(41);
    detectorModels.push_back(42);
    detectorModels.push_back(43);

    std::map<int, int> detModelToRecoVar;
    detModelToRecoVar[39] = 69;
    detModelToRecoVar[40] = 70;
    detModelToRecoVar[85] = 71;
    detModelToRecoVar[41] = 72;
    detModelToRecoVar[42] = 73;
    detModelToRecoVar[43] = 74;

    std::map<int, int> detModelToCellSize;
    detModelToCellSize[39] = 10;
    detModelToCellSize[40] = 20;
    detModelToCellSize[85] = 30;
    detModelToCellSize[41] = 40;
    detModelToCellSize[42] = 50;
    detModelToCellSize[43] = 100;

    TCanvas *pTCanvas = new TCanvas();
    pTCanvas->Draw();

    TGraphErrors *pTGraphErrors = new TGraphErrors("EResVsLayer","EResVsLayer");

    for (std::vector<int>::iterator it = detectorModels.begin(); it != detectorModels.end(); it++)
    {
        const int detModel(*it);
        const int recoVar(detModelToRecoVar.find(detModel)->second);
        const int layerNumber(detModelToCellSize.find(detModel)->second);

        std::string rootFile("/r06/lc/sg568/HCAL_Optimisation_Studies/EnergyResolutionResults/Detector_Model_" + NumberToString(detModel) + "/Reco_Stage_" + NumberToString(recoVar) + "/Kaon0L/EnergyResolution_PandoraSettingsDefault_DetectorModel_" + NumberToString(detModel) + "_ReconstructionVariant_" + NumberToString(recoVar) + "_Kaon0L.root");

        std::cout << rootFile << std::endl;
        TFile *pTFile = new TFile(rootFile.c_str());

        std::string histogramName("Resolution_DetectorModel_" + NumberToString(detModel) + "_ReconstructionVariant_" + NumberToString(recoVar) + "/PFOEnergyHistogram_DetectorModel_" + NumberToString(detModel) + "_ReconstructionVariant_" + NumberToString(recoVar) + ";3");
        std::cout << histogramName << std::endl;
 
        TH1F *pTH1F = (TH1F*)pTFile->Get(histogramName.c_str());

        std::string fitTitle = "PFOEnergyHistogramGaussianFit_DetectorModel_" + NumberToString(detModel) + "_ReconstructionVariant_" + NumberToString(recoVar) + "_Energy" + NumberToString(energy) + "GeV";
        TF1 *pGaussianFit = new TF1(fitTitle.c_str(),"gaus",0,1000);

        pTH1F->Fit(fitTitle.c_str());
        const float fitAmplitude(pGaussianFit->GetParameter(0));
        const float fitMean(pGaussianFit->GetParameter(1));
        const float fitStdDev(pGaussianFit->GetParameter(2));
        const float energyResolution(fitStdDev/fitMean);

        const float meanError(pGaussianFit->GetParError(1));
        const float meanFracError(meanError / fitMean);
        const float stdDevError(pGaussianFit->GetParError(2));
        const float stdDevFracError(stdDevError / fitStdDev);

        const float energyResolutionError = energyResolution * std::pow( (meanFracError*meanFracError) + (stdDevFracError*stdDevFracError) ,0.5);

        pTGraphErrors->SetPoint(pTGraphErrors->GetN(),layerNumber,energyResolution*100.f);
        pTGraphErrors->SetPointError(pTGraphErrors->GetN()-1,0,energyResolutionError*100.f);

        std::cout << "For energy : " << energy << std::endl;
        std::cout << "Amplitude          : " << fitAmplitude << std::endl;
        std::cout << "Mean               : " << fitMean << std::endl;
        std::cout << "Standard Deviation : " << fitStdDev << std::endl;
        std::cout << "Det model " << detModel << std::endl;
        std::cout << "Energy Resolution  : " << energyResolution*100 << std::endl;
    }

    TH2F *pAxes = new TH2F("axesEj","",100,0,110,1000,0,20);
    pAxes->SetTitle("50 GeV Kaon0L Energy Resolution vs HCal Cell Size");
    pAxes->GetYaxis()->SetTitle("#sigma_{Reco} / E_{Reco}");
    pAxes->GetXaxis()->SetTitle("HCal Cell Size [mm^{2}]");
    pAxes->Draw();

    pTGraphErrors->Draw("same PL");
    const std::string name("ER_vs_HCalCellSize_" + NumberToString(energy) + "GeVKaon0L.C");
    const std::string name2("ER_vs_HCalCellSize_" + NumberToString(energy) + "GeVKaon0L.pdf");
    pTCanvas->SaveAs(name.c_str());
    pTCanvas->SaveAs(name2.c_str());
}

template <class T>
std::string NumberToString(T Number)
{
    std::ostringstream ss;
    ss << Number;
    return ss.str();
}

