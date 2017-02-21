#!/usr/bin/python/Results

# -*- coding: utf-8 -*-

import sys
import re
import math
import os
from collections import defaultdict

#===== Start of Results Class =====

class Results:
    m_HadronicEnergyTrunc = defaultdict(dict)
    m_HadronicEnergyTrunc = {38:1, 69:0.5, 70:0.75, 71:1, 72:1.5, 73:2, 74:5, 75:10, 76:1000000, 77:0.5, 78:0.75, 79:1, 80:1.5, 81:2, 82:5, 83:10, 84:1000000}

    m_RecoVarFromTrunc = defaultdict(dict)
    m_RecoVarFromTrunc = {0.5:69, 0.75:70, 1:71, 1.5:72, 2:73, 5:74, 10:75, 1000000:76}

    m_PandoraSettings = ['Default','PerfectPhoton','PerfectPhotonNK0L','PerfectPFA']

    m_DetectorLabel = defaultdict(dict)
    m_DetectorLabel = {85:'Steel HCal Absorber Material, QGSP_BERT', 46:'Steel HCal Absorber Material, QGSP_BERT_HP', 47:'Tungsten HCal Absorber Material, QGSP_BERT', 48:'Tungsten HCal Absorber Material, QGSP_BERT_HP'}

#==================== 

    def __init__(self, resultsName, detectorModelList, xAxisPlottingList, xAxisTitle, reconstructionVariantList, jetEnergyList, algorithm, fixedRecoVar):
        self.resultsName = resultsName
        self.detectorModelList = detectorModelList
        self.xAxisPlottingList = xAxisPlottingList

        self.xAxisPlottingList = xAxisPlottingList
        self.minXAxis = xAxisPlottingList[0] - (xAxisPlottingList[1] - xAxisPlottingList[0])
        self.maxXAxis = xAxisPlottingList[-1] + (xAxisPlottingList[-2] - xAxisPlottingList[-3])

        self.xAxisTitle = xAxisTitle
        self.reconstructionVariantList = reconstructionVariantList
        self.jetEnergyList = jetEnergyList
        self.algorithm = algorithm
        detectorModelFromPlotting = defaultdict(dict)
        for idx, xAxisPlotting in enumerate(xAxisPlottingList):
            detectorModelFromPlotting[(xAxisPlotting)] = detectorModelList[idx]
        self.detectorModelFromPlotting = detectorModelFromPlotting

        self.fixedRecoVar = fixedRecoVar

#==================== 

    def readData(self):
        NumberOfEvents = defaultdict(dict)
        JER = defaultdict(dict)
        JERError = defaultdict(dict)
        for pandoraSettings in Results.m_PandoraSettings:
            for idx, detectorModel in enumerate(self.detectorModelList):
                reconstructionVariant = self.reconstructionVariantList[idx]
                for jetEnergy in self.jetEnergyList:
                    JER[(detectorModel,reconstructionVariant,jetEnergy,pandoraSettings)] = -1
                    JERError[(detectorModel,reconstructionVariant,jetEnergy,pandoraSettings)] = 0
                    fileName = '/r02/lc/sg568/OptimisationStudies/MarlinJobs/Detector_Model_' + str(detectorModel) + '/Reconstruction_Variant_' + str(reconstructionVariant) + '/Z_uds/' + str(jetEnergy) + 'GeV/PandoraSettings' + pandoraSettings + '/AnalysePerformance_PandoraSettings' + pandoraSettings + '_DetectorModel_' + str(detectorModel) + '_Reconstruction_Variant_' + str(reconstructionVariant) + '_Z_uds_' + str(jetEnergy) + 'GeV.txt'
                    if os.path.isfile(fileName):
                        file = open(fileName)
                        allLines = file.readlines()
                        for line in allLines:
                            regex = re.compile("fPFA_L7A \((\d+) entries\)(.*?)sE\/E: (\d\.\d+)\+\-(\d\.\d+)")
                            searchResults = regex.search(line)
                            if searchResults is not None:
                                NumberOfEvents[(detectorModel,reconstructionVariant,jetEnergy,pandoraSettings)] = int(searchResults.group(1))
                                JER[(detectorModel,reconstructionVariant,jetEnergy,pandoraSettings)] = float(searchResults.group(3))
                                JERError[(detectorModel,reconstructionVariant,jetEnergy,pandoraSettings)] = float(searchResults.group(4))
                    else:
                        print 'Missing file: ' + fileName

        self.NumberOfEvents = NumberOfEvents
        self.JER = JER
        self.JERError = JERError

#====================

    def generateConfusionTerms(self):
        for idx, detectorModel in enumerate(self.detectorModelList):
            reconstructionVariant = self.reconstructionVariantList[idx]
            for jetEnergy in self.jetEnergyList:
                # Total Confusion
                JER = defaultdict(dict)
                JER[(detectorModel,reconstructionVariant,jetEnergy,'TotalConfusion')] = math.sqrt( math.fabs( (self.JER[(detectorModel,reconstructionVariant,jetEnergy,'Default')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'Default')]) - (self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPFA')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPFA')]) ) )
                self.JER.update(JER)
                JER.clear()

                JERError = defaultdict(dict)
                JERError[(detectorModel,reconstructionVariant,jetEnergy,'TotalConfusion')] = math.sqrt( math.fabs( ( (self.JERError[(detectorModel,reconstructionVariant,jetEnergy,'Default')] * self.JERError[(detectorModel,reconstructionVariant,jetEnergy,'Default')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'Default')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'Default')]) / (self.JER[(detectorModel,reconstructionVariant,jetEnergy,'TotalConfusion')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'TotalConfusion')]) ) - ( (self.JERError[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPFA')] * self.JERError[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPFA')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPFA')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPFA')]) / (self.JER[(detectorModel,reconstructionVariant,jetEnergy,'TotalConfusion')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'TotalConfusion')]) ) ) )
                self.JERError.update(JERError)
                JERError.clear()

                # Photon Confusion
                JER[(detectorModel,reconstructionVariant,jetEnergy,'PhotonConfusion')] = math.sqrt( math.fabs( (self.JER[(detectorModel,reconstructionVariant,jetEnergy,'Default')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'Default')]) - (self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhoton')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhoton')]) ) )
                self.JER.update(JER)
                JER.clear()

                JERError[(detectorModel,reconstructionVariant,jetEnergy,'PhotonConfusion')] = math.sqrt( math.fabs( ( (self.JERError[(detectorModel,reconstructionVariant,jetEnergy,'Default')] * self.JERError[(detectorModel,reconstructionVariant,jetEnergy,'Default')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'Default')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'Default')]) / (self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PhotonConfusion')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PhotonConfusion')]) ) - ( (self.JERError[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhoton')] * self.JERError[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhoton')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhoton')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhoton')]) / (self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PhotonConfusion')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PhotonConfusion')]) ) ) )
                self.JERError.update(JERError)
                JERError.clear()

                # Neutral Hadron Confusion
                JER[(detectorModel,reconstructionVariant,jetEnergy,'NeutralHadronConfusion')] = math.sqrt( math.fabs( (self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhoton')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhoton')]) - (self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhotonNK0L')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhotonNK0L')]) ) )
                self.JER.update(JER)
                JER.clear()

                JERError[(detectorModel,reconstructionVariant,jetEnergy,'NeutralHadronConfusion')] = math.sqrt( math.fabs( ( (self.JERError[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhoton')] * self.JERError[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhoton')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhoton')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhoton')]) / (self.JER[(detectorModel,reconstructionVariant,jetEnergy,'NeutralHadronConfusion')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'NeutralHadronConfusion')]) ) - ( (self.JERError[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhotonNK0L')] * self.JERError[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhotonNK0L')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhotonNK0L')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhotonNK0L')]) / (self.JER[(detectorModel,reconstructionVariant,jetEnergy,'NeutralHadronConfusion')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'NeutralHadronConfusion')]) ) ) )
                self.JERError.update(JERError)
                JERError.clear()

                # Other Confusion
                JER[(detectorModel,reconstructionVariant,jetEnergy,'OtherConfusion')] = math.sqrt( math.fabs( (self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhotonNK0L')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhotonNK0L')]) - (self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPFA')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPFA')]) ) )
                self.JER.update(JER)
                JER.clear()

                JERError[(detectorModel,reconstructionVariant,jetEnergy,'OtherConfusion')] = math.sqrt( math.fabs( ( (self.JERError[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhotonNK0L')] * self.JERError[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhotonNK0L')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhotonNK0L')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPhotonNK0L')]) / (self.JER[(detectorModel,reconstructionVariant,jetEnergy,'OtherConfusion')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'OtherConfusion')]) ) - ( (self.JERError[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPFA')] * self.JERError[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPFA')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPFA')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'PerfectPFA')]) / (self.JER[(detectorModel,reconstructionVariant,jetEnergy,'OtherConfusion')] * self.JER[(detectorModel,reconstructionVariant,jetEnergy,'OtherConfusion')]) ) ) )
                self.JERError.update(JERError)
                JERError.clear()

#====================

    def optimiseData(self):
        if self.algorithm:
            if 'HCal Cell' in self.resultsName:
                optimalRecoVar = defaultdict(dict)
                optimalRecoVar = { 39:self.m_RecoVarFromTrunc[(0.5)], 40:self.m_RecoVarFromTrunc[(0.75)], 38:self.m_RecoVarFromTrunc[(1)], 41:self.m_RecoVarFromTrunc[(1.5)], 42:self.m_RecoVarFromTrunc[(2)], 43:self.m_RecoVarFromTrunc[(5)], 85:self.m_RecoVarFromTrunc[(1)] }
                self.optimalRecoVar = optimalRecoVar
            else:
                print 'Please speicify optimised energy truncations.'

        else:
            optimalRecoVar = defaultdict(dict)

            for detectorModel in self.detectorModelList:
                optimalRecoVar[(detectorModel)] = self.fixedRecoVar

            self.optimalRecoVar = optimalRecoVar

#==================== 

    def analyseOptimalData(self):
        for detectorModel in self.detectorModelList:
            print 'For detector model ' + str(detectorModel) + ' the optimal reconstruction variant is ' + str(self.optimalRecoVar[(detectorModel)]) + '.'
            print 'This corresponds to an energy truncation of ' + str(Results.m_HadronicEnergyTrunc[(self.optimalRecoVar[(detectorModel)])])
            print '\n'
            print '======================================================================'
            print '| RecoVar\Energy | 91 GeV | 200 GeV | 360 GeV | 500 GeV | Truncation |'
            print '======================================================================'
            for reconstructionVariant in self.reconstructionVariantList:
                printString = '| ' + str(reconstructionVariant) + ' | '  
                printString += str(self.JER[(detectorModel,reconstructionVariant,91,'Default')]) + ' |'
                printString += str(self.JER[(detectorModel,reconstructionVariant,200,'Default')]) + ' |'
                printString += str(self.JER[(detectorModel,reconstructionVariant,360,'Default')]) + ' |'
                printString += str(self.JER[(detectorModel,reconstructionVariant,500,'Default')]) + ' |'
                printString += str(Results.m_HadronicEnergyTrunc[reconstructionVariant]) + ' |'
                print printString
            print '======================================================================'

#==================== 

    def printData(self):
        print 'Jet energy resolutions : '
        print self.JER
        print 'Jet energy resolution errors : '
        print self.JERError
        print 'Number of events : '
        print self.NumberOfEvents

#==================== 

    def plotData(self):
        pandoraSettings = 'Default'

        saveString = '{\n'
        saveString += '    gStyle->SetOptStat(0);\n\n'

        saveString += '    TCanvas *pCanvasEj = new TCanvas();\n'
        saveString += '    pCanvasEj->cd();\n\n'

        saveString += '    TH2F *pAxesEj = new TH2F("axesEj","",1200,' + str(self.minXAxis) + ',' + str(self.maxXAxis) + ',12000,0,6.5);\n'
        saveString += '    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");\n'
        saveString += '    pAxesEj->GetXaxis()->SetTitle("' + self.xAxisTitle + '");\n'
        saveString += '    pAxesEj->Draw();\n\n'

        saveString += '    float xAxisVairable[' + str(len(self.xAxisPlottingList)) + '] = {'
        for idx, xAxisPlotting in enumerate(self.xAxisPlottingList):
            saveString += str(xAxisPlotting)
            if xAxisPlotting is not self.xAxisPlottingList[-1]:
                saveString += ','
        saveString += '};\n\n'

        saveString += '    float xAxisVairableError[' + str(len(self.xAxisPlottingList)) + '] = {'

        for xAxisPlotting in self.xAxisPlottingList:
            saveString += str(0)
            if xAxisPlotting is not self.xAxisPlottingList[-1]:
                saveString += ','
        saveString += '};\n\n'

        for jetEnergy in self.jetEnergyList:
            saveString += '    float Jet_Energy_' + str(jetEnergy) + 'GeV_JER[' + str(len(self.xAxisPlottingList)) + '] = {'
            for xAxisPlotting in self.xAxisPlottingList:
                detectorModel = self.detectorModelFromPlotting[(xAxisPlotting)]
                optimalRecoVar = self.optimalRecoVar[(detectorModel)]
                saveString += str(self.JER[(detectorModel,optimalRecoVar,jetEnergy,pandoraSettings)])
                if xAxisPlotting is not self.xAxisPlottingList[-1]:
                    saveString += ','
            saveString += '};\n\n'

        for jetEnergy in self.jetEnergyList:
            saveString += '    float Jet_Energy_' + str(jetEnergy) + 'GeV_JERError[' + str(len(self.xAxisPlottingList)) + '] = {'
            for xAxisPlotting in self.xAxisPlottingList:
                detectorModel = self.detectorModelFromPlotting[(xAxisPlotting)]
                optimalRecoVar = self.optimalRecoVar[(detectorModel)]
                saveString += str(self.JERError[(detectorModel,optimalRecoVar,jetEnergy,pandoraSettings)])
                if xAxisPlotting is not self.xAxisPlottingList[-1]:
                    saveString += ','
            saveString += '};\n\n'

        rootLineColor = ['4','2','6','1',]
        #rootLineStyle = ['1','2','3','4','5','6']

        saveString += '    TLegend *pLegend = new TLegend(0.6, 0.6, 0.9, 0.9);\n'

        for energyIdx, jetEnergy in enumerate(self.jetEnergyList):
            saveString += '    TGraphErrors *pTGraphErrors_Jet_Energy_' + str(jetEnergy) + ' = new TGraphErrors(' + str(len(self.xAxisPlottingList)) + ',xAxisVairable,Jet_Energy_' + str(jetEnergy) + 'GeV_JER,xAxisVairableError,Jet_Energy_' + str(jetEnergy) + 'GeV_JERError);\n\n'
            saveString += '    pTGraphErrors_Jet_Energy_' + str(jetEnergy) + '->SetLineColor(' + rootLineColor[energyIdx] + ');\n'
            saveString += '    pTGraphErrors_Jet_Energy_' + str(jetEnergy) + '->SetMarkerColor(' + rootLineColor[energyIdx] + ');\n'
            saveString += '    pTGraphErrors_Jet_Energy_' + str(jetEnergy) + '->Draw("lp,same");\n\n'
            saveString += '    pLegend->AddEntry(pTGraphErrors_Jet_Energy_' + str(jetEnergy) + ', "' + str(jetEnergy/2) + ' GeV Jets", "lp");\n\n'

        saveString += '    pLegend->SetFillStyle(0);\n'
        saveString += '    pLegend->Draw("same");\n'
        saveString += '    pCanvasEj->SaveAs("JER_vs_' + str(self.resultsName.replace(' ', '')) + '.pdf");\n'
        saveString += '}\n'

        #===== Write out file =====#
        resultsFile = open("JER_vs_" + str(self.resultsName.replace(' ', '')) + ".C", "w")
        resultsFile.write(saveString)
        resultsFile.close()

#====================

    def plotDataVsJetEnergy(self):
        pandoraSettings = 'Default'

        saveString = '{\n'
        saveString += '    gStyle->SetOptStat(0);\n\n'

        saveString += '    TCanvas *pCanvasEj = new TCanvas();\n'
        saveString += '    pCanvasEj->cd();\n\n'

        saveString += '    TH2F *pAxesEj = new TH2F("axesEj","",300,0,300,650,0,6.5);\n'
        saveString += '    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");\n'
        saveString += '    pAxesEj->GetXaxis()->SetTitle("E_{j} [GeV]");\n'
        saveString += '    pAxesEj->Draw();\n\n'

        saveString += '    float jetEnergy[' + str(len(self.jetEnergyList)) + '] = {'
        for jetEnergy in self.jetEnergyList:
            saveString += str(float(jetEnergy)/2)
            if jetEnergy is not self.jetEnergyList[-1]:
                saveString += ','
        saveString += '};\n\n'

        saveString += '    float jetEnergyError[' + str(len(self.jetEnergyList)) + '] = {'
        for jetEnergy in self.jetEnergyList:
            saveString += str(0)
            if jetEnergy is not self.jetEnergyList[-1]:
                saveString += ','
        saveString += '};\n\n'

        for xAxisPlotting in self.xAxisPlottingList:
            saveString += '    float Variable_' + str(xAxisPlotting) + '_JER[' + str(len(self.jetEnergyList)) + '] = {'
            detectorModel = self.detectorModelFromPlotting[(xAxisPlotting)]
            optimalRecoVar = self.optimalRecoVar[(detectorModel)]
            for jetEnergy in self.jetEnergyList:
                saveString += str(self.JER[(detectorModel,optimalRecoVar,jetEnergy,pandoraSettings)])
                if jetEnergy is not self.jetEnergyList[-1]:
                    saveString += ','
            saveString += '};\n\n'

        for xAxisPlotting in self.xAxisPlottingList:
            saveString += '    float Variable_' + str(xAxisPlotting) + '_JERError[' + str(len(self.jetEnergyList)) + '] = {'
            detectorModel = self.detectorModelFromPlotting[(xAxisPlotting)]
            optimalRecoVar = self.optimalRecoVar[(detectorModel)]
            for jetEnergy in self.jetEnergyList:
                saveString += str(self.JERError[(detectorModel,optimalRecoVar,jetEnergy,pandoraSettings)])
                if jetEnergy is not self.jetEnergyList[-1]:
                    saveString += ','
            saveString += '};\n\n'

        rootLineColor = ['4','2','6','1',]
        #rootLineStyle = ['1','2','3','4','5','6']

        saveString += '    TLegend *pLegend = new TLegend(0.6, 0.6, 0.9, 0.9);\n'

        for idx, xAxisPlotting in enumerate(self.xAxisPlottingList):
            saveString += '    TGraphErrors *pTGraphErrors_Variable_' + str(xAxisPlotting) + ' = new TGraphErrors(' + str(len(self.jetEnergyList)) + ',jetEnergy,Variable_' + str(xAxisPlotting) + '_JER,jetEnergyError,Variable_' + str(xAxisPlotting) + '_JERError);\n\n'
            saveString += '    pTGraphErrors_Variable_' + str(xAxisPlotting) + '->SetLineColor(' + rootLineColor[idx] + ');\n'
            saveString += '    pTGraphErrors_Variable_' + str(xAxisPlotting) + '->SetMarkerColor(' + rootLineColor[idx] + ');\n'
            saveString += '    pTGraphErrors_Variable_' + str(xAxisPlotting) + '->Draw("lp,same");\n\n'
            saveString += '    pLegend->AddEntry(pTGraphErrors_Variable_' + str(xAxisPlotting) + ', "' + Results.m_DetectorLabel[self.detectorModelList[idx]] + '", "lp");\n\n'

        saveString += '    pLegend->SetFillStyle(0);\n'
        saveString += '    pLegend->Draw("same");\n'
        saveString += '    pCanvasEj->SaveAs("JER_vs_JetEnergy_' + str(self.resultsName.replace(' ', '')) + '.pdf");\n'
        saveString += '}\n'

        #===== Write out file =====#
        resultsFile = open("JER_vs_JetEnergy_" + str(self.resultsName.replace(' ', '')) + ".C", "w")
        resultsFile.write(saveString)
        resultsFile.close()

#====================

    def plotConfusionData(self,jetEnergy):
        pandoraSettingsToPlot = ['Default','PerfectPFA','TotalConfusion','PhotonConfusion','NeutralHadronConfusion','OtherConfusion']
        rootLineColor = ['1','4','2','kOrange','kGreen-2','kMagenta']

        saveString = '{\n'
        saveString += '    gStyle->SetOptStat(0);\n\n'

        saveString += '    TCanvas *pCanvasEj = new TCanvas();\n'
        saveString += '    pCanvasEj->cd();\n\n'

        saveString += '    TH2F *pAxesEj = new TH2F("axesEj","",1200,' + str(self.minXAxis) + ',' + str(self.maxXAxis) + ',12000,0,6.5);\n'
        saveString += '    pAxesEj->GetYaxis()->SetTitle("RMS_{90}(E_{j}) / Mean_{90}(E_{j}) [%]");\n'
        saveString += '    pAxesEj->GetXaxis()->SetTitle("' + self.xAxisTitle + '");\n'
        saveString += '    pAxesEj->Draw();\n\n'

        saveString += '    float xAxisVairable[' + str(len(self.xAxisPlottingList)) + '] = {'
        for idx, xAxisPlotting in enumerate(self.xAxisPlottingList):
            saveString += str(xAxisPlotting)
            if xAxisPlotting is not self.xAxisPlottingList[-1]:
                saveString += ','
        saveString += '};\n\n'

        saveString += '    float xAxisVairableError[' + str(len(self.xAxisPlottingList)) + '] = {'

        for xAxisPlotting in self.xAxisPlottingList:
            saveString += str(0)
            if xAxisPlotting is not self.xAxisPlottingList[-1]:
                saveString += ','
        saveString += '};\n\n'

        for pandoraSettings in pandoraSettingsToPlot:
            saveString += '    float Pandora_Settings_' + str(pandoraSettings) + '_JER[' + str(len(self.xAxisPlottingList)) + '] = {'
            for xAxisPlotting in self.xAxisPlottingList:
                detectorModel = self.detectorModelFromPlotting[(xAxisPlotting)]
                optimalRecoVar = self.optimalRecoVar[(detectorModel)]
                saveString += str(self.JER[(detectorModel,optimalRecoVar,jetEnergy,pandoraSettings)])
                if xAxisPlotting is not self.xAxisPlottingList[-1]:
                    saveString += ','
            saveString += '};\n\n'

        for pandoraSettings in pandoraSettingsToPlot:
            saveString += '    float Pandora_Settings_' + str(pandoraSettings) + '_JERError[' + str(len(self.xAxisPlottingList)) + '] = {'
            for xAxisPlotting in self.xAxisPlottingList:
                detectorModel = self.detectorModelFromPlotting[(xAxisPlotting)]
                optimalRecoVar = self.optimalRecoVar[(detectorModel)]
                saveString += str(self.JERError[(detectorModel,optimalRecoVar,jetEnergy,pandoraSettings)])
                if xAxisPlotting is not self.xAxisPlottingList[-1]:
                    saveString += ','
            saveString += '};\n\n'

        saveString += '    TLegend *pLegend = new TLegend(0.6, 0.6, 0.9, 0.9);\n'

        for pandoraIdx, pandoraSettings in enumerate(pandoraSettingsToPlot):
            saveString += '    TGraphErrors *pTGraphErrors_Pandora_Settings' + str(pandoraSettings) + ' = new TGraphErrors(' + str(len(self.xAxisPlottingList)) + ',xAxisVairable,Pandora_Settings_' + str(pandoraSettings) + '_JER,xAxisVairableError,Pandora_Settings_' + str(pandoraSettings) + '_JERError);\n\n'
            saveString += '    pTGraphErrors_Pandora_Settings' + str(pandoraSettings) + '->SetLineColor(' + rootLineColor[pandoraIdx] + ');\n'
            saveString += '    pTGraphErrors_Pandora_Settings' + str(pandoraSettings) + '->SetMarkerColor(' + rootLineColor[pandoraIdx] + ');\n'
            saveString += '    pTGraphErrors_Pandora_Settings' + str(pandoraSettings) + '->Draw("lp,same");\n\n'
            saveString += '    pLegend->AddEntry(pTGraphErrors_Pandora_Settings' + str(pandoraSettings) + ', "' + str(pandoraSettings) + '", "lp");\n\n'

        saveString += '    pLegend->SetFillStyle(0);\n'
        saveString += '    pLegend->Draw("same");\n'
        saveString += '    pCanvasEj->SaveAs("JER_vs_' + str(self.resultsName.replace(' ', '')) + '_' + str(jetEnergy) + 'GeV_DiJet_Breakdown.pdf");\n'
        saveString += '}\n'

        #===== Write out file =====#
        resultsFile = open("JER_vs_" + str(self.resultsName.replace(' ', '')) + "_" + str(jetEnergy) + "GeV_DiJet_Breakdown.C", "w")
        resultsFile.write(saveString)
        resultsFile.close()

#==================== 
#===== End of Results Class =====
#==================== 

