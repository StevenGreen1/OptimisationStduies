#include "ResolutionContainer.h"

//===========================================

ResolutionContainer::ResolutionContainer(TFile *pTFile, int stageNumber, float trueEnergy, std::vector<std::string> rootFiles) :
    m_pTFile(pTFile),
    m_StageNumber(stageNumber),
    m_TrueEnergy(trueEnergy),
    m_RootFiles(rootFiles),
    m_hEnergy(NULL),
    m_BinNumber(50),
    m_MaxHistogramEnergy(0.f),
    m_FitPercentage(90.f),
    m_RMSFitRange(-1.f),
    m_FitStartPoint(0.f),
    m_FitEndPoint(0.f),
    m_GaussianFit(NULL),
    m_FitMean(0.f),
    m_FitStdDev(0.f),
    m_FitAmplitude(0.f),
    m_FitChi2(0.f),
    m_IdealChi2(0.f),
    m_EnergyResolution(0.f),
    m_EnergyResolutionError(0.f)
{
    float binMax = 2 * m_TrueEnergy;

    std::string fitTitle = "PFOEnergyHistogram_RecoStage" + IntToString(m_StageNumber) + "_Energy" + FloatToString(m_TrueEnergy) + "GeV";

    m_hEnergy = new TH1F(fitTitle.c_str(),fitTitle.c_str(),m_BinNumber,0,binMax);
    m_hEnergy->GetXaxis()->SetTitle("PFO Energy [GeV]");
    m_hEnergy->GetYaxis()->SetTitle("Entries");

    this->ReadData();
    this->RMSFitPercentageRange();
    this->Fit();
//    this->Draw();
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
    int nPfoTargetsTotal(0), nPfoTargetsNeutralHadrons(0), nPfosTotal(0), nPfosNeutralHadrons(0);

    for(std::vector<std::string>::iterator it = m_RootFiles.begin(); it != m_RootFiles.end(); ++it)
    {
        std::string rootFileName = *it;
        std::cout << rootFileName << std::endl;
        pTChain->Add(rootFileName.c_str());
    }

    pTChain->SetBranchAddress("pfoEnergyTotal",&pfoEnergyTotal);
    pTChain->SetBranchAddress("nPfoTargetsTotal",&nPfoTargetsTotal);
    pTChain->SetBranchAddress("nPfoTargetsNeutralHadrons",&nPfoTargetsNeutralHadrons);
    pTChain->SetBranchAddress("nPfosTotal",&nPfosTotal);
    pTChain->SetBranchAddress("nPfosNeutralHadrons",&nPfosNeutralHadrons);

    for (unsigned int i = 0; i < pTChain->GetEntries(); i++)
    {
        pTChain->GetEntry(i);

        if(nPfoTargetsTotal==1 and nPfoTargetsNeutralHadrons==1 and nPfosTotal==1 and nPfosNeutralHadrons==1)
        {
            m_hEnergy->Fill(pfoEnergyTotal);

            if(pfoEnergyTotal > m_MaxHistogramEnergy)
                m_MaxHistogramEnergy = pfoEnergyTotal;
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
    std::string pngPlotName = "SingleParticleEnergyResolution_RecoStage_" + IntToString(m_StageNumber) + "_Kaon0L_" + FloatToString(m_TrueEnergy) + "GeV.png";
    std::string dotCPlotName = "SingleParticleEnergyResolution_RecoStage_" + IntToString(m_StageNumber) + "_Kaon0L_" + FloatToString(m_TrueEnergy) + "GeV.C";
    pTCanvas->SaveAs(pngPlotName.c_str());
    pTCanvas->SaveAs(dotCPlotName.c_str());
}

//===========================================

void ResolutionContainer::Fit()
{
    std::string fitTitle = "GaussianFit_RecoStage" + IntToString(m_StageNumber) + "_Energy" + FloatToString(m_TrueEnergy) + "GeV";
    m_GaussianFit = new TF1(fitTitle.c_str(),"gaus",0,50);
    m_hEnergy->Fit(fitTitle.c_str());
    m_FitAmplitude = m_GaussianFit->GetParameter(0);
    m_FitMean = m_GaussianFit->GetParameter(1);
    m_FitStdDev = std::pow(m_GaussianFit->GetParameter(2),-0.5);
    m_FitChi2 = m_GaussianFit->GetChisquare();
    m_EnergyResolution = m_FitStdDev/m_FitMean;

    float meanError = m_GaussianFit->GetParError(1);
    float meanFracError = meanError / m_FitMean;
    float stdDevError = std::fabs(m_GaussianFit->GetParError(2) / (2 * std::pow(m_FitStdDev,1.5)));
    float stdDevFracError = stdDevError / m_FitStdDev;

    m_EnergyResolutionError = m_EnergyResolution * std::pow( (meanFracError*meanFracError) + (stdDevFracError*stdDevFracError) ,0.5);
}

//===========================================

void ResolutionContainer::RMSFitPercentageRange()
{
    static const float FLOAT_MAX(std::numeric_limits<float>::max());

    if (NULL == m_hEnergy)
        return;

    if (5 > m_hEnergy->GetEntries())
    {
        std::cout << m_hEnergy->GetName() << " (" << m_hEnergy->GetEntries() << " entries) - skipped" << std::endl;
        return;
    }

    // Calculate raw properties of distribution (ie rms100)
    float sum = 0., total = 0.;
    double sx = 0., sxx = 0.;
    const unsigned int nbins(m_hEnergy->GetNbinsX());

    for (unsigned int i = 0; i <= nbins; ++i)
    {
        const float binx(m_hEnergy->GetBinLowEdge(i) + (0.5 * m_hEnergy->GetBinWidth(i)));
        const float yi(m_hEnergy->GetBinContent(i));
        sx += yi * binx;
        sxx += yi * binx * binx;
        total += yi;
    }

    const float rawMean(sx / total);
    const float rawMeanSquared(sxx / total);
    const float rawRms(std::sqrt(rawMeanSquared - rawMean * rawMean));

    sum = 0.;
    unsigned int is0 = 0;

    //  The /10 comes from the fact that for rms 90 the start point for the fit must occur in the first 10% of the data.
    float frac = (1 - (m_FitPercentage/100.0));
    for (unsigned int i = 0; (i <= nbins) && (sum < total * frac); ++i)
    {
        sum += m_hEnergy->GetBinContent(i);
        is0 = i;
    }

    // Calculate truncated properties
    float rmsmin(FLOAT_MAX), mean(FLOAT_MAX), low(FLOAT_MAX);
    float high(0.f);

    for (unsigned int istart = 0; istart <= is0; ++istart)
    {
        double sumn = 0.;
        double csum = 0.;
        double sumx = 0.;
        double sumxx = 0.;
        unsigned int iend = 0;

        for (unsigned int i = istart; (i <= nbins) && (csum < (m_FitPercentage/100) * total); ++i)
        {
            const float binx(m_hEnergy->GetBinLowEdge(i) + (0.5 * m_hEnergy->GetBinWidth(i)));
            const float yi(m_hEnergy->GetBinContent(i));
            //csum is the sum of yi from istart and is used to stop the sum when this exceeds X% of data.
            csum += yi;

            if (sumn < (m_FitPercentage/100) * total)
            {
                // These variables define the final sums required once we have considered X% of data, anything else is 
                // continuously overwritten.
                sumn += yi;
                sumx += yi * binx;
                sumxx+= yi * binx * binx;
                iend = i;
            }
        }

        const float localMean(sumx / sumn);
        const float localMeanSquared(sumxx / sumn);
        // Standard deviation formula
        const float localRms(std::sqrt(localMeanSquared - localMean * localMean));

        if (localRms < rmsmin)
        {
            mean = localMean;
            if (istart==0)
            {
                low = 0;
                m_FitStartPoint = 0;
            }
            else
            {
                low = m_hEnergy->GetBinLowEdge(istart);
                m_FitStartPoint = m_hEnergy->GetBinLowEdge(istart) + (0.5 * m_hEnergy->GetBinWidth(istart));
            }
            
            high = m_hEnergy->GetBinLowEdge(iend);
            rmsmin = localRms;
            m_FitEndPoint = m_hEnergy->GetBinLowEdge(iend) + (0.5 * m_hEnergy->GetBinWidth(iend));
        }
    }
    
    m_RMSFitRange = rmsmin;
 
    //std::cout << m_hEnergy->GetName() << " (" << m_hEnergy->GetEntries() << " entries), rawrms: " << rawRms << ", rmsx: " << rmsmin << " (" << low << "-" << high << "), low_fit and high_fit " << " (" << m_FitStartPoint << "-" << m_FitEndPoint << "), << mean: " << mean << std::endl;
}

//==========================================

std::string ResolutionContainer::FloatToString(float a)
{
    std::stringstream ss;
    ss << a;
    std::string str = ss.str();
    return str;
}

//==========================================

std::string ResolutionContainer::IntToString(int a)
{
    std::stringstream ss;
    ss << a;
    std::string str = ss.str();
    return str;
}

//==========================================

