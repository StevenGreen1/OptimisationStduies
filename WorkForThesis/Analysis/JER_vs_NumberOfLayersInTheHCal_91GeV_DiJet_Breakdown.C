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

    float Pandora_Settings_Default_JER[8] = {4.15954,3.81898,3.82021,3.88233,3.68123,3.68144,3.6965,3.70923};

    float Pandora_Settings_PerfectPFA_JER[8] = {3.24679,3.09356,3.0381,3.07996,2.98342,2.99912,2.98816,2.94906};

    float Pandora_Settings_TotalConfusion_JER[8] = {2.60002455902,2.23930676032,2.31602090537,2.36354238957,2.1565387584,2.13501281008,2.17600828684,2.24976272289};

    float Pandora_Settings_PhotonConfusion_JER[8] = {0.574966485545,0.573979860622,0.604622031107,0.576021717733,0.580323420947,0.648790475577,0.535406107175,0.637249202824};

    float Pandora_Settings_NeutralHadronConfusion_JER[8] = {1.42027750475,1.19574403511,1.29581263831,1.449785535,1.25897195644,1.30670141635,1.36540284913,1.35453371457};

    float Pandora_Settings_OtherConfusion_JER[8] = {2.10056017707,1.8042278373,1.82188216963,1.77557131946,1.65193031224,1.55880788633,1.607491034,1.6794594901};

    float Pandora_Settings_Default_JERError[8] = {0.053455,0.0490784,0.0490942,0.0498925,0.0473081,0.0473109,0.0501223,0.0476679};

    float Pandora_Settings_PerfectPFA_JERError[8] = {0.0417251,0.0397559,0.0390431,0.0395811,0.0383405,0.0387216,0.0405176,0.0378989};

    float Pandora_Settings_TotalConfusion_JERError[8] = {0.0678116343994,0.0631602740027,0.0627265328356,0.0636861500813,0.0608936290014,0.0607987456298,0.0644509887392,0.0608977996181};

    float Pandora_Settings_PhotonConfusion_JERError[8] = {0.0752330896501,0.069014744656,0.0689939554472,0.0701687941818,0.0664857102652,0.0663864894992,0.0705094061268,0.0669100498072};

    float Pandora_Settings_NeutralHadronConfusion_JERError[8] = {0.072612666864,0.0668759895129,0.0665011680767,0.0672441322623,0.0640553955559,0.0636841705508,0.0676485937828,0.0640886976659};

    float Pandora_Settings_OtherConfusion_JERError[8] = {0.0648896375376,0.0608167554709,0.0599744607909,0.0604484892859,0.0582294048492,0.0576279253217,0.0613063553714,0.057779614421};

    TLegend *pLegend = new TLegend(0.6, 0.6, 0.9, 0.9);
    TGraphErrors *pTGraphErrors_Pandora_SettingsDefault = new TGraphErrors(8,xAxisVairable,Pandora_Settings_Default_JER,xAxisVairableError,Pandora_Settings_Default_JERError);

    pTGraphErrors_Pandora_SettingsDefault->SetLineColor(1);
    pTGraphErrors_Pandora_SettingsDefault->SetMarkerColor(1);
    pTGraphErrors_Pandora_SettingsDefault->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsDefault, "Default", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsPerfectPFA = new TGraphErrors(8,xAxisVairable,Pandora_Settings_PerfectPFA_JER,xAxisVairableError,Pandora_Settings_PerfectPFA_JERError);

    pTGraphErrors_Pandora_SettingsPerfectPFA->SetLineColor(4);
    pTGraphErrors_Pandora_SettingsPerfectPFA->SetMarkerColor(4);
    pTGraphErrors_Pandora_SettingsPerfectPFA->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsPerfectPFA, "PerfectPFA", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsTotalConfusion = new TGraphErrors(8,xAxisVairable,Pandora_Settings_TotalConfusion_JER,xAxisVairableError,Pandora_Settings_TotalConfusion_JERError);

    pTGraphErrors_Pandora_SettingsTotalConfusion->SetLineColor(2);
    pTGraphErrors_Pandora_SettingsTotalConfusion->SetMarkerColor(2);
    pTGraphErrors_Pandora_SettingsTotalConfusion->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsTotalConfusion, "TotalConfusion", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsPhotonConfusion = new TGraphErrors(8,xAxisVairable,Pandora_Settings_PhotonConfusion_JER,xAxisVairableError,Pandora_Settings_PhotonConfusion_JERError);

    pTGraphErrors_Pandora_SettingsPhotonConfusion->SetLineColor(kOrange);
    pTGraphErrors_Pandora_SettingsPhotonConfusion->SetMarkerColor(kOrange);
    pTGraphErrors_Pandora_SettingsPhotonConfusion->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsPhotonConfusion, "PhotonConfusion", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsNeutralHadronConfusion = new TGraphErrors(8,xAxisVairable,Pandora_Settings_NeutralHadronConfusion_JER,xAxisVairableError,Pandora_Settings_NeutralHadronConfusion_JERError);

    pTGraphErrors_Pandora_SettingsNeutralHadronConfusion->SetLineColor(kGreen-2);
    pTGraphErrors_Pandora_SettingsNeutralHadronConfusion->SetMarkerColor(kGreen-2);
    pTGraphErrors_Pandora_SettingsNeutralHadronConfusion->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsNeutralHadronConfusion, "NeutralHadronConfusion", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsOtherConfusion = new TGraphErrors(8,xAxisVairable,Pandora_Settings_OtherConfusion_JER,xAxisVairableError,Pandora_Settings_OtherConfusion_JERError);

    pTGraphErrors_Pandora_SettingsOtherConfusion->SetLineColor(kMagenta);
    pTGraphErrors_Pandora_SettingsOtherConfusion->SetMarkerColor(kMagenta);
    pTGraphErrors_Pandora_SettingsOtherConfusion->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsOtherConfusion, "OtherConfusion", "lp");

    pLegend->SetFillStyle(0);
    pLegend->Draw("same");
    pCanvasEj->SaveAs("JER_vs_NumberOfLayersInTheHCal_91GeV_DiJet_Breakdown.pdf");
}
