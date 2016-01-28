#include<vector>
#include <iostream>
#include <fstream>

void ECALEndcapCorrectionFactorCalculator()
{
    std::string detectorModel("91");
    std::string recoVar("71");

    TString rootFilesToCompare("/r04/lc/sg568/HCAL_Optimisation_Studies/Calibration/Detector_Model_" + detectorModel + "/Reco_Stage_" + recoVar + "/MuonCalibration/RootFiles/*Photon*.root");
    std::string resultsFileName("ECALEndcapCorrectionFactorCalculator_DetectorModel" + detectorModel + "_RecoStage" + recoVar + ".txt");

    std::ofstream resultsFile;
    resultsFile.open (resultsFileName.c_str());

    float ecalTotalCaloHitEnergy(-1.f);
    std::vector<float> *pPfoTargetCosTheta(NULL);

    TChain *pTChain = new TChain("PfoAnalysisTree");
    pTChain->Add(rootFilesToCompare);
    pTChain->SetBranchAddress("ECalTotalCaloHitEnergy",&ecalTotalCaloHitEnergy);
    pTChain->SetBranchAddress("pfoTargetCosTheta",&pPfoTargetCosTheta);

    TCanvas *pTCanvas = new TCanvas("PhotonDistPic", "PhotonDistPic");
    TH2F *pPhotonDist = new TH2F("PhotonDist","PhotonDist",100,0,1,150,0,15);
    pPhotonDist->GetXaxis()->SetTitle("abs( cos (#theta_{#gamma}) )");
    pPhotonDist->GetYaxis()->SetTitle("ECal Calo Hit Energy [GeV]");

    for (int entry = 0; entry < pTChain->GetEntries(); entry++)
    {
//        std::cout << "Reading entry " << entry << std::endl;
        pTChain->GetEvent(entry);

        if (!pPfoTargetCosTheta->empty())
        {
//            std::cout << "Target cos theta : " << pPfoTargetCosTheta.at(0) << std::endl;
            pPhotonDist->Fill(TMath::Abs(pPfoTargetCosTheta->at(0)),ecalTotalCaloHitEnergy);
        }
    }

    TF1 *barrelFit = new TF1("BarrelFit","[0]",0.1,0.7);
    barrelFit->SetLineColor(kGray);
    barrelFit->SetLineWidth(4);

    TF1 *endcapFit = new TF1("EndcapFit","[0]",0.85,0.95);
    endcapFit->SetLineColor(kGray);
    endcapFit->SetLineWidth(4);

    pTCanvas->cd();
    pPhotonDist->Draw("COLZ");

    pPhotonDist->Fit(barrelFit,"QR+");
    pPhotonDist->Fit(endcapFit,"QR+");

    resultsFile << "For the barrel the best fit is : " << barrelFit->GetParameter(0) << std::endl;
    resultsFile << "For the endcap the best fit is : " << endcapFit->GetParameter(0) << std::endl;
    resultsFile << "ECALEndcapCorrectionFactorCalculator -> " << (barrelFit->GetParameter(0))/(endcapFit->GetParameter(0)) << std::endl;
    resultsFile.close();

    TString picName = "ECALEndcapCorrectionFactorCalculator_DetectorModel" + detectorModel + "_RecoStage" + recoVar + ".pdf";
    pTCanvas->SaveAs(picName);   
}
