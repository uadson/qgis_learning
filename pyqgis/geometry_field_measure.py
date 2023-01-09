import os

from qgis.core import *

# path
path = 'D:\\repos\\qgis\\qgis_learning\\pyqgis\\data\\'
# path = os.getcwd() + '\\data'

# loop getting data
for root, directory, files in os.walk(path):
    for file in files:
        if file.endswith('.shp'):
            path_vector = os.path.join(path, file)
            layer = QgsVectorLayer(path_vector, file[0:-4], "ogr")
            QgsProject.instance().addMapLayer(layer)

# variables
aeroportos = QgsProject.instance().mapLayersByName("aeroportos")[0]
municipios = QgsProject.instance().mapLayersByName("municipios")[0]
rodovias = QgsProject.instance().mapLayersByName("rodovias")[0]

# municipios
# without metrics data
count = 0
for feature in municipios.getFeatures():
    if count < 5:
        print("\n")
        print("-" * 30)
        # city
        print(feature["municipio"])
        geom = feature.geometry()
        area = geom.area()
        perimeter = geom.length()
        print(f"Área: {area:.2f}")
        print(f"Perímetro: {perimeter:.2f}")
    else:
        break
    count += 1

# with metrics data
d = QgsDistanceArea()
d.setEllipsoid("WGS84")

count = 0
for feature in municipios.getFeatures():
    if count < 5:
        print("\n")
        print("-" * 30)
        print(feature["municipio"])
        geom = feature.geometry()
        area = d.measureArea(geom)
        areakm = d.convertAreaMeasurement(area, QgsUnitTypes.AreaSquareKilometers)
        perimeter = d.measurePerimeter(geom)
        print(f"Perímetro(m): {perimeter:.2f}")
        print(f"Área(m²): {area:.2f}")
        print(f"Área(km²): {areakm:.2f}")
    else:
        break
    count += 1

# distance between points
select = aeroportos.selectByExpression("FID_1 in (2411, 2425)", QgsVectorLayer.SetSelection)
selected = aeroportos.selectedFeatures()

d = QgsDistanceArea()
d.setEllipsoid("WGS84")

points = []
for feature in selected:
    municipio = feature["nm_municip"]
    geom = feature.geometry()
    points.append([municipio, geom.asPoint()])

print(points)

# distance calc
distance = d.measureLine(points[0][1], points[1][1])

print(f"Distância(m): entre {distance:.2f}")