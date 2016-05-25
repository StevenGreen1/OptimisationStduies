#include "ResolutionContainer.h"

//===========================================

ResolutionContainer::ResolutionContainer(const int detectorModel, const int reconstructionVariant, TFile *pTFile, const int energy, StringVector rootFiles) :
    m_DetectorModel(detectorModel),
    m_ReconstructionVariant(reconstructionVariant),
    m_pTFile(pTFile),
    m_TrueEnergy(energy),
    m_RootFiles(rootFiles),
    m_hEnergy(NULL),
    m_BinNumber(100),
    m_GaussianFit(NULL),
    m_FitMean(0.f),
    m_FitStdDev(0.f),
    m_FitAmplitude(0.f),
    m_FitChi2(0.f),
    m_EnergyResolution(0.f),
    m_EnergyResolutionError(0.f)
{
    const float binMax = 2.f * energy;
    const std::string fitTitle = "PFOEnergyHistogram_DetectorModel_" + NumberToString(detectorModel) + "_ReconstructionVariant_" + NumberToString(reconstructionVariant);
    m_hEnergy = new TH1F(fitTitle.c_str(),fitTitle.c_str(),m_BinNumber,0.f,binMax);
    m_hEnergy->GetXaxis()->SetTitle("PFO Energy [GeV]");
    m_hEnergy->GetYaxis()->SetTitle("Entries");

    this->ReadData();
    this->Fit();
    this->Save();
}

//===========================================

ResolutionContainer::~ResolutionContainer()
{
    delete m_hEnergy;
    delete m_GaussianFit;
}

//===========================================

void ResolutionContainer::ReadData()
{
    TChain *pTChain = new TChain("PfoAnalysisTree");

    float pfoEnergyTotal(0.f);
    int nPfoTargetsTotal(0), nPfosTotal(0);
    FloatVector *pTargetCosTheta(NULL);

    for(StringVector::iterator it = m_RootFiles.begin(); it != m_RootFiles.end(); ++it)
    {
        std::string rootFileName = *it;
        pTChain->Add(rootFileName.c_str());
    }

    pTChain->SetBranchAddress("pfoEnergyTotal",&pfoEnergyTotal);
    pTChain->SetBranchAddress("nPfoTargetsTotal",&nPfoTargetsTotal);
    pTChain->SetBranchAddress("nPfosTotal",&nPfosTotal);
    pTChain->SetBranchAddress("pfoTargetCosTheta",&pTargetCosTheta);

    for (unsigned int i = 0; i < pTChain->GetEntries(); i++)
    {
        pTChain->GetEntry(i);
        const float currentCosTheta(std::fabs(pTargetCosTheta->at(0)));

        if (nPfoTargetsTotal==1 and nPfosTotal==1 and currentCosTheta < 0.7)
        {
            m_hEnergy->Fill(pfoEnergyTotal);
        }
    }
}

//===========================================

void ResolutionContainer::Save()
{
    m_hEnergy->Write();
}

//===========================================

void ResolutionContainer::Draw()
{
    TCanvas *pTCanvas = new TCanvas("Name","Title",200,10,600,500);
    pTCanvas->cd();
    m_hEnergy->Draw();
    m_GaussianFit->Draw("same");
    const std::string pngPlotName = "SingleParticleEnergyResolution_DetectorModel_" + NumberToString(m_DetectorModel) + "_RecoStage_" + NumberToString(m_ReconstructionVariant) + "_" + NumberToString(m_TrueEnergy) + "GeV.png";
    const std::string dotCPlotName = "SingleParticleEnergyResolution_DetectorModel_" + NumberToString(m_DetectorModel) + "_RecoStage_" + NumberToString(m_ReconstructionVariant) + "_" + NumberToString(m_TrueEnergy) + "GeV.C";
    pTCanvas->SaveAs(pngPlotName.c_str());
    pTCanvas->SaveAs(dotCPlotName.c_str());
}

//===========================================

void ResolutionContainer::Fit()
{
    std::string fitTitle = "PFOEnergyHistogramGaussianFit_DetectorModel_" + NumberToString(m_DetectorModel) + "_ReconstructionVariant_" + NumberToString(m_ReconstructionVariant) + "_Energy" + NumberToString(m_TrueEnergy) + "GeV";
    m_GaussianFit = new TF1(fitTitle.c_str(),"gaus",0,1000);
    m_hEnergy->Fit(fitTitle.c_str());
    m_FitAmplitude = m_GaussianFit->GetParameter(0);
    m_FitMean = m_GaussianFit->GetParameter(1);
    m_FitStdDev = m_GaussianFit->GetParameter(2);
    m_FitChi2 = m_GaussianFit->GetChisquare();
    m_EnergyResolution = m_FitStdDev/m_FitMean;

    const float meanError(m_GaussianFit->GetParError(1));
    const float meanFracError(meanError / m_FitMean);
    const float stdDevError(std::fabs(m_GaussianFit->GetParError(2) / (2 * std::pow(m_FitStdDev,1.5))));
    const float stdDevFracError(stdDevError / m_FitStdDev);

    m_EnergyResolutionError = m_EnergyResolution * std::pow( (meanFracError*meanFracError) + (stdDevFracError*stdDevFracError) ,0.5);
}

//===========================================

template <class T>
std::string ResolutionContainer::NumberToString(T Number)
{
    std::ostringstream ss;
    ss << Number;
    return ss.str();
}

