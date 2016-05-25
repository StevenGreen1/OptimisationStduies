#include "GroupedContainer.h"

//===========================================

GroupedContainer::GroupedContainer(const int detectorModel, const int reconstructionVariant, TFile *pTFile, EnergyRootFileMap energyRootFileMap) :
    m_DetectorModel(detectorModel),
    m_ReconstructionVariant(reconstructionVariant),
    m_pTFile(pTFile),
    m_pResolutionPlot(NULL),
    m_pLinearityPlot(NULL),
    m_pFracLinearityPlot(NULL),
    m_MaxEnergy(0)
{
    std::string directoryName = "Resolution_DetectorModel_" + NumberToString(m_DetectorModel) + "_ReconstructionVariant_" + NumberToString(m_ReconstructionVariant);
    TDirectory *pTDirectory = m_pTFile->mkdir(directoryName.c_str());
    pTDirectory->cd();

    for (EnergyRootFileMap::const_iterator iter = energyRootFileMap.begin(), iterEnd = energyRootFileMap.end(); iter != iterEnd; ++iter)
    {
        const int energy(iter->first);
        if (energy > m_MaxEnergy) m_MaxEnergy = energy;
        std::vector<std::string> rootFiles(iter->second);
        ResolutionContainer *pResolutionContainer = new ResolutionContainer(m_DetectorModel, m_ReconstructionVariant, pTFile, energy, rootFiles);
        this->AddContainer(pResolutionContainer);
        delete pResolutionContainer;
    }

    this->LinearityMakePlot();
    this->FractionalLinearityMakePlot();
    this->ResolutionMakePlot();
    this->Write();
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
}

//===========================================

void GroupedContainer::LinearityMakePlot()
{
    TVectorT<float> tvecMeanPFOEnergy(m_MeanPFOEnergies.size(), &m_MeanPFOEnergies[0]);
    TVectorT<float> tvecTrueEnergy(m_TrueEnergies.size(), &m_TrueEnergies[0]);

    const float maxPlotEnergy(1.05f * m_MaxEnergy);
    m_pLinearityPlot = new TGraph (tvecTrueEnergy,tvecMeanPFOEnergy);
    m_pLinearityPlot->SetTitle("PFO Energy vs True Energy");
    m_pLinearityPlot->GetXaxis()->SetTitle("E_{MC}");
    m_pLinearityPlot->GetXaxis()->SetLimits(0,maxPlotEnergy);
    m_pLinearityPlot->GetXaxis()->SetRangeUser(0,maxPlotEnergy);
    m_pLinearityPlot->GetYaxis()->SetTitle("E_{Reco} [GeV]");
    m_pLinearityPlot->GetYaxis()->SetLimits(0,maxPlotEnergy);
    m_pLinearityPlot->GetYaxis()->SetRangeUser(0,maxPlotEnergy);
}

//===========================================

void GroupedContainer::FractionalLinearityMakePlot()
{
    FloatVector fractionalMean;
    for (FloatVector::iterator it = m_MeanPFOEnergies.begin(); it != m_MeanPFOEnergies.end(); it++)
    {
        const int position(it-m_MeanPFOEnergies.begin());
        const float meanPFOEnergy(m_MeanPFOEnergies.at(position));
        const float trueEnergy(m_TrueEnergies.at(position));
        const float fractionalEnergy(meanPFOEnergy/trueEnergy);
        fractionalMean.push_back(fractionalEnergy);
    }

    TVectorT<float> tvecFractionalEnergy(fractionalMean.size(), &fractionalMean[0]);
    TVectorT<float> tvecTrueEnergy(m_TrueEnergies.size(), &m_TrueEnergies[0]);

    const float maxPlotEnergy(1.05f * m_MaxEnergy);
    m_pFracLinearityPlot = new TGraph (tvecTrueEnergy,tvecFractionalEnergy);
    m_pFracLinearityPlot->SetTitle("Fractional PFO Energy vs True Energy");
    m_pFracLinearityPlot->GetXaxis()->SetTitle("E_{MC} [GeV]");
    m_pFracLinearityPlot->GetXaxis()->SetLimits(0,maxPlotEnergy);
    m_pFracLinearityPlot->GetXaxis()->SetRangeUser(0,maxPlotEnergy);
    m_pFracLinearityPlot->GetYaxis()->SetTitle("E_{Reco} / E_{MC}");
    m_pFracLinearityPlot->GetYaxis()->SetLimits(0,2);
    m_pFracLinearityPlot->GetYaxis()->SetRangeUser(0,2);
}

//===========================================

void GroupedContainer::ResolutionMakePlot()
{
    TVectorT<float> tvecEnergyResolution(m_EnergyResolutions.size(), &m_EnergyResolutions[0]);
    TVectorT<float> tvecTrueEnergy(m_TrueEnergies.size(), &m_TrueEnergies[0]);

    const float maxPlotEnergy(1.05f * m_MaxEnergy);
    m_pResolutionPlot = new TGraph (tvecTrueEnergy,tvecEnergyResolution);
    m_pResolutionPlot->SetTitle("Energy Resolution vs Jet Energy");
    m_pResolutionPlot->GetYaxis()->SetTitle("#sigma_{Reco} / E_{Reco}");
    m_pResolutionPlot->GetYaxis()->SetLimits(0,2);
    m_pResolutionPlot->GetYaxis()->SetRangeUser(0,2);
    m_pResolutionPlot->GetXaxis()->SetTitle("E_{MC} [GeV]");
    m_pResolutionPlot->GetXaxis()->SetLimits(0,maxPlotEnergy);
    m_pResolutionPlot->GetXaxis()->SetRangeUser(0,maxPlotEnergy);
}

//===========================================

void GroupedContainer::Write()
{
    std::string resolutionPlotName = "ResolutionPlot";
    m_pResolutionPlot->SetTitle(resolutionPlotName.c_str());
    m_pResolutionPlot->SetName(resolutionPlotName.c_str());
    m_pResolutionPlot->Write();

    std::string linearityPlotName = "LinearityPlot";
    m_pLinearityPlot->SetTitle(linearityPlotName.c_str());
    m_pLinearityPlot->SetName(linearityPlotName.c_str());
    m_pLinearityPlot->Write();

    std::string fracLinearityPlotName = "FractionalLinearityPlot";
    m_pFracLinearityPlot->SetTitle(fracLinearityPlotName.c_str());
    m_pFracLinearityPlot->SetName(fracLinearityPlotName.c_str());
    m_pFracLinearityPlot->Write();
}

//===========================================

template <class T>
std::string GroupedContainer::NumberToString(T Number)
{
    std::ostringstream ss;
    ss << Number;
    return ss.str();
}

//===========================================
