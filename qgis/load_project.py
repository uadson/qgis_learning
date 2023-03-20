# 1. Importando bibliotecas e módulos necessários
import os
import sys

from pathlib import PureWindowsPath
from datetime import datetime

from qgis.core import *

# 2. Configurando caminho de diretórios

BASE = os.getcwd()
PROJ = BASE + "\\qgis\\data\\projects"
LAYERS = BASE + "\\qgis\\data\\layers"

sys.path.insert(0, BASE)
sys.path.insert(1, PROJ)
sys.path.insert(2, LAYERS)

# 3. Carregando arquivos de projetos
def create_dict(index, file):
    index = 1
    data = {}
    data[index] = file
    return data

def load_projects():
    for index, file in enumerate(os.listdir(PROJ)):
        if file.endswith('.qgz'):
            objects = create_dict(index, file)
    return objects


# 4. Carregando projeto no QGIS
def get_project(proj_num):
    projects = load_projects()
    try:
        proj_path = PureWindowsPath(PROJ).joinpath(projects.get(proj_num))
        project = QgsProject.instance()
        project.read(str(proj_path))
        title = datetime.now().strftime("%Y%m%d")
        project.setTitle(title)
        project.setCrs(QgsCoordinateReferenceSystem("EPSG:31982"))
        project.write(project.absoluteFilePath())
        return project
    except:
        return print("Projeto não encontrado!")


get_project(1)
