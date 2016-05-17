/**
 *  @file
 *
 *  @brief
 *
 *  $Log: $
 */

#include "TApplication.h"
#include "TChain.h"
#include "TCanvas.h"
#include "TF1.h"
#include "TFitResult.h"
#include "TGraphErrors.h"
#include "TH2F.h"
#include "TLegend.h"
#include "TROOT.h"

#include <limits>
#include <math.h>
#include <sstream>
#include <vector>

/**
 *  @brief IsotropyOfDetector class
 */
class IsotropyOfDetector
{
public:
    /**
     *   @brief Constructor
     */
    IsotropyOfDetector();

    /**
     *   @brief Destructor 
     */
    ~IsotropyOfDetector();

    /**
     *   @brief Create plots showing isotropy of detector
     */
    void Process();

    // Inputs set by parsing command line
    std::string      m_RootFileNames;  ///< Input root file names
    float            m_TrueEnergy;     ///< Monte Carlo energy of simulated events
    std::string      m_OutputPath;     ///< Folder to send output plots to
    std::string      m_Info;           ///< Plot mean or resultion

private:
    /**
     *   @brief
     */
    void Initialise();

    void FillHistograms();

    void ApplyFitsCosTheta();

    void MakePlots();

    template <class T>
    std::string NumberToString(T number);

    TChain             *m_pTChain;        ///< Chain of root files
    std::vector<float>  m_CosThetaBins;   ///< Cos theta bins
    TH2F               *m_hCosTheta;      ///< Cos theta energy distribution 
    std::vector<TH1F*>  m_CosThetaHVec;   ///< Vector of energy histrograms, one for each cos theta bin
    TGraphErrors       *m_gCosTheta;      ///< Mean cos theta energy distribution 
    std::vector<float>  m_PhiBins;        ///< Phi bins 
    TH2F               *m_hPhi;           ///< Phi energy distribution 
    std::vector<TH1F*>  m_PhiHVec;        ///< Vector of energy histrograms, one for each cos theta bin
    TGraphErrors       *m_gPhi;           ///< Mean phi energy distribution 
}; 

//========================================================
//========================================================

/**
  *  @brief  Parse the command line arguments, setting the application parameters
  * 
  *  @param  argc argument count
  *  @param  argv argument vector
  *  @param  isotropyOfDetector to receive the application parameters
  * 
  *  @return success
  */
bool ParseCommandLine(int argc, char *argv[], IsotropyOfDetector &isotropyOfDetector);

//========================================================

int main(int argc, char **argv)
{
    TApplication *pTApplication = NULL;

    gROOT->SetBatch();

    try
    {
        IsotropyOfDetector isotropyOfDetector;

        if (!ParseCommandLine(argc, argv, isotropyOfDetector))
            return 1;

        pTApplication = new TApplication("MyTest", &argc, argv);

        isotropyOfDetector.Process();

        delete pTApplication;
    }
    catch (std::exception &exception)
    {
        std::cout << "Exception caught " << exception.what() << std::endl;
        delete pTApplication;
        return 1;
    }
    return 0;
}

//========================================================
//========================================================

IsotropyOfDetector::IsotropyOfDetector() : 
    m_RootFileNames(""),
    m_TrueEnergy(std::numeric_limits<float>::max()),
    m_OutputPath(""),
    m_Info("mean"),
    m_pTChain(NULL),
    m_hCosTheta(NULL),
    m_gCosTheta(NULL),
    m_hPhi(NULL),
    m_gPhi(NULL)
{
    const unsigned int nCosThetaBins(11);
    const float cosThetaBins[nCosThetaBins] = {0.f, 0.1f, 0.2f, 0.3f, 0.4f, 0.5f, 0.6f, 0.7f, 0.8f, 0.9f, 1.f};
    m_CosThetaBins.insert(m_CosThetaBins.begin(), cosThetaBins, cosThetaBins + nCosThetaBins);

    const unsigned int nPhiBins(11);
    const float phiBins[nPhiBins] = {-1.f*M_PI, -0.8f*M_PI, -0.6f*M_PI, -0.4f*M_PI, -0.2f*M_PI, 0.f, 0.2f*M_PI, 0.4f*M_PI, 0.6f*M_PI, 0.8f*M_PI, 1.f*M_PI};
    m_PhiBins.insert(m_PhiBins.begin(), phiBins, phiBins + nPhiBins);
}

//========================================================

IsotropyOfDetector::~IsotropyOfDetector()
{
}

//========================================================

void IsotropyOfDetector::Process()
{
    m_pTChain = new TChain("PfoAnalysisTree");
    m_pTChain->Add(m_RootFileNames.c_str());

    this->Initialise();
    this->FillHistograms();
    this->ApplyFitsCosTheta();
    this->MakePlots();
}

//========================================================
//========================================================

bool ParseCommandLine(int argc, char *argv[], IsotropyOfDetector &isotropyOfDetector)
{
    int c(0);

    while (((c = getopt(argc, argv, "a:b:c:d:e")) != -1) || (argc == 1))
    {
        switch (c)
        {
        case 'a':
            isotropyOfDetector.m_RootFileNames = optarg;
            break;
        case 'b':
            isotropyOfDetector.m_TrueEnergy = atof(optarg);
            break;
        case 'c':
            isotropyOfDetector.m_OutputPath = optarg;
            break;
        case 'd':
            isotropyOfDetector.m_Info = optarg;
            break;
        case 'e':
        default:
            std::cout << std::endl << "Calibrate " << std::endl
                      << "    -a        (mandatory, input file name(s), can include wildcards if string is in quotes)           " << std::endl
                      << "    -b value  (mandatory, true energy of photons being used for calibration)                          " << std::endl
                      << "    -c        (mandatory, output path to send results to)                                             " << std::endl
                      << "    -d        (mandatory, plot using either 'mean' or 'resolution')                                   " << std::endl
                      << std::endl;
            return false;
        }
    }
    return true;
}

//========================================================

void IsotropyOfDetector::Initialise()
{
    for (std::vector<float>::iterator itCos = m_CosThetaBins.begin(); itCos != m_CosThetaBins.end() - 1; itCos++)
    {
        const int position(itCos-m_CosThetaBins.begin());
        const float cosThetaStart(m_CosThetaBins.at(position));
        const float cosThetaEnd(m_CosThetaBins.at(position+1));
        std::string title = "StartCosTheta " + this->NumberToString(cosThetaStart) + " EndCosTheta " + this->NumberToString(cosThetaEnd);
        std::string name = "CosThetaPosition_" + NumberToString(position);
        const float maxEnergy(1.5f*m_TrueEnergy); 
        TH1F *pTH1F = new TH1F(name.c_str(), title.c_str(), 1000,0,maxEnergy);
        pTH1F->GetXaxis()->SetTitle("Pfo Energy [GeV]");
        pTH1F->GetYaxis()->SetTitle("Entries");
        m_CosThetaHVec.push_back(pTH1F);
    }

    for (std::vector<float>::iterator itPhi = m_PhiBins.begin(); itPhi != m_PhiBins.end() - 1; itPhi++)
    {
        const int position(itPhi-m_PhiBins.begin());
        const float phiStart(m_PhiBins.at(position));
        const float phiEnd(m_PhiBins.at(position+1));
        std::string title = "StartPhi " + this->NumberToString(phiStart) + " EndPhi " + this->NumberToString(phiEnd);
        std::string name = "PhiPosition_" + NumberToString(position);
        const float maxEnergy(1.5f*m_TrueEnergy);
        TH1F *pTH1F = new TH1F(name.c_str(), title.c_str(), 1000,0,maxEnergy);
        pTH1F->GetXaxis()->SetTitle("Pfo Energy [GeV]");
        pTH1F->GetYaxis()->SetTitle("Entries");
        m_PhiHVec.push_back(pTH1F);
    }

    std::string namePhi("HistogramPhiVsEReco");
    m_hPhi = new TH2F(namePhi.c_str(),namePhi.c_str(),1000,-M_PI,M_PI,1000,0,2);

    std::string nameCosTheta("HistogramCosThetaVsEReco");
    m_hCosTheta = new TH2F(nameCosTheta.c_str(),nameCosTheta.c_str(),1000,0.f,1.f,1000,0,2);
}

//========================================================

void IsotropyOfDetector::FillHistograms()
{
    float pfoEnergy(-1.f);
    std::vector<float> *pTargetCosTheta(NULL);
    std::vector<float> *pPfoTargetPx(NULL);
    std::vector<float> *pPfoTargetPy(NULL);

    m_pTChain->SetBranchAddress("pfoEnergyTotal",&pfoEnergy);
    m_pTChain->SetBranchAddress("pfoTargetCosTheta",&pTargetCosTheta);
    m_pTChain->SetBranchAddress("pfoTargetPx",&pPfoTargetPx);
    m_pTChain->SetBranchAddress("pfoTargetPy",&pPfoTargetPy);

    if (0 == m_pTChain->GetEntries()) return;

    for (unsigned int i = 0; i < m_pTChain->GetEntries(); i++)
    {
        m_pTChain->GetEntry(i);

        const float currentCosTheta(std::fabs(pTargetCosTheta->at(0)));
        const float currentTargetPx(pPfoTargetPx->at(0));
        const float currentTargetPy(pPfoTargetPy->at(0));
        const float currentPhi(atan2(currentTargetPy,currentTargetPx));

        for (std::vector<float>::iterator itCos = m_CosThetaBins.begin(); itCos != m_CosThetaBins.end() - 1; itCos++)
        {
            const int position(itCos-m_CosThetaBins.begin());
            const float cosThetaStart(m_CosThetaBins.at(position));
            const float cosThetaEnd(m_CosThetaBins.at(position+1));

            if (cosThetaStart <= currentCosTheta && cosThetaEnd > currentCosTheta)
            {
                m_CosThetaHVec.at(position)->Fill(pfoEnergy);
                m_hCosTheta->Fill(currentCosTheta,(pfoEnergy/m_TrueEnergy));
                break;
            }
        }

        for (std::vector<float>::iterator itPhi = m_PhiBins.begin(); itPhi != m_PhiBins.end() - 1; itPhi++)
        {
            const int position(itPhi-m_PhiBins.begin());
            const float phiStart(m_PhiBins.at(position));
            const float phiEnd(m_PhiBins.at(position+1));

            if (phiStart <= currentPhi && phiEnd > currentPhi)
            {
                m_PhiHVec.at(position)->Fill(pfoEnergy);
                m_hPhi->Fill(currentPhi,pfoEnergy);
                break;
            }
        }
    }
}

//========================================================

void IsotropyOfDetector::ApplyFitsCosTheta()
{
    std::string energy(this->NumberToString(m_TrueEnergy));
    std::string tgraphName("CosThetaDistribution_" + energy + "GeV");
    std::string tgraphTitle("CosThetaDistribution " + energy + "GeV");

    m_gCosTheta = new TGraphErrors(tgraphName.c_str(), tgraphTitle.c_str());

    for (std::vector<float>::iterator itCos = m_CosThetaBins.begin(); itCos != m_CosThetaBins.end() - 1; itCos++)
    {
        const int position(itCos-m_CosThetaBins.begin());
        TH1F *pTH1F(m_CosThetaHVec.at(position));
        const float cosThetaStart(m_CosThetaBins.at(position));
        const float cosThetaEnd(m_CosThetaBins.at(position+1));
        const float x((cosThetaStart + cosThetaEnd) * 0.5f);
        const float eX((cosThetaEnd - cosThetaStart) * 0.5f);

        std::string fitTitle = "GaussianFit" + this->NumberToString(position);
        const float maxEnergy(1.5f*m_TrueEnergy);
        TF1 *pGaussianFit = new TF1(fitTitle.c_str(),"gaus",0,1000);
        const float lowE(0.75*m_TrueEnergy);
        const float highE(1.25*m_TrueEnergy);
        pGaussianFit->SetParLimits(1,lowE,highE);
        pGaussianFit->SetParameter(1,m_TrueEnergy);

        const float amp(pTH1F->GetBinContent(pTH1F->GetMaximumBin()));
        pGaussianFit->SetParameter(0,amp);

        const float stdDev(pTH1F->GetRMS());
        pGaussianFit->SetParameter(2,stdDev);

        TFitResultPtr pTFitResultPtr = pTH1F->Fit(fitTitle.c_str(), "SM", "", 0, maxEnergy);

        bool isValidFit(pTFitResultPtr->IsValid());
        int fitQuality(pTFitResultPtr->CovMatrixStatus());
        bool isGoodFit(true);

        if (isValidFit != 1 || fitQuality != 3)
        {
            std::cout << "Poor fit quality for cos theta in range  " << cosThetaStart << " to " << cosThetaEnd << ".  Using raw histogram mean and error for plotting." << std::endl; 
            isGoodFit = false;
        }

        const float fitAmplitude(pGaussianFit->GetParameter(0));
        const float fitMean(pGaussianFit->GetParameter(1));
        const float fitMeanError(pGaussianFit->GetParError(1));
        const float fitStdDev(pGaussianFit->GetParameter(2));
        const float fitStdDevError(pGaussianFit->GetParError(2));
        const float fitChi2(pGaussianFit->GetChisquare());
        const float energyResolution(fitStdDev / fitMean);
        const float meanFracError(fitMeanError / fitMean);
        const float stdDevFracError(fitStdDevError / fitStdDev);
        const float energyResolutionError(energyResolution * std::pow( (meanFracError*meanFracError) + (stdDevFracError*stdDevFracError), 0.5));

        if (true)
        {
            TCanvas *pTCanvas = new TCanvas();
            pTH1F->Draw();
            pGaussianFit->SetLineColor(kRed);
            pGaussianFit->Draw("same");
            std::string name = this->NumberToString(m_TrueEnergy) + "GeV_Photons_" + this->NumberToString(position) + ".png";
            pTCanvas->SaveAs(name.c_str());
        }

        float y(-1.f);
        float eY(-1.f);

        if (isGoodFit)
        {
            if (m_Info == "mean")
            {
                y = fitMean / m_TrueEnergy;
                eY = fitMeanError / m_TrueEnergy;
            }
            else if (m_Info == "resolution")
            {
                y = energyResolution * 100;
                eY = energyResolutionError * 100;
            }
        }
        else
        {
            if (m_Info == "mean")
            {
                y = pTH1F->GetMean() / m_TrueEnergy;
                eY = pTH1F->GetMeanError() / m_TrueEnergy;
            }
            else if (m_Info == "resolution")
            {
                const float subEnergyResolution(pTH1F->GetStdDev()/pTH1F->GetMean());
                const float subMeanFracError(pTH1F->GetMeanError() / pTH1F->GetMean());
                const float subStdDevFracError(pTH1F->GetStdDevError() / pTH1F->GetStdDev());
                const float subEnergyResolutionError(subEnergyResolution * std::pow( (subMeanFracError*subMeanFracError) + (subStdDevFracError*subStdDevFracError), 0.5));
                y = subEnergyResolution * 100;
                eY = subEnergyResolutionError * 100;
            }
        }

        m_gCosTheta->SetPoint(m_gCosTheta->GetN(),x,y);
        m_gCosTheta->SetPointError(m_gCosTheta->GetN()-1,eX,eY);
    }
}

//========================================================

void IsotropyOfDetector::MakePlots()
{
    TH2F *pAxes;
    std::string plotName("Temp.C");

    if (m_Info == "mean")
    {
        const float minE(m_gCosTheta->GetHistogram()->GetMinimum());
        const float maxE(m_gCosTheta->GetHistogram()->GetMaximum());
        pAxes = new TH2F("mean","Mean Energy",100,0,1,100,minE,maxE);
        pAxes->GetYaxis()->SetTitle("E_{Reco} / E_{MC}");
        pAxes->GetXaxis()->SetTitle("|cos #theta|");
        plotName = "MeanPFOEnergy_CosTheta_" + this->NumberToString(m_TrueEnergy) + "_GeV_Photons.C";
    }
    else if (m_Info == "resolution")
    {
        const float minRes(m_gCosTheta->GetHistogram()->GetMinimum());
        const float maxRes(m_gCosTheta->GetHistogram()->GetMaximum());
        pAxes = new TH2F("resolution","Energy Resolution",100,0,1,100,minRes,maxRes);
        pAxes->GetYaxis()->SetTitle("RMS_{Gauss} / E_{Gauss} [%]");
        pAxes->GetXaxis()->SetTitle("|cos #theta|");
        plotName = "ResolutionPFOEnergy_CosTheta_" + this->NumberToString(m_TrueEnergy) + "_GeV_Photons.C";
    }

    TCanvas *pCanvas = new TCanvas();
    pCanvas->cd();

    pAxes->Draw();
    TLegend *pLegend = new TLegend(0.6, 0.6, 0.9, 0.9);
    const int col(4);
    m_gCosTheta->SetLineColor(col);
    m_gCosTheta->SetMarkerColor(col);
    m_gCosTheta->SetMarkerStyle();
    m_gCosTheta->Draw("PL same");
    std::string label = this->NumberToString(m_TrueEnergy) + " GeV Photons";
    pLegend->AddEntry(m_gCosTheta, label.c_str(), "lp");
    pLegend->Draw();
    pCanvas->SaveAs(plotName.c_str());
    delete pCanvas;

    TCanvas *pCanvas2 = new TCanvas();
    pCanvas2->cd();
    m_hCosTheta->Draw("COLZ");
    std::string name("ERecoVsCosTheta_" + this->NumberToString(m_TrueEnergy) + "GeV.C");
    pCanvas2->SaveAs(name.c_str());
    delete pCanvas2;
}

//========================================================

template <class T>
std::string IsotropyOfDetector::NumberToString(T number)
{
    std::ostringstream ss;
    ss << number;
    return ss.str();
}

//=======================================

