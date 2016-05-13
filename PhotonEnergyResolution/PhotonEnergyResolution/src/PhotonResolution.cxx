/**
 *  @file   
 * 
 *  @brief  
 */

#include <fstream>
#include <iostream>
#include <sstream>
#include <string> 
#include <vector>

#include "TCanvas.h"
#include "TLegend.h"
#include "TFile.h"
#include "TGraphErrors.h"
#include "TROOT.h"

#include "SingleDetectorContainer.h"

std::string IntToString(int a);
std::string FloatToString(float a);
float DetectorModelLabel(int detModel);

int main(int argc, char **argv)
{
    std::string runFileName = argv[1];
    std::string outputRootFileName = argv[2];

    std::string rootFile("");
    std::string stringDetectorModel("");
    std::ifstream runFile(runFileName.c_str()); 

    std::map<int,std::vector<std::string> > fileInformation;

    while (runFile >> rootFile >> stringDetectorModel)
    {
        int detectorModel = std::atoi(stringDetectorModel.c_str());

        if (fileInformation.find(detectorModel) == fileInformation.end())
        {
            std::vector<std::string> rootFiles;
            rootFiles.push_back(rootFile);
            std::pair<int,std::vector<std::string> > elementToAdd(detectorModel,rootFiles);
            fileInformation.insert(elementToAdd);
        }

        else
        {
            fileInformation[detectorModel].push_back(rootFile);
        }
    }

    runFile.close();

    TFile *pTFile = new TFile(outputRootFileName.c_str(), "recreate");
    TDirectory *homeDir = gDirectory;

    TGraphErrors *PhotonResolution = new TGraphErrors();
    std::map<int, std::vector<std::string> >::iterator it;

    for (it = fileInformation.begin(); it != fileInformation.end(); ++it)
    {
        int detModel = it->first;
        std::vector<std::string> rootFiles = it->second;
        SingleDetectorContainer *pSingleDetectorContainer = new SingleDetectorContainer(detModel, rootFiles);
        int pointNumber = PhotonResolution->GetN();
        std::cout << pSingleDetectorContainer->GetResolution() << std::endl;
        std::cout << pSingleDetectorContainer->GetResolutionError() << std::endl;
        PhotonResolution->SetPoint(pointNumber,DetectorModelLabel(it->first),pSingleDetectorContainer->GetResolution());
        PhotonResolution->SetPointError(pointNumber,0,pSingleDetectorContainer->GetResolutionError());
        TH1F *pPhotonEnergyHist = pSingleDetectorContainer->GetEnergyHist();
        TH1F *pPhotonRawEnergyHist = pSingleDetectorContainer->GetRawEnergyHist();
        TH1F *pECosThetaHist = pSingleDetectorContainer->GetECosThetaHist();
        TH1F *pEResCosThetaHist = pSingleDetectorContainer-> GetEResCosThetaHist();

        std::string directoryName = "DetectorModel" + IntToString(detModel);
        TDirectory *pTDirectory = pTFile->mkdir(directoryName.c_str());
        pTDirectory->cd();
        pPhotonRawEnergyHist->Write();
        pPhotonEnergyHist->Write();
        pECosThetaHist->Write();
        pEResCosThetaHist->Write();
        std::cout << "Entries in hist : " << pPhotonEnergyHist->GetEntries() << std::endl;
        std::cout << "Entries in raw hist : " << pPhotonRawEnergyHist->GetEntries() << std::endl;
        delete pPhotonEnergyHist;
    }

//    TCanvas *pTCanvas =  new TCanvas();
//    PhotonResolution->Draw("");
//    pTCanvas->SaveAs("Test.png");

    homeDir->cd();
    PhotonResolution->SetTitle("Photon Energy Resolution");
    PhotonResolution->SetName("PhotonEnergyResolution");
    PhotonResolution->GetXaxis()->SetTitle("Number of ECal Layers");
    PhotonResolution->GetYaxis()->SetTitle("#sigma_{reco} / E_{reco}");
    PhotonResolution->Write();
}

//============================================================

float DetectorModelLabel(int detModel)
{
    std::map<int,float> Labels;
    Labels[96] = 30.f;
    Labels[97] = 26.f;
    Labels[98] = 20.f;
    Labels[99] = 16.f;
    return Labels[detModel];
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
