import os

from PyQt5.QtCore import QVariant
from qgis.core import *

path_wd = 'D:\\repos\\qgis\\qgis_learning\\pyqgis\\data\\'

shapefile = 'aeroportos.shp'
feature = "TipoAero = 'Nacional'"

# scripts
layer = QgsVectorLayer(os.path.join(path_wd, shapefile), shapefile[0:-4].title(), "ogr")

QgsProject.instance().addMapLayer(layer)

layer.selectByExpression(feature, QgsVectorLayer.SetSelection)
layer.invertSelection()

# add to selection
layer.selectByExpression("nome ilike 'N%'", QgsVectorLayer.AddToSelection)

# remove to selection
layer.selectByExpression("nome ilike 'N%'", QgsVectorLayer.RemoveFromSelection)

# creating a object with selection
selection = layer.selectedFeatures()

for feature in selection:
    print(feature.attributes())

# removing field x
layer.startEditing()
layer.deleteAttribute(14)
# for many attributes
# layer.deleteAttributes([])
layer.commitChanges()

# add new columns - text type
layer.startEditing()
layer.addAttribute(QgsField('execute', QVariant.String, 'text', 255))
layer.commitChanges()

# update table values selected
layer.startEditing()
index = 14
for feature in selection:
    id = feature.id()
    layer.changeAttributeValue(id, index, 'uadson')

layer.commitChanges()

# removing all selected
layer.removeSelection()
