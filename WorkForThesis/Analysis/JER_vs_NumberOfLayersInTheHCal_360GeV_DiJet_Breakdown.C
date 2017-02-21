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

    float Pandora_Settings_Default_JER[8] = {3.38347,3.07476,2.96963,2.93226,2.87282,2.84624,2.92408,2.88876};

    float Pandora_Settings_PerfectPFA_JER[8] = {1.99352,1.86839,1.86131,1.79188,1.82326,1.79003,1.74387,1.72612};

    float Pandora_Settings_TotalConfusion_JER[8] = {2.73381551142,2.44198031636,2.31392035749,2.32105897667,2.22009408017,2.2128883245,2.34716025646,2.31634282506};

    float Pandora_Settings_PhotonConfusion_JER[8] = {1.11994666538,0.93268089157,0.999256626348,0.90616427578,0.83987053544,1.01562417296,1.05367161716,0.962662707286};

    float Pandora_Settings_NeutralHadronConfusion_JER[8] = {1.87631637503,1.76022766028,1.66824360391,1.67154866827,1.7232184231,1.61270117331,1.68377262167,1.74617055066};

    float Pandora_Settings_OtherConfusion_JER[8] = {1.64283400805,1.41243506187,1.25406415047,1.33120476565,1.11980064065,1.1245342154,1.25053874438,1.17881847763};

    float Pandora_Settings_Default_JERError[8] = {0.0430955,0.0391634,0.0378243,0.0373483,0.0365912,0.0363619,0.0372442,0.0367943};

    float Pandora_Settings_PerfectPFA_JERError[8] = {0.0253915,0.0237978,0.0237075,0.0228232,0.023223,0.0228684,0.0222118,0.0219857};

    float Pandora_Settings_TotalConfusion_JERError[8] = {0.0500195834651,0.0458269214315,0.0446400006657,0.0437698165125,0.0433384065969,0.0429552070939,0.0433646586329,0.0428624628451};

    float Pandora_Settings_PhotonConfusion_JERError[8] = {0.0592536673728,0.0540962618398,0.0519555487313,0.0515416857305,0.0506298094406,0.0497590592529,0.0509333580848,0.0505694880832};

    float Pandora_Settings_NeutralHadronConfusion_JERError[8] = {0.0523097974335,0.0477769452752,0.0456713279366,0.045498109129,0.0443533294032,0.0433959252777,0.0442048789971,0.0437297961672};

    float Pandora_Settings_OtherConfusion_JERError[8] = {0.0415610052982,0.0381617243155,0.0371381917479,0.0364596294411,0.0358055190112,0.0353883731911,0.035219562874,0.0345279528007};

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
    pCanvasEj->SaveAs("JER_vs_NumberOfLayersInTheHCal_360GeV_DiJet_Breakdown.pdf");
}
