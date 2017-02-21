{
//=========Macro generated from canvas: c1/c1
//=========  (Sat May 28 11:11:32 2016) by ROOT version5.34/30
   TCanvas *c1 = new TCanvas("c1", "c1",10,32,700,500);
   gStyle->SetOptStat(0);
   c1->Range(0,0,1,1);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetTickx(1);
   c1->SetTicky(1);
   c1->SetFrameLineWidth(2);
   c1->SetFrameBorderMode(0);
   
   TH2F *axesEj = new TH2F("axesEj","10 GeV Photon Energy Resolution vs Number of Layers in ECal (Sc)",100,14,32,1000,5.4,8.2);
   axesEj->SetStats(0);
   axesEj->SetLineWidth(2);
   axesEj->SetMarkerStyle(20);
   axesEj->GetXaxis()->SetTitle("Number of ECal Layers");
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
   gre->SetPoint(0,30,5.631621);
   gre->SetPointError(0,0,0.0638466);
   gre->SetPoint(1,26,5.908011);
   gre->SetPointError(1,0,0.06430803);
   gre->SetPoint(2,20,6.898712);
   gre->SetPointError(2,0,0.0719096);
   gre->SetPoint(3,16,7.845701);
   gre->SetPointError(3,0,0.08262583);
   gre->Draw(" pl");
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
