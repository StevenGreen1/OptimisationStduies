{
    gStyle->SetOptStat(0);

    TCanvas *pCanvasEj = new TCanvas();
    pCanvasEj->cd();

    TH2F *pAxesEj = new TH2F("axesEj","",1200,0,110,12000,0,6.5);
    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");
    pAxesEj->GetXaxis()->SetTitle("HCal Cell Size [mm^{2}]");
    pAxesEj->Draw();

    float xAxisVairable[6] = {10,20,30,40,50,100};

    float xAxisVairableError[6] = {0,0,0,0,0,0};

    float Pandora_Settings_Default_JER[6] = {2.79637,2.83941,2.88127,2.9959,3.016,3.30898};

    float Pandora_Settings_PerfectPFA_JER[6] = {2.06792,2.07743,2.13528,2.11565,2.11659,2.19115};

    float Pandora_Settings_TotalConfusion_JER[6] = {1.88238998364,1.93559648253,1.93450152094,2.1211887911,2.14855830079,2.47955849253};

    float Pandora_Settings_PhotonConfusion_JER[6] = {0.749196127393,0.700243689011,0.582085005218,0.74484861623,0.824439641878,0.727618856476};

    float Pandora_Settings_NeutralHadronConfusion_JER[6] = {1.30940128608,1.38300221836,1.49392151691,1.56669014017,1.59481828883,1.85505657102};

    float Pandora_Settings_OtherConfusion_JER[6] = {1.12586210754,1.15909334534,1.08243784233,1.22070652947,1.1803205812,1.47565112269};

    float Pandora_Settings_Default_JERError[6] = {0.0358421,0.0363937,0.0368969,0.0383995,0.0386571,0.0424124};

    float Pandora_Settings_PerfectPFA_JERError[6] = {0.0265053,0.0267615,0.0273439,0.0272381,0.0271291,0.0280848};

    float Pandora_Settings_TotalConfusion_JERError[6] = {0.0445778621256,0.0450026973228,0.0459246378909,0.0469394096037,0.0472266311105,0.050868106922};

    float Pandora_Settings_PhotonConfusion_JERError[6] = {0.0497711962843,0.0506800537848,0.0516450825859,0.0534600728183,0.0536381666387,0.0592510045509};

    float Pandora_Settings_NeutralHadronConfusion_JERError[6] = {0.0458605829755,0.0466225599461,0.0473883220578,0.0486158719781,0.0484517416519,0.0534633774771};

    float Pandora_Settings_OtherConfusion_JERError[6] = {0.0401659044333,0.0401955037051,0.0410793164926,0.0411787721717,0.0412412561633,0.0439911714514};

    TLegend *pLegend = new TLegend(0.6, 0.6, 0.9, 0.9);
    TGraphErrors *pTGraphErrors_Pandora_SettingsDefault = new TGraphErrors(6,xAxisVairable,Pandora_Settings_Default_JER,xAxisVairableError,Pandora_Settings_Default_JERError);

    pTGraphErrors_Pandora_SettingsDefault->SetLineColor(1);
    pTGraphErrors_Pandora_SettingsDefault->SetMarkerColor(1);
    pTGraphErrors_Pandora_SettingsDefault->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsDefault, "Default", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsPerfectPFA = new TGraphErrors(6,xAxisVairable,Pandora_Settings_PerfectPFA_JER,xAxisVairableError,Pandora_Settings_PerfectPFA_JERError);

    pTGraphErrors_Pandora_SettingsPerfectPFA->SetLineColor(4);
    pTGraphErrors_Pandora_SettingsPerfectPFA->SetMarkerColor(4);
    pTGraphErrors_Pandora_SettingsPerfectPFA->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsPerfectPFA, "PerfectPFA", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsTotalConfusion = new TGraphErrors(6,xAxisVairable,Pandora_Settings_TotalConfusion_JER,xAxisVairableError,Pandora_Settings_TotalConfusion_JERError);

    pTGraphErrors_Pandora_SettingsTotalConfusion->SetLineColor(2);
    pTGraphErrors_Pandora_SettingsTotalConfusion->SetMarkerColor(2);
    pTGraphErrors_Pandora_SettingsTotalConfusion->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsTotalConfusion, "TotalConfusion", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsPhotonConfusion = new TGraphErrors(6,xAxisVairable,Pandora_Settings_PhotonConfusion_JER,xAxisVairableError,Pandora_Settings_PhotonConfusion_JERError);

    pTGraphErrors_Pandora_SettingsPhotonConfusion->SetLineColor(kOrange);
    pTGraphErrors_Pandora_SettingsPhotonConfusion->SetMarkerColor(kOrange);
    pTGraphErrors_Pandora_SettingsPhotonConfusion->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsPhotonConfusion, "PhotonConfusion", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsNeutralHadronConfusion = new TGraphErrors(6,xAxisVairable,Pandora_Settings_NeutralHadronConfusion_JER,xAxisVairableError,Pandora_Settings_NeutralHadronConfusion_JERError);

    pTGraphErrors_Pandora_SettingsNeutralHadronConfusion->SetLineColor(kGreen-2);
    pTGraphErrors_Pandora_SettingsNeutralHadronConfusion->SetMarkerColor(kGreen-2);
    pTGraphErrors_Pandora_SettingsNeutralHadronConfusion->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsNeutralHadronConfusion, "NeutralHadronConfusion", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsOtherConfusion = new TGraphErrors(6,xAxisVairable,Pandora_Settings_OtherConfusion_JER,xAxisVairableError,Pandora_Settings_OtherConfusion_JERError);

    pTGraphErrors_Pandora_SettingsOtherConfusion->SetLineColor(kMagenta);
    pTGraphErrors_Pandora_SettingsOtherConfusion->SetMarkerColor(kMagenta);
    pTGraphErrors_Pandora_SettingsOtherConfusion->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsOtherConfusion, "OtherConfusion", "lp");

    pLegend->SetFillStyle(0);
    pLegend->Draw("same");
    pCanvasEj->SaveAs("JER_vs_HCalCellSize_200GeV_DiJet_Breakdown.pdf");
}
