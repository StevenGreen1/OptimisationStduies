{
    gStyle->SetOptStat(0);

    TCanvas *pCanvasEj = new TCanvas();
    pCanvasEj->cd();

    TH2F *pAxesEj = new TH2F("axesEj","",1200,0.5,5.5,12000,0,6.5);
    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");
    pAxesEj->GetXaxis()->SetTitle("Magentic Field Strength [T]");
    pAxesEj->Draw();

    float xAxisVairable[9] = {1,1.5,2,2.5,3,3.5,4,4.5,5};

    float xAxisVairableError[9] = {0,0,0,0,0,0,0,0,0};

    float Pandora_Settings_Default_JER[9] = {3.47664,3.22453,3.16111,3.04102,2.95643,2.97777,2.8029,2.82693,2.7952};

    float Pandora_Settings_PerfectPFA_JER[9] = {2.04964,2.01372,2.03741,2.03908,2.03741,2.06891,2.1598,2.16883,2.20092};

    float Pandora_Settings_TotalConfusion_JER[9] = {2.80820254967,2.51843711109,2.41693544059,2.25609294888,2.14229756028,2.14166420916,1.7864804421,1.81320425104,1.72310597283};

    float Pandora_Settings_PhotonConfusion_JER[9] = {1.1702933936,1.0848208866,1.04761115458,0.931257662519,0.799907244185,0.739792622834,0.607875557906,0.705193924605,0.469956138272};

    float Pandora_Settings_NeutralHadronConfusion_JER[9] = {2.02457675577,1.79722330413,1.74037294279,1.67999355654,1.59252101374,1.58347157793,1.3555303035,1.26781370457,1.24845061801};

    float Pandora_Settings_OtherConfusion_JER[9] = {1.55483243242,1.39128628312,1.30965255423,1.18335802275,1.18889194559,1.23776016332,0.992238515882,1.08768543026,1.09069082517};

    float Pandora_Settings_Default_JERError[9] = {0.0469174,0.0413299,0.040517,0.0389778,0.0378936,0.0381671,0.0359258,0.0362338,0.035827};

    float Pandora_Settings_PerfectPFA_JERError[9] = {0.0276599,0.0258106,0.0261141,0.0261356,0.0261141,0.0265179,0.0276829,0.0277987,0.0282099};

    float Pandora_Settings_TotalConfusion_JERError[9] = {0.0544639234146,0.048727222916,0.0482035176399,0.0469290693154,0.0460204403215,0.0464750423901,0.0453543050173,0.0456689688467,0.0456001639873};

    float Pandora_Settings_PhotonConfusion_JERError[9] = {0.0644447360535,0.0567710905359,0.0557036791143,0.0538143287611,0.0526000052587,0.0531367373535,0.0502065407812,0.0504389776539,0.0503052455917};

    float Pandora_Settings_NeutralHadronConfusion_JERError[9] = {0.0561883358036,0.049990115297,0.0492450081668,0.0478532348952,0.0473808928133,0.0481842252935,0.0464545839278,0.046886279,0.047313009845};

    float Pandora_Settings_OtherConfusion_JERError[9] = {0.044389615998,0.0406248283872,0.0405671364344,0.0399526025673,0.0399518544596,0.0407196470018,0.0411637934255,0.0417118170981,0.0422739243769};

    TLegend *pLegend = new TLegend(0.6, 0.6, 0.9, 0.9);
    TGraphErrors *pTGraphErrors_Pandora_SettingsDefault = new TGraphErrors(9,xAxisVairable,Pandora_Settings_Default_JER,xAxisVairableError,Pandora_Settings_Default_JERError);

    pTGraphErrors_Pandora_SettingsDefault->SetLineColor(1);
    pTGraphErrors_Pandora_SettingsDefault->SetMarkerColor(1);
    pTGraphErrors_Pandora_SettingsDefault->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsDefault, "Default", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsPerfectPFA = new TGraphErrors(9,xAxisVairable,Pandora_Settings_PerfectPFA_JER,xAxisVairableError,Pandora_Settings_PerfectPFA_JERError);

    pTGraphErrors_Pandora_SettingsPerfectPFA->SetLineColor(4);
    pTGraphErrors_Pandora_SettingsPerfectPFA->SetMarkerColor(4);
    pTGraphErrors_Pandora_SettingsPerfectPFA->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsPerfectPFA, "PerfectPFA", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsTotalConfusion = new TGraphErrors(9,xAxisVairable,Pandora_Settings_TotalConfusion_JER,xAxisVairableError,Pandora_Settings_TotalConfusion_JERError);

    pTGraphErrors_Pandora_SettingsTotalConfusion->SetLineColor(2);
    pTGraphErrors_Pandora_SettingsTotalConfusion->SetMarkerColor(2);
    pTGraphErrors_Pandora_SettingsTotalConfusion->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsTotalConfusion, "TotalConfusion", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsPhotonConfusion = new TGraphErrors(9,xAxisVairable,Pandora_Settings_PhotonConfusion_JER,xAxisVairableError,Pandora_Settings_PhotonConfusion_JERError);

    pTGraphErrors_Pandora_SettingsPhotonConfusion->SetLineColor(kOrange);
    pTGraphErrors_Pandora_SettingsPhotonConfusion->SetMarkerColor(kOrange);
    pTGraphErrors_Pandora_SettingsPhotonConfusion->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsPhotonConfusion, "PhotonConfusion", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsNeutralHadronConfusion = new TGraphErrors(9,xAxisVairable,Pandora_Settings_NeutralHadronConfusion_JER,xAxisVairableError,Pandora_Settings_NeutralHadronConfusion_JERError);

    pTGraphErrors_Pandora_SettingsNeutralHadronConfusion->SetLineColor(kGreen-2);
    pTGraphErrors_Pandora_SettingsNeutralHadronConfusion->SetMarkerColor(kGreen-2);
    pTGraphErrors_Pandora_SettingsNeutralHadronConfusion->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsNeutralHadronConfusion, "NeutralHadronConfusion", "lp");

    TGraphErrors *pTGraphErrors_Pandora_SettingsOtherConfusion = new TGraphErrors(9,xAxisVairable,Pandora_Settings_OtherConfusion_JER,xAxisVairableError,Pandora_Settings_OtherConfusion_JERError);

    pTGraphErrors_Pandora_SettingsOtherConfusion->SetLineColor(kMagenta);
    pTGraphErrors_Pandora_SettingsOtherConfusion->SetMarkerColor(kMagenta);
    pTGraphErrors_Pandora_SettingsOtherConfusion->Draw("lp,same");

    pLegend->AddEntry(pTGraphErrors_Pandora_SettingsOtherConfusion, "OtherConfusion", "lp");

    pLegend->SetFillStyle(0);
    pLegend->Draw("same");
    pCanvasEj->SaveAs("JER_vs_MagneticFieldStrength_200GeV_DiJet_Breakdown.pdf");
}
