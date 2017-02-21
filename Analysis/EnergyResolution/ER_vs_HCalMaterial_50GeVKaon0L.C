{
//=========Macro generated from canvas: c1_n2/c1_n2
//=========  (Tue Feb 21 10:43:08 2017) by ROOT version5.34/30
   TCanvas *c1_n2 = new TCanvas("c1_n2", "c1_n2",12,51,700,500);
   gStyle->SetOptStat(0);
   c1_n2->Range(0,0,1,1);
   c1_n2->SetFillColor(0);
   c1_n2->SetBorderMode(0);
   c1_n2->SetBorderSize(2);
   c1_n2->SetTickx(1);
   c1_n2->SetTicky(1);
   c1_n2->SetFrameLineWidth(2);
   c1_n2->SetFrameBorderMode(0);
   
   TH2F *axesEj = new TH2F("axesEj","50 GeV Kaon0L Energy Resolution vs HCal Material",100,0,5,1000,0,20);
   axesEj->SetStats(0);
   axesEj->SetLineWidth(2);
   axesEj->SetMarkerStyle(20);
   axesEj->GetXaxis()->SetTitle("HCal Material");
   axesEj->GetXaxis()->SetNdivisions(505);
   axesEj->GetXaxis()->SetLabelFont(132);
   axesEj->GetXaxis()->SetLabelSize(0.03);
   axesEj->GetXaxis()->SetTitleSize(0.036);
   axesEj->GetXaxis()->SetTitleFont(132);
   axesEj->GetYaxis()->SetTitle("#sigma_{Reco} / E_{Reco}");
   axesEj->GetYaxis()->SetLabelFont(132);
   axesEj->GetYaxis()->SetLabelSize(0.03);
   axesEj->GetYaxis()->SetTitleSize(0.036);
   axesEj->GetYaxis()->SetTitleFont(132);
   axesEj->GetZaxis()->SetLabelFont(132);
   axesEj->GetZaxis()->SetLabelSize(0.03);
   axesEj->GetZaxis()->SetTitleSize(0.036);
   axesEj->GetZaxis()->SetTitleFont(132);
   axesEj->Draw("");
   
   TGraphErrors *gre = new TGraphErrors(4);
   gre->SetName("Graph0");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);
   gre->SetLineWidth(2);
   gre->SetMarkerStyle(20);
   gre->SetPoint(0,1,10.7208);
   gre->SetPointError(0,0,0.1265632);
   gre->SetPoint(1,2,10.53864);
   gre->SetPointError(1,0,0.1298456);
   gre->SetPoint(2,3,12.7054);
   gre->SetPointError(2,0,0.2064619);
   gre->SetPoint(3,4,12.90654);
   gre->SetPointError(3,0,0.2062716);
   gre->Draw(" pl");
   c1_n2->Modified();
   c1_n2->cd();
   c1_n2->SetSelected(c1_n2);
}
