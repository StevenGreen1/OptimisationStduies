
// /r06/lc/sg568/HCAL_Optimisation_Studies/EnergyResolutionResults/Detector_Model_103/Reco_Stage_38/Photon
// EnergyResolution_PandoraSettingsDefault_DetectorModel_103_ReconstructionVariant_38_Photon.root
void DrawNumLayersSiECal10GeV() 
{
    const int recoVar(71);
    const int energy(10);

    std::vector<int> detectorModels;
    detectorModels.push_back(96);
    detectorModels.push_back(97);
    detectorModels.push_back(98);
    detectorModels.push_back(99);

    std::map<int, int> detModelToLayerNumber;
    detModelToLayerNumber[96] = 30;
    detModelToLayerNumber[97] = 26;
    detModelToLayerNumber[98] = 20;
    detModelToLayerNumber[99] = 16;

    TCanvas *pTCanvas = new TCanvas();

    TGraphErrors *pTGraphErrors = new TGraphErrors("EResVsLayer","EResVsLayer");

    for (std::vector<int>::iterator it = detectorModels.begin(); it != detectorModels.end(); it++)
    {
        const int detModel(*it);
        const int layerNumber(detModelToLayerNumber.find(detModel)->second);

        std::string rootFile("/r06/lc/sg568/HCAL_Optimisation_Studies/EnergyResolutionResults/Detector_Model_" + NumberToString(detModel) + "/Reco_Stage_" + NumberToString(recoVar) + "/Photon/EnergyResolution_PandoraSettingsDefault_DetectorModel_" + NumberToString(detModel) + "_ReconstructionVariant_" + NumberToString(recoVar) + "_Photon.root");
        std::cout << rootFile << std::endl;
        TFile *pTFile = new TFile(rootFile.c_str());

        std::string histogramName("Resolution_DetectorModel_" + NumberToString(detModel) + "_ReconstructionVariant_" + NumberToString(recoVar) + "/PFOEnergyHistogram_DetectorModel_" + NumberToString(detModel) + "_ReconstructionVariant_" + NumberToString(recoVar) + ";1");

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

    TH2F *pAxes = new TH2F("axesEj","",100,14,32,1000,5.5,8.5);
    pAxes->SetTitle("100 GeV Photon Energy Resolution vs Number of Layers in ECal (Si)");
    pAxes->GetYaxis()->SetTitle("#sigma_{Reco} / E_{Reco}");
    pAxes->GetXaxis()->SetTitle("Number of ECal Layers");
    pAxes->Draw();

    pTGraphErrors->Draw("same PL");
    const std::string name("SiECal" + NumberToString(energy) + "GeVPhotonResVsLayerNumber.C");
    pTCanvas->SaveAs(name.c_str());
}

template <class T>
std::string NumberToString(T Number)
{
    std::ostringstream ss;
    ss << Number;
    return ss.str();
}

