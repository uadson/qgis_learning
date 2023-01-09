import os

from qgis.core import *

path = 'D:\\repos\\pyqgis\\qgis_learning\\data\\'
project = QgsProject.instance()

for file in os.listdir(path):
    if file.endswith('shp'):
        try:
            layer = QgsVectorLayer(
                os.path.join(path, file),
                file[0:-4].title(),
                "ogr"
            )
            project.addMapLayer(layer)
            print("Project uploaded !")
        except Exception as error:
            print(error)

municipios = QgsProject.instance().mapLayersByName("Municipios")[0]
print(municipios)
print(municipios.featureCount())

# add filter
go = municipios.setSubsetString("uf = 'GO'")
print(go)
print(municipios.featureCount())

# remove filter
empty = municipios.setSubsetString("")
print(empty)
print(municipios.featureCount())