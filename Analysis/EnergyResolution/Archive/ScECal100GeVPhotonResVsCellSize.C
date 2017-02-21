{
//=========Macro generated from canvas: c1/c1
//=========  (Tue May 31 12:29:50 2016) by ROOT version5.34/30
   TCanvas *c1 = new TCanvas("c1", "c1",12,51,700,500);
   gStyle->SetOptStat(0);
   c1->Range(0,0,1,1);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetTickx(1);
   c1->SetTicky(1);
   c1->SetFrameLineWidth(2);
   c1->SetFrameBorderMode(0);
   
   TH2F *axesEj = new TH2F("axesEj","100 GeV Photon Energy Resolution vs Cell Size in ECal (Sc)",100,0,25,1000,0,5);
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
   gre->SetPoint(0,3,2.968634);
   gre->SetPointError(0,0,0.1355989);
   gre->SetPoint(1,5,2.653211);
   gre->SetPointError(1,0,0.0721394);
   gre->SetPoint(2,7,2.746706);
   gre->SetPointError(2,0,0.06947832);
   gre->SetPoint(3,10,2.636897);
   gre->SetPointError(3,0,0.03522774);
   gre->SetPoint(4,15,2.512898);
   gre->SetPointError(4,0,0.02927103);
   gre->SetPoint(5,20,2.331064);
   gre->SetPointError(5,0,0.02587937);
   gre->Draw(" pl");
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
