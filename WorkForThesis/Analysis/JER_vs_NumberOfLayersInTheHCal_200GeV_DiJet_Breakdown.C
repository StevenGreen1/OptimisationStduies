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

    float Pandora_Settings_Default_JER[8] = {3.35045,3.13551,2.96886,2.89729,2.92353,2.88127,2.89581,2.85293};

    float Pandora_Settings_PerfectPFA_JER[8] = {2.28332,2.20111,2.16996,2.10737,2.09374,2.13528,2.04716,2.08622};

    float Pandora_Settings_TotalConfusion_JER[8] = {2.45193086772,2.23305569299,2.02617948317,1.98828595207,2.04041183914,1.93450152094,2.04813366031,1.94599478327};

    float Pandora_Settings_PhotonConfusion_JER[8] = {0.877013241405,0.816329158918,0.774745777336,0.663303571904,0.805964517395,0.582085005218,0.792877691451,0.82748178276};

    float Pandora_Settings_NeutralHadronConfusion_JER[8] = {1.54070465593,1.46514949954,1.33278350174,1.38056672421,1.41809816924,1.49392151691,1.43686792378,1.38281551915};

    float Pandora_Settings_OtherConfusion_JER[8] = {1.69382464196,1.47427316882,1.3148613676,1.26781107374,1.22584634127,1.08243784233,1.22540076159,1.09086701101};

    float Pandora_Settings_Default_JERError[8] = {0.0429439,0.0401889,0.0380529,0.0371356,0.037472,0.0368969,0.0371166,0.036567};

    float Pandora_Settings_PerfectPFA_JERError[8] = {0.0292661,0.0282124,0.0278132,0.0270108,0.0268362,0.0273439,0.0262391,0.0267399};

    float Pandora_Settings_TotalConfusion_JERError[8] = {0.0519681166325,0.0491027964535,0.0471337267642,0.0459200295663,0.0460905582134,0.0459246378909,0.0454547967522,0.0453007441446};

    float Pandora_Settings_PhotonConfusion_JERError[8] = {0.0596822517493,0.0558639040901,0.0528896684708,0.0518237399042,0.0519769354922,0.0516450825859,0.0514979065223,0.050614090137};

    float Pandora_Settings_NeutralHadronConfusion_JERError[8] = {0.0551876217695,0.0515623866458,0.0490616427788,0.0479631138553,0.0475866729011,0.0473883220578,0.047005517419,0.0462080185626};

    float Pandora_Settings_OtherConfusion_JERError[8] = {0.0467370436775,0.0441469362798,0.0427920337583,0.0415120314386,0.0410760762575,0.0410793164926,0.040295337755,0.0403175573253};

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
    pCanvasEj->SaveAs("JER_vs_NumberOfLayersInTheHCal_200GeV_DiJet_Breakdown.pdf");
}
