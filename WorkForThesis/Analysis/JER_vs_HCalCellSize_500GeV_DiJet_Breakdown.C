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

    float Pandora_Settings_Default_JER[6] = {2.77741,2.8979,2.97436,3.08927,3.09817,3.52004};

    float Pandora_Settings_PerfectPFA_JER[6] = {1.67941,1.6809,1.69254,1.68182,1.65124,1.84401};

    float Pandora_Settings_TotalConfusion_JER[6] = {2.2121456462,2.36059306108,2.44583845705,2.59134533023,2.62146215141,2.99838435186};

    float Pandora_Settings_PhotonConfusion_JER[6] = {1.11452773303,1.07810769309,1.17751627891,1.23843728303,1.14694618287,1.14637068263};

    float Pandora_Settings_NeutralHadronConfusion_JER[6] = {1.52130010856,1.68124957829,1.63527070224,1.78615355255,1.84158144257,2.04928927863};

    float Pandora_Settings_OtherConfusion_JER[6] = {1.15631408882,1.25836531166,1.38617131023,1.41102771171,1.47144692575,1.86455260907};

    float Pandora_Settings_Default_JERError[6] = {0.0354884,0.0370281,0.0453691,0.0394732,0.039587,0.0449774};

    float Pandora_Settings_PerfectPFA_JERError[6] = {0.0214587,0.0214778,0.0241841,0.0214896,0.0210988,0.0235619};

    float Pandora_Settings_TotalConfusion_JERError[6] = {0.0414716952761,0.042806266537,0.0525734765383,0.0449436238056,0.044858548067,0.0507752757324};

    float Pandora_Settings_PhotonConfusion_JERError[6] = {0.0481255133266,0.0498328376185,0.0615962308486,0.0535335647788,0.0540327426037,0.0618974860522};

    float Pandora_Settings_NeutralHadronConfusion_JERError[6] = {0.0416579941237,0.0437871489429,0.0573927626654,0.0457667717505,0.0463788562679,0.0541404744605};

    float Pandora_Settings_OtherConfusion_JERError[6] = {0.0337526361631,0.0346836426515,0.0358201434281,0.0353362401517,0.0352675952544,0.0409625513987};

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
    pCanvasEj->SaveAs("JER_vs_HCalCellSize_500GeV_DiJet_Breakdown.pdf");
}
