{
    gStyle->SetOptStat(0);

    TCanvas *pCanvasEj = new TCanvas();
    pCanvasEj->cd();

    TH2F *pAxesEj = new TH2F("axesEj","",1200,1,25,12000,0,6.5);
    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");
    pAxesEj->GetXaxis()->SetTitle("Scintillator ECal Cell Size [mm^{2}]");
    pAxesEj->Draw();

    float xAxisVairable[6] = {3,5,7,10,15,20};

    float xAxisVairableError[6] = {0,0,0,0,0,0};

    float Pandora_Settings_Default_JER[6] = {3.67495,4.3272,5.1161,5.39392,5.72032,6.85441};

    float Pandora_Settings_PerfectPFA_JER[6] = {1.68305,2.07992,2.37609,2.49349,2.23507,2.57219};

    float Pandora_Settings_TotalConfusion_JER[6] = {3.26689458048,3.79454775087,4.53085814409,4.78297821303,5.26559806646,6.3534852681};

    float Pandora_Settings_PhotonConfusion_JER[6] = {1.41284585231,1.56575365875,2.25419657785,2.79564282667,3.45761229405,4.3699554083};

    float Pandora_Settings_NeutralHadronConfusion_JER[6] = {2.36190264981,2.81567495136,3.04766905065,2.98718060226,3.07963704132,3.30471955626};

    float Pandora_Settings_OtherConfusion_JER[6] = {1.76008030226,2.00474005347,2.48173057925,2.47750152805,2.50744410011,3.21700068946};

    float Pandora_Settings_Default_JERError[6] = {0.04693,0.058179,0.0653338,0.0688816,0.0771047,0.0923996};

    float Pandora_Settings_PerfectPFA_JERError[6] = {0.021493,0.0279644,0.0303432,0.0318425,0.0301267,0.034674};

    float Pandora_Settings_TotalConfusion_JERError[6] = {0.0516175505401,0.0645507987906,0.0720362226682,0.0758855379345,0.0827813582787,0.0986912693327};

    float Pandora_Settings_PhotonConfusion_JERError[6] = {0.0638694659421,0.0795393171272,0.0877971999117,0.0906354098393,0.0985808087678,0.11664123058};

    float Pandora_Settings_NeutralHadronConfusion_JERError[6] = {0.0533296188343,0.0667091904885,0.0732457057442,0.0740610532461,0.0763086871985,0.0902795701243};

    float Pandora_Settings_OtherConfusion_JERError[6] = {0.0378033588258,0.047859341561,0.0533464327466,0.0550351122412,0.0543834398471,0.0654612823983};

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
    pCanvasEj->SaveAs("JER_vs_ScintillatorECalCellSize_500GeV_DiJet_Breakdown.pdf");
}
