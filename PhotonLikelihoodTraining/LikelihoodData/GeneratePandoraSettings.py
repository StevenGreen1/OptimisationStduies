import os 
import re

detModelList = range(84,90) + range(96,100)
recoVarList = [38, 71]

for detModel in detModelList:
    for recoVar in recoVarList:
        pandoraSettingsName = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudies/PhotonLikelihoodTraining/LikelihoodData/Detector_Model_' + str(detModel) + '/Reco_Stage_' + str(recoVar) + '/Z_uds/500GeV/PandoraSettingsDefault.xml' 
        photonLikelihoodFile = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudies/PhotonLikelihoodTraining/LikelihoodData/Detector_Model_' + str(detModel) + '/Reco_Stage_' + str(recoVar) + '/Z_uds/500GeV/PandoraLikelihoodData_DetModel_' + str(detModel) + '_RecoStage_' + str(recoVar) + '.xml'
        baseFileName = 'PandoraSettingsDefault.xml'
        baseFile = open(baseFileName,'r')
        pandoraSettingsTemplate = baseFile.read()
        baseFile.close()
        pandoraSettingsTemplate = re.sub('PhotonLikelihoodData',photonLikelihoodFile,pandoraSettingsTemplate)
        if os.path.isfile(photonLikelihoodFile):
            with open(pandoraSettingsName ,"w") as pandoraSettingsFile:
                pandoraSettingsFile.write(pandoraSettingsTemplate)
        else:
            print 'Missing File : ' + photonLikelihoodFile
