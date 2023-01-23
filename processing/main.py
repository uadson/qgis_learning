import os
import sys

BASE_DIR = os.getcwd()

DIR = 'pyqgis'

path = os.path.join(os.path.join(BASE_DIR, DIR), 'data')
funct_path = '/mnt/DADOS/github/qgis_learning/processing/'

# gambiarra
sys.path.insert(0, os.path.join(BASE_DIR, DIR))
sys.path.insert(1, funct_path)


from functions import reproject_layers, apply_filter, aero_alert


reproject_layers(path, 5880, 'layers', 'shp')

rep_layers_path = os.path.join(path, '5880_layers/')

apply_filter(rep_layers_path, 5880, 'aeroportos', 'go', 'shp')

aero_alert(rep_layers_path, 'aeroportos', 'chuva', 'shp')
