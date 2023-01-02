path = '/mnt/DADOS/repos/qgis/qgis_learning/pyqgis/data/'
filename = 'aeroportos.shp'

# QgsVectorLayer(file_path:str, filename:str, ogr:str)    
layer = QgsVectorLayer(os.path.join(path, filename), filename[0:-4].title(), "ogr")

# Add Layer
QgsProject.instance().addMapLayer(layer)  

# Add attributes
layer.startEditing()
layer.addAttribute(QgsField('x', QVariant.Double))
layer.commitChanges()

# Common types: String, Double, Int

count = 0
for feature in layer.getFeatures():
    while count < 5:
        print(feature.geometry())
        count += 1
        
count = 0
for feature in layer.getFeatures():
    while count < 5:
        print(feature.id(), feature.geometry().asPoint()[0])
        count += 1

layer.fields().count() # 15 -> 0 until 14

layer.startEditing()
layer.addAttribute(QgsField('x', QVariant.Double))
for feature in layer.getFeatures():
    id = feature.id()
    x = feature.geometry().asPoint()[0]
    attr_value = {14: x}
    layer.changeAttributeValues(id, attr_value)
    
layer.commitChanges()