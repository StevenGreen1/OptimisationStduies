{
    gStyle->SetOptStat(0);

    TCanvas *pCanvasEj = new TCanvas();
    pCanvasEj->cd();

    TH2F *pAxesEj = new TH2F("axesEj","",1200,1,25,12000,0,6.5);
    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");
    pAxesEj->GetXaxis()->SetTitle("Silicon ECal Cell Size [mm^{2}]");
    pAxesEj->Draw();

    float xAxisVairable[6] = {3,5,7,10,15,20};

    float xAxisVairableError[6] = {0,0,0,0,0,0};

    float Pandora_Settings_Default_JER[6] = {3.11829,3.07604,3.18398,3.58679,4.15968,4.53885};

    float Pandora_Settings_PerfectPFA_JER[6] = {1.6967,1.68383,1.66269,1.77235,1.79134,1.82917};

    float Pandora_Settings_TotalConfusion_JER[6] = {2.61628393606,2.57424525108,2.71536196561,3.11830690946,3.75420280576,4.1539494982};

    float Pandora_Settings_PhotonConfusion_JER[6] = {1.21267485964,0.994501169431,1.28038896602,2.03890501439,2.78392958869,3.12799646585};

    float Pandora_Settings_NeutralHadronConfusion_JER[6] = {1.84811469268,1.90500096997,1.94940754736,1.8875833184,1.87867742167,2.00989517339};

    float Pandora_Settings_OtherConfusion_JER[6] = {1.3995832957,1.41727814528,1.39054123071,1.41553295264,1.6776012331,1.85236495735};

    float Pandora_Settings_Default_JERError[6] = {0.0419215,0.0439165,0.0406602,0.0590143,0.0684402,0.0692329};

    float Pandora_Settings_PerfectPFA_JERError[6] = {0.02281,0.02404,0.021233,0.0291608,0.0294734,0.0279011};

    float Pandora_Settings_TotalConfusion_JERError[6] = {0.04772534501,0.0500657443313,0.0458703564044,0.0658258834653,0.0745166962998,0.0746435758506};

    float Pandora_Settings_PhotonConfusion_JERError[6] = {0.0570003432463,0.0604622490843,0.0551284606758,0.0764198802165,0.0852646050035,0.0854979153458};

    float Pandora_Settings_NeutralHadronConfusion_JERError[6] = {0.0486411331982,0.0521001180104,0.0463904722806,0.0612380575553,0.0649348725033,0.0639805582761};

    float Pandora_Settings_OtherConfusion_JERError[6] = {0.0373444679923,0.039563576974,0.0348854834046,0.0473620266956,0.0499923299748,0.0485312856848};

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
    pCanvasEj->SaveAs("JER_vs_SiliconECalCellSize_500GeV_DiJet_Breakdown.pdf");
}
