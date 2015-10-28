#ifndef GROUPED_CONTAINER_H
#define GROUPED_CONTAINER_H

#include <iostream>
#include <string>

#include "TDirectory.h"
#include "TGraph.h"
#include "TFile.h"
#include "TH1F.h"
#include "TF1.h"
#include "TMath.h"
#include "TVector.h"

#include "ResolutionContainer.h"

class GroupedContainer
{
    private:
        /*
         * Private Variables
         */
        TFile *m_pTFile;
        int m_StageNumber;
        std::vector<float> m_TrueEnergies;
        std::vector<TH1F*> m_hPFOEnergy;
        std::vector<float> m_MeanPFOEnergies;
        std::vector<float> m_StdDevPFOEnergies;
        std::vector<float> m_EnergyResolutions;
        std::vector<float> m_EnergyResolutionErrors;
        TGraph *m_pResolutionPlot; 
        TGraph *m_pScaledResolutionPlot; 
        TGraph *m_pLinearityPlot; 
        TGraph *m_pLinearityDifferencePlot; 
        TF1 *m_pResolutionFit;
        TF1 *m_pLinearityFit;
        float m_StochasticTerm;
        float m_ConstantTerm;
        float m_NoiseTerm;
        float m_LinearityGradTerm;
        float m_LinearityIntTerm;

    public:
        /*
         * Default Constructor
         */
        GroupedContainer(TFile *pTFile, int stageNumber, std::vector<float> energies, std::vector<std::vector<std::string> > rootFiles);

        /*
         * Default Destructor
         */
        ~GroupedContainer();

        /*
         * Read data from all data files in m_FileNames
         */
        void AddContainer(ResolutionContainer *pResolutionContainer);

        /*
         * Make plot of PFO energy vs true energy 
         */
        void LinearityMakePlot();

        /*
         * Make plot of PFO energy - true energy vs true energy
         */
        void LinearityMakeDifferencePlot();

        /*
         * Fit the linearity plot 
         */
        void LinearityFit();

        /*
         * Draw the resolution plot
         */
        void LinearityDrawPlot();

        /*
         * Make the resolution plot
         */
        void ResolutionMakePlot();

        /*
         * Make the resolution scaled plot (resolution * sqrt(True Energy)
         */
        void ResolutionMakeScaledPlot();

        /*
         * Fit the resolution plot
         */
        void ResolutionFit();

        /*
         * Draw the resolution plot
         */
        void ResolutionDrawPlot();

        /*
         * Write plots to root file
         */
        void Write();

        /*
         * Tools
         */
        std::string IntToString(int a);

        /*
         * Get Parameter Functions
         */
        TGraph* GetLinearityPlot() { return m_pLinearityPlot; }
        TGraph* GetLinearityDifferencePlot() { return m_pLinearityDifferencePlot; }
        TGraph* GetResolutionPlot() { return m_pResolutionPlot; }
        TGraph* GetScaledResolutionPlot() { return m_pScaledResolutionPlot; }
        TF1* GetResolutionFit() { return m_pResolutionFit; }
        TF1* GetLinearityFit() { return m_pLinearityFit; }
};

#endif
