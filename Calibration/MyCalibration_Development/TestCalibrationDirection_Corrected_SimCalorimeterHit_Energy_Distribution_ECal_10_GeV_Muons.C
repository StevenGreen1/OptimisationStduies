{
//=========Macro generated from canvas: Direction_Corrected_SimCalorimeterHit_Energy_Distribution_ECal/Direction Corrected SimCalorimeterHit Energy Distribution ECal
//=========  (Thu Jan 28 10:27:33 2016) by ROOT version5.34/30
   TCanvas *Direction_Corrected_SimCalorimeterHit_Energy_Distribution_ECal = new TCanvas("Direction_Corrected_SimCalorimeterHit_Energy_Distribution_ECal", "Direction Corrected SimCalorimeterHit Energy Distribution ECal",0,0,5000,5000);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_ECal->SetHighLightColor(2);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_ECal->Range(-0.000125,-0.13125,0.001125,1.18125);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_ECal->SetFillColor(0);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_ECal->SetBorderMode(0);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_ECal->SetBorderSize(2);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_ECal->SetFrameBorderMode(0);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_ECal->SetFrameBorderMode(0);
   
   TH1F *ECalDirectionCorrectedSimCaloHit = new TH1F("ECalDirectionCorrectedSimCaloHit","Distribution of Direction Corrected SimCaloHits in the ECal (1==nPfoTargetsTotal && 1==nPfoTargetsTracks)",200,0,0.001);
   
   TPaveStats *ptstats = new TPaveStats(0.78,0.775,0.98,0.935,"brNDC");
   ptstats->SetName("stats");
   ptstats->SetBorderSize(1);
   ptstats->SetFillColor(0);
   ptstats->SetTextAlign(12);
   ptstats->SetTextFont(42);
   TText *text = ptstats->AddText("ECalDirectionCorrectedSimCaloHit");
   text->SetTextSize(0.0368);
   text = ptstats->AddText("Entries = 0      ");
   text = ptstats->AddText("Mean  =      0");
   text = ptstats->AddText("RMS   =      0");
   ptstats->SetOptStat(1111);
   ptstats->SetOptFit(0);
   ptstats->Draw();
   ECalDirectionCorrectedSimCaloHit->GetListOfFunctions()->Add(ptstats);
   ptstats->SetParent(ECalDirectionCorrectedSimCaloHit);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   ECalDirectionCorrectedSimCaloHit->SetLineColor(ci);
   ECalDirectionCorrectedSimCaloHit->GetXaxis()->SetTitle("Direction Corrected SimCaloHit Measurement");
   ECalDirectionCorrectedSimCaloHit->GetXaxis()->SetLabelFont(42);
   ECalDirectionCorrectedSimCaloHit->GetXaxis()->SetLabelSize(0.035);
   ECalDirectionCorrectedSimCaloHit->GetXaxis()->SetTitleSize(0.035);
   ECalDirectionCorrectedSimCaloHit->GetXaxis()->SetTitleFont(42);
   ECalDirectionCorrectedSimCaloHit->GetYaxis()->SetTitle("Entries");
   ECalDirectionCorrectedSimCaloHit->GetYaxis()->SetLabelFont(42);
   ECalDirectionCorrectedSimCaloHit->GetYaxis()->SetLabelSize(0.035);
   ECalDirectionCorrectedSimCaloHit->GetYaxis()->SetTitleSize(0.035);
   ECalDirectionCorrectedSimCaloHit->GetYaxis()->SetTitleFont(42);
   ECalDirectionCorrectedSimCaloHit->GetZaxis()->SetLabelFont(42);
   ECalDirectionCorrectedSimCaloHit->GetZaxis()->SetLabelSize(0.035);
   ECalDirectionCorrectedSimCaloHit->GetZaxis()->SetTitleSize(0.035);
   ECalDirectionCorrectedSimCaloHit->GetZaxis()->SetTitleFont(42);
   ECalDirectionCorrectedSimCaloHit->Draw("");
   
   TPaveText *pt = new TPaveText(0.15,0.9356275,0.85,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   text = pt->AddText("Distribution of Direction Corrected SimCaloHits in the ECal (1==nPfoTargetsTotal && 1==nPfoTargetsTracks)");
   pt->Draw();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_ECal->Modified();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_ECal->cd();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_ECal->SetSelected(Direction_Corrected_SimCalorimeterHit_Energy_Distribution_ECal);
}
