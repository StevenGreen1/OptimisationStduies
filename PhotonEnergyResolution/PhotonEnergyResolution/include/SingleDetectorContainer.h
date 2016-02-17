#ifndef SINGLE_DETECTOR_CONTAINER_H
#define SINGLE_DETECTOR_CONTAINER_H

#include <iostream>
#include <sstream>
#include <stdexcept>
#include <vector>

#include "TCanvas.h"
#include "TChain.h"
#include "TF1.h"
#include "TH1F.h"

class SingleDetectorContainer
{
    private:
        /*
         * Private Variables
         */
        int            m_DetectorModel;
        std::vector<std::string>    m_RootFiles;
        TH1F          *m_hEnergy;
        TChain        *m_pTChain;
        TF1           *m_GaussianFit;
        float          m_FitMean;
        float          m_FitStdDev;
        float          m_FitAmplitude;
        float          m_FitChi2;
        float          m_IdealChi2;
        float          m_EnergyResolution;
        float          m_EnergyResolutionError;

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
};

#endif
