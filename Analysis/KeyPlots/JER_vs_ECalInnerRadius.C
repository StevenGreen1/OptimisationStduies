{
    gStyle->SetOptStat(0);

    TCanvas *pCanvasEj = new TCanvas();
    pCanvasEj->cd();

    TH2F *pAxesEj = new TH2F("axesEj","",1200,1008,2208,12000,0,6.5);
    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");
    pAxesEj->GetXaxis()->SetTitle("ECal Inner Radius [mm]");
    pAxesEj->Draw();

    float xAxisVairable[5] = {1208,1408,1608,1808,2008};

    float xAxisVairableError[5] = {0,0,0,0,0};

    float Jet_Energy_91GeV_JER[5] = {4.02663,3.79414,3.72287,3.69,3.68405};

    float Jet_Energy_200GeV_JER[5] = {3.52743,3.27195,3.01776,2.87939,2.8394};

    float Jet_Energy_360GeV_JER[5] = {3.68281,3.27146,3.04211,2.83474,2.78224};

    float Jet_Energy_500GeV_JER[5] = {3.83597,3.46806,3.1829,2.9734,2.87552};

    float Jet_Energy_91GeV_JERError[5] = {0.051747,0.0487592,0.0478432,0.0474208,0.0473443};

    float Jet_Energy_200GeV_JERError[5] = {0.0452124,0.0419377,0.0386796,0.0369062,0.0363936};

    float Jet_Energy_360GeV_JERError[5] = {0.0469081,0.0416687,0.0387475,0.0361062,0.0354375};

    float Jet_Energy_500GeV_JERError[5] = {0.0490143,0.0443132,0.0406696,0.0379927,0.0367421};

    TLegend *pLegend = new TLegend(0.6, 0.6, 0.9, 0.9);
    TGraphErrors *pTGraphErrors_Jet_Energy_91 = new TGraphErrors(5,xAxisVairable,Jet_Energy_91GeV_JER,xAxisVairableError,Jet_Energy_91GeV_JERError);

    pTGraphErrors_Jet_Energy_91->SetLineColor(4);
    pTGraphErrors_Jet_Energy_91->SetMarkerColor(4);
    pTGraphErrors_Jet_Energy_91->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_91, "45 GeV Jets", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_200 = new TGraphErrors(5,xAxisVairable,Jet_Energy_200GeV_JER,xAxisVairableError,Jet_Energy_200GeV_JERError);

    pTGraphErrors_Jet_Energy_200->SetLineColor(2);
    pTGraphErrors_Jet_Energy_200->SetMarkerColor(2);
    pTGraphErrors_Jet_Energy_200->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_200, "100 GeV Jets", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_360 = new TGraphErrors(5,xAxisVairable,Jet_Energy_360GeV_JER,xAxisVairableError,Jet_Energy_360GeV_JERError);

    pTGraphErrors_Jet_Energy_360->SetLineColor(6);
    pTGraphErrors_Jet_Energy_360->SetMarkerColor(6);
    pTGraphErrors_Jet_Energy_360->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_360, "180 GeV Jets", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_500 = new TGraphErrors(5,xAxisVairable,Jet_Energy_500GeV_JER,xAxisVairableError,Jet_Energy_500GeV_JERError);

    pTGraphErrors_Jet_Energy_500->SetLineColor(1);
    pTGraphErrors_Jet_Energy_500->SetMarkerColor(1);
    pTGraphErrors_Jet_Energy_500->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_500, "250 GeV Jets", "lp");

    pLegend->SetFillStyle(0);
    pLegend->Draw("same");
    pCanvasEj->SaveAs("JER_vs_ECalInnerRadius.pdf");
}
