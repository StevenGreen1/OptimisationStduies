#include "SingleDetectorContainer.h"

//===========================================

SingleDetectorContainer::SingleDetectorContainer(int detectorModel, std::vector<std::string> rootFiles) :
    m_DetectorModel(detectorModel),
    m_RootFiles(rootFiles),
    m_pTChain(NULL),
    m_hEnergy(NULL),
    m_FitMean(0.f),
    m_FitStdDev(0.f),
    m_FitAmplitude(0.f),
    m_FitChi2(0.f),
    m_EnergyResolution(0.f),
    m_EnergyResolutionError(0.f)
{
    m_pTChain = new TChain("PfoAnalysisTree");

    std::string histTitle = "PhotonEnergyResolution_DetectorModel" + IntToString(detectorModel);
    m_hEnergy = new TH1F(histTitle.c_str(),histTitle.c_str(),400,0,200);
    m_hEnergy->GetXaxis()->SetTitle("PFO Energy [GeV]");
    m_hEnergy->GetYaxis()->SetTitle("Entries");

    this->ChainRootFiles();
    this->MakeDistribution();
    this->CalculateResolution();
}

//===========================================

SingleDetectorContainer::~SingleDetectorContainer()
{
    delete m_hEnergy;
    delete m_pTChain;
}

//===========================================

void SingleDetectorContainer::ChainRootFiles()
{
    for (std::vector<std::string>::iterator it = m_RootFiles.begin() ; it != m_RootFiles.end(); ++it)
    {
        TString rootFile = *it;
        m_pTChain->Add(rootFile);
    }
}

//===========================================

void SingleDetectorContainer::MakeDistribution()
{
    float pfoEnergyTotal(0.f);
    int nPfoTargetsTotal(0), nPfoTargetsPhotons(0), nPfosTotal(0), nPfosPhotons(0);
    std::vector<float> *pfoTargetCosTheta(NULL);

    m_pTChain->SetBranchAddress("pfoEnergyTotal",&pfoEnergyTotal);
    m_pTChain->SetBranchAddress("nPfoTargetsTotal",&nPfoTargetsTotal);
    m_pTChain->SetBranchAddress("nPfoTargetsPhotons",&nPfoTargetsPhotons);
    m_pTChain->SetBranchAddress("nPfosTotal",&nPfosTotal);
    m_pTChain->SetBranchAddress("nPfosPhotons",&nPfosPhotons);
    m_pTChain->SetBranchAddress("pfoTargetCosTheta", &pfoTargetCosTheta);

    for (unsigned int i = 0; i < m_pTChain->GetEntries(); i++)
    {
        m_pTChain->GetEntry(i);
        float absCosTheta = std::fabs(pfoTargetCosTheta->at(0));

        if(nPfoTargetsTotal==1 and nPfoTargetsPhotons==1 and nPfosTotal==1 and nPfosPhotons==1 and absCosTheta<0.7)
        {
            m_hEnergy->Fill(pfoEnergyTotal);
        }    
    }
}

//===========================================

void SingleDetectorContainer::CalculateResolution()
{
    std::string fitTitle = "GaussianFit";
    m_GaussianFit = new TF1(fitTitle.c_str(),"gaus",0,200);
    m_hEnergy->Fit(fitTitle.c_str());
    m_FitAmplitude = m_GaussianFit->GetParameter(0);
    m_FitMean = m_GaussianFit->GetParameter(1);
    m_FitStdDev = m_GaussianFit->GetParameter(2);
    m_FitChi2 = m_GaussianFit->GetChisquare();
    m_EnergyResolution = m_FitStdDev/m_FitMean;

    float meanError = m_GaussianFit->GetParError(1);
    float meanFracError = meanError / m_FitMean;
    float stdDevError = std::fabs(m_GaussianFit->GetParError(2) / (2 * std::pow(m_FitStdDev,1.5)));
    float stdDevFracError = stdDevError / m_FitStdDev;

    m_EnergyResolutionError = m_EnergyResolution * std::pow( (meanFracError*meanFracError) + (stdDevFracError*stdDevFracError) ,0.5);
}

//===========================================

std::string SingleDetectorContainer::FloatToString(float a)
{
    std::stringstream ss;
    ss << a;
    std::string str = ss.str();
    return str;
}

//==========================================

std::string SingleDetectorContainer::IntToString(int a)
{
    std::stringstream ss;
    ss << a;
    std::string str = ss.str();
    return str;
}

//==========================================

