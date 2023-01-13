import os

from qgis.core import *
from PyQt5.QtGui import QColor


filepath ='/mnt/DADOS/github/qgis_learning/pyqgis/data/merge.tif'

rlayer = QgsRasterLayer(filepath, "demo")

fcn = QgsColorRampShader()
fcn.setColorRampType(QgsColorRampShader.Interpolated)

colors = [
	QgsColorRampShader.ColorRampItem(0, QColor(255, 0, 0)),
	QgsColorRampShader.ColorRampItem(300, QColor(255, 153, 0)),
	QgsColorRampShader.ColorRampItem(900, QColor(255, 255, 102)),
	QgsColorRampShader.ColorRampItem(1100, QColor(153, 255, 102)),
	QgsColorRampShader.ColorRampItem(1600, QColor(0, 51, 0)),
]

fcn.setColorRampItemList(colors)
shader = QgsRasterShader()

shader.setRasterShaderFunction(fcn)

renderer = QgsSingleBandPseudoColorRenderer(rlayer.dataProvider(), 1, shader)

rlayer.setRenderer(renderer)

rlayer.triggerRepaint()

project = QgsProject.instance().addMapLayer(rlayer)

print(project)
