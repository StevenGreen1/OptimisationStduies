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

void plot(int energy, TCanvas *pTCanvas, TFile *pTFile, TLegend *pTLegend, int colour, int style, int recoVar);

void MakePlots(int detectorModel, int energy)
{
//    std::string rootFile = "/r06/lc/sg568/HCAL_Optimisation_Studies/AnalysePerformanceResults/Detector_Model_38/Reco_Stage_69/Z_uds/200GeV/AnalysePerformance_PandoraSettingsDefault_DetectorModel_38_Reco_Stage_69_Z_uds_200GeV.root";

 //   int energy(200);

//    const int recoVarArray[] = {46,71,54,38};// MHHHE 1
//    const int recoVarArray[] = {51,76,59,43};// MHHHE 10^6
//    const int recoVarArray[] = {69,70,71,72,73,74,75,76};
    const int recoVarArray[] = {69,71,73,76};
    std::vector<int> recoVars (recoVarArray, recoVarArray + sizeof(recoVarArray) / sizeof(recoVarArray[0]) );

//    TCanvas *pTCanvas1 = new TCanvas("Name1","Title1",200,10,600,500);
//    TCanvas *pTCanvas2 = new TCanvas("Name2","Title2",200,10,600,500);
//    TCanvas *pTCanvas3 = new TCanvas("Name3","Title3",200,10,600,500);
//    TCanvas *pTCanvas4 = new TCanvas("Name4","Title4",200,10,600,500);
    TCanvas *pTCanvas5 = new TCanvas("Name5","Title5",200,10,600,500);
//    TCanvas *pTCanvas6 = new TCanvas("Name6","Title6",200,10,600,500);
//    TCanvas *pTCanvas7 = new TCanvas("Name7","Title7",200,10,600,500);
//    TCanvas *pTCanvas8 = new TCanvas("Name8","Title8",200,10,600,500);

//    TMultiGraph *pTMultiGraph1 = new TMultiGraph();
//    TMultiGraph *pTMultiGraph2 = new TMultiGraph();
//    TMultiGraph *pTMultiGraph3 = new TMultiGraph();
//    TMultiGraph *pTMultiGraph4 = new TMultiGraph();

//    TLegend *pTLegend1 = new TLegend(0.15,0.55,0.45,0.85);
//    TLegend *pTLegend2 = new TLegend(0.55,0.55,0.85,0.85);
//    TLegend *pTLegend3 = new TLegend(0.15,0.55,0.45,0.85);
//    TLegend *pTLegend4 = new TLegend(0.55,0.55,0.85,0.85);
    TLegend *pTLegend5 = new TLegend(0.55,0.55,0.85,0.85);
//    TLegend *pTLegend6 = new TLegend(0.55,0.55,0.85,0.85);
//    TLegend *pTLegend7 = new TLegend(0.55,0.55,0.85,0.85);
//    TLegend *pTLegend8 = new TLegend(0.55,0.55,0.85,0.85);

    for (std::vector<int>::iterator it = recoVars.begin(); it != recoVars.end(); ++it)
    {
        int counter = it - recoVars.begin();
        int recoVar = *it;

        std::string rootFileToAdd = "/r06/lc/sg568/HCAL_Optimisation_Studies/AnalysePerformanceResults/Detector_Model_" + IntToString(detectorModel) + "/Reco_Stage_" + IntToString(recoVar) + "/Z_uds/" + IntToString(energy) + "GeV/AnalysePerformance_PandoraSettingsDefault_DetectorModel_" + IntToString(detectorModel) + "_Reco_Stage_" + IntToString(recoVar) + "_Z_uds_" + IntToString(energy) + "GeV.root";
        std::cout << rootFileToAdd << std::endl;
        TFile *pTFile = new TFile(rootFileToAdd.c_str());

/*        std::string graphName1 = "ResultsContainer_Stage" + IntToString(recoVar) + "/LinearityPlot_Stage" + IntToString(recoVar);
        std::string graphName2 = "ResultsContainer_Stage" + IntToString(recoVar) + "/ResolutionPlot_Stage" + IntToString(recoVar);
        std::string graphName3 = "ResultsContainer_Stage" + IntToString(recoVar) + "/LinearityDifferencePlot_Stage" + IntToString(recoVar);
        std::string graphName4 = "ResultsContainer_Stage" + IntToString(recoVar) + "/ScaledResolutionPlot_Stage" + IntToString(recoVar);

        TGraph *pTGraph1 = (TGraph*)pTFile->Get(graphName1.c_str());
        TGraph *pTGraph2 = (TGraph*)pTFile->Get(graphName2.c_str());
        TGraph *pTGraph3 = (TGraph*)pTFile->Get(graphName3.c_str());
        TGraph *pTGraph4 = (TGraph*)pTFile->Get(graphName4.c_str());
*/
        int rootColor = RootColour(recoVar);
/*
        pTGraph1->SetMarkerColor(rootColor);
        pTGraph1->SetLineColor(rootColor);
        pTGraph2->SetMarkerColor(rootColor);
        pTGraph2->SetLineColor(rootColor);
        pTGraph3->SetMarkerColor(rootColor);
        pTGraph3->SetLineColor(rootColor);
        pTGraph4->SetMarkerColor(rootColor);
        pTGraph4->SetLineColor(rootColor);

        pTLegend1->AddEntry(pTGraph1,legendLabel(recoVar).c_str(),"lp");
        pTLegend2->AddEntry(pTGraph2,legendLabel(recoVar).c_str(),"lp");
        pTLegend3->AddEntry(pTGraph3,legendLabel(recoVar).c_str(),"lp");
        pTLegend4->AddEntry(pTGraph4,legendLabel(recoVar).c_str(),"lp");

        pTMultiGraph1->Add(pTGraph1);
        pTMultiGraph2->Add(pTGraph2);
        pTMultiGraph3->Add(pTGraph3);
        pTMultiGraph4->Add(pTGraph4);
*/
        plot(energy,pTCanvas5,pTFile,pTLegend5,RootColour(recoVar),1,recoVar);
//        plot(energy,pTCanvas6,pTFile,pTLegend6,RootColour(recoVar),1,recoVar);
//        plot(energy,pTCanvas7,pTFile,pTLegend7,RootColour(recoVar),1,recoVar);

        pTFile->Close();

        delete pTFile;
    }
/*
    pTLegend1->SetFillStyle(0);
    pTLegend2->SetFillStyle(0);
    pTLegend3->SetFillStyle(0);
    pTLegend4->SetFillStyle(0);

    pTCanvas1->cd();
    pTMultiGraph1->Draw("APL");
    pTLegend1->Draw("same");
    pTMultiGraph1->GetYaxis()->SetTitle("Total PFO Energy [GeV]");
    pTMultiGraph1->GetXaxis()->SetTitle("True Energy [GeV]");
    gPad->Modified();

    pTCanvas2->cd();
    pTMultiGraph2->Draw("APL");
    pTLegend2->Draw("same");
    pTMultiGraph2->GetYaxis()->SetTitle("Energy Resolution #frac{#sigma_{Reco}}{E_{Reco}}");
    pTMultiGraph2->GetXaxis()->SetTitle("True Energy [GeV]");
    gPad->Modified();

    pTCanvas3->cd();
    pTMultiGraph3->Draw("APL");
    pTLegend3->Draw("same");
    pTMultiGraph3->GetYaxis()->SetTitle("Total PFO - True Energy [GeV]");
    pTMultiGraph3->GetXaxis()->SetTitle("True Energy [GeV]");
    gPad->Modified();

    pTCanvas4->cd();
    pTMultiGraph4->Draw("APL");
    pTLegend4->Draw("same");
    pTMultiGraph4->GetYaxis()->SetTitle("Scaled Energy Resolution #frac{#sigma_{Reco}}{E_{Reco}} #sqrt{E_{Reco}}");
    pTMultiGraph4->GetXaxis()->SetTitle("True Energy [GeV]");
    gPad->Modified();

    std::string resultsName1 =  "Reco_vs_True_Kaon0L_Detector_Model_" + IntToString(detectorModel) + "_HadronicEnergyScan_HadEnergyTrunc_1000000GeV.pdf";
    std::string resultsName1a = "Reco_vs_True_Kaon0L_Detector_Model_" + IntToString(detectorModel) + "_HadronicEnergyScan_HadEnergyTrunc_1000000GeV.C";
    std::string resultsName2 =  "EnergyResolution_vs_True_Kaon0L_Detector_Model_" + IntToString(detectorModel) + "_HadronicEnergyScan_HadEnergyTrunc_1000000GeV.pdf";
    std::string resultsName2a = "EnergyResolution_vs_True_Kaon0L_Detector_Model_" + IntToString(detectorModel) + "_HadronicEnergyScan_HadEnergyTrunc_1000000GeV.C";
    std::string resultsName3 =  "RecoMinusTrue_vs_True_Kaon0L_Detector_Model_" + IntToString(detectorModel) + "_HadronicEnergyScan_HadEnergyTrunc_1000000GeV.pdf";
    std::string resultsName3a = "RecoMinusTrue_vs_True_Kaon0L_Detector_Model_" + IntToString(detectorModel) + "_HadronicEnergyScan_HadEnergyTrunc_1000000GeV.C";
    std::string resultsName4 =  "ScaledEnergyResolution_vs_True_Kaon0L_Detector_Model_" + IntToString(detectorModel) + "_HadronicEnergyScan_HadEnergyTrunc_1000000GeV.pdf";
    std::string resultsName4a = "ScaledEnergyResolution_vs_True_Kaon0L_Detector_Model_" + IntToString(detectorModel) + "_HadronicEnergyScan_HadEnergyTrunc_1000000GeV.C";

    pTCanvas1->SaveAs(resultsName1.c_str());
    pTCanvas1->SaveAs(resultsName1a.c_str());
    pTCanvas2->SaveAs(resultsName2.c_str());
    pTCanvas2->SaveAs(resultsName2a.c_str());
    pTCanvas3->SaveAs(resultsName3.c_str());
    pTCanvas3->SaveAs(resultsName3a.c_str());
    pTCanvas4->SaveAs(resultsName4.c_str());
    pTCanvas4->SaveAs(resultsName4a.c_str());*/
}

//==========

void plot(int energy, TCanvas *pTCanvas, TFile *pTFile, TLegend *pTLegend, int colour, int style, int recoVar)
{
    pTCanvas->cd();
    std::string graphName = "fPFA_L7A";
    TH1F *pTH1F = (TH1F*)pTFile->Get(graphName.c_str());
    std::cout << pTH1F->GetMean() << std::endl;
    pTH1F->SetTitle("");

    pTH1F->Rebin(5);
    pTH1F->GetXaxis()->SetLimits(0, 2*energy); 
    double fraction = (2*energy/5000.f);
    int bins = floor(pTH1F->GetNbinsX()*fraction);
    pTH1F->SetBins(bins, 0, 2*energy);
    pTH1F->GetXaxis()->SetTitle("Jet Energy [GeV]");

    int maxBinContent = pTH1F->GetBinContent(pTH1F->GetMaximumBin());
    int maxNumberEntriesHist = ceil( (maxBinContent * 1.2) / 10 ) * 10;

    pTH1F->GetYaxis()->SetRangeUser(0,maxNumberEntriesHist);
    pTH1F->GetYaxis()->SetTitle("Entries");

    pTH1F->AddDirectory(kFALSE);
    pTH1F->SetMarkerColor(colour);
    pTH1F->SetFillStyle(3002);
    pTH1F->SetFillColor(colour);
    pTH1F->SetLineColor(colour);
    pTH1F->SetLineStyle(style);
    pTLegend->SetFillStyle(0);
    pTLegend->AddEntry(pTH1F->Clone(),legendLabel(recoVar).c_str(),"l");
//    std::string fitFunctionName = "GaussianFit_RecoStage" + IntToString(recoVar) + "_Energy" + IntToString(energy) + "GeV";
//    pTH1F->GetFunction(fitFunctionName.c_str())->Delete();
    if (recoVar == 69) // or recoVar == 46)
        pTH1F->DrawCopy("");
    else
        pTH1F->DrawCopy("same");
    pTLegend->Draw("same");
    gPad->Modified();

    if (recoVar == 76) // or recoVar == 38)
    {
        std::string resultsName1 = IntToString(energy) + "GeV_Detector_Model_38_HadronicEnergyScan_TimingCut100ns.C";
        std::string resultsName2 = IntToString(energy) + "GeV_Detector_Model_38_HadronicEnergyScan_TimingCut100ns.pdf";
        pTCanvas->SaveAs(resultsName1.c_str());
        pTCanvas->SaveAs(resultsName2.c_str());
    }
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

