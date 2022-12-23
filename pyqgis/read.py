from .create import project

project.read(r'/mnt/DADOS/repos/qgis/qgis_learning/pyqgis/projects')
print(project.fileName())

print(project)