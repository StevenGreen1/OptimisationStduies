{
//=========Macro generated from canvas: c1_n3/c1_n3
//=========  (Tue Feb 21 11:39:38 2017) by ROOT version5.34/30
   TCanvas *c1_n3 = new TCanvas("c1_n3", "c1_n3",12,51,700,500);
   gStyle->SetOptStat(0);
   c1_n3->Range(0,0,1,1);
   c1_n3->SetFillColor(0);
   c1_n3->SetBorderMode(0);
   c1_n3->SetBorderSize(2);
   c1_n3->SetTickx(1);
   c1_n3->SetTicky(1);
   c1_n3->SetFrameLineWidth(2);
   c1_n3->SetFrameBorderMode(0);
   
   TH2F *axesEj = new TH2F("axesEj","100 GeV Photon Energy Resolution vs Cell Size in ECal (Si)",100,0,25,1000,0,5);
   axesEj->SetStats(0);
   axesEj->SetLineWidth(2);
   axesEj->SetMarkerStyle(20);
   axesEj->GetXaxis()->SetTitle("ECal Cell Size [mm]");
   axesEj->GetXaxis()->SetNdivisions(505);
   axesEj->GetXaxis()->SetLabelFont(132);
   axesEj->GetXaxis()->SetLabelSize(0.03);
   axesEj->GetXaxis()->SetTitleSize(0.036);
   axesEj->GetXaxis()->SetTitleFont(132);
   axesEj->GetYaxis()->SetTitle("#sigma_{Reco} / E_{Reco} [%]");
   axesEj->GetYaxis()->SetLabelFont(132);
   axesEj->GetYaxis()->SetLabelSize(0.03);
   axesEj->GetYaxis()->SetTitleSize(0.036);
   axesEj->GetYaxis()->SetTitleFont(132);
   axesEj->GetZaxis()->SetLabelFont(132);
   axesEj->GetZaxis()->SetLabelSize(0.03);
   axesEj->GetZaxis()->SetTitleSize(0.036);
   axesEj->GetZaxis()->SetTitleFont(132);
   axesEj->Draw("");
   
   TGraphErrors *gre = new TGraphErrors(6);
   gre->SetName("Graph0");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);
   gre->SetLineWidth(2);
   gre->SetMarkerStyle(20);
   gre->SetPoint(0,3,2.279611);
   gre->SetPointError(0,0,0.1088644);
   gre->SetPoint(1,5,2.242834);
   gre->SetPointError(1,0,0.05860003);
   gre->SetPoint(2,7,2.30786);
   gre->SetPointError(2,0,0.03700382);
   gre->SetPoint(3,10,2.421574);
   gre->SetPointError(3,0,0.0304779);
   gre->SetPoint(4,15,2.440132);
   gre->SetPointError(4,0,0.02984348);
   gre->SetPoint(5,20,2.506358);
   gre->SetPointError(5,0,0.02963816);
   gre->Draw(" pl");
   c1_n3->Modified();
   c1_n3->cd();
   c1_n3->SetSelected(c1_n3);
}
