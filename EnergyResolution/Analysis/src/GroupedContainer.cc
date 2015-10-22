#include "GroupedContainer.h"

Double_t ResolutionFitFunction(Double_t *x, Double_t *par);

//===========================================

GroupedContainer::GroupedContainer(int stageNumber, std::vector<float> energies, std::vector<std::string> rootFiles, std::string plotPath) :
    m_StageNumber(stageNumber),
    m_PlotPath(plotPath),
    m_pResolutionPlot(NULL),
    m_pLinearityPlot(NULL),
    m_pResolutionFit(NULL),
    m_pLinearityFit(NULL),
    m_StochasticTerm(0.f),
    m_ConstantTerm(0.f),
    m_NoiseTerm(0.f),
    m_LinearityGradTerm(0.f),
    m_LinearityIntTerm(0.f)
{
    for (std::vector<float>::const_iterator it = energies.begin(); it != energies.end(); ++it)
    {
        float energy = *it;
        int position = it - energies.begin();
        ResolutionContainer *pResolutionContainer = new ResolutionContainer(m_StageNumber,energy,rootFiles.at(position), m_PlotPath);
        this->AddContainer(pResolutionContainer);
        delete pResolutionContainer;
    }

    this->LinearityMakePlot();
    this->LinearityFit();
    this->LinearityDrawPlot();
    this->ResolutionMakePlot();
//    this->ResolutionFit();
    this->ResolutionDrawPlot();
}

//===========================================

GroupedContainer::~GroupedContainer()
{
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
    m_pLinearityFit->SetParameter(0,0);

    m_pLinearityPlot->Fit("LinearityFit","RM");
    m_LinearityGradTerm = m_pLinearityFit->GetParameter(0);
    m_LinearityIntTerm = m_pLinearityFit->GetParameter(1); 
}

//===========================================

void GroupedContainer::LinearityDrawPlot()
{
    TCanvas *pTCanvas = new TCanvas("Name","Title",200,10,3000,2500);
    pTCanvas->cd();

    TF1 *pTF1 = new TF1("IdealFit","x",10,50);
    pTF1->SetLineColor(kBlue);
    pTF1->SetLineStyle(2);

    m_pLinearityPlot->Draw("AP");
    m_pLinearityFit->SetLineColor(kRed);
    m_pLinearityFit->SetLineStyle(2);
    m_pLinearityFit->Draw("same");
    pTF1->Draw("same");

    std::string pngPlotName = m_PlotPath + "SingleParticleEnergyResolution_RecoStage_" + IntToString(m_StageNumber) + "_Linearity.png";
    std::string dotCPlotName = m_PlotPath + "SingleParticleEnergyResolution_RecoStage_" + IntToString(m_StageNumber) + "_Linearity.C";
    pTCanvas->SaveAs(pngPlotName.c_str());
    pTCanvas->SaveAs(dotCPlotName.c_str());
}

//===========================================

void GroupedContainer::ResolutionMakePlot()
{
    TVectorT<float> tvecEnergyResolution(m_EnergyResolutions.size(), &m_EnergyResolutions[0]);
    TVectorT<float> tvecTrueEnergy(m_TrueEnergies.size(), &m_TrueEnergies[0]);

    m_pResolutionPlot = new TGraph (tvecTrueEnergy,tvecEnergyResolution);
    m_pResolutionPlot->SetTitle("Energy Resolution vs Jet Energy");
    m_pResolutionPlot->GetYaxis()->SetTitle("Energy Resolution  #sigma_{Reco} / E_{Reco}");
    m_pResolutionPlot->GetYaxis()->SetLimits(0,0.25);
    m_pResolutionPlot->GetYaxis()->SetRangeUser(0,0.25);
    m_pResolutionPlot->GetXaxis()->SetTitle("True Energy [GeV]");
    m_pResolutionPlot->GetXaxis()->SetLimits(0,55);
    m_pResolutionPlot->GetXaxis()->SetRangeUser(0,55);
}

//===========================================

void GroupedContainer::ResolutionFit()
{
    m_pResolutionFit = new TF1("ResolutionFit",ResolutionFitFunction,10,50,3);

    m_pResolutionFit->SetParameter(0,0);
//    m_pResolutionFit->FixParameter(0,0.55);
    m_pResolutionFit->SetParLimits(0,0,1);

    m_pResolutionFit->SetParameter(1,0);
//    m_pResolutionFit->FixParameter(1,0);
    m_pResolutionFit->SetParLimits(1,0,1);

    m_pResolutionFit->SetParameter(2,0);
//    m_pResolutionFit->FixParameter(2,0);
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

    std::string pngPlotName = m_PlotPath + "SingleParticleEnergyResolution_RecoStage_" + IntToString(m_StageNumber) + "_Resolution.png";
    std::string dotCPlotName = m_PlotPath + "SingleParticleEnergyResolution_RecoStage_" + IntToString(m_StageNumber) + "_Resolution.C";
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
