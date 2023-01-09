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
"""empty = municipios.setSubsetString("")
print(empty)
print(municipios.featureCount())"""

# exporting

## features
options = QgsVectorFileWriter.SaveVectorOptions()
# for shapefile
## options.driverName = "ESRI Shapefile"
## filename = 'go.shp'

path_results = 'D:\\repos\\pyqgis\\qgis_learning\\pyqgis\\results\\'
filename = 'go.gpkg'
out_path = os.path.join(path_results, filename)
transform_context = project.transformContext()
##
try:
    QgsVectorFileWriter.writeAsVectorFormatV3(
        # layer (filtered)
        municipios,
        # path_output
        out_path,
        # transform_context
        transform_context,
        # options
        options
    )
    print("Vector exported successfully! ")
except Exception as error:
    print(error)
