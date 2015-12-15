{
    gStyle->SetOptStat(0);

    TCanvas *pCanvasEj = new TCanvas();
    pCanvasEj->cd();

    TH2F *pAxesEj = new TH2F("axesEj","",1200,0,110,12000,0,6.5);
    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");
    pAxesEj->GetXaxis()->SetTitle("HCal Cell Size [mm^{2}]");
    pAxesEj->Draw();

// 10^6 GeV
    float xAxisVairable[6] = {10,20,30,40,50,100};

    float xAxisVairableError[6] = {0,0,0,0,0,0};

    float Jet_Energy_91GeV_JER1[6] = {3.8816,3.72843,3.80701,3.76075,3.79037,3.89635};

    float Jet_Energy_200GeV_JER1[6] = {2.97386,3.0235,3.07541,3.11606,3.12319,3.42026};

    float Jet_Energy_360GeV_JER1[6] = {2.95202,3.07411,3.07959,3.14819,3.1911,3.49264};

    float Jet_Energy_500GeV_JER1[6] = {3.09093,3.12106,3.19677,3.25966,3.25167,3.66404};

    float Jet_Energy_91GeV_JERError1[6] = {0.0498832,0.0479147,0.0489246,0.0483301,0.0487107,0.0500727};

    float Jet_Energy_200GeV_JERError1[6] = {0.038117,0.0400016,0.0394186,0.0399396,0.0400311,0.0438387};

    float Jet_Energy_360GeV_JERError1[6] = {0.0376,0.040372,0.039414,0.0400987,0.0406452,0.0449513};

    float Jet_Energy_500GeV_JERError1[6] = {0.0394944,0.0417965,0.0408469,0.0416504,0.0415483,0.0470368};

    TLegend *pLegend = new TLegend(0.6, 0.6, 0.9, 0.9);
    TGraphErrors *pTGraphErrors1_Jet_Energy_91 = new TGraphErrors(6,xAxisVairable,Jet_Energy_91GeV_JER1,xAxisVairableError,Jet_Energy_91GeV_JERError1);

    pTGraphErrors1_Jet_Energy_91->SetLineColor(4);
    pTGraphErrors1_Jet_Energy_91->SetLineStyle(2);
    pTGraphErrors1_Jet_Energy_91->SetMarkerColor(4);
    pTGraphErrors1_Jet_Energy_91->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors1_Jet_Energy_91, "45 GeV Jets, Hadronic Energy Truncation 10^{6} GeV", "lp");

    TGraphErrors *pTGraphErrors1_Jet_Energy_200 = new TGraphErrors(6,xAxisVairable,Jet_Energy_200GeV_JER1,xAxisVairableError,Jet_Energy_200GeV_JERError1);

    pTGraphErrors1_Jet_Energy_200->SetLineColor(2);
    pTGraphErrors1_Jet_Energy_200->SetLineStyle(2);
    pTGraphErrors1_Jet_Energy_200->SetMarkerColor(2);
    pTGraphErrors1_Jet_Energy_200->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors1_Jet_Energy_200, "100 GeV Jets, Hadronic Energy Truncation 10^{6} GeV", "lp");

    TGraphErrors *pTGraphErrors1_Jet_Energy_360 = new TGraphErrors(6,xAxisVairable,Jet_Energy_360GeV_JER1,xAxisVairableError,Jet_Energy_360GeV_JERError1);

    pTGraphErrors1_Jet_Energy_360->SetLineColor(6);
    pTGraphErrors1_Jet_Energy_360->SetLineStyle(2);
    pTGraphErrors1_Jet_Energy_360->SetMarkerColor(6);
    pTGraphErrors1_Jet_Energy_360->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors1_Jet_Energy_360, "180 GeV Jets, Hadronic Energy Truncation 10^{6} GeV", "lp");

    TGraphErrors *pTGraphErrors1_Jet_Energy_500 = new TGraphErrors(6,xAxisVairable,Jet_Energy_500GeV_JER1,xAxisVairableError,Jet_Energy_500GeV_JERError1);

    pTGraphErrors1_Jet_Energy_500->SetLineColor(1);
    pTGraphErrors1_Jet_Energy_500->SetLineStyle(2);
    pTGraphErrors1_Jet_Energy_500->SetMarkerColor(1);
    pTGraphErrors1_Jet_Energy_500->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors1_Jet_Energy_500, "250 GeV Jets, Hadronic Energy Truncation 10^{6} GeV", "lp");

// 1 GeV

    float Jet_Energy_91GeV_JER[6] = {3.84955,3.65245,3.68144,3.57664,3.63403,3.8261};

    float Jet_Energy_200GeV_JER[6] = {2.92168,2.90008,2.90164,2.94619,2.9251,3.29337};

    float Jet_Energy_360GeV_JER[6] = {2.81705,2.83686,2.8942,2.99264,3.05344,3.67346};

    float Jet_Energy_500GeV_JER[6] = {2.85819,2.8913,2.9751,3.11762,3.27605,4.33888};

    float Jet_Energy_91GeV_JERError[6] = {0.0494713,0.0469383,0.0473109,0.0498393,0.0467016,0.0491699};

    float Jet_Energy_200GeV_JERError[6] = {0.0374482,0.0375495,0.0371913,0.0383172,0.0380687,0.0422122};

    float Jet_Energy_360GeV_JERError[6] = {0.0358809,0.0365083,0.0368636,0.0401995,0.0388918,0.046789};

    float Jet_Energy_500GeV_JERError[6] = {0.0365206,0.037342,0.0381957,0.0451166,0.0418598,0.0554402};

    TGraphErrors *pTGraphErrors_Jet_Energy_91 = new TGraphErrors(6,xAxisVairable,Jet_Energy_91GeV_JER,xAxisVairableError,Jet_Energy_91GeV_JERError);

    pTGraphErrors_Jet_Energy_91->SetLineColor(4);
    pTGraphErrors_Jet_Energy_91->SetMarkerColor(4);
    pTGraphErrors_Jet_Energy_91->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_91, "45 GeV Jets, Hadronic Energy Truncation 1 GeV", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_200 = new TGraphErrors(6,xAxisVairable,Jet_Energy_200GeV_JER,xAxisVairableError,Jet_Energy_200GeV_JERError);

    pTGraphErrors_Jet_Energy_200->SetLineColor(2);
    pTGraphErrors_Jet_Energy_200->SetMarkerColor(2);
    pTGraphErrors_Jet_Energy_200->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_200, "100 GeV Jets, Hadronic Energy Truncation 1 GeV", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_360 = new TGraphErrors(6,xAxisVairable,Jet_Energy_360GeV_JER,xAxisVairableError,Jet_Energy_360GeV_JERError);

    pTGraphErrors_Jet_Energy_360->SetLineColor(6);
    pTGraphErrors_Jet_Energy_360->SetMarkerColor(6);
    pTGraphErrors_Jet_Energy_360->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_360, "180 GeV Jets, Hadronic Energy Truncation 1 GeV", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_500 = new TGraphErrors(6,xAxisVairable,Jet_Energy_500GeV_JER,xAxisVairableError,Jet_Energy_500GeV_JERError);

    pTGraphErrors_Jet_Energy_500->SetLineColor(1);
    pTGraphErrors_Jet_Energy_500->SetMarkerColor(1);
    pTGraphErrors_Jet_Energy_500->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_500, "250 GeV Jets, Hadronic Energy Truncation 1 GeV", "lp");

    pLegend->SetFillStyle(0);
    pLegend->Draw("same");
    pCanvasEj->SaveAs("JER_vs_HCalCellSizeMHHHEComp.pdf");
}
