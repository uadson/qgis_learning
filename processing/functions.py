import os

import processing

import qgis.utils
from qgis.core import *

BASE_DIR = os.getcwd()

DIR = 'pyqgis'

path = os.path.join(os.path.join(BASE_DIR, DIR), 'data')


def makedir(path, espg, new_dir):
	if not os.path.exists(os.path.join(path, f"{espg}_{new_dir}")):
		os.makedirs(os.path.join(path, f"{espg}_{new_dir}"))
	else:
		pass


def get_files(path:str, ext:str) -> list():
	"""
		Get layer files to load in QGIS and return a list

		Formats:
		shapefiles (.shp)
		geopackges (.gpkg)
		rasters    (.tif)

		:invalid path or extension if there is not one of these:

		:value error exception for path or extension(ext) context:

		if user typing file name with or without '.' of extension. This will be adds.

		read all files on directory and return a list of this files.
	"""

	try:
		if not ext.startswith('.'):
			ext = f".{ext}"

		return [file for file in os.listdir(path) if file.endswith(ext)]

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


def reproject_layers(path, espg, new_dir, layer_ext):
	makedir(path, espg, new_dir)
	for file in get_files(path, layer_ext):
		input_path = os.path.join(path, file)
		output_path = os.path.join(
				os.path.join(path, f"{espg}_{new_dir}", os.path.join(f"{espg}_{file}"))
			)
		processing.run(
				"native:reprojectlayer",
				{
					'INPUT': input_path,
					'TARGET_CRS': QgsCoordinateReferenceSystem(f"ESPG: {espg}"),
					'OUTPUT': output_path
				}
			)
	return


def apply_filter(path:str, espg:int, layer, layer_name:str, state:str, ext:str):
	"""
		Filter objects by State

		:path      : files path
		:layer_name: the layer name
		:state     : the name state
		:espg      : ESPG code
		:ext       : file extension
	"""
	if espg != 0:
		layer_name = f"{espg}_{layer_name}{ext}"

	return layer[layer_name[0:-4]].setSubsetString(f"uf = '{state}'")


def aero_alert(path:str, espg:int, layer_name:str, state:str, weather:str, ext:str):

	state = state.upper()

	if not ext.startswith('.'):
		ext = f".{ext}"
	
	layer = open_vector_layers(path, ext)

	apply_filter(path, espg, layer, layer_name, state, ext)

	if espg != 0:
		layer_name = f"{espg}_{layer_name}{ext}"

	if weather == 'seco':
		buffer = 0.1
	elif weather == 'chuva':
		buffer = 0.5
	else:
		buffer = 1

	output_path = os.path.join(path, f"buffer{ext}")

	processing.run(
			"native:buffer",
			{
				'INPUT':layer[layer_name[0:-4]],
				'DISTANCE':buffer,
				'SEGMENTS':5,
				'END_CAP_STYLE':0,
				'JOIN_STYLE':0,
				'MITER_LIMIT':2,
				'DISSOLVE':True,
				'OUTPUT':output_path
			}
		)
	obj = QgsVectorLayer(str(output_path), "analise", "ogr")
	QgsProject.instance().addMapLayer(obj)
	return 
