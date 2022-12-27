# Vector data

# provedor
# vector layer = ogr
# raster = gedal
path = '/mnt/DADOS/repos/qgis/qgis_learning/pyqgis/data/'

# filename
FILENAME = 'aeroportos.shp'

# open a vector layer
path_layer = path + FILENAME

# add layer on canvas - two ways
# 1
layer = QgsVectorLayer(path_layer, "Aeroportos", "ogr")

QgsProject.instance().addMapLayer(layer)

# 2
layer = iface.addVectorLayer(path_layer, "Aeroportos", "ogr")
