{
//=========Macro generated from canvas: Canvas_1/Canvas_1
//=========  (Thu Feb 18 11:44:26 2016) by ROOT version5.34/30
   TCanvas *Canvas_1 = new TCanvas("Canvas_1", "Canvas_1",258,102,1633,827);
   gStyle->SetOptStat(0);
   Canvas_1->Range(12.5,0.01056588,33.5,0.06212792);
   Canvas_1->SetFillColor(0);
   Canvas_1->SetBorderMode(0);
   Canvas_1->SetBorderSize(2);
   Canvas_1->SetTickx(1);
   Canvas_1->SetTicky(1);
   Canvas_1->SetFrameLineWidth(2);
   Canvas_1->SetFrameBorderMode(0);
   Canvas_1->SetFrameLineWidth(2);
   Canvas_1->SetFrameBorderMode(0);
   
   TGraphErrors *gre = new TGraphErrors(4);
   gre->SetName("PhotonEnergyResolution");
   gre->SetTitle("Photon Energy Resolution");
   gre->SetLineWidth(2);
   gre->SetMarkerStyle(20);
   gre->SetPoint(0,30,0.01940704);
   gre->SetPointError(0,0,0.0002474928);
   gre->SetPoint(1,26,0.03129558);
   gre->SetPointError(1,0,0.0004430216);
   gre->SetPoint(2,20,0.04379452);
   gre->SetPointError(2,0,0.000512505);
   gre->SetPoint(3,16,0.05283291);
   gre->SetPointError(3,0,0.0007013328);
   
   TH1F *Graph_PhotonEnergyResolution1 = new TH1F("Graph_PhotonEnergyResolution1","Photon Energy Resolution",100,14.6,31.4);
   Graph_PhotonEnergyResolution1->SetMinimum(0.01572208);
   Graph_PhotonEnergyResolution1->SetMaximum(0.05697171);
   Graph_PhotonEnergyResolution1->SetDirectory(0);
   Graph_PhotonEnergyResolution1->SetStats(0);
   Graph_PhotonEnergyResolution1->SetLineWidth(2);
   Graph_PhotonEnergyResolution1->SetMarkerStyle(20);
   Graph_PhotonEnergyResolution1->GetXaxis()->SetTitle("Number of ECal Layers");
   Graph_PhotonEnergyResolution1->GetXaxis()->SetNdivisions(505);
   Graph_PhotonEnergyResolution1->GetXaxis()->SetLabelFont(132);
   Graph_PhotonEnergyResolution1->GetXaxis()->SetLabelSize(0.03);
   Graph_PhotonEnergyResolution1->GetXaxis()->SetTitleSize(0.036);
   Graph_PhotonEnergyResolution1->GetXaxis()->SetTitleFont(132);
   Graph_PhotonEnergyResolution1->GetYaxis()->SetTitle("#sigma_{reco} / E_{reco}");
   Graph_PhotonEnergyResolution1->GetYaxis()->SetLabelFont(132);
   Graph_PhotonEnergyResolution1->GetYaxis()->SetLabelSize(0.03);
   Graph_PhotonEnergyResolution1->GetYaxis()->SetTitleSize(0.036);
   Graph_PhotonEnergyResolution1->GetYaxis()->SetTitleFont(132);
   Graph_PhotonEnergyResolution1->GetZaxis()->SetLabelFont(132);
   Graph_PhotonEnergyResolution1->GetZaxis()->SetLabelSize(0.03);
   Graph_PhotonEnergyResolution1->GetZaxis()->SetTitleSize(0.036);
   Graph_PhotonEnergyResolution1->GetZaxis()->SetTitleFont(132);
   gre->SetHistogram(Graph_PhotonEnergyResolution1);
   
   gre->Draw("alp");
   
   TPaveText *pt = new TPaveText(0.01,0.9439672,0.2761633,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(1);
   pt->SetFillColor(0);
   pt->SetLineWidth(2);
   pt->SetTextFont(132);
   TText *text = pt->AddText("Photon Energy Resolution");
   pt->Draw();
   Canvas_1->Modified();
   Canvas_1->cd();
   Canvas_1->SetSelected(Canvas_1);
}
