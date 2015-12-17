{
    gStyle->SetOptStat(0);

    TCanvas *pCanvasEj = new TCanvas();
    pCanvasEj->cd();

    pCanvasEj->Divide(2,2);

    pCanvasEj->cd(1);

    TH2F *pAxesEj = new TH2F("axesEj","",1200,0,110,12000,2.5,4.0);
    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");
    pAxesEj->GetXaxis()->SetTitle("No Truncation HCal Cell Size [mm^{2}]");
    pAxesEj->SetTitle("45 GeV Jets");
    pAxesEj->DrawClone("same");

    pCanvasEj->cd(2);
    pAxesEj->SetTitle("100 GeV Jets");
    pAxesEj->DrawClone("same");

    pCanvasEj->cd(3);
    pAxesEj->SetTitle("180 GeV Jets");
    pAxesEj->DrawClone("same");

    pCanvasEj->cd(4);
    pAxesEj->SetTitle("250 GeV Jets");
    pAxesEj->DrawClone("same");

    // No Truncation

    float xAxisVairable[6] = {10,20,30,40,50,100};

    float xAxisVairableError[6] = {0,0,0,0,0,0};

    float Jet_Energy_91GeV_JER[6] = {3.8816,3.72843,3.80701,3.76075,3.79037,3.89635};

    float Jet_Energy_200GeV_JER[6] = {2.97386,3.0235,3.07541,3.11606,3.12319,3.42026};

    float Jet_Energy_360GeV_JER[6] = {2.95202,3.07411,3.07959,3.14819,3.1911,3.49264};

    float Jet_Energy_500GeV_JER[6] = {3.09093,3.12106,3.19677,3.25966,3.25167,3.66404};

    float Jet_Energy_91GeV_JERError[6] = {0.0498832,0.0479147,0.0489246,0.0483301,0.0487107,0.0500727};

    float Jet_Energy_200GeV_JERError[6] = {0.038117,0.0400016,0.0394186,0.0399396,0.0400311,0.0438387};

    float Jet_Energy_360GeV_JERError[6] = {0.0376,0.040372,0.039414,0.0400987,0.0406452,0.0449513};

    float Jet_Energy_500GeV_JERError[6] = {0.0394944,0.0417965,0.0408469,0.0416504,0.0415483,0.0470368};

    TLegend *pLegend2 = new TLegend(0.1, 0.6, 0.6, 0.9);
    TGraphErrors *pTGraphErrors_Jet_Energy_91 = new TGraphErrors(6,xAxisVairable,Jet_Energy_91GeV_JER,xAxisVairableError,Jet_Energy_91GeV_JERError);

    pTGraphErrors_Jet_Energy_91->SetLineColor(1);
    pTGraphErrors_Jet_Energy_91->SetMarkerColor(1);
    pCanvasEj->cd(1);
    pTGraphErrors_Jet_Energy_91->Draw("pl,same");

    TGraphErrors *pTGraphErrors_Jet_Energy_200 = new TGraphErrors(6,xAxisVairable,Jet_Energy_200GeV_JER,xAxisVairableError,Jet_Energy_200GeV_JERError);

    pTGraphErrors_Jet_Energy_200->SetLineColor(1);
    pTGraphErrors_Jet_Energy_200->SetMarkerColor(1);
    pCanvasEj->cd(2);
    pTGraphErrors_Jet_Energy_200->Draw("pl,same");

    TGraphErrors *pTGraphErrors_Jet_Energy_360 = new TGraphErrors(6,xAxisVairable,Jet_Energy_360GeV_JER,xAxisVairableError,Jet_Energy_360GeV_JERError);

    pTGraphErrors_Jet_Energy_360->SetLineColor(1);
    pTGraphErrors_Jet_Energy_360->SetMarkerColor(1);
    pCanvasEj->cd(3);
    pTGraphErrors_Jet_Energy_360->Draw("pl,same");

    TGraphErrors *pTGraphErrors_Jet_Energy_500 = new TGraphErrors(6,xAxisVairable,Jet_Energy_500GeV_JER,xAxisVairableError,Jet_Energy_500GeV_JERError);

    pTGraphErrors_Jet_Energy_500->SetLineColor(1);
    pTGraphErrors_Jet_Energy_500->SetMarkerColor(1);
    pCanvasEj->cd(4);
    pTGraphErrors_Jet_Energy_500->Draw("pl,same");

    pLegend2->AddEntry(pTGraphErrors_Jet_Energy_500, "No Software Compensation", "p");

    // Optimised 

    float Jet_Energy_91GeV_JER2[6] = {3.76041,3.62514,3.68144,3.6621,3.75071,3.89806};

    float Jet_Energy_200GeV_JER2[6] = {2.85165,2.85699,2.90164,2.99719,3.01076,3.38944};

    float Jet_Energy_360GeV_JER2[6] = {2.73798,2.82388,2.8942,3.0058,3.01171,3.39641};

    float Jet_Energy_500GeV_JER2[6] = {2.7797,2.8985,2.9751,3.05676,3.07095,3.56517};

    float Jet_Energy_91GeV_JERError2[6] = {0.0483257,0.0465874,0.0473109,0.0487716,0.0482011,0.0500947};

    float Jet_Energy_200GeV_JERError2[6] = {0.036723,0.0371633,0.0371913,0.040588,0.0387945,0.0434436};

    float Jet_Energy_360GeV_JERError2[6] = {0.0348738,0.0363413,0.0368636,0.0411637,0.0383602,0.0434937};

    float Jet_Energy_500GeV_JERError2[6] = {0.0357018,0.0372184,0.0381957,0.0396481,0.0392391,0.0460569};

    TGraphErrors *pTGraphErrors_Jet_Energy_91_2 = new TGraphErrors(6,xAxisVairable,Jet_Energy_91GeV_JER2,xAxisVairableError,Jet_Energy_91GeV_JERError2);

    pTGraphErrors_Jet_Energy_91_2->SetLineColor(kGreen+2);
    pTGraphErrors_Jet_Energy_91_2->SetMarkerColor(kGreen+2);
    pCanvasEj->cd(1);
    pTGraphErrors_Jet_Energy_91_2->Draw("lp,same");

    TGraphErrors *pTGraphErrors_Jet_Energy_200_2 = new TGraphErrors(6,xAxisVairable,Jet_Energy_200GeV_JER2,xAxisVairableError,Jet_Energy_200GeV_JERError2);

    pTGraphErrors_Jet_Energy_200_2->SetLineColor(kGreen+2);
    pTGraphErrors_Jet_Energy_200_2->SetMarkerColor(kGreen+2);
    pCanvasEj->cd(2);
    pTGraphErrors_Jet_Energy_200_2->Draw("lp,same");

    TGraphErrors *pTGraphErrors_Jet_Energy_360_2 = new TGraphErrors(6,xAxisVairable,Jet_Energy_360GeV_JER2,xAxisVairableError,Jet_Energy_360GeV_JERError2);

    pTGraphErrors_Jet_Energy_360_2->SetLineColor(kGreen+2);
    pTGraphErrors_Jet_Energy_360_2->SetMarkerColor(kGreen+2);
    pCanvasEj->cd(3);
    pTGraphErrors_Jet_Energy_360_2->Draw("lp,same");

    TGraphErrors *pTGraphErrors_Jet_Energy_500_2 = new TGraphErrors(6,xAxisVairable,Jet_Energy_500GeV_JER2,xAxisVairableError,Jet_Energy_500GeV_JERError2);

    pTGraphErrors_Jet_Energy_500_2->SetLineColor(kGreen+2);
    pTGraphErrors_Jet_Energy_500_2->SetMarkerColor(kGreen+2);
    pCanvasEj->cd(4);
    pTGraphErrors_Jet_Energy_500_2->Draw("lp,same");
    pLegend2->AddEntry(pTGraphErrors_Jet_Energy_500_2, "Optimised HCal Hadronic Energy Truncation", "p");

    // Software Compensation 

    float Jet_Energy_91GeV_JER3[6] = {3.63,3.54,3.64,3.57,3.58,3.74};

    float Jet_Energy_200GeV_JER3[6] = {2.98,3.02,3.07,3.00,2.98,3.23};

    float Jet_Energy_360GeV_JER3[6] = {3.12,3.04,3.07,3.07,3.13,3.40};

    float Jet_Energy_500GeV_JER3[6] = {3.18,3.11,3.13,3.11,3.23,3.48};

    float Jet_Energy_91GeV_JERError3[6] = {0.f,0.f,0.f,0.f,0.f,0.f};

    float Jet_Energy_200GeV_JERError3[6] = {0.f,0.f,0.f,0.f,0.f,0.f};

    float Jet_Energy_360GeV_JERError3[6] = {0.f,0.f,0.f,0.f,0.f,0.f};

    float Jet_Energy_500GeV_JERError3[6] = {0.f,0.f,0.f,0.f,0.f,0.f};

    TLegend *pLegend = new TLegend(0.6, 0.6, 0.9, 0.9);
    TGraphErrors *pTGraphErrors_Jet_Energy_91_3 = new TGraphErrors(6,xAxisVairable,Jet_Energy_91GeV_JER3,xAxisVairableError,Jet_Energy_91GeV_JERError3);

    pTGraphErrors_Jet_Energy_91_3->SetLineColor(kAzure+7);
    pTGraphErrors_Jet_Energy_91_3->SetMarkerColor(kAzure+7);
    pCanvasEj->cd(1);
    pTGraphErrors_Jet_Energy_91_3->Draw("lp,same");

    TGraphErrors *pTGraphErrors_Jet_Energy_200_3 = new TGraphErrors(6,xAxisVairable,Jet_Energy_200GeV_JER3,xAxisVairableError,Jet_Energy_200GeV_JERError3);

    pTGraphErrors_Jet_Energy_200_3->SetLineColor(kAzure+7);
    pTGraphErrors_Jet_Energy_200_3->SetMarkerColor(kAzure+7);
    pCanvasEj->cd(2);
    pTGraphErrors_Jet_Energy_200_3->Draw("lp,same");

    TGraphErrors *pTGraphErrors_Jet_Energy_360_3 = new TGraphErrors(6,xAxisVairable,Jet_Energy_360GeV_JER3,xAxisVairableError,Jet_Energy_360GeV_JERError3);

    pTGraphErrors_Jet_Energy_360_3->SetLineColor(kAzure+7);
    pTGraphErrors_Jet_Energy_360_3->SetMarkerColor(kAzure+7);
    pCanvasEj->cd(3);
    pTGraphErrors_Jet_Energy_360_3->Draw("lp,same");

    TGraphErrors *pTGraphErrors_Jet_Energy_500_3 = new TGraphErrors(6,xAxisVairable,Jet_Energy_500GeV_JER3,xAxisVairableError,Jet_Energy_500GeV_JERError3);

    pTGraphErrors_Jet_Energy_500_3->SetLineColor(kAzure+7);
    pTGraphErrors_Jet_Energy_500_3->SetMarkerColor(kAzure+7);
    pCanvasEj->cd(4);
    pTGraphErrors_Jet_Energy_500_3->Draw("lp,same");
    pLegend2->AddEntry(pTGraphErrors_Jet_Energy_500_3, "Software Compensation (Post Reclustering)", "p");

    pLegend2->SetFillStyle(0);
    pLegend2->Draw("same");
    pCanvasEj->SaveAs("JER_vs_NoTruncationHCalCellSize.pdf");
}
