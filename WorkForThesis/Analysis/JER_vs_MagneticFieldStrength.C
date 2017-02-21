{
    gStyle->SetOptStat(0);

    TCanvas *pCanvasEj = new TCanvas();
    pCanvasEj->cd();

    TH2F *pAxesEj = new TH2F("axesEj","",1200,0.5,5.5,12000,0,6.5);
    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");
    pAxesEj->GetXaxis()->SetTitle("Magentic Field Strength [T]");
    pAxesEj->Draw();

    float xAxisVairable[9] = {1,1.5,2,2.5,3,3.5,4,4.5,5};

    float xAxisVairableError[9] = {0,0,0,0,0,0,0,0,0};

    float Jet_Energy_91GeV_JER[9] = {3.81173,3.75338,3.76262,3.70532,3.67285,3.6469,3.64717,3.75486,3.76242};

    float Jet_Energy_200GeV_JER[9] = {3.47664,3.22453,3.16111,3.04102,2.95643,2.88127,2.8029,2.82693,2.7952};

    float Jet_Energy_360GeV_JER[9] = {3.61798,3.47626,3.25132,3.13399,3.01075,2.84624,2.80579,2.72983,2.67988};

    float Jet_Energy_500GeV_JER[9] = {3.90015,3.60143,3.47668,3.27105,3.17437,2.97436,2.93853,2.87302,2.85326};

    float Jet_Energy_91GeV_JERError[9] = {0.0489853,0.0482354,0.0509861,0.0476177,0.0472005,0.0464093,0.0468704,0.0482544,0.0483515};

    float Jet_Energy_200GeV_JERError[9] = {0.0469174,0.0413299,0.040517,0.0389778,0.0378936,0.0368969,0.0359258,0.0362338,0.035827};

    float Jet_Energy_360GeV_JERError[9] = {0.0460823,0.0442773,0.0414122,0.0399178,0.038348,0.0363619,0.0357375,0.03477,0.0341337};

    float Jet_Energy_500GeV_JERError[9] = {0.0525323,0.0460174,0.0444234,0.0417959,0.0405606,0.0453691,0.0375471,0.0367101,0.0364576};

    TLegend *pLegend = new TLegend(0.6, 0.6, 0.9, 0.9);
    TGraphErrors *pTGraphErrors_Jet_Energy_91 = new TGraphErrors(9,xAxisVairable,Jet_Energy_91GeV_JER,xAxisVairableError,Jet_Energy_91GeV_JERError);

    pTGraphErrors_Jet_Energy_91->SetLineColor(4);
    pTGraphErrors_Jet_Energy_91->SetMarkerColor(4);
    pTGraphErrors_Jet_Energy_91->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_91, "45 GeV Jets", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_200 = new TGraphErrors(9,xAxisVairable,Jet_Energy_200GeV_JER,xAxisVairableError,Jet_Energy_200GeV_JERError);

    pTGraphErrors_Jet_Energy_200->SetLineColor(2);
    pTGraphErrors_Jet_Energy_200->SetMarkerColor(2);
    pTGraphErrors_Jet_Energy_200->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_200, "100 GeV Jets", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_360 = new TGraphErrors(9,xAxisVairable,Jet_Energy_360GeV_JER,xAxisVairableError,Jet_Energy_360GeV_JERError);

    pTGraphErrors_Jet_Energy_360->SetLineColor(6);
    pTGraphErrors_Jet_Energy_360->SetMarkerColor(6);
    pTGraphErrors_Jet_Energy_360->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_360, "180 GeV Jets", "lp");

    TGraphErrors *pTGraphErrors_Jet_Energy_500 = new TGraphErrors(9,xAxisVairable,Jet_Energy_500GeV_JER,xAxisVairableError,Jet_Energy_500GeV_JERError);

    pTGraphErrors_Jet_Energy_500->SetLineColor(1);
    pTGraphErrors_Jet_Energy_500->SetMarkerColor(1);
    pTGraphErrors_Jet_Energy_500->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Jet_Energy_500, "250 GeV Jets", "lp");

    pLegend->SetFillStyle(0);
    pLegend->Draw("same");
    pCanvasEj->SaveAs("JER_vs_MagneticFieldStrength.pdf");
}
