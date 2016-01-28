{
    gStyle->SetOptStat(0);

    TCanvas *pCanvasEj = new TCanvas();
    pCanvasEj->cd();

    TH2F *pAxesEj = new TH2F("axesEj","",300,0,300,650,0,6.5);
    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");
    pAxesEj->GetXaxis()->SetTitle("E_{j} [GeV]");
    pAxesEj->Draw();

    float jetEnergy[8] = {45.5,100.0,180.0,250.0,375.0,500.0,1000.0,1500.0};

    float jetEnergyError[8] = {0,0,0,0,0,0,0,0};

    float Variable_1_JER[8] = {{},{},{},{},{},{},{},{}};

    float Variable_1_JERError[8] = {{},{},{},{},{},{},{},{}};

    TLegend *pLegend = new TLegend(0.6, 0.6, 0.9, 0.9);
    TGraphErrors *pTGraphErrors_Variable_1 = new TGraphErrors(8,jetEnergy,Variable_1_JER,jetEnergyError,Variable_1_JERError);

    pTGraphErrors_Variable_1->SetLineColor(4);
    pTGraphErrors_Variable_1->SetMarkerColor(4);
    pTGraphErrors_Variable_1->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Variable_1, "High Energy Jets", "lp");

    pLegend->SetFillStyle(0);
    pLegend->Draw("same");
    pCanvasEj->SaveAs("JER_vs_JetEnergy_HighEnergyJets.pdf");
}
