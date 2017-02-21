{
//=========Macro generated from canvas: c1/c1
//=========  (Tue May 31 11:40:44 2016) by ROOT version5.34/30
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
   
   TH2F *axesEj = new TH2F("axesEj","100 GeV Photon Energy Resolution vs Number of Layers in ECal (Sc)",100,14,32,1000,2.4,3.8);
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

   // Scintillator - No Real Digi
   TGraphErrors *gre = new TGraphErrors(4);
   gre->SetName("Graph0");
   gre->SetTitle("Scintillator No Realistic Digitsation");
   gre->SetFillColor(0);
   gre->SetLineWidth(2);
   gre->SetLineStyle(2);
   gre->SetLineColor(kBlue);
   gre->SetMarkerStyle(20);
   gre->SetPoint(0,30,2.562965);
   gre->SetPointError(0,0,0.1217961);
   gre->SetPoint(1,26,3.085893);
   gre->SetPointError(1,0,0.1260904);
   gre->SetPoint(2,20,3.257795);
   gre->SetPointError(2,0,0.1400707);
   gre->SetPoint(3,16,3.222571);
   gre->SetPointError(3,0,0.1528007);
   gre->Draw(" pl");
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);

   // Silicon - No Real Digi
   TGraphErrors *gre = new TGraphErrors(4);
   gre->SetName("Graph0");
   gre->SetTitle("Silicon No Realistic Digitsation");
   gre->SetFillColor(0);
   gre->SetLineWidth(2);
   gre->SetLineColor(kBlue);
   gre->SetMarkerStyle(20);
   gre->SetPoint(0,30,2.571387);
   gre->SetPointError(0,0,0.05887271);
   gre->SetPoint(1,26,2.70673);
   gre->SetPointError(1,0,0.06553239);
   gre->SetPoint(2,20,3.027453);
   gre->SetPointError(2,0,0.08651062);
   gre->SetPoint(3,16,3.226278);
   gre->SetPointError(3,0,0.07909768);
   gre->Draw(" pl");
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);

   // Silicon - Real Digi
   TGraphErrors *gre = new TGraphErrors(4);
   gre->SetName("Graph0");
   gre->SetTitle("Silicon Realistic Digitsation");
   gre->SetFillColor(0);
   gre->SetLineWidth(2);
   gre->SetMarkerStyle(20);
   gre->SetPoint(0,30,2.589786);
   gre->SetPointError(0,0,0.05956549);
   gre->SetPoint(1,26,2.735755);
   gre->SetPointError(1,0,0.06401784);
   gre->SetPoint(2,20,2.990485);
   gre->SetPointError(2,0,0.08775328);
   gre->SetPoint(3,16,3.19947);
   gre->SetPointError(3,0,0.08651526);
   gre->Draw(" pl");
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);

   // Scintillator - Real Digi
   TGraphErrors *gre = new TGraphErrors(4);
   gre->SetName("Graph0");
   gre->SetTitle("Scintillator Realistic Digtisation");
   gre->SetFillColor(0);
   gre->SetLineWidth(2);
   gre->SetLineStyle(2);
   gre->SetMarkerStyle(20);
   gre->SetPoint(0,30,2.870869);
   gre->SetPointError(0,0,0.08241485);
   gre->SetPoint(1,26,2.936696);
   gre->SetPointError(1,0,0.08618624);
   gre->SetPoint(2,20,3.207647);
   gre->SetPointError(2,0,0.1478414);
   gre->SetPoint(3,16,3.486066);
   gre->SetPointError(3,0,0.1686523);
   gre->Draw(" pl");
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);


}
