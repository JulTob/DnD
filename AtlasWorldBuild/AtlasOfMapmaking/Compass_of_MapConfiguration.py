# Compass of Map Configuration

import math
from random import randint
from enum import Enum


class MapShape(Enum):
	"""Enum to define possible map shapes."""
	SQUARE = "Square"
	TRIANGULAR = "Triangular"
	HEXAGONAL = "Hexagonal"
	OCTAGONAL = "Octagonal"

class MapConfig:
	"""Configuration for map dimensions and hex properties."""
	BASE = 20
	RADIUS = BASE
	GRID_WIDTH = randint(30,70)
	GRID_HEIGHT = randint(30,70)
	GRID_AREA = GRID_WIDTH * GRID_HEIGHT
	MARGIN =  8 * BASE
	ROUGHNESS = randint(1,10)
	MIN_HEIGHT = -10
	MAX_HEIGHT = 45
	BACKGROUND_COLOR = "oldlace"
	PARCHMENT_COLOR = "antiquewhite"
	SHAPE = MapShape.SQUARE

	@staticmethod
	def SetTriangular():
		MapConfig.SHAPE = MapShape.TRIANGULAR
	def SetHexagonal():
		MapConfig.SHAPE = MapShape.HEXAGONAL
	def SetOctagonal():
		MapConfig.SHAPE = MapShape.OCTAGONAL
	def SetSquare():
		MapConfig.SHAPE = MapShape.SQUARE

	@staticmethod
	def width():
		w = MapConfig.GRID_WIDTH * MapConfig.RADIUS
		if MapConfig.SHAPE == MapShape.TRIANGULAR:
			w //= 2
		if MapConfig.SHAPE == MapShape.HEXAGONAL:
			w = 0.77 *  MapConfig.GRID_WIDTH  * MapConfig.RADIUS
		if MapConfig.SHAPE == MapShape.OCTAGONAL:
			# Approximate width for octagonal grids.
			w = MapConfig.GRID_WIDTH * MapConfig.RADIUS * 1.5
		return int(w) + 2 * MapConfig.MARGIN

	@staticmethod
	def height():
		"""Return the height of the map based on the selected shape."""
		h = MapConfig.GRID_HEIGHT * MapConfig.RADIUS
		if MapConfig.SHAPE == MapShape.TRIANGULAR:
			# Triangular maps reduce height proportionally.
			h = h * 0.9

		if MapConfig.SHAPE == MapShape.HEXAGONAL:
			# Hexagonal maps stagger rows with a 1.5 * RADIUS vertical distance.
			hex_width = MapConfig.RADIUS
			h = MapConfig.GRID_HEIGHT * hex_width * 0.9
		if MapConfig.SHAPE == MapShape.OCTAGONAL:
			# Octagonal maps approximate each row as 2 * RADIUS tall.
			h = MapConfig.GRID_HEIGHT * 1.5 * MapConfig.RADIUS
		return int(h)+ 2 * MapConfig.MARGIN

	@staticmethod
	def svg_dimensions():
		return (MapConfig.width(), MapConfig.height())
