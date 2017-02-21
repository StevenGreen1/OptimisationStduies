{
    gStyle->SetOptStat(0);

    TCanvas *pCanvasEj = new TCanvas();
    pCanvasEj->cd();

    TH2F *pAxesEj = new TH2F("axesEj","",1200,0.0,0.3,12000,0,6.5);
    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");
    pAxesEj->GetXaxis()->SetTitle("Sampling Fraction In The HCal");
    pAxesEj->Draw();

    float xAxisVairable[5] = {0.05,0.1,0.15,0.2,0.25};

    float xAxisVairableError[5] = {0,0,0,0,0};

    float Pandora_Settings_Default_JER[5] = {3.12931,3.02298,2.97436,2.94966,2.99758};

    float Pandora_Settings_PerfectPFA_JER[5] = {1.70713,1.6875,1.69254,1.67789,1.66522};

    float Pandora_Settings_TotalConfusion_JER[5] = {2.62264908808,2.50813712352,2.44583845705,2.42593884167,2.49249437472};

    float Pandora_Settings_PhotonConfusion_JER[5] = {1.03358427813,1.17977618759,1.17751627891,1.27128542271,1.23184982181};

    float Pandora_Settings_NeutralHadronConfusion_JER[5] = {1.95211357088,1.7600357654,1.63527070224,1.60740006159,1.69232398458};

    float Pandora_Settings_OtherConfusion_JER[5] = {1.4139463871,1.34207081859,1.38617131023,1.29818245232,1.35318651918};

    float Pandora_Settings_Default_JERError[5] = {0.0399849,0.0386262,0.0453691,0.0396687,0.0383017};

    float Pandora_Settings_PerfectPFA_JERError[5] = {0.0218129,0.0215621,0.0241841,0.0225652,0.0212775};

    float Pandora_Settings_TotalConfusion_JERError[5] = {0.0455477413768,0.0442369272277,0.0525734765383,0.0456376497929,0.043814918276};

    float Pandora_Settings_PhotonConfusion_JERError[5] = {0.0549833880116,0.0525043941189,0.0615962308486,0.0534311480452,0.0518297194389};

    float Pandora_Settings_NeutralHadronConfusion_JERError[5] = {0.0471867570089,0.0449858695209,0.0573927626654,0.0457745033891,0.0443953118013};

    float Pandora_Settings_OtherConfusion_JERError[5] = {0.0357492861781,0.0349845263717,0.0358201434281,0.0363756184384,0.0347046066085};

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
    pCanvasEj->SaveAs("JER_vs_SamplingFractionInTheHCal_500GeV_DiJet_Breakdown.pdf");
}
