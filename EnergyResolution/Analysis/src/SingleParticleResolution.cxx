/**
 *  @file   
 * 
 *  @brief  
 */

#include <iostream>
#include <sstream>
#include <vector>

#include "TROOT.h"

#include "GroupedContainer.h"

std::string IntToString(int a);
std::string FloatToString(float a);

int main(int argc, char **argv)
{
    gROOT->ProcessLine(".x /var/clus/usera/sg568/StyleFile/CLICStyleMod.C");

    std::string pathForPlots = "/usera/sg568/ilcsoft_v01_17_07/JEREvolution/SingleParticleResolution/Plots/Stage43/";

    const float energiesArray[] = {1,2,3,4,5,6,7,8,9,10,15,20,25,30,35,40,45,50};
    std::vector<float> energies (energiesArray, energiesArray + sizeof(energiesArray) / sizeof(energiesArray[0]) );

    TCanvas *pTCanvas = new TCanvas();
    TCanvas *pTCanvas2 = new TCanvas();

    for (unsigned int stageNumber = 36; stageNumber <= 59; stageNumber++)
    {
        std::vector<std::string> resultsFiles;

        for (std::vector<float>::const_iterator it = energies.begin(); it != energies.end(); ++it)
        {
            std::string resultsFile = "/r06/lc/sg568/ReviewJER/RootFiles/Stage" + IntToString(stageNumber) + "/5x5_30x30/MarlinReco_ILD_o1_v06_GJN38_" + FloatToString(*it) +  "_GeV_Energy_130_pdg_SN_*_Default.root";
            resultsFiles.push_back(resultsFile);
        }

        GroupedContainer *pGroupedContainer = new GroupedContainer(stageNumber, energies, resultsFiles, pathForPlots);

        pTCanvas->cd();
        pGroupedContainer->GetLinearityPlot()->Draw("AP same");

        pTCanvas2->cd();
        pGroupedContainer->GetResolutionPlot()->Draw("AP same");
    }

    pTCanvas->SaveAs("Linearity.png");
    pTCanvas2->SaveAs("Resolution.png");
}

//============================================================

std::string IntToString(int a)
{
    std::stringstream ss;
    ss << a;
    std::string str = ss.str();
    return str;
}

//============================================================

std::string FloatToString(float a)
{
    std::stringstream ss;
    ss << a;
    std::string str = ss.str();
    return str;
}

//============================================================
