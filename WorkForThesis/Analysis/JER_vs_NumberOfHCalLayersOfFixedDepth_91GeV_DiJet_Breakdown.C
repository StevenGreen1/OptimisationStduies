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

    float Pandora_Settings_Default_JER[5] = {3.74875,3.6974,3.6469,3.71188,3.55531};

    float Pandora_Settings_PerfectPFA_JER[5] = {3.0391,3.02638,2.93851,3.02028,2.96141};

    float Pandora_Settings_TotalConfusion_JER[5] = {2.19476599037,2.12409765679,2.15987004005,2.15776779474,1.96730272404};

    float Pandora_Settings_PhotonConfusion_JER[5] = {0.663030497036,0.628679001081,0.642371540154,0.722980850576,0.614341799978};

    float Pandora_Settings_NeutralHadronConfusion_JER[5] = {1.32174425442,1.29919397705,1.19578154255,1.35778846924,1.33398997927};

    float Pandora_Settings_OtherConfusion_JER[5] = {1.62184476396,1.5584121981,1.68003092138,1.51316589259,1.30894419132};

    float Pandora_Settings_Default_JERError[5] = {0.0517574,0.0498738,0.0464093,0.0519564,0.0501794};

    float Pandora_Settings_PerfectPFA_JERError[5] = {0.0419595,0.0408226,0.0373946,0.0422758,0.0417972};

    float Pandora_Settings_TotalConfusion_JERError[5] = {0.066629150416,0.0644503928495,0.0596000757346,0.0669830042019,0.0653066669162};

    float Pandora_Settings_PhotonConfusion_JERError[5] = {0.0726220139619,0.0700172206679,0.0651211866296,0.0727777587238,0.0704323798679};

    float Pandora_Settings_NeutralHadronConfusion_JERError[5] = {0.0696923703163,0.0672602532766,0.0627883325016,0.0695193537935,0.0673132305303};

    float Pandora_Settings_OtherConfusion_JERError[5] = {0.0634242014617,0.0614395837704,0.0570422465453,0.0634276897863,0.0619298514103};

    TLegend *pLegend = new TLegend(0.6, 0.6, 0.9, 0.9);
    TGraphErrors *pTGraphErrors_Pandora_SettingsDefault = new TGraphErrors(5,xAxisVairable,Pandora_Settings_Default_JER,xAxisVairableError,Pandora_Settings_Default_JERError);

    pTGraphErrors_Pandora_SettingsDefault->SetLineColor(1);
    pTGraphErrors_Pandora_SettingsDefault->SetMarkerColor(1);
    pTGraphErrors_Pandora_SettingsDefault->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsDefault, "Default", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsPerfectPFA = new TGraphErrors(5,xAxisVairable,Pandora_Settings_PerfectPFA_JER,xAxisVairableError,Pandora_Settings_PerfectPFA_JERError);

    pTGraphErrors_Pandora_SettingsPerfectPFA->SetLineColor(4);
    pTGraphErrors_Pandora_SettingsPerfectPFA->SetMarkerColor(4);
    pTGraphErrors_Pandora_SettingsPerfectPFA->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsPerfectPFA, "PerfectPFA", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsTotalConfusion = new TGraphErrors(5,xAxisVairable,Pandora_Settings_TotalConfusion_JER,xAxisVairableError,Pandora_Settings_TotalConfusion_JERError);

    pTGraphErrors_Pandora_SettingsTotalConfusion->SetLineColor(2);
    pTGraphErrors_Pandora_SettingsTotalConfusion->SetMarkerColor(2);
    pTGraphErrors_Pandora_SettingsTotalConfusion->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsTotalConfusion, "TotalConfusion", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsPhotonConfusion = new TGraphErrors(5,xAxisVairable,Pandora_Settings_PhotonConfusion_JER,xAxisVairableError,Pandora_Settings_PhotonConfusion_JERError);

    pTGraphErrors_Pandora_SettingsPhotonConfusion->SetLineColor(kOrange);
    pTGraphErrors_Pandora_SettingsPhotonConfusion->SetMarkerColor(kOrange);
    pTGraphErrors_Pandora_SettingsPhotonConfusion->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsPhotonConfusion, "PhotonConfusion", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsNeutralHadronConfusion = new TGraphErrors(5,xAxisVairable,Pandora_Settings_NeutralHadronConfusion_JER,xAxisVairableError,Pandora_Settings_NeutralHadronConfusion_JERError);

    pTGraphErrors_Pandora_SettingsNeutralHadronConfusion->SetLineColor(kGreen-2);
    pTGraphErrors_Pandora_SettingsNeutralHadronConfusion->SetMarkerColor(kGreen-2);
    pTGraphErrors_Pandora_SettingsNeutralHadronConfusion->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsNeutralHadronConfusion, "NeutralHadronConfusion", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsOtherConfusion = new TGraphErrors(5,xAxisVairable,Pandora_Settings_OtherConfusion_JER,xAxisVairableError,Pandora_Settings_OtherConfusion_JERError);

    pTGraphErrors_Pandora_SettingsOtherConfusion->SetLineColor(kMagenta);
    pTGraphErrors_Pandora_SettingsOtherConfusion->SetMarkerColor(kMagenta);
    pTGraphErrors_Pandora_SettingsOtherConfusion->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsOtherConfusion, "OtherConfusion", "lp");

    pLegend->SetFillStyle(0);
    pLegend->Draw("same");
    pCanvasEj->SaveAs("JER_vs_NumberOfHCalLayersOfFixedDepth_91GeV_DiJet_Breakdown.pdf");
}
