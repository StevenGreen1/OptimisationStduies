{
    gStyle->SetOptStat(0);

    TCanvas *pCanvasEj = new TCanvas();
    pCanvasEj->cd();

    TH2F *pAxesEj = new TH2F("axesEj","",300,0,300,650,0,6.5);
    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");
    pAxesEj->GetXaxis()->SetTitle("E_{j} [GeV]");
    pAxesEj->Draw();

    float jetEnergy[4] = {45.5,100.0,180.0,250.0};

    float jetEnergyError[4] = {0,0,0,0};

    float Variable_1_JER[4] = {3.67,2.85823,2.87901,3.05794};

    float Variable_2_JER[4] = {3.67166,2.91541,2.86234,3.02512};

    float Variable_3_JER[4] = {3.66999,3.12068,3.35563,3.75508};

    float Variable_4_JER[4] = {3.68914,3.02638,3.38325,3.79916};

    float Variable_1_JERError[4] = {0.0471638,0.0366349,0.0366701,0.039073};

    float Variable_2_JERError[4] = {0.0497581,0.0373679,0.0364577,0.0386536};

    float Variable_3_JERError[4] = {0.0471637,0.0421138,0.0427408,0.0479807};

    float Variable_4_JERError[4] = {0.0474098,0.0387902,0.0430926,0.0485439};

    TLegend *pLegend = new TLegend(0.6, 0.6, 0.9, 0.9);
    TGraphErrors *pTGraphErrors_Variable_1 = new TGraphErrors(4,jetEnergy,Variable_1_JER,jetEnergyError,Variable_1_JERError);

    pTGraphErrors_Variable_1->SetLineColor(4);
    pTGraphErrors_Variable_1->SetMarkerColor(4);
    pTGraphErrors_Variable_1->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Variable_1, "Steel HCal Absorber Material, QGSP_BERT", "lp");

    TGraphErrors *pTGraphErrors_Variable_2 = new TGraphErrors(4,jetEnergy,Variable_2_JER,jetEnergyError,Variable_2_JERError);

    pTGraphErrors_Variable_2->SetLineColor(2);
    pTGraphErrors_Variable_2->SetMarkerColor(2);
    pTGraphErrors_Variable_2->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Variable_2, "Steel HCal Absorber Material, QGSP_BERT_HP", "lp");

    TGraphErrors *pTGraphErrors_Variable_3 = new TGraphErrors(4,jetEnergy,Variable_3_JER,jetEnergyError,Variable_3_JERError);

    pTGraphErrors_Variable_3->SetLineColor(6);
    pTGraphErrors_Variable_3->SetMarkerColor(6);
    pTGraphErrors_Variable_3->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Variable_3, "Tungsten HCal Absorber Material, QGSP_BERT", "lp");

    TGraphErrors *pTGraphErrors_Variable_4 = new TGraphErrors(4,jetEnergy,Variable_4_JER,jetEnergyError,Variable_4_JERError);

    pTGraphErrors_Variable_4->SetLineColor(1);
    pTGraphErrors_Variable_4->SetMarkerColor(1);
    pTGraphErrors_Variable_4->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Variable_4, "Tungsten HCal Absorber Material, QGSP_BERT_HP", "lp");

    pLegend->SetFillStyle(0);
    pLegend->Draw("same");
    pCanvasEj->SaveAs("JER_vs_JetEnergy_HCalAbsorberMaterial.pdf");
}
