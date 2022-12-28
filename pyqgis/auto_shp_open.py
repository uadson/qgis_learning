import os

path = '/mnt/DADOS/repos/qgis/qgis_learning/pyqgis/data/'

for root, directory, files in os.walk(path):
    for file in files:
        if file.endswith('.shp'):
            layer = QgsVectorLayer(
                # path + filename
                os.path.join(path, file),
                # file.shp -> file
                file[0:-4],
                "ogr")
            QgsProject.instance().addMapLayer(layer)
