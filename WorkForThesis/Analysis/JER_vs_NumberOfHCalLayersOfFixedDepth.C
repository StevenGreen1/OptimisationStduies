{
    gStyle->SetOptStat(0);

    TCanvas *pCanvasEj = new TCanvas();
    pCanvasEj->cd();

    TH2F *pAxesEj = new TH2F("axesEj","",1200,30,66,12000,0,6.5);
    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");
    pAxesEj->GetXaxis()->SetTitle("Number Of HCal Layers Of Fixed Depth");
    pAxesEj->Draw();

    float xAxisVairable[5] = {36,42,48,54,60};

    float xAxisVairableError[5] = {0,0,0,0,0};

    float Jet_Energy_91GeV_JER[5] = {3.74875,3.6974,3.6469,3.71188,3.55531};

    float Jet_Energy_200GeV_JER[5] = {3.07079,2.91977,2.88127,2.79668,2.84442};

    float Jet_Energy_360GeV_JER[5] = {3.13096,3.01579,2.84624,2.83286,2.78186};

    float Jet_Energy_500GeV_JER[5] = {3.4203,3.14647,2.97436,2.99137,2.92701};

    float Jet_Energy_91GeV_JERError[5] = {0.0517574,0.0498738,0.0464093,0.0519564,0.0501794};

    float Jet_Energy_200GeV_JERError[5] = {0.0418269,0.039667,0.0368969,0.0385539,0.0401901};

    float Jet_Energy_360GeV_JERError[5] = {0.0438379,0.042069,0.0363619,0.038872,0.039468};

    float Jet_Energy_500GeV_JERError[5] = {0.0463091,0.0428259,0.0453691,0.041708,0.0397544};

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
    pCanvasEj->SaveAs("JER_vs_NumberOfHCalLayersOfFixedDepth.pdf");
}
