import os

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

energies = [10,20,50,100,200,500]
particles = ['Photon','Kaon0L']

fc = FileCatalogClient()

for particle in particles:
    for energy in energies:
        path = '/ilc/user/s/sgreen/HEPEvtFiles/' + str(particle) + '/' + str(energy) + 'GeV'
        pathdict = {'path':path, 'meta':{'JobDescription':'HEPEvt','EvtType':str(particle),'Energy':energy}}
        res = fc.setMetadata(pathdict['path'], pathdict['meta'])
