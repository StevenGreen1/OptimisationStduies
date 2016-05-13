#include "SingleDetectorContainer.h"

//===========================================

SingleDetectorContainer::SingleDetectorContainer(int detectorModel, std::vector<std::string> rootFiles) :
    m_DetectorModel(detectorModel),
    m_RootFiles(rootFiles),
    m_pTChain(NULL),
    m_hEnergy(NULL),
    m_hRawEnergy(NULL),
    m_FitMean(0.f),
    m_FitMeanError(0.f),
    m_FitStdDev(0.f),
    m_FitStdDevError(0.f),
    m_FitAmplitude(0.f),
    m_FitChi2(0.f),
    m_EnergyResolution(0.f),
    m_EnergyResolutionError(0.f),
    m_NCosThetaBins(13),
    m_pEVsCosTheta(NULL),
    m_pEResVsCosTheta(NULL),
    m_FitPercentage(90.f),
    m_FitStartPoint(-1.f),
    m_FitEndPoint(-1.f),
    m_RMSFitRange(-1.f)
{
    const unsigned int nCosThetaBins(13);
    const float cosThetaBinEdges[nCosThetaBins + 1] = {0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.925, 0.95, 0.975, 1.0};

    m_pEVsCosTheta = new TH1F("EnergyVsCosTheta", "Energy vs cos(#theta)", m_NCosThetaBins, cosThetaBinEdges);
    m_pEVsCosTheta->GetXaxis()->SetTitle("|cos(#theta)_{#gamma}|"); 
    m_pEVsCosTheta->GetYaxis()->SetTitle("E_{reco}");

    m_pEResVsCosTheta = new TH1F("EnergyResVsCosTheta", "Energy resolution vs cos(#theta)", m_NCosThetaBins, cosThetaBinEdges);
    m_pEResVsCosTheta->GetXaxis()->SetTitle("|cos(#theta_{#gamma})|"); 
    m_pEResVsCosTheta->GetYaxis()->SetTitle("#sigma_{reco} / E_{reco}");

    m_pTChain = new TChain("PfoAnalysisTree");

    std::string histTitle = "PhotonEnergyResolution_DetectorModel" + IntToString(detectorModel);
    m_hEnergy = new TH1F(histTitle.c_str(),histTitle.c_str(),400,0,200);
    m_hEnergy->GetXaxis()->SetTitle("PFO Energy [GeV]");
    m_hEnergy->GetYaxis()->SetTitle("Entries");

    std::string histTitleRaw = "PhotonEnergyResolution_DetectorModel" + IntToString(detectorModel) + "_RawDistribution";
    m_hRawEnergy = new TH1F(histTitleRaw.c_str(),histTitleRaw.c_str(),400,0,200);
    m_hRawEnergy->GetXaxis()->SetTitle("PFO Energy [GeV]");
    m_hRawEnergy->GetYaxis()->SetTitle("Entries");

    for (unsigned int iBin = 0; iBin < m_NCosThetaBins; ++iBin)
    {
        std::ostringstream oss;
        oss << iBin;
        std::string energyName("EnergyVsCosTheta_" + oss.str());
        m_EnergyVsCosThetaHists.push_back(new TH1F(energyName.c_str(), energyName.c_str(), 400, 0, 200));
    }

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
        std::cout << "Chaining root file : " << rootFile << std::endl;
        m_pTChain->Add(rootFile);
    }
    std::cout << "Number of chain entries " << m_pTChain->GetEntries() << std::endl;
}

//===========================================

void SingleDetectorContainer::MakeDistribution()
{
    float pfoEnergyTotal(0.f);
    int nPfoTargetsTotal(0), nPfoTargetsPhotons(0), nPfosTotal(0), nPfosPhotons(0);
    std::vector<float> *pfoTargetCosTheta(NULL);
    const unsigned int nCosThetaBins(13);
    const float cosThetaBinEdges[nCosThetaBins + 1] = {0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.925, 0.95, 0.975, 1.0};

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

        m_hRawEnergy->Fill(pfoEnergyTotal);

        int cosThetaBinNumber(0);
        for (unsigned int iBin = 1; iBin <= m_NCosThetaBins; ++iBin)
        {
            if (cosThetaBinEdges[iBin] > absCosTheta)
            {
                cosThetaBinNumber = iBin - 1;
                break;
            }
        }

        if(nPfoTargetsTotal==1 and nPfoTargetsPhotons==1)
        {
            m_EnergyVsCosThetaHists[cosThetaBinNumber]->Fill(pfoEnergyTotal);
        }

//        if(nPfoTargetsTotal==1 and nPfoTargetsPhotons==1 and nPfosTotal==1 and nPfosPhotons==1 and absCosTheta<0.7) <- Overkill for energy resolution, not bothered about pattern recognition really here.
        if(nPfoTargetsTotal==1 and nPfoTargetsPhotons==1 and absCosTheta<0.7)
        {
            m_hEnergy->Fill(pfoEnergyTotal);
        }    
    }

    for (unsigned int iBin = 0; iBin < m_NCosThetaBins; ++iBin)
    {
        TH1F *pTH1F = m_EnergyVsCosThetaHists[iBin];

        if (1 >= pTH1F->GetEntries())
            continue;

        float mean(0.f), rms(0.f), eMean(0.f), eRms(0.f), trueEnergy(100.f);
       
        if (!FitGaussian2(pTH1F, trueEnergy, mean, rms, eMean, eRms))
           continue;

        m_pEVsCosTheta->SetBinContent(iBin + 1, mean);
        m_pEVsCosTheta->SetBinError(iBin + 1, eMean);

        float res = rms / mean;
        float meanFracError = eMean / mean;
        float stdDevFracError = eRms / rms;
        float resError = res * std::pow( (meanFracError*meanFracError) + (stdDevFracError*stdDevFracError) ,0.5);

        m_pEResVsCosTheta->SetBinContent(iBin + 1, res);
        m_pEResVsCosTheta->SetBinError(iBin + 1, resError);
    }
}

//===========================================

bool SingleDetectorContainer::FitGaussian()
{
    const float expectedPeak(100.f);
/*    int centerBin(0);
    for (int i = 1; i <= m_hEnergy->GetNbinsX(); ++i)
    {
        if (m_hEnergy->GetBinLowEdge(i) > expectedPeak)
        {
            centerBin = i - 1;
            break;
        }
    }

    const float peakValue(m_hEnergy->GetBinContent(centerBin));
    const float threshold(peakValue / 20.f);

    float lowX(-10.f); int lowXBin(0);
    int nSuccessiveZeroes(0);
    float lastValue(std::numeric_limits<float>::max());
    for (int i = centerBin; i > 0; --i)
    {
        const float thisValue(m_hEnergy->GetBinContent(i));
        if (threshold > thisValue) ++nSuccessiveZeroes;
        else nSuccessiveZeroes = 0;

        if ((nSuccessiveZeroes > 2))// || (0.25f * thisValue > lastValue))
        {
            lowX = m_hEnergy->GetBinCenter(i);
            lowXBin = i;
            break;
        }
        lastValue = thisValue;
    }

    float highX(90.f); int highXBin(0);
    nSuccessiveZeroes = 0;
    lastValue = std::numeric_limits<float>::max();
    for (int i = centerBin; i <= m_hEnergy->GetNbinsX(); ++i)
    {
        const float thisValue(m_hEnergy->GetBinContent(i));
        if (threshold > thisValue) ++nSuccessiveZeroes;
        else nSuccessiveZeroes = 0;

        if ((nSuccessiveZeroes > 2))// || (0.25f * thisValue > lastValue))
        {
            highX =  m_hEnergy->GetBinCenter(i);
            highXBin = i;
            break;
        }
        lastValue = thisValue;
    }
*/

    this->RMSFitPercentageRange();
    m_GaussianFit = new TF1("Gaus", "gaus", m_FitStartPoint, m_FitEndPoint);
    m_GaussianFit->SetParameter(1, expectedPeak);
    m_GaussianFit->SetParameter(2, m_hEnergy->GetRMS());
    TFitResultPtr pTFitResultPtr = m_hEnergy->Fit(m_GaussianFit, "QS", "", m_FitStartPoint, m_FitEndPoint);

    m_FitMean = m_GaussianFit->GetParameter(1);
    m_FitStdDev = m_GaussianFit->GetParameter(2);
    m_FitMeanError = m_GaussianFit->GetParError(1);
    m_FitStdDevError = m_GaussianFit->GetParError(2);
    m_FitAmplitude = m_GaussianFit->GetParameter(0);

    const bool fitSuccess(pTFitResultPtr.Get()->IsValid());
    delete m_GaussianFit;
    std::cout << m_hEnergy->GetName() << ", m_FitMean " << m_FitMean << ", m_FitStdDev " << m_FitStdDev << " pass " << fitSuccess << " (lowX " << m_FitStartPoint << ", highX " << m_FitEndPoint << ") " << std::endl;
    return fitSuccess;
}

//===========================================

void SingleDetectorContainer::RMSFitPercentageRange2(TH1F *pTH1F, float &xLow, float &xHigh)
{
    static const float FLOAT_MAX(std::numeric_limits<float>::max());

    if (NULL == pTH1F)
        return;

    if (5 > pTH1F->GetEntries())
    {
        std::cout << pTH1F->GetName() << " (" << pTH1F->GetEntries() << " entries) - skipped" << std::endl;
        return;
    }

    float sum = 0., total = 0.;
    double sx = 0., sxx = 0.;
    const unsigned int nbins(pTH1F->GetNbinsX());

    for (unsigned int i = 0; i <= nbins; ++i)
    {
        const float binx(pTH1F->GetBinLowEdge(i) + (0.5 * pTH1F->GetBinWidth(i)));
        const float yi(pTH1F->GetBinContent(i));
        sx += yi * binx;
        sxx += yi * binx * binx;
        total += yi;
    }

    const float rawMean(sx / total);
    const float rawMeanSquared(sxx / total);
    const float rawRms(std::sqrt(rawMeanSquared - rawMean * rawMean));

    sum = 0.;
    unsigned int is0 = 0;

    float frac = (1 - (m_FitPercentage/100.0));
    for (unsigned int i = 0; (i <= nbins) && (sum < total * frac); ++i)
    {
        sum += pTH1F->GetBinContent(i);
        is0 = i;
    }

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
            const float binx(pTH1F->GetBinLowEdge(i) + (0.5 * pTH1F->GetBinWidth(i)));
            const float yi(pTH1F->GetBinContent(i));
            csum += yi;

            if (sumn < (m_FitPercentage/100) * total)
            {
                sumn += yi;
                sumx += yi * binx;
                sumxx+= yi * binx * binx;
                iend = i;
            }
        }

        const float localMean(sumx / sumn);
        const float localMeanSquared(sumxx / sumn);
        const float localRms(std::sqrt(localMeanSquared - localMean * localMean));

        if (localRms < rmsmin)
        {
            mean = localMean;
            if (istart==0)
            {
                low = 0;
                xLow = 0;
            }
            else
            {
                low = pTH1F->GetBinLowEdge(istart);
                xLow = pTH1F->GetBinLowEdge(istart) + (0.5 * pTH1F->GetBinWidth(istart));
            }

            high = pTH1F->GetBinLowEdge(iend);
            rmsmin = localRms;
            xHigh = pTH1F->GetBinLowEdge(iend) + (0.5 * pTH1F->GetBinWidth(iend));
        }
    }
}

//===========================================

void SingleDetectorContainer::RMSFitPercentageRange()
{
    static const float FLOAT_MAX(std::numeric_limits<float>::max());

    if (NULL == m_hEnergy)
        return;

    if (5 > m_hEnergy->GetEntries())
    {
        std::cout << m_hEnergy->GetName() << " (" << m_hEnergy->GetEntries() << " entries) - skipped" << std::endl;
        return;
    }

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

    float frac = (1 - (m_FitPercentage/100.0));
    for (unsigned int i = 0; (i <= nbins) && (sum < total * frac); ++i)
    {
        sum += m_hEnergy->GetBinContent(i);
        is0 = i;
    }

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
            csum += yi;

            if (sumn < (m_FitPercentage/100) * total)
            {
                sumn += yi;
                sumx += yi * binx;
                sumxx+= yi * binx * binx;
                iend = i;
            }
        }

        const float localMean(sumx / sumn);
        const float localMeanSquared(sumxx / sumn);
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
}

//===========================================

bool SingleDetectorContainer::FitGaussian2(TH1F *pTH1F, const float expectedPeak, float &mean, float &rms, float &eMean, float &eRms)
{
/*    int centerBin(0);
    for (int i = 1; i <= pTH1F->GetNbinsX(); ++i)
    {
        if (pTH1F->GetBinLowEdge(i) > expectedPeak)
        {
            centerBin = i - 1;
            break;
        }
    }

    const float peakValue(pTH1F->GetBinContent(centerBin));
    const float threshold(peakValue / 20.f);

    float lowX(-10.f); int lowXBin(0);
    int nSuccessiveZeroes(0);
    float lastValue(std::numeric_limits<float>::max());
    for (int i = centerBin; i > 0; --i)
    {
        const float thisValue(pTH1F->GetBinContent(i));
        if (threshold > thisValue) ++nSuccessiveZeroes;
        else nSuccessiveZeroes = 0;

        if ((nSuccessiveZeroes > 2))// || (0.25f * thisValue > lastValue))
        {
            lowX = pTH1F->GetBinCenter(i);
            lowXBin = i;
            break;
        }
        lastValue = thisValue;
    }

    float highX(90.f); int highXBin(0);
    nSuccessiveZeroes = 0;
    lastValue = std::numeric_limits<float>::max();
    for (int i = centerBin; i <= pTH1F->GetNbinsX(); ++i)
    {
        const float thisValue(pTH1F->GetBinContent(i));
        if (threshold > thisValue) ++nSuccessiveZeroes;
        else nSuccessiveZeroes = 0;

        if ((nSuccessiveZeroes > 2))// || (0.25f * thisValue > lastValue))
        {
            highX =  pTH1F->GetBinCenter(i);
            highXBin = i;
            break;
        }
        lastValue = thisValue;
    }
*/
    float xLow(0), xHigh(0);
    this->RMSFitPercentageRange2(pTH1F, xLow, xHigh);

    TF1 *pGaus = new TF1("Gaus", "gaus", xLow, xHigh);
    pGaus->SetParameter(1, expectedPeak);
    pGaus->SetParameter(2, pTH1F->GetRMS());
    TFitResultPtr pTFitResultPtr = pTH1F->Fit(pGaus, "QS", "", xLow, xHigh);

    mean = pGaus->GetParameter(1);
    rms = pGaus->GetParameter(2);
    eMean = pGaus->GetParError(1);
    eRms = pGaus->GetParError(2);
    int eventsInRange = pTH1F->Integral(xLow, xHigh);

    const bool fitSuccess(pTFitResultPtr.Get()->IsValid());
    delete pGaus;
    std::cout << pTH1F->GetName() << ", mean " << mean << ", rms " << rms << " pass " << fitSuccess << " (lowX " << xLow << ", highX " << xHigh << ") " << std::endl;
    return fitSuccess;
}        

//===========================================

void SingleDetectorContainer::CalculateResolution()
{
/*    std::string fitTitle = "GaussianFit";
    m_GaussianFit = new TF1(fitTitle.c_str(),"gaus",0,200);
    m_hEnergy->Fit(fitTitle.c_str());
    m_FitAmplitude = m_GaussianFit->GetParameter(0);
    m_FitMean = m_GaussianFit->GetParameter(1);
    m_FitStdDev = m_GaussianFit->GetParameter(2);
    m_FitChi2 = m_GaussianFit->GetChisquare();
    m_EnergyResolution = m_FitStdDev/m_FitMean;
*/
    this->FitGaussian();

    m_EnergyResolution = m_FitStdDev/m_FitMean;
    float meanFracError = m_FitMeanError / m_FitMean;
    float stdDevFracError = m_FitStdDevError / m_FitStdDev;

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

