import os
import pandas as pd

from qgis.core import *


def get_files(path:str, extension:str) -> list():
	"""
		Get layer files to load in QGIS

		Formats:
		shapefiles (.shp)
		geopackges (.gpkg)
		rasters    (.tif)

		:invalid path or extension if there is not one of these:

		:value error exception for path or extension context:

		if user typing file name with or without '.' of extension. This will be adds.

		read all files on directory and return a list of this files.
	"""

	try:
		if not extension.startswith('.'):
			extension = f".{extension}"

		return [file for file in os.listdir(path) if file.endswith(extension)]

	except (TypeError, ValueError, NameError, NotADirectoryError, AttributeError) as error:
		return f"{error}"


def open_vector_layers(path:str, extension:str) -> dict():
	"""
		Choose a default file location path;
		Selects files according to their extension;
		Adds the files to qgis through the addMapLayer() function;
		Populates a dictionary with the objects created on the canvas;
		Returns the dictionary, which can be stored in a variable and will be iterable.
	"""
	files = get_files(path, extension)
	objects = {}
	for file in files:
		filename = file.split('.')[0]
		layer = QgsVectorLayer(path+file, filename, "ogr")
		obj = QgsProject.instance().addMapLayer(layer)
		objects.update({filename:obj})
	return objects


path = '/mnt/DADOS/github/qgis_learning/pyqgis/data/'

print(get_files(path, 'shp'))
print(get_files(path, 'gpkg'))
print(get_files(path, 'tif'))
print('-' * 40)
print(open_vector_layers(path, 'shp'))
print(open_vector_layers(path, 'gpkg'))
print(open_vector_layers(path, 'tif'))
print('-' * 40)
layers = open_vector_layers(path, 'shp')
print(dir(layers))
print('-' * 40)
for key, value in layers.items():
	print(key, '-', value)
print('-' * 40)
print(layers['aeroportos'])
for obj in layers['aeroportos'].getFeatures():
	print(obj.attributes())

print(dir(pd))