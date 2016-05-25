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
        typedef std::vector<std::string> StringVector;
        typedef std::vector<float> FloatVector;

        const int      m_DetectorModel;
        const int      m_ReconstructionVariant;
        TFile         *m_pTFile;
        const int      m_TrueEnergy;
        StringVector   m_RootFiles;
        TH1F          *m_hEnergy;
        int            m_BinNumber;
        TF1           *m_GaussianFit;
        float          m_FitMean;
        float          m_FitStdDev;
        float          m_FitAmplitude;
        float          m_FitChi2;
        float          m_EnergyResolution;
        float          m_EnergyResolutionError;

    public:
        /*
         * Default Constructor
         */
        ResolutionContainer(const int detectorModel, const int reconstructionVariant, TFile *pTFile, const int energy, StringVector rootFiles);

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
        template <class T>
        std::string NumberToString(T Number);

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
