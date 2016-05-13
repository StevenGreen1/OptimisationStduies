#ifndef SINGLE_DETECTOR_CONTAINER_H
#define SINGLE_DETECTOR_CONTAINER_H

#include <iostream>
#include <limits>
#include <sstream>
#include <stdexcept>
#include <vector>

#include "TCanvas.h"
#include "TChain.h"
#include "TF1.h"
#include "TH1F.h"
#include "TFitResult.h"

class SingleDetectorContainer
{
    private:
        /*
         * Private Variables
         */
        int            m_DetectorModel;
        std::vector<std::string>    m_RootFiles;
        TH1F          *m_hEnergy;
        TH1F          *m_hRawEnergy;
        TChain        *m_pTChain;
        TF1           *m_GaussianFit;
        float          m_FitMean;
        float          m_FitMeanError;
        float          m_FitStdDev;
        float          m_FitStdDevError;
        float          m_FitAmplitude;
        float          m_FitChi2;
        float          m_IdealChi2;
        float          m_EnergyResolution;
        float          m_EnergyResolutionError;
        float          m_FitPercentage;
        float          m_FitStartPoint;
        float          m_FitEndPoint;
        float          m_RMSFitRange;
        int            m_NCosThetaBins;
        TH1F          *m_pEVsCosTheta;
        TH1F          *m_pEResVsCosTheta;
        typedef std::vector<TH1F*> HistVector;
        HistVector     m_EnergyVsCosThetaHists;

    public:
        /*
         * Default Constructor
         */
        SingleDetectorContainer(int detectorModel, std::vector<std::string> rootFiles);

        /*
         * Default Destructor
         */
        ~SingleDetectorContainer();

        /*
         * Chain root files together
         */
        void ChainRootFiles();

        /*
         * Make PFO energy histogram
         */
        void MakeDistribution();

        /*
         * Calculate energy resolution
         */
        void CalculateResolution();

        /*
         * RMS90 range finding
         */
        void RMSFitPercentageRange();

        /*
         * RMS90 again for some reason....
         */
        void RMSFitPercentageRange2(TH1F *pTH1F, float &xLow, float &xHigh);

        /*
         * Gaussian fit to histogram
         */
        bool FitGaussian();

        /*
         * Don't ask....
         */
        bool FitGaussian2(TH1F *pTH1F, const float expectedPeak, float &mean, float &rms, float &eMean, float &eRms);
 
        /*
         * Tools
         */
        std::string FloatToString(float a);
        std::string IntToString(int a);

        /*
         * Get Parameter Functions
         */
        float GetResolution(){ return m_EnergyResolution; }
        float GetResolutionError(){ return m_EnergyResolutionError; }
        float GetMeanEnergy(){ return m_FitMean; }
        float GetStdDevEnergy(){ return m_FitStdDev; }
        TH1F* GetEnergyHist(){ return m_hEnergy; }
        TH1F* GetRawEnergyHist(){ return m_hRawEnergy; }
        TH1F* GetECosThetaHist(){ return m_pEVsCosTheta; }
        TH1F* GetEResCosThetaHist(){ return m_pEResVsCosTheta; }

};

#endif
