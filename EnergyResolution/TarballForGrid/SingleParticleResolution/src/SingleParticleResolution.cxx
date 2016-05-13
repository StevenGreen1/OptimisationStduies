/**
 *  @file   
 * 
 *  @brief  
 */

#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

#include "TLegend.h"
#include "TFile.h"
#include "TMultiGraph.h"
#include "TROOT.h"

#include "GroupedContainer.h"

std::string IntToString(int a);
std::string FloatToString(float a);
int RootColor(int a);
int RootMarker(int a);
std::string Label(int a);

int main(int argc, char **argv)
{
//    gROOT->ProcessLine(".x CLICStyleMod.C");

//    const float energiesArray[] = {1,2,3,4,5,6,7,8,9,10,15,20,25,30,35,40,45,50};
//    std::vector<float> energies (energiesArray, energiesArray + sizeof(energiesArray) / sizeof(energiesArray[0]) );

    std::string firstArguement = argv[1];
    int stageNumber = atoi(firstArguement.c_str());
    std::string runFileName = argv[2];
    std::string outputRootFileName = argv[3];

    TFile *pTFile = new TFile(outputRootFileName.c_str(), "recreate");

    std::vector<float> energies;
    std::vector<std::vector<std::string> > resultsFiles;

    std::ifstream runFile(runFileName.c_str());
    std::string line; 

    std::string searchString("Kaon0L_Energy_");
    std::string searchStringEntryEnd("===End_Entry===");

    float energy(-1);
    std::vector<std::string> activeRootFileList;

    while (std::getline(runFile, line))
    {
        if (line.find(searchString) != std::string::npos) 
        {
            std::string lineCopy = line;
            std::string energyString = lineCopy.erase(0,14);
            energy = atof(energyString.c_str());
            std::cout << "energy " << energy << std::endl;
        }

        else if (line.find(searchStringEntryEnd) != std::string::npos)
        {
            energies.push_back(energy);
            resultsFiles.push_back(activeRootFileList);
            std::cout << "push back energy " << energy << std::endl;
            energy = -1.f;
            activeRootFileList.clear();
        }

        else
        {
            activeRootFileList.push_back(line);
            std::cout << line << std::endl; 
        }
    }

    GroupedContainer *pGroupedContainer = new GroupedContainer(pTFile, stageNumber, energies, resultsFiles);

    pTFile->Write();
}

//============================================================

std::string Label(int a)
{
    if (a == 36)
        return "MHHHE 0.5, GeV TC: 10^{6} ns";
    else if (a == 37)
        return "MHHHE 0.75, GeV TC: 10^{6} ns";
    else if (a == 38)
        return "MHHHE 1 GeV, TC: 10^{6} ns";
    else if (a == 39)
        return "MHHHE 1.5 GeV, TC: 10^{6} ns";
    else if (a == 40)
        return "MHHHE 2 GeV, TC: 10^{6} ns";
    else if (a == 41)
        return "MHHHE 5 GeV, TC: 10^{6} ns";
    else if (a == 42)
        return "MHHHE 10 GeV, TC: 10^{6} ns";
}

//============================================================

int RootColor(int a)
{
    static const int rootColorArray[] = {1,2,3,4,6,7,8,9};
    return rootColorArray[(a % (sizeof(rootColorArray) / sizeof(int)))];
}

//============================================================

int RootMarker(int a)
{
    static const int rootMarkerArray[] = {20,21,22,23};
    if (a <= 7)
        return rootMarkerArray[0];
    else if (a <= 15)
        return rootMarkerArray[1];
    else if (a <= 23)
        return rootMarkerArray[2];
    else if (a <= 31)
        return rootMarkerArray[3];
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
