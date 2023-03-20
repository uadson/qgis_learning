import os
import sys


BASE = os.getcwd()
PROJ = BASE + "\\qgis\\data\\projects"
LAYERS = BASE + "\\qgis\\data\\layers"

sys.path.insert(0, BASE)
sys.path.insert(1, PROJ)
sys.path.insert(2, LAYERS)


def list_shp():
    index = 1
    data = {}
    for file in os.listdir(LAYERS):
        if file.endswith('.shp'):
            data[index] = file
            index += 1
    return data

files = list_shp()

for num, file in files.items():
    print(f"{num} - {file}")