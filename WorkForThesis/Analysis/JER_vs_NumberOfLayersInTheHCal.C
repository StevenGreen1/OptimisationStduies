{
    gStyle->SetOptStat(0);

    TCanvas *pCanvasEj = new TCanvas();
    pCanvasEj->cd();

    TH2F *pAxesEj = new TH2F("axesEj","",1200,12,66,12000,0,6.5);
    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");
    pAxesEj->GetXaxis()->SetTitle("Number Of Layers In The HCal");
    pAxesEj->Draw();

    float xAxisVairable[8] = {18,24,30,36,42,48,54,60};

    float xAxisVairableError[8] = {0,0,0,0,0,0,0,0};

    float Jet_Energy_91GeV_JER[8] = {4.15954,3.81898,3.82021,3.88233,3.68123,3.6469,3.6965,3.70923};

    float Jet_Energy_200GeV_JER[8] = {3.35045,3.13551,2.96886,2.89729,2.92353,2.88127,2.89581,2.85293};

    float Jet_Energy_360GeV_JER[8] = {3.38347,3.07476,2.96963,2.93226,2.87282,2.84624,2.92408,2.88876};

    float Jet_Energy_500GeV_JER[8] = {3.5954,3.33187,3.19261,3.15088,3.06618,2.97436,3.02383,2.91974};

    float Jet_Energy_91GeV_JERError[8] = {0.053455,0.0490784,0.0490942,0.0498925,0.0473081,0.0464093,0.0501223,0.0476679};

    float Jet_Energy_200GeV_JERError[8] = {0.0429439,0.0401889,0.0380529,0.0371356,0.037472,0.0368969,0.0371166,0.036567};

    float Jet_Energy_360GeV_JERError[8] = {0.0430955,0.0391634,0.0378243,0.0373483,0.0365912,0.0363619,0.0372442,0.0367943};

    float Jet_Energy_500GeV_JERError[8] = {0.0459403,0.0425731,0.0407937,0.0402604,0.0391782,0.0453691,0.038637,0.0373071};

    TLegend *pLegend = new TLegend(0.6, 0.6, 0.9, 0.9);
    TGraphErrors *pTGraphErrors_Jet_Energy_91 = new TGraphErrors(8,xAxisVairable,Jet_Energy_91GeV_JER,xAxisVairableError,Jet_Energy_91GeV_JERError);

    pTGraphErrors_Jet_Energy_91->SetLineColor(4);
    pTGraphErrors_Jet_Energy_91->SetMarkerColor(4);
    pTGraphErrors_Jet_Energy_91->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_91, "45 GeV Jets", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_200 = new TGraphErrors(8,xAxisVairable,Jet_Energy_200GeV_JER,xAxisVairableError,Jet_Energy_200GeV_JERError);

    pTGraphErrors_Jet_Energy_200->SetLineColor(2);
    pTGraphErrors_Jet_Energy_200->SetMarkerColor(2);
    pTGraphErrors_Jet_Energy_200->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_200, "100 GeV Jets", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_360 = new TGraphErrors(8,xAxisVairable,Jet_Energy_360GeV_JER,xAxisVairableError,Jet_Energy_360GeV_JERError);

    pTGraphErrors_Jet_Energy_360->SetLineColor(6);
    pTGraphErrors_Jet_Energy_360->SetMarkerColor(6);
    pTGraphErrors_Jet_Energy_360->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_360, "180 GeV Jets", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_500 = new TGraphErrors(8,xAxisVairable,Jet_Energy_500GeV_JER,xAxisVairableError,Jet_Energy_500GeV_JERError);

    pTGraphErrors_Jet_Energy_500->SetLineColor(1);
    pTGraphErrors_Jet_Energy_500->SetMarkerColor(1);
    pTGraphErrors_Jet_Energy_500->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_500, "250 GeV Jets", "lp");

    pLegend->SetFillStyle(0);
    pLegend->Draw("same");
    pCanvasEj->SaveAs("JER_vs_NumberOfLayersInTheHCal.pdf");
}
