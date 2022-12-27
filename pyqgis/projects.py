# creating a project instance
project = QgsProject.instance()

# Reading the project path
print(project.read(r'/mnt/DADOS/repos/qgis/qgis_learning/pyqgis/projects/exemplo.qgz')

# Getting the project name
print(project.fileName())

# Getting the absolute project path
print(project.absolutePath())

# Getting the absolute file project path
print(project.absoluteFilePath())

# Getting Coordinate Reference System- CRS
project.crs()

# Setting Coordinate Reference System
project.setCrs(QgsCoordinateReferenceSystem("EPSG:4674"))

# Saving the project - two ways
# 1 - Overwrite
project.write(project.absoluteFilePath())

# 2 - A new project
project.write(r'/mnt/DADOS/repos/qgis/qgis_learning/pyqgis/projects/new_example.qgz')

# Setting background color
project.setBackgroundColor(QColor(51, 153, 255))

# Coming the color
project.setBackgroundColor(QColor(255, 255, 255))

# Amount layers
project.count() 
# return 0 for this project

# Getting or defing the project title
project.title()

title = 'PyQgis Course'
project.setTitle(title)
project.title()

# Getting the ellipsoid
project.ellipsoid()
# return 'EPSG:7030'

# Getting last modified
project.lastModified()
# return PyQt5.QtCore.QDateTime(2022, 12, 23, 18, 28, 43, 251)

# Loading script
print(project)