import os

# projects path
path = '/mnt/DADOS/repos/qgis/qgis_learning/pyqgis/data/'

project = QgsProject.instance()

for root, directory, files in os.walk(path):
    for file in files:
        if file.endswith('.shp'):
            layer = QgsVectorLayer(
                # path + file
                os.path.join(path, file),
                # file.shp -> file
                file[0:-4],
                "ogr")
            project.addMapLayer(layer)
