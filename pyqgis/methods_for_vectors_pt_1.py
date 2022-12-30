import os

path = '/mnt/DADOS/repos/qgis/qgis_learning/pyqgis/data/'
filename = 'aeroportos.shp'
    
layer = QgsVectorLayer(os.path.join(path, filename), filename[0:-4].title(), "ogr")

QgsProject.instance().addMapLayer(layer)  

# Getting id
print(layer.id())

# Getting extent
print(layer.extent())

# Add attributes
layer.startEditing()
layer.addAttribute(QgsField('new_field', QVariant.String))
layer.commitChanges()

# Common types: String, Double, Int

# Fields
layer.fields().count()

# Getting fields names
layer.fields().names()

# Filtering
layer.fields().names()[4]

# Deleting attributes
layer.startEditing()
layer.deleteAttribute(15)
layer.commitChanges()