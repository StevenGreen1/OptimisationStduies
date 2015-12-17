{
    gStyle->SetOptStat(0);

    TCanvas *pCanvasEj = new TCanvas();
    pCanvasEj->cd();

    TH2F *pAxesEj = new TH2F("axesEj","",1200,0,110,12000,0,6.5);
    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");
    pAxesEj->GetXaxis()->SetTitle("Optimised HCal Cell Size [mm^{2}]");
    pAxesEj->Draw();

    float xAxisVairable[6] = {10,20,30,40,50,100};

    float xAxisVairableError[6] = {0,0,0,0,0,0};

    float Jet_Energy_91GeV_JER[6] = {3.76041,3.62514,3.68144,3.6621,3.75071,3.89806};

    float Jet_Energy_200GeV_JER[6] = {2.85165,2.85699,2.90164,2.99719,3.01076,3.38944};

    float Jet_Energy_360GeV_JER[6] = {2.73798,2.82388,2.8942,3.0058,3.01171,3.39641};

    float Jet_Energy_500GeV_JER[6] = {2.7797,2.8985,2.9751,3.05676,3.07095,3.56517};

    float Jet_Energy_91GeV_JERError[6] = {0.0483257,0.0465874,0.0473109,0.0487716,0.0482011,0.0500947};

    float Jet_Energy_200GeV_JERError[6] = {0.036723,0.0371633,0.0371913,0.040588,0.0387945,0.0434436};

    float Jet_Energy_360GeV_JERError[6] = {0.0348738,0.0363413,0.0368636,0.0411637,0.0383602,0.0434937};

    float Jet_Energy_500GeV_JERError[6] = {0.0357018,0.0372184,0.0381957,0.0396481,0.0392391,0.0460569};

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

    pLegend->SetFillStyle(0);
    pLegend->Draw("same");
    pCanvasEj->SaveAs("JER_vs_OptimisedHCalCellSize.pdf");
}
