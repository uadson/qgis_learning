import os
import sys


BASE = os.getcwd()
PROJ = BASE + "\\qgis\\data\\projects"
LAYERS = BASE + "\\qgis\\data\\layers"

sys.path.insert(0, BASE)
sys.path.insert(1, PROJ)
sys.path.insert(2, LAYERS)


def load_projects():
    index = 1
    data = {}
    for file in os.listdir(PROJ):
        if file.endswith('.qgz'):
            data[index] = file
            index += 1
    return data

projects = load_projects()
for num, project in projects.items():
    print(f"{num} - {project}")