import os
from qgis.core import *

filepath = '/mnt/DADOS/github/qgis_learning/pyqgis/data/cbers.tif'

#1
rlayer = QgsRasterLayer(filepath, 'cbers')
project = QgsProject.instance().addMapLayer(rlayer)
print(project)

# or
# 2
# iface.addRasterLayer(filepath, 'cbers')

# getting informations
print(rlayer.htmlMetadata())

# width and height
print(rlayer.width(), rlayer.height())

# raster extension
print(rlayer.extent().toString())

# raster type
print(rlayer.rasterType())

# amount band
print(rlayer.bandCount())

# raster name
print(rlayer.bandName(1))

# render
print(rlayer.renderer().type())