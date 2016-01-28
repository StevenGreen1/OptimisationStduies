{
//=========Macro generated from canvas: Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal/Direction Corrected SimCalorimeterHit Energy Distribution HCal
//=========  (Thu Jan 28 10:27:32 2016) by ROOT version5.34/30
   TCanvas *Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal = new TCanvas("Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal", "Direction Corrected SimCalorimeterHit Energy Distribution HCal",0,0,5000,5000);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal->SetHighLightColor(2);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal->Range(0,0,1,1);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal->SetFillColor(0);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal->SetBorderMode(0);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal->SetBorderSize(2);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal->SetFrameBorderMode(0);
  
// ------------>Primitives in pad: Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_1
   TPad *Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_1 = new TPad("Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_1", "Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_1",0.01,0.6766667,0.99,0.99);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_1->Draw();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_1->cd();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_1->Range(-0.000125,-0.13125,0.001125,1.18125);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_1->SetFillColor(0);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_1->SetBorderMode(0);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_1->SetBorderSize(2);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_1->SetFrameBorderMode(0);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_1->SetFrameBorderMode(0);
   
   TH1F *HCalDirectionCorrectedSimCaloHitBarrel = new TH1F("HCalDirectionCorrectedSimCaloHitBarrel","Distribution of Direction Corrected SimCaloHits in the HCal Barrel (1==nPfoTargetsTotal && 1==nPfoTargetsTracks)",200,0,0.001);
   
   TPaveStats *ptstats = new TPaveStats(0.78,0.775,0.98,0.935,"brNDC");
   ptstats->SetName("stats");
   ptstats->SetBorderSize(1);
   ptstats->SetFillColor(0);
   ptstats->SetTextAlign(12);
   ptstats->SetTextFont(42);
   TText *text = ptstats->AddText("HCalDirectionCorrectedSimCaloHitBarrel");
   text->SetTextSize(0.0368);
   text = ptstats->AddText("Entries = 0      ");
   text = ptstats->AddText("Mean  =      0");
   text = ptstats->AddText("RMS   =      0");
   ptstats->SetOptStat(1111);
   ptstats->SetOptFit(0);
   ptstats->Draw();
   HCalDirectionCorrectedSimCaloHitBarrel->GetListOfFunctions()->Add(ptstats);
   ptstats->SetParent(HCalDirectionCorrectedSimCaloHitBarrel);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   HCalDirectionCorrectedSimCaloHitBarrel->SetLineColor(ci);
   HCalDirectionCorrectedSimCaloHitBarrel->GetXaxis()->SetTitle("Direction Corrected SimCaloHit Measurement");
   HCalDirectionCorrectedSimCaloHitBarrel->GetXaxis()->SetLabelFont(42);
   HCalDirectionCorrectedSimCaloHitBarrel->GetXaxis()->SetLabelSize(0.035);
   HCalDirectionCorrectedSimCaloHitBarrel->GetXaxis()->SetTitleSize(0.035);
   HCalDirectionCorrectedSimCaloHitBarrel->GetXaxis()->SetTitleFont(42);
   HCalDirectionCorrectedSimCaloHitBarrel->GetYaxis()->SetTitle("Entries");
   HCalDirectionCorrectedSimCaloHitBarrel->GetYaxis()->SetLabelFont(42);
   HCalDirectionCorrectedSimCaloHitBarrel->GetYaxis()->SetLabelSize(0.035);
   HCalDirectionCorrectedSimCaloHitBarrel->GetYaxis()->SetTitleSize(0.035);
   HCalDirectionCorrectedSimCaloHitBarrel->GetYaxis()->SetTitleFont(42);
   HCalDirectionCorrectedSimCaloHitBarrel->GetZaxis()->SetLabelFont(42);
   HCalDirectionCorrectedSimCaloHitBarrel->GetZaxis()->SetLabelSize(0.035);
   HCalDirectionCorrectedSimCaloHitBarrel->GetZaxis()->SetTitleSize(0.035);
   HCalDirectionCorrectedSimCaloHitBarrel->GetZaxis()->SetTitleFont(42);
   HCalDirectionCorrectedSimCaloHitBarrel->Draw("");
   
   TPaveText *pt = new TPaveText(0.15,0.9349189,0.85,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   text = pt->AddText("Distribution of Direction Corrected SimCaloHits in the HCal Barrel (1==nPfoTargetsTotal && 1==nPfoTargetsTracks)");
   pt->Draw();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_1->Modified();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal->cd();
  
// ------------>Primitives in pad: Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_2
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_2 = new TPad("Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_2", "Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_2",0.01,0.3433333,0.99,0.6566667);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_2->Draw();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_2->cd();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_2->Range(-0.000125,-0.13125,0.001125,1.18125);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_2->SetFillColor(0);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_2->SetBorderMode(0);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_2->SetBorderSize(2);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_2->SetFrameBorderMode(0);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_2->SetFrameBorderMode(0);
   
   TH1F *HCalDirectionCorrectedSimCaloHitEndCap = new TH1F("HCalDirectionCorrectedSimCaloHitEndCap","Distribution of Direction Corrected SimCaloHits in the HCal EndCap (1==nPfoTargetsTotal && 1==nPfoTargetsTracks)",200,0,0.001);
   
   ptstats = new TPaveStats(0.78,0.775,0.98,0.935,"brNDC");
   ptstats->SetName("stats");
   ptstats->SetBorderSize(1);
   ptstats->SetFillColor(0);
   ptstats->SetTextAlign(12);
   ptstats->SetTextFont(42);
   text = ptstats->AddText("HCalDirectionCorrectedSimCaloHitEndCap");
   text->SetTextSize(0.0368);
   text = ptstats->AddText("Entries = 0      ");
   text = ptstats->AddText("Mean  =      0");
   text = ptstats->AddText("RMS   =      0");
   ptstats->SetOptStat(1111);
   ptstats->SetOptFit(0);
   ptstats->Draw();
   HCalDirectionCorrectedSimCaloHitEndCap->GetListOfFunctions()->Add(ptstats);
   ptstats->SetParent(HCalDirectionCorrectedSimCaloHitEndCap);

   ci = TColor::GetColor("#000099");
   HCalDirectionCorrectedSimCaloHitEndCap->SetLineColor(ci);
   HCalDirectionCorrectedSimCaloHitEndCap->GetXaxis()->SetTitle("Direction Corrected SimCaloHit Measurement");
   HCalDirectionCorrectedSimCaloHitEndCap->GetXaxis()->SetLabelFont(42);
   HCalDirectionCorrectedSimCaloHitEndCap->GetXaxis()->SetLabelSize(0.035);
   HCalDirectionCorrectedSimCaloHitEndCap->GetXaxis()->SetTitleSize(0.035);
   HCalDirectionCorrectedSimCaloHitEndCap->GetXaxis()->SetTitleFont(42);
   HCalDirectionCorrectedSimCaloHitEndCap->GetYaxis()->SetTitle("Entries");
   HCalDirectionCorrectedSimCaloHitEndCap->GetYaxis()->SetLabelFont(42);
   HCalDirectionCorrectedSimCaloHitEndCap->GetYaxis()->SetLabelSize(0.035);
   HCalDirectionCorrectedSimCaloHitEndCap->GetYaxis()->SetTitleSize(0.035);
   HCalDirectionCorrectedSimCaloHitEndCap->GetYaxis()->SetTitleFont(42);
   HCalDirectionCorrectedSimCaloHitEndCap->GetZaxis()->SetLabelFont(42);
   HCalDirectionCorrectedSimCaloHitEndCap->GetZaxis()->SetLabelSize(0.035);
   HCalDirectionCorrectedSimCaloHitEndCap->GetZaxis()->SetTitleSize(0.035);
   HCalDirectionCorrectedSimCaloHitEndCap->GetZaxis()->SetTitleFont(42);
   HCalDirectionCorrectedSimCaloHitEndCap->Draw("");
   
   pt = new TPaveText(0.15,0.9349189,0.85,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   text = pt->AddText("Distribution of Direction Corrected SimCaloHits in the HCal EndCap (1==nPfoTargetsTotal && 1==nPfoTargetsTracks)");
   pt->Draw();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_2->Modified();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal->cd();
  
// ------------>Primitives in pad: Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_3
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_3 = new TPad("Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_3", "Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_3",0.01,0.01,0.99,0.3233333);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_3->Draw();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_3->cd();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_3->Range(-0.000625,-0.13125,0.005625,1.18125);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_3->SetFillColor(0);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_3->SetBorderMode(0);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_3->SetBorderSize(2);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_3->SetFrameBorderMode(0);
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_3->SetFrameBorderMode(0);
   
   TH1F *HCalDirectionCorrectedSimCaloHitOther = new TH1F("HCalDirectionCorrectedSimCaloHitOther","Distribution of Direction Corrected SimCaloHits in the HCal Other (1==nPfoTargetsTotal && 1==nPfoTargetsTracks)",200,0,0.005);
   
   ptstats = new TPaveStats(0.78,0.775,0.98,0.935,"brNDC");
   ptstats->SetName("stats");
   ptstats->SetBorderSize(1);
   ptstats->SetFillColor(0);
   ptstats->SetTextAlign(12);
   ptstats->SetTextFont(42);
   text = ptstats->AddText("HCalDirectionCorrectedSimCaloHitOther");
   text->SetTextSize(0.0368);
   text = ptstats->AddText("Entries = 0      ");
   text = ptstats->AddText("Mean  =      0");
   text = ptstats->AddText("RMS   =      0");
   ptstats->SetOptStat(1111);
   ptstats->SetOptFit(0);
   ptstats->Draw();
   HCalDirectionCorrectedSimCaloHitOther->GetListOfFunctions()->Add(ptstats);
   ptstats->SetParent(HCalDirectionCorrectedSimCaloHitOther);

   ci = TColor::GetColor("#000099");
   HCalDirectionCorrectedSimCaloHitOther->SetLineColor(ci);
   HCalDirectionCorrectedSimCaloHitOther->GetXaxis()->SetTitle("Direction Corrected SimCaloHit Measurement");
   HCalDirectionCorrectedSimCaloHitOther->GetXaxis()->SetLabelFont(42);
   HCalDirectionCorrectedSimCaloHitOther->GetXaxis()->SetLabelSize(0.035);
   HCalDirectionCorrectedSimCaloHitOther->GetXaxis()->SetTitleSize(0.035);
   HCalDirectionCorrectedSimCaloHitOther->GetXaxis()->SetTitleFont(42);
   HCalDirectionCorrectedSimCaloHitOther->GetYaxis()->SetTitle("Entries");
   HCalDirectionCorrectedSimCaloHitOther->GetYaxis()->SetLabelFont(42);
   HCalDirectionCorrectedSimCaloHitOther->GetYaxis()->SetLabelSize(0.035);
   HCalDirectionCorrectedSimCaloHitOther->GetYaxis()->SetTitleSize(0.035);
   HCalDirectionCorrectedSimCaloHitOther->GetYaxis()->SetTitleFont(42);
   HCalDirectionCorrectedSimCaloHitOther->GetZaxis()->SetLabelFont(42);
   HCalDirectionCorrectedSimCaloHitOther->GetZaxis()->SetLabelSize(0.035);
   HCalDirectionCorrectedSimCaloHitOther->GetZaxis()->SetTitleSize(0.035);
   HCalDirectionCorrectedSimCaloHitOther->GetZaxis()->SetTitleFont(42);
   HCalDirectionCorrectedSimCaloHitOther->Draw("");
   
   pt = new TPaveText(0.15,0.9349189,0.85,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   text = pt->AddText("Distribution of Direction Corrected SimCaloHits in the HCal Other (1==nPfoTargetsTotal && 1==nPfoTargetsTracks)");
   pt->Draw();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal_3->Modified();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal->cd();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal->Modified();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal->cd();
   Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal->SetSelected(Direction_Corrected_SimCalorimeterHit_Energy_Distribution_HCal);
}
