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
        typedef std::map<const int,std::vector<std::string> > EnergyRootFileMap;
        typedef std::vector<std::string> StringVector;
        typedef std::vector<float> FloatVector;
        typedef std::vector<int> IntVector;
        typedef std::vector<TH1F*> HistVector;

        const int m_DetectorModel;
        const int m_ReconstructionVariant;
        TFile *m_pTFile;
        EnergyRootFileMap m_energyRootFileMap;
        FloatVector m_TrueEnergies;
        HistVector m_hPFOEnergy;
        FloatVector m_MeanPFOEnergies;
        FloatVector m_StdDevPFOEnergies;
        FloatVector m_EnergyResolutions;
        FloatVector m_EnergyResolutionErrors;
        TGraph *m_pResolutionPlot; 
        TGraph *m_pLinearityPlot; 
        TGraph *m_pFracLinearityPlot; 
        int m_MaxEnergy;

    public:
        /*
         * Default Constructor
         */
        GroupedContainer(const int detectorModel, const int reconstructionVariant, TFile *pTFile, EnergyRootFileMap energyRootFileMap);

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
         * Make plot of PFO energy / true energy vs true energy
         */
        void FractionalLinearityMakePlot();

        /*
         * Make the resolution plot
         */
        void ResolutionMakePlot();

        /*
         * Write plots to root file
         */
        void Write();

        /*
         * Tools
         */
        template <class T>
        std::string NumberToString(T Number);

        /*
         * Get Parameter Functions
         */
        TGraph* GetResolutionPlot() { return m_pResolutionPlot; }
        TGraph* GetLinearityPlot() { return m_pLinearityPlot; }
        TGraph* GetFractionalLinearityPlot() { return m_pFracLinearityPlot; }
};

#endif
