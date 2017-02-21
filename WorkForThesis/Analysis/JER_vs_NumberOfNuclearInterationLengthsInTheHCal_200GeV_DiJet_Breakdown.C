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

    float Pandora_Settings_Default_JER[5] = {3.01715,2.91707,2.88127,2.89516,2.81696};

    float Pandora_Settings_PerfectPFA_JER[5] = {2.1163,2.06612,2.13528,2.08562,2.13034};

    float Pandora_Settings_TotalConfusion_JER[5] = {2.15045772628,2.05923420972,1.93450152094,2.00801908387,1.84307219772};

    float Pandora_Settings_PhotonConfusion_JER[5] = {0.689963971885,0.709863508359,0.582085005218,0.701770356456,0.506557953249};

    float Pandora_Settings_NeutralHadronConfusion_JER[5] = {1.53519619476,1.46884529029,1.49392151691,1.49856910311,1.39347603108};

    float Pandora_Settings_OtherConfusion_JER[5] = {1.33850319148,1.25659573579,1.08243784233,1.13751907729,1.09477793036};

    float Pandora_Settings_Default_JERError[5] = {0.0386718,0.0373891,0.0368969,0.0371082,0.0361059};

    float Pandora_Settings_PerfectPFA_JERError[5] = {0.0271253,0.0264822,0.0273439,0.0267322,0.0273054};

    float Pandora_Settings_TotalConfusion_JERError[5] = {0.0472365444155,0.0458175663784,0.0459246378909,0.0457341663661,0.0452681326088};

    float Pandora_Settings_PhotonConfusion_JERError[5] = {0.0539698709427,0.0520879985187,0.0516450825859,0.0517017922813,0.0506454758032};

    float Pandora_Settings_NeutralHadronConfusion_JERError[5] = {0.0494713847317,0.0477058851545,0.0473883220578,0.0471519050169,0.0469463751063};

    float Pandora_Settings_OtherConfusion_JERError[5] = {0.042022677447,0.0407680834346,0.0410793164926,0.0405185994641,0.041085950213};

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
    pCanvasEj->SaveAs("JER_vs_NumberOfNuclearInterationLengthsInTheHCal_200GeV_DiJet_Breakdown.pdf");
}
