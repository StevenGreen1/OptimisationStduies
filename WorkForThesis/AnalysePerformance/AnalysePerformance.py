import subprocess
import os

executable = '/usera/sg568/ilcsoft_v01_17_07/OptimisationStudies/PandoraAnalysis_OptimisationStudies/LCPandoraAnalysis/bin/AnalysePerformance'

jobDescription = 'OptimisationStudies'

eventsToAnalyse = [
#                       { 'DetectorModel' : 38, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
                       { 'DetectorModel' : 39, 'ReconstructionVariant' : 69, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
                       { 'DetectorModel' : 40, 'ReconstructionVariant' : 70, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
                       { 'DetectorModel' : 41, 'ReconstructionVariant' : 72, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
                       { 'DetectorModel' : 42, 'ReconstructionVariant' : 73, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
                       { 'DetectorModel' : 43, 'ReconstructionVariant' : 74, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] }
#                       { 'DetectorModel' : 45, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 46, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 47, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 48, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 49, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 50, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 51, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 52, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 53, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 54, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 55, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 56, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 57, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 58, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 59, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 60, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 61, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 62, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 63, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 64, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 65, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 66, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 67, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 68, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 69, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 70, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 71, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 72, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 73, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 74, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 75, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 76, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] },
#                       { 'DetectorModel' : 77, 'ReconstructionVariant' : 71, 'EventType' : 'Z_uds', 'Energies' : [91, 200, 360, 500], 'ReconstructionSettings' : ['Default', 'PerfectPFA', 'PerfectPhoton', 'PerfectPhotonNK0L'] }
                   ]

for eventSelection in eventsToAnalyse:
    detectorModel = eventSelection['DetectorModel']
    reconstructionVariant = eventSelection['ReconstructionVariant']
    eventType = eventSelection['EventType']
    for energy in eventSelection['Energies']:
        for settings in eventSelection['ReconstructionSettings']:
            localPath = '/r02/lc/sg568/' + jobDescription + '/MarlinJobs/Detector_Model_' + str(detectorModel) + '/Reconstruction_Variant_' + str(reconstructionVariant) + '/' + eventType + '/' + str(energy) + 'GeV/PandoraSettings' + settings
            inputRootFile = '/r02/lc/sg568/' + jobDescription + '/MarlinJobs/Detector_Model_' + str(detectorModel) + '/Reconstruction_Variant_' + str(reconstructionVariant) + '/' + eventType + '/' + str(energy) + 'GeV/PandoraSettings' + settings + '/MarlinReco_ILD_o1_v06_GJN' + str(detectorModel) + '_uds' + str(energy) + '_*_' + settings + '.root'
            outputRootFile = os.path.join(localPath, 'AnalysePerformance_PandoraSettings' + settings + '_DetectorModel_' + str(detectorModel) + '_Reconstruction_Variant_' + str(reconstructionVariant) + '_' + eventType + '_' + str(energy) + 'GeV.root')
            analysePerformance = subprocess.Popen([executable, inputRootFile, outputRootFile], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = analysePerformance.communicate()

            outputTextFile = os.path.join(localPath, 'AnalysePerformance_PandoraSettings' + settings + '_DetectorModel_' + str(detectorModel) + '_Reconstruction_Variant_' + str(reconstructionVariant) + '_' + eventType + '_' + str(energy) + 'GeV.txt')

            resultsFile = open(outputTextFile, 'w')
            resultsFile.write(out)
            resultsFile.close()

# Results files /r06/lc/sg568/HCAL_Optimisation_Studies/AnalysePerformanceResults/Detector_Model_38/Reconstruction_Variant_71/Z_uds/91GeV/AnalysePerformance_PandoraSettingsDefault_DetectorModel_38_Reconstruction_Variant_71_Z_uds_91GeV.txt <- Just out
# Results files /r06/lc/sg568/HCAL_Optimisation_Studies/AnalysePerformanceResults/Detector_Model_38/Reconstruction_Variant_71/Z_uds/91GeV/AnalysePerformance_PandoraSettingsDefault_DetectorModel_38_Reconstruction_Variant_71_Z_uds_91GeV.root
