#include <iostream>
#include <cmath>
#include <string>
#include <sstream>

#include "TAxis.h"
#include "TCanvas.h"
#include "TColor.h"
#include "TFile.h"
#include "TGraph.h"
#include "TH1F.h"
#include "TLegend.h"
#include "TMultiGraph.h"
#include "TROOT.h"

std::string IntToString(int a);
int RootColour(int a);
std::string legendLabel(int a);

void MakePlots_JetsMean(int detectorModel)
{
    const int recoVarArray[] = {69,71,73,76};
//    const int recoVarArray[] = {51,76,59,43};// MHHHE 10^6
    //const int recoVarArray[] = {69,71,73,76};
    std::vector<int> recoVars (recoVarArray, recoVarArray + sizeof(recoVarArray) / sizeof(recoVarArray[0]) );

    const int energyArray[] = {91,200,360,500};
    std::vector<int> energies (energyArray, energyArray + sizeof(energyArray) / sizeof(energyArray[0]) );

    TCanvas *pTCanvas = new TCanvas("Name","Title",200,10,600,500);
    TH1F *pTH1F = new TH1F("Name","",1000,0,1000);
    pTH1F->GetXaxis()->SetTitle("True Energy [GeV]");
    pTH1F->GetXaxis()->SetRangeUser(0,550);
    pTH1F->GetYaxis()->SetTitle("Total PFO Energy [GeV]");
    pTH1F->GetYaxis()->SetRangeUser(0,550); 
    pTH1F->Draw("AXIS");

    TCanvas *pTCanvas2 = new TCanvas("Name2","Title2",200,10,600,500);
    TH1F *pTH1F2 = new TH1F("Name","",1000,0,1000);
    pTH1F2->GetXaxis()->SetTitle("True Energy [GeV]");
    pTH1F2->GetXaxis()->SetRangeUser(0,550);
    pTH1F2->GetYaxis()->SetTitle("Total PFO - True Energy [GeV]");
    pTH1F2->GetYaxis()->SetRangeUser(-25,5);
    pTH1F2->Draw("AXIS");

    TLegend *pTLegend = new TLegend(0.15,0.55,0.45,0.85);
    TLegend *pTLegend2 = new TLegend(0.15,0.15,0.45,0.45);

    for (std::vector<int>::iterator it = recoVars.begin(); it != recoVars.end(); ++it)
    {
        int counter = it - recoVars.begin();
        int recoVar = *it;

        TGraph *pTGraph = new TGraph();
        int rootColor = RootColour(recoVar);
        pTGraph->SetLineColor(rootColor);
        pTGraph->SetMarkerColor(rootColor);
//        pTGraph->GetXaxis()->SetTitle("True Energy [GeV]");
//        pTGraph->GetXaxis()->SetRangeUser(0,525);
//        pTGraph->GetYaxis()->SetTitle("Total PFO Energy [GeV]");
//        pTGraph->GetYaxis()->SetRangeUser(0,525);

        TGraph *pTGraph2 = new TGraph();
        pTGraph2->SetLineColor(rootColor);
        pTGraph2->SetMarkerColor(rootColor);
        pTGraph2->GetXaxis()->SetTitle("True Energy [GeV]");
        pTGraph2->GetXaxis()->SetRangeUser(0,525);
        pTGraph2->GetYaxis()->SetTitle("Total PFO - True Energy [GeV]");
        pTGraph2->GetYaxis()->SetRangeUser(-30,10);

        for (std::vector<int>::iterator iter = energies.begin(); iter != energies.end(); ++iter)
        {
            int energyCounter = iter - recoVars.begin();
            int energy = *iter;
            std::string rootFileToAdd = "/r06/lc/sg568/HCAL_Optimisation_Studies/AnalysePerformanceResults/Detector_Model_" + IntToString(detectorModel) + "/Reco_Stage_" + IntToString(recoVar) + "/Z_uds/" + IntToString(energy) + "GeV/AnalysePerformance_PandoraSettingsDefault_DetectorModel_" + IntToString(detectorModel) + "_Reco_Stage_" + IntToString(recoVar) + "_Z_uds_" + IntToString(energy) + "GeV.root";
            TFile *pTFile = new TFile(rootFileToAdd.c_str());
            TH1F *pTH1F = (TH1F*)pTFile->Get("fPFA_L7A");
            float meanReco(pTH1F->GetMean());
            float difference(meanReco-(float)(energy));
            pTFile->Close();
            delete pTFile, pTH1F;
            pTGraph->SetPoint(pTGraph->GetN(),energy,meanReco);
            pTGraph2->SetPoint(pTGraph2->GetN(),energy,difference);
        }
        pTCanvas->cd();
        pTGraph->DrawClone("PL");

        pTCanvas2->cd();
        pTGraph2->DrawClone("PL");

        pTLegend->AddEntry(pTGraph,legendLabel(recoVar).c_str(),"lp");
        pTLegend2->AddEntry(pTGraph,legendLabel(recoVar).c_str(),"lp");
    }

    pTCanvas->cd();
    pTLegend->Draw("same");
    pTCanvas2->cd();
    pTLegend2->Draw("same");

    std::string resultsName =  "True_vs_True_Jets_Detector_Model_" + IntToString(detectorModel) + "_TimingCut100ns_HadEnergyTruncScan.pdf";
    pTCanvas->SaveAs(resultsName.c_str());
    std::string resultsName2 =  "RecoMinusTrue_vs_True_Jets_Detector_Model_" + IntToString(detectorModel) + "_TimingCut100ns_HadEnergyTruncScan.pdf";
    pTCanvas2->SaveAs(resultsName2.c_str());
}

//==========

std::string legendLabel(int a)
{   
    if (a == 69)
        return "#splitline{Timing Cut in ECal and HCal 100 ns,}{Hadronic Energy Truncation 0.5 GeV}";
    else if (a == 70)
        return "#splitline{Timing Cut in ECal and HCal 100 ns,}{Hadronic Energy Truncation 0.75 GeV}";
    else if (a == 71)
        return "#splitline{Timing Cut in ECal and HCal 100 ns,}{Hadronic Energy Truncation 1 GeV}";
    else if (a == 72)
        return "#splitline{Timing Cut in ECal and HCal 100 ns,}{Hadronic Energy Truncation 1.5 GeV}";
    else if (a == 73)
        return "#splitline{Timing Cut in ECal and HCal 100 ns,}{Hadronic Energy Truncation 2 GeV}";
    else if (a == 74)
        return "#splitline{Timing Cut in ECal and HCal 100 ns,}{Hadronic Energy Truncation 5 GeV}";
    else if (a == 75)
        return "#splitline{Timing Cut in ECal and HCal 100 ns,}{Hadronic Energy Truncation 10 GeV}";
    else if (a == 76)
        return "#splitline{Timing Cut in ECal and HCal 100 ns,}{Hadronic Energy Truncation 10^{6} GeV}";
}

//==========

int RootColour(int a)
{
    int colour = 0;

    if (a==69)
        colour = 2; // Red <==
    else if (a==70)
        colour = 10001;  // Orange
    else if (a==71)
        colour = 10004; // Gold <==
    else if (a==72)
        colour = 8; // Green
    else if (a==73)
        colour = 10003; // Light Blue <==
    else if (a==74)
        colour = 4; // Blue
    else if (a==75)
        colour = 10002; // Violet
    else if (a==76)
        colour = 1; // Black
    return colour;
}

//==========

std::string IntToString(int a)
{
    std::stringstream ss;
    ss << a;
    std::string str = ss.str();
    return str;
}

