{
    gStyle->SetOptStat(0);

    TCanvas *pCanvasEj = new TCanvas();
    pCanvasEj->cd();

    TH2F *pAxesEj = new TH2F("axesEj","",1200,1,25,12000,0,6.5);
    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");
    pAxesEj->GetXaxis()->SetTitle("Silicon ECal Cell Size [mm^{2}]");
    pAxesEj->Draw();

    float xAxisVairable[6] = {3,5,7,10,15,20};

    float xAxisVairableError[6] = {0,0,0,0,0,0};

    float Jet_Energy_91GeV_JER[6] = {3.71643,3.63179,3.65898,3.81863,4.05563,4.46735};

    float Jet_Energy_200GeV_JER[6] = {2.93072,2.9336,2.94133,3.13555,3.60691,4.21006};

    float Jet_Energy_360GeV_JER[6] = {2.94181,2.90597,2.97897,3.30067,3.78615,4.40714};

    float Jet_Energy_500GeV_JER[6] = {3.11829,3.07604,3.18398,3.58679,4.15968,4.53885};

    float Jet_Energy_91GeV_JERError[6] = {0.0472942,0.0462171,0.046563,0.0485948,0.0516107,0.0568502};

    float Jet_Energy_200GeV_JERError[6] = {0.0375302,0.0396941,0.0396644,0.0401532,0.0461893,0.0539131};

    float Jet_Energy_360GeV_JERError[6] = {0.0395882,0.0414674,0.0401721,0.0545883,0.0483698,0.059345};

    float Jet_Energy_500GeV_JERError[6] = {0.0419215,0.0439165,0.0406602,0.0590143,0.0684402,0.0692329};

    TLegend *pLegend = new TLegend(0.6, 0.6, 0.9, 0.9);
    TGraphErrors *pTGraphErrors_Jet_Energy_91 = new TGraphErrors(6,xAxisVairable,Jet_Energy_91GeV_JER,xAxisVairableError,Jet_Energy_91GeV_JERError);

    pTGraphErrors_Jet_Energy_91->SetLineColor(4);
    pTGraphErrors_Jet_Energy_91->SetMarkerColor(4);
    pTGraphErrors_Jet_Energy_91->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_91, "45 GeV Jets", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_200 = new TGraphErrors(6,xAxisVairable,Jet_Energy_200GeV_JER,xAxisVairableError,Jet_Energy_200GeV_JERError);

    pTGraphErrors_Jet_Energy_200->SetLineColor(2);
    pTGraphErrors_Jet_Energy_200->SetMarkerColor(2);
    pTGraphErrors_Jet_Energy_200->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_200, "100 GeV Jets", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_360 = new TGraphErrors(6,xAxisVairable,Jet_Energy_360GeV_JER,xAxisVairableError,Jet_Energy_360GeV_JERError);

    pTGraphErrors_Jet_Energy_360->SetLineColor(6);
    pTGraphErrors_Jet_Energy_360->SetMarkerColor(6);
    pTGraphErrors_Jet_Energy_360->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_360, "180 GeV Jets", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_500 = new TGraphErrors(6,xAxisVairable,Jet_Energy_500GeV_JER,xAxisVairableError,Jet_Energy_500GeV_JERError);

    pTGraphErrors_Jet_Energy_500->SetLineColor(1);
    pTGraphErrors_Jet_Energy_500->SetMarkerColor(1);
    pTGraphErrors_Jet_Energy_500->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_500, "250 GeV Jets", "lp");

    // JM

    float Jet_Energy_91GeV_JER2[6] = {3.83198,3.71857,3.76248,3.81663,3.89675,4.24582};

    float Jet_Energy_200GeV_JER2[6] = {2.89635,2.95584,2.99462,3.06939,3.31222,3.63837};

    float Jet_Energy_360GeV_JER2[6] = {2.90833,2.80891,2.92188,3.09324,3.48797,3.82164};

    float Jet_Energy_500GeV_JER2[6] = {2.9144,2.9323,3.12089,3.22925,3.65169,4.02738};

    float Jet_Energy_91GeV_JERError2[6] = {0.0494872,0.0480225,0.0489708,0.049289,0.0504078,0.0548316};

    float Jet_Energy_200GeV_JERError2[6] = {0.0373234,0.0380899,0.0385897,0.0395894,0.0427072,0.0468852};

    float Jet_Energy_360GeV_JERError2[6] = {0.0372313,0.036077,0.0374048,0.0395983,0.0446515,0.0489231};

    float Jet_Energy_500GeV_JERError2[6] = {0.037435,0.0376649,0.0400873,0.0414792,0.0471195,0.0517438};

    TGraphErrors *pTGraphErrors_Jet_Energy_91_2 = new TGraphErrors(6,xAxisVairable,Jet_Energy_91GeV_JER2,xAxisVairableError,Jet_Energy_91GeV_JERError2);

    pTGraphErrors_Jet_Energy_91_2->SetLineColor(4);
    pTGraphErrors_Jet_Energy_91_2->SetLineStyle(2);
    pTGraphErrors_Jet_Energy_91_2->SetMarkerColor(4);
    pTGraphErrors_Jet_Energy_91_2->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_91_2, "JM : 45 GeV Jets", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_200_2 = new TGraphErrors(6,xAxisVairable,Jet_Energy_200GeV_JER2,xAxisVairableError,Jet_Energy_200GeV_JERError2);

    pTGraphErrors_Jet_Energy_200_2->SetLineColor(2);
    pTGraphErrors_Jet_Energy_200_2->SetLineStyle(2);
    pTGraphErrors_Jet_Energy_200_2->SetMarkerColor(2);
    pTGraphErrors_Jet_Energy_200_2->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_200_2, "JM : 100 GeV Jets", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_360_2 = new TGraphErrors(6,xAxisVairable,Jet_Energy_360GeV_JER2,xAxisVairableError,Jet_Energy_360GeV_JERError2);

    pTGraphErrors_Jet_Energy_360_2->SetLineColor(6);
    pTGraphErrors_Jet_Energy_360_2->SetLineStyle(2);
    pTGraphErrors_Jet_Energy_360_2->SetMarkerColor(6);
    pTGraphErrors_Jet_Energy_360_2->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_360_2, "JM : 180 GeV Jets", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_500_2 = new TGraphErrors(6,xAxisVairable,Jet_Energy_500GeV_JER2,xAxisVairableError,Jet_Energy_500GeV_JERError2);

    pTGraphErrors_Jet_Energy_500_2->SetLineColor(1);
    pTGraphErrors_Jet_Energy_500_2->SetLineStyle(2);
    pTGraphErrors_Jet_Energy_500_2->SetMarkerColor(1);
    pTGraphErrors_Jet_Energy_500_2->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_500_2, "JM : 250 GeV Jets", "lp");

    pLegend->SetFillStyle(0);
    pLegend->Draw("same");
    pCanvasEj->SaveAs("JER_vs_SiliconECalCellSize_JMComp.pdf");
}
