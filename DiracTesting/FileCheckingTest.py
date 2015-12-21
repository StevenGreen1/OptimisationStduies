import os

from DIRAC.Core.Base import Script
Script.parseCommandLine()

lfnExists = '/ilc/user/s/sgreen/OptimisationStudies/AnalysePerformance/Detector_Model_84_Run3/Reco_Stage_79/Z_uds/360GeV/AnalysePerformance_PandoraSettingsPerfectPhoton_DetectorModel_84_Reco_Stage_79_Z_uds_360GeV.root'
lfnDoesnt = '/ilc/user/s/sgreen/OptimisationStudies/AnalysePerformance/Detector_Model_84_Run3/Reco_Stage_79/Z_uds/360GeV/AnalysePerformance_PandoraSettingsPerfectPhoton_DetectorModel_84_Reco_Stage_79_Z_uds_360GeV.rot'

def doesFileExist(lfn):
    from DIRAC.DataManagementSystem.Client.DataManager import DataManager
    dm = DataManager()
    result = dm.getActiveReplicas(lfn)
    if result[('Value')][('Successful')]:
        print 'File exists.'
    else:
        print 'File does notexists.'

print 'The result if a file exists on the grid is: '
doesFileExist(lfnExists)

print 'The result if a file does not exists on the grid is: '
doesFileExist(lfnDoesnt)

