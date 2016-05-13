#ifndef RESOLUTION_CONTAINER_H
#define RESOLUTION_CONTAINER_H

#include <iostream>
#include <sstream>
#include <stdexcept>
#include <vector>

#include "TCanvas.h"
#include "TChain.h"
#include "TF1.h"
#include "TFitResult.h"
#include "TFile.h"
#include "TH1F.h"

class ResolutionContainer
{
    private:
        /*
         * Private Variables
         */
        TFile         *m_pTFile;
        int            m_StageNumber;
        float          m_TrueEnergy;
        std::vector<std::string>    m_RootFiles;
        TH1F          *m_hEnergy;
        int            m_BinNumber;
        float          m_MaxHistogramEnergy;
        float          m_FitPercentage;          // Percentage of data with narrowest rms to fit to
        float          m_RMSFitRange;            // Fit range
        float          m_FitStartPoint;          // Fit start
        float          m_FitEndPoint;            // Fit end
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
        ResolutionContainer(TFile *pTFile, int stageNumber, float energy, std::vector<std::string> rootFiles);

        /*
         * Default Destructor
         */
        ~ResolutionContainer();

        /*
         * Read data from all data files in m_RootFiles and fill PFOEnergy histogram
         */
        void ReadData();

        /*
         * Perform Gaussian fit on PFO energy histograms
         */
        void Fit();

        /*
         * Find fit range
         */
        void RMSFitPercentageRange();

        /*
         * Draw the histogram
         */
        void Draw();

        /*
         * Save histograms to TFile
         */

        void Save();

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
        float GetTrueEnergy(){ return m_TrueEnergy; }
        float GetMeanEnergy(){ return m_FitMean; }
        float GetStdDevEnergy(){ return m_FitStdDev; }
        TH1F* GetEnergyHist(){ return m_hEnergy; }
};

#endif
