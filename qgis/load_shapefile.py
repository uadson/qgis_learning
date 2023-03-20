# 1. Importando bibliotecas e módulos necessários
import os
import sys

import fileinput

from pathlib import PureWindowsPath
from datetime import datetime

from qgis.core import *
from PyQt5.QtWidgets import QInputDialog

# 2. Configurando caminho de diretórios

BASE = os.getcwd()
PROJ = BASE + "\\qgis\\data\\projects"
LAYERS = BASE + "\\qgis\\data\\layers"

sys.path.insert(0, BASE)
sys.path.insert(1, PROJ)
sys.path.insert(2, LAYERS)

# 3. Carregando arquivos de projetos
def list_shp():
    index = 1
    data = {}

    for file in os.listdir(LAYERS):
        if file.endswith('.shp'):
            data[index] = file
            index += 1
    return data


# 4. Carregando projeto no QGIS
def get_shp(file_num):
    files = list_shp()
    try:
        shp_path = PureWindowsPath(LAYERS).joinpath(files.get(file_num))
        project = QgsProject.instance()
        filename = files.get(file_num)
        layer = QgsVectorLayer(
            str(shp_path),
            filename[0:-4].upper(),
            "ogr"
        )
        title = datetime.now().strftime("%Y%m%d")
        project.setTitle(title + filename[0:-4])
        project.setCrs(QgsCoordinateReferenceSystem("EPSG:31982"))
        project.write(project.absoluteFilePath())
        print("Arquivo carregado com sucesso !!")
        return project.addMapLayer(layer)
    except:
        print("Arquivo não encontrado")


def get_input():
    files = list_shp()
    for num, file in files.items():
        print(f"{num} - {file}")

    answer = QInputDialog().getText(None, "Input", "Selecione um arquivo:  ")
    return int(answer[0])
    
get_shp(get_input())
