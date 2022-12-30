import os
import qgis.core as qg

from geoscript.models import GeoScript

# 1. directory name files
data = 'data'
projects = 'projects'

# 2. creating a object from GeoScript
project = GeoScript()

# 3. getting files list
"""project.list_files(data)
project.list_files(projects)"""

# 4. loading project
project.instance()
project.load(projects, 'aeroportos')

"""import os

from pathlib import PureWindowsPath
from projects import BASE_DIR, projects

import qgis.core as qg

# data path
data = PureWindowsPath(BASE_DIR).joinpath('../data')

# projects path
project_path = PureWindowsPath(BASE_DIR).joinpath(str(projects))

# new project path
new_project = PureWindowsPath(project_path).joinpath('aeroportos.qgz')

# save new project
project = qg.QgsProject.instance()
project.write(str(new_project))

# loading this project
project.read(str(new_project))

for root, directory, files in os.walk(data):
    for file in files:
        if file.endswith('.shp'):
            layer = qg.QgsVectorLayer(
                # path + file
                os.path.join(data, file),
                # file.shp -> file
                file[0:-4],
                "ogr")
            project.addMapLayer(layer)
"""