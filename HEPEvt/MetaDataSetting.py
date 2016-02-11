import os

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

energies = [100]
particles = ['Photon']

fc = FileCatalogClient()

for particle in particles:
    for energy in energies:
        path = '/ilc/user/s/sgreen/HEPEvtFiles/' + str(particle) + '/' + str(energy) + 'GeV'
        pathdict = {'path':path, 'meta':{'JobDescription':'HEPEvt','EvtType':str(particle),'Energy':energy}}
        res = fc.setMetadata(pathdict['path'], pathdict['meta'])
