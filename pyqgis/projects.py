import qgis.core as qgis
from pathlib import Path, PureWindowsPath


# creating a project instance
project = qgis.QgsProject.instance()
print(project)

# reading the project path
## base directory
BASE_DIR = Path(__file__).resolve().parent

## projects directory within base
projects = PureWindowsPath(BASE_DIR).joinpath('projects')
file = PureWindowsPath(projects).joinpath('exemplo.qgz')
new_file = PureWindowsPath(projects).joinpath('new_file.qgz')

# reading and open file project
print(project.read(str(file)))

# getting the project name
print(project.fileName())

# getting the absolute project path
print(project.absolutePath())

# getting the absolute file project path
print(project.absoluteFilePath())

# getting coordinate reference system - CRS
print(project.crs())

# setting coordinate reference system
project.setCrs(qgis.QgsCoordinateReferenceSystem("EPSG:4674"))
print(project.crs())

# saving the project - two ways
## 1 - Overwrite
project.write(project.absoluteFilePath())

## 2 - As a new project
project.write(str(new_file))

# amout layers
print(project.count())

# project title
print(project.title())

title = 'PyQgis Course'
project.setTitle(title)
print(project.title())

# ellipsoid
print(project.ellipsoid())

print(project.lastModified())

"""
# Setting background color
project.setBackgroundColor(QColor(51, 153, 255))

# Coming the color
project.setBackgroundColor(QColor(255, 255, 255))
"""