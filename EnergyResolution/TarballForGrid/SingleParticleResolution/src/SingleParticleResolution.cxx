/**
 *  @file   
 * 
 *  @brief  
 */

#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

#include "TFile.h"
#include "TROOT.h"

#include "GroupedContainer.h"

template <class T>
std::string NumberToString(T Number);

int main(int argc, char **argv)
{
    const int detectorModel(std::atoi(argv[1]));
    const int reconstructionVariant(std::atoi(argv[2]));
    const std::string runFileName = argv[3];
    const std::string outputRootFileName = argv[4];

    typedef std::map<const int,std::vector<std::string> > EnergyRootFileMap;
    EnergyRootFileMap energyRootFileMap;

    // Read in root file names
    std::ifstream runFile(runFileName.c_str());
    std::string energyString("");
    std::string rootFileString("");

    while (runFile >> energyString >> rootFileString)
    {
        const int energy = std::atoi(energyString.c_str());

        if (energyRootFileMap.find(energy) == energyRootFileMap.end())
        {
            std::vector<std::string> rootFiles;
            rootFiles.push_back(rootFileString);
            energyRootFileMap.insert(EnergyRootFileMap::value_type(energy, rootFiles));
        }
        else
        {
            energyRootFileMap[energy].push_back(rootFileString);
        }
    }
    runFile.close();


    TFile *pTFile = new TFile(outputRootFileName.c_str(), "recreate");
    TDirectory *homeDir = gDirectory;

    GroupedContainer *pGroupedContainer = new GroupedContainer(detectorModel, reconstructionVariant, pTFile, energyRootFileMap);

    pTFile->Write();
}

//============================================================

template <class T>
std::string NumberToString(T Number)
{
    std::ostringstream ss;
    ss << Number;
    return ss.str();
}

//============================================================
