{
    gStyle->SetOptStat(0);

    TCanvas *pCanvasEj = new TCanvas();
    pCanvasEj->cd();

    TH2F *pAxesEj = new TH2F("axesEj","",1200,4.004,7.436,12000,0,6.5);
    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");
    pAxesEj->GetXaxis()->SetTitle("Number Of Nuclear Interation Lengths In The HCal [#lambda_{I}]");
    pAxesEj->Draw();

    float xAxisVairable[5] = {4.576,5.148,5.72,6.292,6.864};

    float xAxisVairableError[5] = {0,0,0,0,0};

    float Jet_Energy_91GeV_JER[5] = {3.71038,3.74718,3.68144,3.63755,3.67255};

    float Jet_Energy_200GeV_JER[5] = {3.01715,2.91707,2.90164,2.89516,2.81696};

    float Jet_Energy_360GeV_JER[5] = {3.04182,2.92116,2.8942,2.92063,2.82046};

    float Jet_Energy_500GeV_JER[5] = {3.27065,3.13523,2.9751,2.97863,2.98947};

    float Jet_Energy_91GeV_JERError[5] = {0.0476828,0.0481557,0.0473109,0.0467468,0.0471966};

    float Jet_Energy_200GeV_JERError[5] = {0.0386718,0.0373891,0.0371913,0.0371082,0.0361059};

    float Jet_Energy_360GeV_JERError[5] = {0.0387437,0.0372069,0.0368636,0.0392358,0.0359244};

    float Jet_Energy_500GeV_JERError[5] = {0.0440535,0.0400605,0.0381957,0.0380595,0.0381981};

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
    pCanvasEj->SaveAs("JER_vs_NumberOfNuclearInterationLengthsInTheHCal.pdf");
}
