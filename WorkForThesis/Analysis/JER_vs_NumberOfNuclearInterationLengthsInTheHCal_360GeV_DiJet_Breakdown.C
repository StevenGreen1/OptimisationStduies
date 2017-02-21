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

    float Pandora_Settings_Default_JER[5] = {3.04182,2.92116,2.84624,2.92063,2.82046};

    float Pandora_Settings_PerfectPFA_JER[5] = {1.74127,1.77086,1.79003,1.76792,1.76538};

    float Pandora_Settings_TotalConfusion_JER[5] = {2.49412263121,2.32319405259,2.2128883245,2.324766326,2.19964271353};

    float Pandora_Settings_PhotonConfusion_JER[5] = {0.863677228772,0.933224977805,1.01562417296,1.0244906512,1.01189820412};

    float Pandora_Settings_NeutralHadronConfusion_JER[5] = {1.87344784088,1.69920539003,1.61270117331,1.73252585366,1.60476756373};

    float Pandora_Settings_OtherConfusion_JER[5] = {1.40174981059,1.28024325396,1.1245342154,1.16331919201,1.11319861575};

    float Pandora_Settings_Default_JERError[5] = {0.0387437,0.0372069,0.0363619,0.0392358,0.0359244};

    float Pandora_Settings_PerfectPFA_JERError[5] = {0.0221786,0.0225555,0.0228684,0.0237503,0.0224857};

    float Pandora_Settings_TotalConfusion_JERError[5] = {0.0446426157848,0.0435098110725,0.0429552070939,0.0458641757501,0.0423812984576};

    float Pandora_Settings_PhotonConfusion_JERError[5] = {0.053675037529,0.0512578309596,0.0497590592529,0.0537534222263,0.0491434757719};

    float Pandora_Settings_NeutralHadronConfusion_JERError[5] = {0.046805356923,0.0449191470149,0.0433959252777,0.0464581066877,0.0427909841542};

    float Pandora_Settings_OtherConfusion_JERError[5] = {0.0360908786001,0.0358246615367,0.0353883731911,0.0370456511669,0.0348176372924};

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
    pCanvasEj->SaveAs("JER_vs_NumberOfNuclearInterationLengthsInTheHCal_360GeV_DiJet_Breakdown.pdf");
}
