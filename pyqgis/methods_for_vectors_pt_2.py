import os

path = '/mnt/DADOS/repos/qgis/qgis_learning/pyqgis/data/'
filename = 'aeroportos.shp'
    
layer = QgsVectorLayer(os.path.join(path, filename), filename[0:-4].title(), "ogr")

QgsProject.instance().addMapLayer(layer)  

# Getting features
layer.getFeatures()