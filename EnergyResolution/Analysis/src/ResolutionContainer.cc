#include "ResolutionContainer.h"

//===========================================

ResolutionContainer::ResolutionContainer(int stageNumber, float trueEnergy, std::string rootFiles, std::string plotPath) :
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
    m_EnergyResolutionError(0.f),
    m_PlotPath(plotPath)
{
    float binMax = 2 * m_TrueEnergy;

    m_hEnergy = new TH1F("Name","Title",m_BinNumber,0,binMax);
    m_hEnergy->GetXaxis()->SetTitle("PFO Energy [GeV]");
    m_hEnergy->GetYaxis()->SetTitle("Entries");

    this->ReadData();
    this->RMSFitPercentageRange();
    this->Fit();
    this->Draw();
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

    pTChain->Add(m_RootFiles.c_str());
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

void ResolutionContainer::Draw()
{
    TCanvas *pTCanvas = new TCanvas("Name","Title",200,10,600,500);
    pTCanvas->cd();
    m_hEnergy->Draw();
    m_GaussianFit->Draw("same");
    std::string pngPlotName = m_PlotPath + "SingleParticleEnergyResolution_RecoStage_" + IntToString(m_StageNumber) + "_Kaon0L_" + FloatToString(m_TrueEnergy) + "GeV.png";
    std::string dotCPlotName = m_PlotPath + "SingleParticleEnergyResolution_RecoStage_" + IntToString(m_StageNumber) + "_Kaon0L_" + FloatToString(m_TrueEnergy) + "GeV.C";
    pTCanvas->SaveAs(pngPlotName.c_str());
    pTCanvas->SaveAs(dotCPlotName.c_str());
}

//===========================================

void ResolutionContainer::Fit()
{
    m_GaussianFit = new TF1("Gaussian","gaus",0,50);
    m_hEnergy->Fit("Gaussian");
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
/*
void ResolutionContainer::Fit()
{
    try
    {
        if (m_hEnergy->GetEntries() != 0)
        {
            // Fit Function
            m_GaussianFit = new TF1("m_GaussianFit","[0] * TMath::Exp( -0.5 * [2] * TMath::Power(x-[1],2) )");

            // Initial Param Guess
            float histAmplitude = m_hEnergy->GetBinContent(m_hEnergy->GetMaximumBin());
            float histMean = m_hEnergy->GetMean();
            float histStdDev = m_hEnergy->GetRMS();
            float histVarianceInverse = std::pow(histStdDev,-2);

            m_GaussianFit->SetParameters(0, histAmplitude);
            m_GaussianFit->SetParameters(1, histMean);
            m_GaussianFit->SetParameters(2, histVarianceInverse);
            m_GaussianFit->SetParLimits(2,0,100);

            // Perform Fit and Get Results
            TFitResultPtr pTFitResultPtr = m_hEnergy->Fit(m_GaussianFit, "SML", "", m_FitStartPoint, m_FitEndPoint);

            bool isValidFit = pTFitResultPtr->IsValid();
            int fitQuality = pTFitResultPtr->CovMatrixStatus();
            int count = 0;

            // Amplitude Checking
            bool isSensibleAmplitude (false);
            int binMax = m_hEnergy->GetMaximumBin();
            float histogramPeak = m_hEnergy->GetBinContent(binMax);

            if ( std::fabs( (m_GaussianFit->GetParameter(0) / histogramPeak) - 1) < 0.15)
                isSensibleAmplitude = true;

            // Mean Checking
            bool isSensibleMean (false);
            m_FitMean = m_GaussianFit->GetParameter(1);
            float deltaMeanRange = (m_FitEndPoint - m_FitStartPoint) * 1 / 10;
            float meanRangeLow = (m_FitStartPoint + m_FitEndPoint)/2 + deltaMeanRange;
            float meanRangeHigh = (m_FitStartPoint + m_FitEndPoint)/2 - deltaMeanRange;

            if ( m_FitMean > meanRangeLow && m_FitMean < meanRangeHigh)
                isSensibleMean = true;

            // Standard Deviation Checking
            bool isSensibleStdDev (false);
            m_FitStdDev = std::pow(m_GaussianFit->GetParameter(2),-0.5);
            float stdDevRangeLow = 0.9 * histStdDev;
            float stdDevRangeHigh = 1.1 * histStdDev;

            if ( m_FitStdDev > stdDevRangeLow && m_FitStdDev < stdDevRangeHigh)
                isSensibleStdDev = true;

            // Chi Sqaured Testing
            m_IdealChi2 = (m_BinNumber * ( m_FitEndPoint - m_FitStartPoint ) / m_MaxHistogramEnergy) - 3;
            m_FitChi2 = m_GaussianFit->GetChisquare();
            bool isSensibleChi2 (false);

            float chiPrecision = 0.5;

            // Not necessarily Gaussian at low energies (Novosibirsk), therefore weaker constraint.  Also leakage at high
            // energies means non Gaussian data. 
            if (m_TrueEnergy < 2 or m_TrueEnergy > 50 or std::fabs(m_FitChi2 - m_IdealChi2) < chiPrecision * m_IdealChi2)
                isSensibleChi2 = true;

            // While loop until fit converges
            while (isValidFit != 1 || fitQuality != 3 || !isSensibleAmplitude || !isSensibleMean || !isSensibleStdDev || !isSensibleChi2)
            {
                isSensibleAmplitude = false;
                isSensibleMean = false;
                isSensibleStdDev = false;
                isSensibleChi2 = false;

                m_GaussianFit->SetParameters(0, this->RandomRescaleFactor() * histAmplitude);
                m_GaussianFit->SetParameters(1, this->RandomRescaleFactor() * histMean);
                m_GaussianFit->SetParameters(2, this->RandomRescaleFactor() * histVarianceInverse);

                m_GaussianFit->SetParLimits(0, this->RandomLowerFraction() * this->RandomRescaleFactor() * histAmplitude, this->RandomUpperFraction() * this->RandomRescaleFactor() * histAmplitude);
                m_GaussianFit->SetParLimits(1, this->RandomLowerFraction() * this->RandomRescaleFactor() * histMean, this->RandomUpperFraction() * this->RandomRescaleFactor() * histMean);
                m_GaussianFit->SetParLimits(2, this->RandomLowerFraction() * this->RandomRescaleFactor() * histVarianceInverse, this->RandomUpperFraction() * this->RandomRescaleFactor() * histVarianceInverse);

                pTFitResultPtr = m_hEnergy->Fit(m_GaussianFit, "SML", "", m_FitStartPoint, m_FitEndPoint);

                isValidFit = pTFitResultPtr->IsValid();
                fitQuality = pTFitResultPtr->CovMatrixStatus();
                count++;

                // If statement for limiting maximum number of fits.  Turned off to get fits to converge fully
                if (count > 1000)
                    throw std::runtime_error("Fitting attempts exceeding maximum limit (1000).");

                if ( std::fabs( (m_GaussianFit->GetParameter(0) / histogramPeak) - 1) < 0.15)
                    isSensibleAmplitude = true;

                if ( m_GaussianFit->GetParameter(1) > meanRangeLow && m_GaussianFit->GetParameter(1) < meanRangeHigh)
                    isSensibleMean = true;

                m_FitStdDev = std::pow(m_GaussianFit->GetParameter(2),-0.5);

                if ( m_FitStdDev > stdDevRangeLow && m_FitStdDev < stdDevRangeHigh)
                    isSensibleStdDev = true;

                m_FitChi2 = m_GaussianFit->GetChisquare();

                if (m_TrueEnergy < 2 or m_TrueEnergy > 50 or std::fabs(m_FitChi2 - m_IdealChi2) < chiPrecision * m_IdealChi2)
                {
                    isSensibleChi2 = true;
                }

                chiPrecision = chiPrecision * 1.001;
            }

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
        
        else
        {
            std::cout << "Histogram is empty, no fit possible." << std::endl;
        }
    }
    
    catch (const std::runtime_error &e)
    {
        std::cout << "An exception occurred. " << e.what() << '\n';
    }
}
*/
//===========================================

const float ResolutionContainer::RandomSign()
{
    const float sign(((static_cast<float>(std::rand()) / static_cast<float>(RAND_MAX)) > 0.5f) ? 1.f : -1.f);
    return sign;
}

//===========================================

const float ResolutionContainer::RandomLowerFraction()
{
    const float lowerFraction = 1 - std::numeric_limits<float>::epsilon() - (0.5 * static_cast<float>(std::rand()) / static_cast<float>(RAND_MAX));
    return lowerFraction;
}

//===========================================

const float ResolutionContainer::RandomUpperFraction()
{
    const float upperFraction = 1 + std::numeric_limits<float>::epsilon() + (0.5 * static_cast<float>(std::rand()) / static_cast<float>(RAND_MAX));
    return upperFraction;
}

//===========================================

const float ResolutionContainer::RandomRescaleFactor()
{
    const float sign = this->RandomSign();
    const float rescaleFactor = 1 + (0.5 * sign * static_cast<float>(std::rand()) / static_cast<float>(RAND_MAX));
    return rescaleFactor;
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

