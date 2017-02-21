{
//=========Macro generated from canvas: c1_n3/c1_n3
//=========  (Tue Feb 21 10:43:08 2017) by ROOT version5.34/30
   TCanvas *c1_n3 = new TCanvas("c1_n3", "c1_n3",12,51,700,500);
   gStyle->SetOptStat(0);
   c1_n3->Range(30.5,-3.125,65.5,28.125);
   c1_n3->SetFillColor(0);
   c1_n3->SetBorderMode(0);
   c1_n3->SetBorderSize(2);
   c1_n3->SetTickx(1);
   c1_n3->SetTicky(1);
   c1_n3->SetFrameLineWidth(2);
   c1_n3->SetFrameBorderMode(0);
   c1_n3->SetFrameLineWidth(2);
   c1_n3->SetFrameBorderMode(0);
   
   TH2F *axesEj = new TH2F("axesEj","50 GeV Kaon0L Energy Resolution vs Number of Fixed Layers in HCal",100,34,62,1000,0,25);
   axesEj->SetStats(0);
   axesEj->SetLineWidth(2);
   axesEj->SetMarkerStyle(20);
   axesEj->GetXaxis()->SetTitle("Number of HCal Layers");
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
   
   TGraphErrors *gre = new TGraphErrors(5);
   gre->SetName("Graph0");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);
   gre->SetLineWidth(2);
   gre->SetMarkerStyle(20);
   gre->SetPoint(0,36,11.41395);
   gre->SetPointError(0,0,0.1500727);
   gre->SetPoint(1,42,10.87529);
   gre->SetPointError(1,0,0.1429474);
   gre->SetPoint(2,48,10.7208);
   gre->SetPointError(2,0,0.1265632);
   gre->SetPoint(3,54,10.08832);
   gre->SetPointError(3,0,0.1206454);
   gre->SetPoint(4,60,9.982009);
   gre->SetPointError(4,0,0.1207062);
   
   TH1F *Graph_Graph1 = new TH1F("Graph_Graph1","Graph",100,33.6,62.4);
   Graph_Graph1->SetMinimum(9.691032);
   Graph_Graph1->SetMaximum(11.73429);
   Graph_Graph1->SetDirectory(0);
   Graph_Graph1->SetStats(0);
   Graph_Graph1->SetLineWidth(2);
   Graph_Graph1->SetMarkerStyle(20);
   Graph_Graph1->GetXaxis()->SetNdivisions(505);
   Graph_Graph1->GetXaxis()->SetLabelFont(132);
   Graph_Graph1->GetXaxis()->SetLabelSize(0.03);
   Graph_Graph1->GetXaxis()->SetTitleSize(0.036);
   Graph_Graph1->GetXaxis()->SetTitleFont(132);
   Graph_Graph1->GetYaxis()->SetLabelFont(132);
   Graph_Graph1->GetYaxis()->SetLabelSize(0.03);
   Graph_Graph1->GetYaxis()->SetTitleSize(0.036);
   Graph_Graph1->GetYaxis()->SetTitleFont(132);
   Graph_Graph1->GetZaxis()->SetLabelFont(132);
   Graph_Graph1->GetZaxis()->SetLabelSize(0.03);
   Graph_Graph1->GetZaxis()->SetTitleSize(0.036);
   Graph_Graph1->GetZaxis()->SetTitleFont(132);
   gre->SetHistogram(Graph_Graph1);
   
   gre->Draw(" pl");
   
   TPaveText *pt = new TPaveText(0.01,0.9416102,0.71,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(1);
   pt->SetFillColor(0);
   pt->SetLineWidth(2);
   pt->SetTextFont(132);
   TText *text = pt->AddText("50 GeV Kaon0L Energy Resolution vs Number of Fixed Layers in HCal");
   pt->Draw();
   c1_n3->Modified();
   c1_n3->cd();
   c1_n3->SetSelected(c1_n3);
}
