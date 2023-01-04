import os
import qgis.core as qg

# projects path
path = '/mnt/DADOS/repos/qgis/qgis_learning/pyqgis/data/'
path_windows = 'D:\\repos\\qgis\\qgis_learning\\pyqgis\\data\\'

project = qg.QgsProject.instance()
def open_layer_lx():
    for root, directory, files in os.walk(path):
        for file in files:
            if file.endswith('.shp'):
                layer = qg.QgsVectorLayer(
                    # path + file
                    os.path.join(path, file),
                    # file.shp -> file
                    file[0:-4],
                    "ogr")
                project.addMapLayer(layer)


def open_layer_wd():
    for root, directory, files in os.walk(path_windows):
        for file in files:
            if file.endswith('.shp'):
                layer = qg.QgsVectorLayer(
                    # path + file
                    os.path.join(path_windows, file),
                    # file.shp -> file
                    file[0:-4],
                    "ogr")
                project.addMapLayer(layer)


open_layer_wd()
