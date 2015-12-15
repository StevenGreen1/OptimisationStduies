#!/usr/bin/python/Results

# -*- coding: utf-8 -*-

import sys
import re
import math
import os
from collections import defaultdict
#import matplotlib.pyplot as plt
#import numpy as np
#import scipy.interpolate
#from pylab import *

#===== Start of Results Class =====

class Results:
    HadronicEnergyTrunc = defaultdict(dict)
    HadronicEnergyTrunc = {69:0.5, 70:0.75, 71:1, 72:1.5, 73:2, 74:5, 75:10, 76:1000000};

    RecoVarFromTrunc = defaultdict(dict)
    RecoVarFromTrunc = {0.5:69, 0.75:70, 1:71, 1.5:72, 2:73, 5:74, 10:75, 1000000:76};

#==================== 

    def __init__(self, resultsName, detectorModelList, xAxisPlottingList, xAxisTitle, reconstructionVariantList, jetEnergyList, algorithm):
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

#==================== 

    def readData(self):
        NumberOfEvents = defaultdict(dict)
        JER = defaultdict(dict)
        JERError = defaultdict(dict)
        for detectorModel in self.detectorModelList:
            for reconstructionVariant in self.reconstructionVariantList:
                for jetEnergy in self.jetEnergyList:
                    JER[(detectorModel,reconstructionVariant,jetEnergy)] = -1
                    fileName = '/r06/lc/sg568/HCAL_Optimisation_Studies/AnalysePerformanceResults/Detector_Model_' + str(detectorModel) + '/Reco_Stage_' + str(reconstructionVariant) + '/Z_uds/' + str(jetEnergy) + 'GeV/AnalysePerformance_PandoraSettingsDefault_DetectorModel_' + str(detectorModel) + '_Reco_Stage_' + str(reconstructionVariant) + '_Z_uds_' + str(jetEnergy) + 'GeV.txt'
                    if os.path.isfile(fileName):
                        file = open(fileName)
                        allLines = file.readlines()
                        for line in allLines:
                            regex = re.compile("fPFA_L7A \((\d+) entries\)(.*?)sE\/E: (\d\.\d+)\+\-(\d\.\d+)")
                            searchResults = regex.search(line)
                            if searchResults is not None:
                                NumberOfEvents[(detectorModel,reconstructionVariant,jetEnergy)] = int(searchResults.group(1))
                                JER[(detectorModel,reconstructionVariant,jetEnergy)] = float(searchResults.group(3))
                                JERError[(detectorModel,reconstructionVariant,jetEnergy)] = float(searchResults.group(4))
        self.NumberOfEvents = NumberOfEvents
        self.JER = JER
        self.JERError = JERError

#==================== 

    def optimiseData(self):
        if self.algorithm:
             if 'HCal Cell' in self.resultsName:
                 optimalRecoVar = defaultdict(dict)
                 optimalRecoVar = { 39:self.RecoVarFromTrunc[(0.5)], 40:self.RecoVarFromTrunc[(0.75)], 38:self.RecoVarFromTrunc[(1)], 41:self.RecoVarFromTrunc[(1.5)], 42:self.RecoVarFromTrunc[(2)], 43:self.RecoVarFromTrunc[(5)] }
                 self.optimalRecoVar = optimalRecoVar

             else:
                 print 'Please speicify optimisaed energy truncations.'

#            optimalRecoVar = defaultdict(dict)
#            for detectorModel in self.detectorModelList:
#                optimalSumJER = 100
#                optimalReconstructionVariant = 0
#                for reconstructionVariant in self.reconstructionVariantList:
#                    sumJER = 0
#                    for jetEnergy in self.jetEnergyList:
#                        if not self.JER[(detectorModel,reconstructionVariant,jetEnergy)]:
#                            print 'There is a problem with the jet energy resolution results file for detector model ' + str(detectorModel) + '. reconstruction variant ' + str(reconstructionVariant) + ' and jet energy ' + str(jetEnergy) + 'GeV.  Please check this file.  For now this will be set to 10 to allow this script to produce some results.'
#                            self.JER[(detectorModel,reconstructionVariant,jetEnergy)] = 10
#                            self.JERError[(detectorModel,reconstructionVariant,jetEnergy)] = 10
#                        sumJER += self.JER[(detectorModel,reconstructionVariant,jetEnergy)]
#                        if sumJER < optimalSumJER:
#                            print sumJER
#                            optimalSumJER = sumJER
#                            optimalReconstructionVariant = reconstructionVariant
#                optimalRecoVar[(detectorModel)] = optimalReconstructionVariant
#            self.optimalRecoVar = optimalRecoVar 

        else:
            optimalRecoVar = defaultdict(dict)
            for detectorModel in self.detectorModelList:
                optimalRecoVar[(detectorModel)] = 71
            self.optimalRecoVar = optimalRecoVar

#==================== 

    def analyseOptimalData(self):
        for detectorModel in self.detectorModelList:
            print 'For detector model ' + str(detectorModel) + ' the optimal reconstruction variant is ' + str(self.optimalRecoVar[(detectorModel)]) + '.'
            print 'This corresponds to an energy truncation of ' + str(Results.HadronicEnergyTrunc[(self.optimalRecoVar[(detectorModel)])])
            print '\n'
            print '======================================================================'
            print '| RecoVar\Energy | 91 GeV | 200 GeV | 360 GeV | 500 GeV | Truncation |'
            print '======================================================================'
            for reconstructionVariant in self.reconstructionVariantList:
                printString = '| ' + str(reconstructionVariant) + ' | '  
                printString += str(self.JER[(detectorModel,reconstructionVariant,91)]) + ' |'
                printString += str(self.JER[(detectorModel,reconstructionVariant,200)]) + ' |'
                printString += str(self.JER[(detectorModel,reconstructionVariant,360)]) + ' |'
                printString += str(self.JER[(detectorModel,reconstructionVariant,500)]) + ' |'
                printString += str(Results.HadronicEnergyTrunc[reconstructionVariant]) + ' |'
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

        for xAxisPlotting in xAxisPlottingList:
            saveString += str(0)
            if xAxisPlotting is not self.xAxisPlottingList[-1]:
                saveString += ','
        saveString += '};\n\n'

        for jetEnergy in self.jetEnergyList:
            saveString += '    float Jet_Energy_' + str(jetEnergy) + 'GeV_JER[' + str(len(self.xAxisPlottingList)) + '] = {'
            for xAxisPlotting in xAxisPlottingList:
                detectorModel = self.detectorModelFromPlotting[(xAxisPlotting)]
                optimalRecoVar = self.optimalRecoVar[(detectorModel)]
                saveString += str(self.JER[(detectorModel,optimalRecoVar,jetEnergy)])
                if xAxisPlotting is not xAxisPlottingList[-1]:
                    saveString += ','
            saveString += '};\n\n'

        for jetEnergy in self.jetEnergyList:
            saveString += '    float Jet_Energy_' + str(jetEnergy) + 'GeV_JERError[' + str(len(self.xAxisPlottingList)) + '] = {'
            for xAxisPlotting in xAxisPlottingList:
                detectorModel = self.detectorModelFromPlotting[(xAxisPlotting)]
                optimalRecoVar = self.optimalRecoVar[(detectorModel)]
                saveString += str(self.JERError[(detectorModel,optimalRecoVar,jetEnergy)])
                if xAxisPlotting is not xAxisPlottingList[-1]:
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

    def fancyPlot(self):
        for jetEnergy in self.jetEnergyList:
            xlist = []
            ylist = []
            zlist = []
            for idx, detectorModel in enumerate(self.detectorModelList):
                for reconstructionVariant in self.reconstructionVariantList[:-1]:
                    jer = self.JER[(detectorModel,reconstructionVariant,jetEnergy)]
                    if jer > 0:
                        xlist.append(self.xAxisPlottingList[idx])
                        ylist.append(Results.HadronicEnergyTrunc[reconstructionVariant])
                        zlist.append(jer)

#            zlist2 = [n * 10 for n in zlist]
#            fig = gcf()
#            ax = fig.gca()
#            s = ax.scatter(xlist, ylist, s=zlist2, c=zlist)
#            plt.xlabel(self.xAxisTitle)
#            plt.ylabel('Hadronic Energy Truncation [GeV]')
#            cb = plt.colorbar(s)
#            cb.set_label('Jet Energy Resolution') 

#            plt.savefig('Fancy_' + str(jetEnergy) + 'GeVJets_' + str(self.resultsName.replace(' ', '')) + '.png')
#            plt.clf()

#==================== 
#===== End of Results Class =====
#==================== 

#===== User Input =====#
jetEnergyList = [91,200,360,500]
reconstructionVariantList = range(69,77)

# ECal Cell Size Silicon
resultsName = 'Silicon ECal Cell Size'
detectorModelList = [84,85,86,87,88,89]
xAxisPlottingList = [3,5,7,10,15,20]
xAxisTitle = 'Silicon ECal Cell Size [mm^{2}]'

ecalCellSizeResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False)
ecalCellSizeResults.readData()
ecalCellSizeResults.optimiseData()
ecalCellSizeResults.plotData()
ecalCellSizeResults.analyseOptimalData()

# ECal Cell Size Scintillator
resultsName = 'Scintillator ECal Cell Size'
detectorModelList = [90,91,92]
xAxisPlottingList = [3,5,7]
xAxisTitle = 'Scintillator ECal Cell Size [mm^{2}]'

ecalCellSize2Results = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False)
ecalCellSize2Results.readData()
ecalCellSize2Results.optimiseData()
ecalCellSize2Results.plotData()
ecalCellSize2Results.analyseOptimalData()

sys.exit()

# Material
resultsName = 'HCal Absorber Material'
detectorModelList = [45,46,47,48]
xAxisPlottingList = [1,2,3,4]
xAxisTitle = 'HCal Absorber Material'

hcalMaterialResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False)
hcalMaterialResults.readData()
hcalMaterialResults.optimiseData()
hcalMaterialResults.plotData()

# Number of HCal Layers
resultsName = 'HCal Cell Size'
detectorModelList = [39,40,38,41,42,43]
xAxisPlottingList = [10,20,30,40,50,100]
xAxisTitle = 'HCal Cell Size [mm^{2}]'

hcalCellSizeResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, True)
hcalCellSizeResults.readData()
hcalCellSizeResults.optimiseData()
hcalCellSizeResults.analyseOptimalData()
hcalCellSizeResults.plotData()
hcalCellSizeResults.fancyPlot()

# Number of HCal Layers
resultsName = 'Number Of Layers In The HCal'
detectorModelList = [49,50,51,52,53,38,54,55]
xAxisPlottingList = [18,24,30,36,42,48,54,60]
xAxisTitle = 'Number Of Layers In The HCal'

layerResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False)
layerResults.readData()
layerResults.optimiseData()
layerResults.plotData()
layerResults.fancyPlot()

# Number of HCal Interation Lengths
resultsName = 'Number Of Nuclear Interation Lengths In The HCal'
detectorModelList = [56,57,38,58,59]
xAxisPlottingList = [4.576,5.148,5.72,6.292,6.864]
xAxisTitle = 'Number Of Nuclear Interation Lengths In The HCal [#lambda_{I}]'

lengthResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False)
lengthResults.readData()
lengthResults.optimiseData()
lengthResults.plotData()
lengthResults.fancyPlot()

# Sampling Fraction in HCal
resultsName = 'Sampling Fraction In The HCal'
detectorModelList = [60,61,38,62,63]
xAxisPlottingList = [0.05,0.10,0.15,0.20,0.25]
xAxisTitle = 'Sampling Fraction In The HCal'

sampFraclengthResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False)
sampFraclengthResults.readData()
sampFraclengthResults.optimiseData()
sampFraclengthResults.plotData()
sampFraclengthResults.fancyPlot()

# B Field
resultsName = 'Magnetic Field Strength'
detectorModelList = [64,65,66,67,68,69,70,71,72]
xAxisPlottingList = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
xAxisTitle = 'Magentic Field Strength [T]'

bFieldResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False)
bFieldResults.readData()
bFieldResults.optimiseData()
bFieldResults.plotData()
bFieldResults.fancyPlot()

# Sampling Fraction in HCal
resultsName = 'ECal Inner Radius'
detectorModelList = [73,74,75,76,77]
xAxisPlottingList = [1208,1408,1608,1808,2008]
xAxisTitle = 'ECal Inner Radius [mm]'

ecalInnerRadResults = Results(resultsName,detectorModelList,xAxisPlottingList,xAxisTitle,reconstructionVariantList,jetEnergyList, False)
ecalInnerRadResults.readData()
ecalInnerRadResults.optimiseData()
ecalInnerRadResults.plotData()
ecalInnerRadResults.fancyPlot()


