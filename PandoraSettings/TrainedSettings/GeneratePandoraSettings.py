import os 
import re

detModelList = range(84,104)
recoVarList = [38, 63, 71]

for detModel in detModelList:
    for recoVar in recoVarList:
        pandoraSettingsName = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudies/PandoraSettings/TrainedSettings/LikelihoodData/Detector_Model_' + str(detModel) + '/Reco_Stage_' + str(recoVar) + '/Z_uds/500GeV/PandoraSettingsDefault.xml' 
        photonLikelihoodFile = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudies/PandoraSettings/TrainedSettings/LikelihoodData/Detector_Model_' + str(detModel) + '/Reco_Stage_' + str(recoVar) + '/Z_uds/500GeV/PandoraLikelihoodData_DetModel_' + str(detModel) + '_RecoStage_' + str(recoVar) + '.xml'

        if not os.path.isfile(photonLikelihoodFile):
            missingDataFile = open("MissingData.txt", "a")
            missingDataFile.write("The Pandora settings file is missing for detector model " + str(detModel) + " and reconstruction variant " + str(recoVar) + "." + "\n")
            missingDataFile.close()
            continue

        baseFileName = '../PandoraSettingsDefault.xml'
        baseFile = open(baseFileName,'r')
        pandoraSettingsTemplate = baseFile.read()
        baseFile.close()
        pandoraSettingsTemplate = re.sub('PandoraLikelihoodData9EBin.xml',photonLikelihoodFile,pandoraSettingsTemplate)
        with open(pandoraSettingsName ,"w") as pandoraSettingsFile:
            pandoraSettingsFile.write(pandoraSettingsTemplate)
