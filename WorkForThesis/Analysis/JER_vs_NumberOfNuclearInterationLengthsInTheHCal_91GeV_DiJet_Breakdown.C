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

    float Pandora_Settings_Default_JER[5] = {3.71038,3.74718,3.6469,3.63755,3.67255};

    float Pandora_Settings_PerfectPFA_JER[5] = {2.96922,2.94988,2.93851,2.94842,2.95066};

    float Pandora_Settings_TotalConfusion_JER[5] = {2.22500614291,2.31075008125,2.15987004005,2.13039656076,2.1866021739};

    float Pandora_Settings_PhotonConfusion_JER[5] = {0.559782079295,0.695392827329,0.642371540154,0.599011978511,0.616648144731};

    float Pandora_Settings_NeutralHadronConfusion_JER[5] = {1.4004500588,1.41993218993,1.19578154255,1.3174408315,1.33908923246};

    float Pandora_Settings_OtherConfusion_JER[5] = {1.63585940487,1.68516685515,1.68003092138,1.56336937772,1.61487279994};

    float Pandora_Settings_Default_JERError[5] = {0.0476828,0.0481557,0.0464093,0.0467468,0.0471966};

    float Pandora_Settings_PerfectPFA_JERError[5] = {0.038158,0.0379094,0.0373946,0.0378906,0.0379195};

    float Pandora_Settings_TotalConfusion_JERError[5] = {0.061071145894,0.0612870639221,0.0596000757346,0.0601745456388,0.0605425418871};

    float Pandora_Settings_PhotonConfusion_JERError[5] = {0.0670491413972,0.0675138746776,0.0651211866296,0.0656579872441,0.0662749167919};

    float Pandora_Settings_NeutralHadronConfusion_JERError[5] = {0.0641863813889,0.0643834067375,0.0627883325016,0.0629716814908,0.0635079914521};

    float Pandora_Settings_OtherConfusion_JERError[5] = {0.0579138875356,0.0578209673014,0.0570422465453,0.0572282258447,0.0575017367385};

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
    pCanvasEj->SaveAs("JER_vs_NumberOfNuclearInterationLengthsInTheHCal_91GeV_DiJet_Breakdown.pdf");
}
