#include "GroupedContainer.h"

Double_t ResolutionFitFunction(Double_t *x, Double_t *par);

//===========================================

GroupedContainer::GroupedContainer(TFile *pTFile, int stageNumber, std::vector<float> energies, std::vector<std::vector<std::string> > rootFiles) :
    m_pTFile(pTFile),
    m_StageNumber(stageNumber),
    m_pResolutionPlot(NULL),
    m_pScaledResolutionPlot(NULL),
    m_pLinearityPlot(NULL),
    m_pLinearityDifferencePlot(NULL),
    m_pResolutionFit(NULL),
    m_pLinearityFit(NULL),
    m_StochasticTerm(0.f),
    m_ConstantTerm(0.f),
    m_NoiseTerm(0.f),
    m_LinearityGradTerm(0.f),
    m_LinearityIntTerm(0.f)
{
    std::string directoryName = "ResultsContainer_Stage" + IntToString(m_StageNumber);
    TDirectory *pTDirectory = m_pTFile->mkdir(directoryName.c_str());
    pTDirectory->cd();

    for (std::vector<float>::const_iterator it = energies.begin(); it != energies.end(); ++it)
    {
        float energy = *it;
        int position = it - energies.begin();
        ResolutionContainer *pResolutionContainer = new ResolutionContainer(m_pTFile, m_StageNumber, energy, rootFiles.at(position));
        this->AddContainer(pResolutionContainer);
        delete pResolutionContainer;
    }

    this->LinearityMakePlot();
    this->LinearityMakeDifferencePlot();
//    this->LinearityFit();
//    this->LinearityDrawPlot();
    this->ResolutionMakePlot();
    this->ResolutionMakeScaledPlot();
//    this->ResolutionFit();
//    this->ResolutionDrawPlot();
    this->Write();
}

//===========================================

GroupedContainer::~GroupedContainer()
{
}

//===========================================

void GroupedContainer::Write()
{
    std::string resolutionPlotName = "ResolutionPlot_Stage" + IntToString(m_StageNumber);
    m_pResolutionPlot->SetTitle(resolutionPlotName.c_str());
    m_pResolutionPlot->SetName(resolutionPlotName.c_str());
    m_pResolutionPlot->Write();

    std::string scaledResolutionPlotName = "ScaledResolutionPlot_Stage" + IntToString(m_StageNumber);
    m_pScaledResolutionPlot->SetTitle(scaledResolutionPlotName.c_str());
    m_pScaledResolutionPlot->SetName(scaledResolutionPlotName.c_str());
    m_pScaledResolutionPlot->Write();

    std::string linearityPlotName = "LinearityPlot_Stage" + IntToString(m_StageNumber);
    m_pLinearityPlot->SetTitle(linearityPlotName.c_str());
    m_pLinearityPlot->SetName(linearityPlotName.c_str());
    m_pLinearityPlot->Write();

    std::string linearityDifferencePlotName = "LinearityDifferencePlot_Stage" + IntToString(m_StageNumber);
    m_pLinearityDifferencePlot->SetTitle(linearityDifferencePlotName.c_str());
    m_pLinearityDifferencePlot->SetName(linearityDifferencePlotName.c_str());
    m_pLinearityDifferencePlot->Write();
}

//===========================================

void GroupedContainer::AddContainer(ResolutionContainer *pResolutionContainer)
{
    m_hPFOEnergy.push_back(pResolutionContainer->GetEnergyHist());
    m_TrueEnergies.push_back(pResolutionContainer->GetTrueEnergy());
    m_MeanPFOEnergies.push_back(pResolutionContainer->GetMeanEnergy());
    m_StdDevPFOEnergies.push_back(pResolutionContainer->GetStdDevEnergy());
    m_EnergyResolutions.push_back(pResolutionContainer->GetResolution());
    m_EnergyResolutionErrors.push_back(pResolutionContainer->GetResolutionError());
    std::cout << pResolutionContainer->GetResolution() << std::endl;
    std::cout << pResolutionContainer->GetTrueEnergy() << std::endl;
}

//===========================================

void GroupedContainer::LinearityMakeDifferencePlot()
{
    std::vector<float> differences;

    for (std::vector<float>::iterator it = m_MeanPFOEnergies.begin(); it != m_MeanPFOEnergies.end(); ++it) 
    {
        float meanPFOEnergy = *it;
        int counter = it - m_MeanPFOEnergies.begin();
        float trueEnergy = m_TrueEnergies.at(counter);
        float difference = meanPFOEnergy-trueEnergy;
        differences.push_back(difference);
    }

    TVectorT<float> tvecDifference(differences.size(), &differences[0]);
    TVectorT<float> tvecTrueEnergy(m_TrueEnergies.size(), &m_TrueEnergies[0]);

    m_pLinearityDifferencePlot = new TGraph (tvecTrueEnergy,tvecDifference);
    m_pLinearityDifferencePlot->SetTitle("PFO Energy - True Energy vs True Energy");
    m_pLinearityDifferencePlot->GetXaxis()->SetTitle("True Energy [GeV]");
    m_pLinearityDifferencePlot->GetXaxis()->SetLimits(0,55);
    m_pLinearityDifferencePlot->GetXaxis()->SetRangeUser(0,55);
    m_pLinearityDifferencePlot->GetYaxis()->SetTitle("PFO Energy - True Energy [GeV]");
    m_pLinearityDifferencePlot->GetYaxis()->SetLimits(-10,10);
    m_pLinearityDifferencePlot->GetYaxis()->SetRangeUser(-10,10);
}

//===========================================

void GroupedContainer::LinearityMakePlot()
{
    TVectorT<float> tvecMeanPFOEnergy(m_MeanPFOEnergies.size(), &m_MeanPFOEnergies[0]);
    TVectorT<float> tvecTrueEnergy(m_TrueEnergies.size(), &m_TrueEnergies[0]);

    m_pLinearityPlot = new TGraph (tvecTrueEnergy,tvecMeanPFOEnergy);
    m_pLinearityPlot->SetTitle("PFO Energy vs True Energy");
    m_pLinearityPlot->GetXaxis()->SetTitle("True Energy [GeV]");
    m_pLinearityPlot->GetXaxis()->SetLimits(0,55);
    m_pLinearityPlot->GetXaxis()->SetRangeUser(0,55);
    m_pLinearityPlot->GetYaxis()->SetTitle("PFO Energy [GeV]");
    m_pLinearityPlot->GetYaxis()->SetLimits(0,55);
    m_pLinearityPlot->GetYaxis()->SetRangeUser(0,55);
}

//===========================================

void GroupedContainer::LinearityFit()
{
    m_pLinearityFit = new TF1("LinearityFit","[0] * x + [1]",10,50);
    m_pLinearityFit->SetParameter(0,0);
    m_pLinearityFit->SetParameter(1,1);

    m_pLinearityPlot->Fit("LinearityFit","RM");
    m_LinearityGradTerm = m_pLinearityFit->GetParameter(0);
    m_LinearityIntTerm = m_pLinearityFit->GetParameter(1); 
}

//===========================================

void GroupedContainer::LinearityDrawPlot()
{
    TCanvas *pTCanvas = new TCanvas("Name","Title",200,10,3000,2500);
    pTCanvas->cd();

//    TF1 *pTF1 = new TF1("IdealFit","x",10,50);
//    pTF1->SetLineColor(kBlue);
//    pTF1->SetLineStyle(2);

    m_pLinearityPlot->Draw("AP");
    m_pLinearityFit->SetLineColor(kRed);
    m_pLinearityFit->SetLineStyle(2);
    m_pLinearityFit->Draw("same");
//    pTF1->Draw("same");

    std::string pngPlotName = "SingleParticleEnergyResolution_RecoStage_" + IntToString(m_StageNumber) + "_Linearity.png";
    std::string dotCPlotName = "SingleParticleEnergyResolution_RecoStage_" + IntToString(m_StageNumber) + "_Linearity.C";
    pTCanvas->SaveAs(pngPlotName.c_str());
    pTCanvas->SaveAs(dotCPlotName.c_str());
}

//===========================================

void GroupedContainer::ResolutionMakeScaledPlot()
{
    std::vector<float> scaledResolutions;

    for (std::vector<float>::iterator it = m_TrueEnergies.begin(); it != m_TrueEnergies.end(); ++it)
    {
        float trueEnergy = *it;
        int counter = it - m_TrueEnergies.begin();
        float resolution = m_EnergyResolutions.at(counter);

        float scaledResolution = resolution * pow(trueEnergy,0.5);
        scaledResolutions.push_back(scaledResolution);
    }

    TVectorT<float> tvecScaledEnergyResolution(scaledResolutions.size(), &scaledResolutions[0]);
    TVectorT<float> tvecTrueEnergy(m_TrueEnergies.size(), &m_TrueEnergies[0]);

    m_pScaledResolutionPlot = new TGraph (tvecTrueEnergy,tvecScaledEnergyResolution);
    m_pScaledResolutionPlot->SetTitle("Scaled Energy Resolution vs Jet Energy");
    m_pScaledResolutionPlot->GetYaxis()->SetTitle("ScaledEnergy Resolution  #frac{#sigma_{Reco}}{E_{Reco}}#sqrt{E_{Reco}}");
    m_pScaledResolutionPlot->GetYaxis()->SetLimits(0,2);
    m_pScaledResolutionPlot->GetYaxis()->SetRangeUser(0,2);
    m_pScaledResolutionPlot->GetXaxis()->SetTitle("True Energy [GeV]");
    m_pScaledResolutionPlot->GetXaxis()->SetLimits(0,55);
    m_pScaledResolutionPlot->GetXaxis()->SetRangeUser(0,55);
}

//===========================================

void GroupedContainer::ResolutionMakePlot()
{
    TVectorT<float> tvecEnergyResolution(m_EnergyResolutions.size(), &m_EnergyResolutions[0]);
    TVectorT<float> tvecTrueEnergy(m_TrueEnergies.size(), &m_TrueEnergies[0]);

    m_pResolutionPlot = new TGraph (tvecTrueEnergy,tvecEnergyResolution);
    m_pResolutionPlot->SetTitle("Energy Resolution vs Jet Energy");
    m_pResolutionPlot->GetYaxis()->SetTitle("Energy Resolution  #sigma_{Reco} / E_{Reco}");
    m_pResolutionPlot->GetYaxis()->SetLimits(0,2);
    m_pResolutionPlot->GetYaxis()->SetRangeUser(0,2);
    m_pResolutionPlot->GetXaxis()->SetTitle("True Energy [GeV]");
    m_pResolutionPlot->GetXaxis()->SetLimits(0,55);
    m_pResolutionPlot->GetXaxis()->SetRangeUser(0,55);
}

//===========================================

void GroupedContainer::ResolutionFit()
{
    m_pResolutionFit = new TF1("ResolutionFit",ResolutionFitFunction,10,50,3);

    m_pResolutionFit->SetParameter(0,0);
    m_pResolutionFit->SetParLimits(0,0,1);

    m_pResolutionFit->SetParameter(1,0);
    m_pResolutionFit->SetParLimits(1,0,1);

    m_pResolutionFit->SetParameter(2,0);
    m_pResolutionFit->SetParLimits(2,0,1);

    m_pResolutionPlot->Fit("ResolutionFit","RM");
    m_StochasticTerm = pow(m_pResolutionFit->GetParameter(0),0.5); // a 0
    m_ConstantTerm = pow(m_pResolutionFit->GetParameter(1),0.5);   // b 1
    m_NoiseTerm = pow(m_pResolutionFit->GetParameter(2),0.5);      // c 2
}

//===========================================

void GroupedContainer::ResolutionDrawPlot()
{
    TCanvas *pTCanvas = new TCanvas("Name","Title",200,10,3000,2500);
    pTCanvas->cd();

    TF1 *pTF1 = new TF1("IdealFit","0.55/TMath::Sqrt(x)",10,50);
    pTF1->SetLineColor(kBlue);
    pTF1->SetLineStyle(2);

    m_pResolutionPlot->Draw("AP");
    if (m_pResolutionFit != NULL)
    {
        m_pResolutionFit->SetLineColor(kRed);
        m_pResolutionFit->Draw("same");
    }
    pTF1->Draw("same");

    std::string pngPlotName = "SingleParticleEnergyResolution_RecoStage_" + IntToString(m_StageNumber) + "_Resolution.png";
    std::string dotCPlotName = "SingleParticleEnergyResolution_RecoStage_" + IntToString(m_StageNumber) + "_Resolution.C";
    pTCanvas->SaveAs(pngPlotName.c_str());
    pTCanvas->SaveAs(dotCPlotName.c_str());
}

//===========================================

Double_t ResolutionFitFunction(Double_t *x, Double_t *par) 
{
    // Quadrature addition
    Double_t term1 = par[0] / x[0];          // Stochastic
    Double_t term2 = par[1];                 // Constant
    Double_t term3 = par[2] / (x[0] * x[0]); // Noise
    return TMath::Sqrt(term1 + term2 + term3);
}

//===========================================

std::string GroupedContainer::IntToString(int a)
{
    std::stringstream ss;
    ss << a;
    std::string str = ss.str();
    return str;
}

//===========================================
