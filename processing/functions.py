import os

import processing

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


reproject_layers(path, 5880, 'layers', 'shp')
