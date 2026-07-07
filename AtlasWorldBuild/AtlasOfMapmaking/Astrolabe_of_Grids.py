import math
from math import sqrt
from AtlasOfMapmaking.Compass_of_MapConfiguration import MapConfig
from random import randint
from random import choice

SIZE = MapConfig.BASE
ROUGHNESS = MapConfig.ROUGHNESS

class Cell:
	"""Base class for all cell types in the grid."""
	def __init__(cell, position, size = SIZE):
		cell.position = position  # Grid position, e.g., (row, col)
		cell.neighbors = []  # Adjacent cells
		cell.levels = cell.Full_Range()
		cell.size = SIZE

	def __lt__(cell, other):
		return cell.Level() < other.Level()

	def __eq__(cell, other):
		return cell.position == other.position and cell.Level() == other.Level()
	def __hash__(self):

		return hash(self.position)
	def connect(cell, neighbor):
		"""Bidirectional connection to another cell."""
		if neighbor not in cell.neighbors:
			cell.neighbors.append(neighbor)
			neighbor.neighbors.append(cell)
	def find_neighbors(self, grid):
		"""
		Find neighbors in a Cartesian square grid by default.
		This implementation assumes each cell has up to 4 orthogonal neighbors.
		Subclasses can override this to provide custom behavior.
		"""
		r, c = self.position
		potential_positions = [
			(r - 1, c),  # Up
			(r + 1, c),  # Down
			(r, c - 1),  # Left
			(r, c + 1)   # Right
			]
		for pos in potential_positions:
			neighbor = grid.get_cell(pos)
			if neighbor:
				self.connect(neighbor)

	def calculate_points(cell):
		"""
		Calculate the cell's points based on its center and shape.
		Default Cell: Shapeless, so just center point.
		<center_x> X coordinate of the cell's center.
		<center_y> Y coordinate of the cell's center.
		"""
		base = MapConfig.BASE
		cell.points = []
		for neighbor in cell.neighbors:
			n_r, n_c = neighbor.position
			x = MapConfig.MARGIN + n_c * base
			y = MapConfig.MARGIN + n_r * base
			cell.points += [(x, y)]

	def Full_Range(cell):
		cell.levels = list(range(
			MapConfig.MIN_HEIGHT,
			MapConfig.MAX_HEIGHT +1
			))
	def Set_Range(cell, floor, roof):
		cell.levels = list(range(
			floor,
			roof +1
			))
	def Nadir(cell):
		if not cell.levels:
				raise ValueError("Levels are empty, cannot determine Nadir.")
		return min(cell.levels)
	def Zenith(cell):
		if not cell.levels:
			raise ValueError("Levels are empty, cannot determine Zenith.")
		return max(cell.levels)
	def fixed(cell):
		try:
			if len(cell.levels) == 1:
				return True
			if len(cell.levels) > 1:
				return False
		except:
			cell.Full_Range()
			return cell.fixed()
	def is_valid(cell):
		"""
		Check if a cell's level range is valid.
		A cell is valid if Nadir <= Zenith and levels are non-empty.
		"""
		return len(cell.levels) > 0 and cell.Nadir() <= cell.Zenith()
	def Limitate(cell, top, bot, validity = 1):
		if top == cell.Zenith() and bot == cell.Nadir():
			return
		roof = min(cell.Zenith(), top)
		floor = max(cell.Nadir(), bot)
		if cell.is_valid() and roof == floor:
			cell.levels = [roof]
		elif cell.is_valid() and roof > floor:
			cell.Set_Range(floor,roof)
		else:
			raise ValueError(f"Cell Level({cell.levels = }) Range Out of Bounds: {roof = }, { floor = }")
	def Level(cell):
		if cell.fixed():
			return cell.levels[0]
		raise ValueError(f"Cell is not fixed, cannot determine level. Levels: {cell.levels = }")
	def Collapse(cell):
		if not cell.fixed():
			chosen = choice(cell.levels)
			cell.Limitate(chosen,chosen)
			cell.Constrains()
	def Constrains(cell, visited = None, roughness = ROUGHNESS):
		propagate_constraints(cell, roughness=roughness)
		return
		roughness = abs(roughness)
		if visited is None:
			visited = set()
		if cell in visited:
			return
		visited.add(cell)
		new_top = cell.Zenith()+roughness
		new_bot = cell.Nadir()-roughness
		for neighbor in cell.neighbors:
			if not neighbor.fixed():
				if neighbor not in visited:
					if neighbor.Zenith() > new_top and neighbor.Nadir()< new_bot:
						neighbor.Limitate(new_top, new_bot)
						neighbor.Constrains(visited=visited, roughness=roughness)

def propagate_constraints(seed_cell, roughness=1):
	from collections import deque
	queue = deque([seed_cell])
	visited = set()
	while queue:
		cell = queue.popleft()
		if cell in visited:
			continue
		visited.add(cell)
		roughness = randint(1,roughness)
		new_top = cell.Zenith()+roughness
		new_bot = cell.Nadir()-roughness


		for neighbor in cell.neighbors:

			if neighbor in visited:
				continue
			if neighbor.fixed():
				continue
			old_levels = set(neighbor.levels)  # Save current levels
			if neighbor.Zenith() > new_top and neighbor.Nadir()< new_bot:
				neighbor.Limitate(new_top, new_bot)
			new_levels = set(neighbor.levels)
			# Only add the neighbor to the queue if its levels have changed
			if old_levels != new_levels:
				queue.append(neighbor)

class HexCell(Cell):
	def __init__(Hex, position, size = SIZE):
		super().__init__(position, size)
		Hex.radius = size / 2
		Hex.corners = []  # Hex corners will be calculated dynamically
		Hex.points = []
	def calculate_corners(Hex):
		"""Calculate the corners of the hex based on its position and radius."""
		x, y = Hex.position
		Hex.corners = [
			hex_corner(x, y, Hex.radius, i)
			for i in range(6)
		]
	def find_neighbors(Hex, grid):
		"""
		Determine neighbors for a hexagonal cell in a pointy-top hex grid.
		Connect to 2 neighbors in the previous row, 2 in the next row, and 1 horizontal neighbor.
		"""
		r, c = Hex.position
		# Connect based on row parity (even or odd)
		if c % 2 == 0:  # Even column
			potential_positions = [
				(r - 1, c),      # Top-left
				(r - 1, c + 1),  # Top-right
				(r, c - 1),      # Left
				(r, c + 1),      # Right
				(r + 1, c),      # Bottom-left
				(r + 1, c + 1)   # Bottom-right
			]
		else:  # Odd column
			potential_positions = [
				(r - 1, c - 1),  # Top-left
				(r - 1, c),      # Top-right
				(r, c - 1),      # Left
				(r, c + 1),      # Right
				(r + 1, c - 1),  # Bottom-left
				(r + 1, c)       # Bottom-right
			]
		for pos in potential_positions:
			neighbor = grid.get_cell(pos)
			if neighbor:
				Hex.connect(neighbor)
	def calculate_points(Hex):
		"""
		Calculate the cell's points based on its center and shape.
		Hexagon Cell.
		<center_x> X coordinate of the cell's center.
		<center_y> Y coordinate of the cell's center.
		"""
		row, col = Hex.position
		center_x = MapConfig.MARGIN + col * Hex.radius * 1.5
		center_y = MapConfig.MARGIN + row * Hex.radius * sqrt(3)
		if col % 2 == 1:
			center_y += Hex.radius * (sqrt(3) / 2) / 2
		for i in range(6):
			Hex.points += [hex_corner(center_x, center_y, Hex.radius, i)]

def hex_corner(center_x, center_y, radius, corner):
	"""
	Calculate the coordinates of a corner of a hexagon.

	<center_x> X coordinate of the hexagon center.
	<center_y> Y coordinate of the hexagon center.
	<radius> Radius of the hexagon.
	<corner> Index of the corner mod %6 (0-5).
	<< return: Tuple (x, y) of the corner's coordinates.
	"""
	angle_deg = 60 * (corner%6)
	angle_rad = math.radians(angle_deg)
	x = center_x + radius * math.cos(angle_rad)
	y = center_y + radius * math.sin(angle_rad)
	return (x, y)

class TriangleCell(Cell):
	def __init__(Trig, position = (0,0), size = SIZE):
		super().__init__(position, size)
		x, y = position
		Trig.orientation = (x + y) % 2
		Trig.points = []  # Triangle points will be calculated dynamically
	def is_Up(Trig):
		return Trig.orientation == 0
	def calculate_points(Trig):
		"""Calculate the vertices of the triangle."""
		row, col = Trig.position
		size = Trig.size
		base_width = size
		height = size * (3 ** 0.5) / 2
		spacing_x = base_width / 2
		spacing_y = height

		# Translate grid position to canvas coordinates
		canvas_x = MapConfig.MARGIN + col * spacing_x
		canvas_y = MapConfig.MARGIN + row * spacing_y

		# Calculate triangle vertices
		if Trig.is_Up():  # Upward-pointing triangle
			Trig.points = [
				(canvas_x, canvas_y - height / 2),
				(canvas_x - base_width / 2, canvas_y + height / 2),
				(canvas_x + base_width / 2, canvas_y + height / 2),
			]
		else:  # Downward-pointing triangle
			Trig.points = [
				(canvas_x, canvas_y + height / 2),
				(canvas_x - base_width / 2, canvas_y - height / 2),
				(canvas_x + base_width / 2, canvas_y - height / 2),
			]
		#print(f"Cell at {Trig.position =} with orientation {Trig.orientation =}: Points={Trig.points =}")
	def find_neighbors(Trig, grid):
		"""Determine neighbors for a triangular cell."""
		r, c = Trig.position
		if Trig.orientation == 0:  # Upward-pointing triangle
			potential_positions = [
				(r - 1, c),     # Top neighbor
				(r, c - 1),     # Bottom-left neighbor
				(r, c + 1)      # Bottom-right neighbor
			]
		else:  # Downward-pointing triangle
			potential_positions = [
				(r + 1, c),     # Bottom neighbor
				(r, c - 1),     # Top-left neighbor
				(r, c + 1)      # Top-right neighbor
			]
		for pos in potential_positions:
			neighbor = grid.get_cell(pos)
			if neighbor:
				if not Trig.orientation == neighbor.orientation:
					Trig.connect(neighbor)
	def to_cartesian_points(Trig):
		"""Calculate the vertices of the triangle."""
		x, y = Trig.position  # Position in the grid
		size = Trig.size
		spacing_x = size  # Horizontal spacing
		spacing_y = size * (3 ** 0.5) / 2  # Vertical spacing (based on equilateral triangle height)

		# Translate grid position to canvas coordinates
		canvas_x = x * spacing_x
		canvas_y = y * spacing_y
		Trig.points = triangle_points(x, y, size, Trig.orientation)

def triangle_points(center_x, center_y, size, orientation):
	"""
	Calculate the vertices of a triangle.

	<center_x> X coordinate of the triangle center.
	<center_y> Y coordinate of the triangle center.
	<size> Side length of the triangle.
	<orientation> Orientation of the triangle (0 or 1).
	<< return: List of tuples representing triangle vertices [(x1, y1), (x2, y2), (x3, y3)].
	"""
	height = size * (3 ** 0.5) / 2
	if orientation == 0:  # Upward pointing
		return [
			(center_x, center_y - height / 2),
			(center_x - size / 2, center_y + height / 2),
			(center_x + size / 2, center_y + height / 2)
		]
	else:  # Downward pointing
		return [
			(center_x, center_y + height / 2),
			(center_x - size / 2, center_y - height / 2),
			(center_x + size / 2, center_y - height / 2)
		]

class OctagonalCell(Cell):
	def __init__(Oct, position, size):
		super().__init__(position, size)
		Oct.points = []  # Octagon corners, calculated if needed
		Oct.calculate_points()
	def find_neighbors(Oct, grid):
		"""
		Determine neighbors for an octagonal cell.
		Octagonal cells connect to 8 potential neighbors:
		- 4 orthogonal (sides): top, bottom, left, right
		- 4 diagonal: top-left, top-right, bottom-left, bottom-right
		"""
		r, c = Oct.position
		potential_positions = [
			(r - 1, c),      # Top
			(r + 1, c),      # Bottom
			(r, c - 1),      # Left
			(r, c + 1),      # Right
			(r - 1, c - 1),  # Top-left diagonal
			(r - 1, c + 1),  # Top-right diagonal
			(r + 1, c - 1),  # Bottom-left diagonal
			(r + 1, c + 1)   # Bottom-right diagonal
			]
		for pos in potential_positions:
			neighbor = grid.get_cell(pos)
			if neighbor:
				Oct.connect(neighbor)
	def calculate_points(Oct):
		"""
		Calculate the octagon's points
		"""
		row, col = Oct.position
		size = Oct.size
		center_x = MapConfig.MARGIN + col * size * 1.5
		center_y = MapConfig.MARGIN + row * size * 1.5
		Oct.points = octagon_points(center_x, center_y, size)
def octagon_points(center_x, center_y, size):
	"""
	Calculate the 8 corners of an octagon based on a square with truncated corners.
	:param center_x: X coordinate of the octagon's center.
	:param center_y: Y coordinate of the octagon's center.
	:param size: Side length of the base square (edge length of the octagon).
	:return: List of 8 corner coordinates [(x1, y1), ..., (x8, y8)].
	"""
	# Half size for offsets
	half_size = size
	# Corner truncation factor (e.g., 0.3 can be adjusted for more or less truncation)
	truncate = 2*size * 0.3

	# Calculate the 8 points of the octagon
	points = [
		(center_x - half_size, center_y - half_size + truncate),  # Top-left
		(center_x - half_size + truncate, center_y - half_size),  # Top
		(center_x + half_size - truncate, center_y - half_size),  # Top-right
		(center_x + half_size, center_y - half_size + truncate),  # Right
		(center_x + half_size, center_y + half_size - truncate),  # Bottom-right
		(center_x + half_size - truncate, center_y + half_size),  # Bottom
		(center_x - half_size + truncate, center_y + half_size),  # Bottom-left
		(center_x - half_size, center_y + half_size - truncate)   # Left
		]

	return points

class Grid:
	def __init__(grid):
		grid.cells = {}
			# Dictionary of cells: {(row, col): Cell}
		grid.rows = 0
		grid.cols = 0
	def add_cell(grid, cell):
		"""Add a cell to the grid."""
		grid.cells[cell.position] = cell
		c,r = cell.position
		grid.cols= max(grid.cols , 1+c)
		grid.rows= max(grid.rows , 1+ r)
		cell.calculate_points()
	def get_cell(grid, position):
		"""Retrieve a cell by its position."""
		return grid.cells.get(position)
	def expand(grid, position=(0,0), cell_type = Cell, size = SIZE):
		"""
		Expand the grid by adding a new cell of the given type.
		<position> Position of the new cell (row, col)
		<cell_type> Class of the cell to add (e.g., Triangle)
		"""
		if position not in grid.cells:
			# Create a new cell and connect to neighbors
			new_cell = cell_type(position=position, size=size)
			grid.add_cell(new_cell)
			grid.connect_neighbors(new_cell)
			return new_cell
		return grid.get_cell(position)
	def connect_neighbors(grid, cell):
		"""Delegate neighbor connection to the cell."""
		cell.find_neighbors(grid)
	def display(grid):
		"""Display the grid's cells and their neighbors."""
		for position, cell in grid.cells.items():
			neighbor_positions = [n.position for n in cell.neighbors]
			print(f"{CellIcon(cell)} Cell at {position} has neighbors: {neighbor_positions}")
	def visual(grid):
		"""Display the grid's cells and their neighbors."""
		# Determine grid boundaries
		min_row = min(cell.position[0] for cell in grid.cells.values())
		max_row = max(cell.position[0] for cell in grid.cells.values())
		min_col = min(cell.position[1] for cell in grid.cells.values())
		max_col = max(cell.position[1] for cell in grid.cells.values())

		# Create a display buffer (matrix) for the grid
		display_rows = [[" " for _ in range((max_col - min_col + 1) * 3)]
						for _ in range((max_row - min_row + 1) * 3)]

		# Populate the display buffer with cell icons and connections
		for cell in grid.cells.values():
			r, c = cell.position
			icon_r = (r - min_row) * 3 + 1  # Center row for the cell
			icon_c = (c - min_col) * 3 + 1  # Center column for the cell
			display_rows[icon_r][icon_c] = CellIcon(cell)

			for n in cell.neighbors:
				nr, nc = n.position
				dr, dc = nr - r, nc - c
				connection_r = icon_r + dr  # Adjust for neighbor's relative position
				connection_c = icon_c + dc  # Adjust for neighbor's relative position

				# Determine the appropriate symbol based on relative position
				if dr == -1 and dc == -1:  # Top-left
					display_rows[icon_r - 1][icon_c - 1] = "╲"
				elif dr == -1 and dc == 0:  # Top
					display_rows[icon_r - 1][icon_c] = "│"
				elif dr == -1 and dc == 1:  # Top-right
					display_rows[icon_r - 1][icon_c + 1] = "╱"
				elif dr == 0 and dc == -1:  # Left
					display_rows[icon_r][icon_c - 1] = "─"
				elif dr == 0 and dc == 1:  # Right
					display_rows[icon_r][icon_c + 1] = "─"
				elif dr == 1 and dc == -1:  # Bottom-left
					display_rows[icon_r + 1][icon_c - 1] = "╱"
				elif dr == 1 and dc == 0:  # Bottom
					display_rows[icon_r + 1][icon_c] = "│"
				elif dr == 1 and dc == 1:  # Bottom-right
					display_rows[icon_r + 1][icon_c + 1] = "╲"

		# Print the grid
		for row in display_rows:
			print("".join(row))
	def initialize(grid):
		for cell in grid.cells.values():
			cell.Full_Range()

def CellShape(n):
	cell_type = Cell
	if n == "octagonal" or n == 8:
		MapConfig.SetOctagonal()
		return OctagonalCell
	if n == "hexagonal" or n == 6:
		MapConfig.SetHexagonal()
		return HexCell
	if n == "triangular" or n == 3:
		MapConfig.SetTriangular()
		return TriangleCell
	MapConfig.SetSquare()
	return Cell

def CellIcon(cell):
	if isinstance(cell, OctagonalCell):
		return "✷"
	if isinstance(cell, HexCell):
		return "⬡"
	if isinstance(cell, TriangleCell):
		if cell.orientation == 0:
			return "▽"
		else:
			return "△"
	if isinstance(cell, Cell):
		return "·"
	return "﹖"

def create_grid(rows, cols, size = SIZE, shape="triangular"):
	"""
	Creates a grid structure based on the specified grid type.

	<rows> Number of rows in the grid.
	<cols> Number of columns in the grid.
	<size> Base size of each grid cell (e.g., radius for hexagonal).
	<grid> Type of grid to create ("hexagonal" or "triangular").
	<< return: A grid data structure as a dictionary.
	"""
	cell_type = CellShape(shape)
	grid = Grid()
	for row in range(rows):
		for col in range(cols):
			grid.expand((row, col), cell_type, size)
	return grid

def create_hexagonal_grid(rows, cols, size):
	"""
	Creates a hexagonal grid.

	<rows> Number of rows.
	<cols> Number of columns.
	<size> Radius of each hexagon.
	<< return: A dictionary representing the hexagonal grid.
	"""
	MapConfig.SetHexagonal()
	return create_grid(rows, cols, size, 6)

def create_triangular_grid(rows, cols, size):
	"""
	Creates a triangular grid.

	<rows> Number of rows.
	<cols> Number of columns.
	<size> Side length of each triangle.
	<< return: A dictionary representing the triangular grid.
	"""
	MapConfig.SetTriangular()
	return create_grid(rows, cols, size, 3)

def visual_grid(grid):
	"""
	Display the grid using symbolic representation for each cell type and levels.
	<grid> The grid object containing cells.
	"""
	# Display grid dimensions
	print(f"{grid.rows}r x {grid.cols}c")

	# Determine grid boundaries
	min_row = min(cell.position[0] for cell in grid.cells.values())
	max_row = max(cell.position[0] for cell in grid.cells.values())
	min_col = min(cell.position[1] for cell in grid.cells.values())
	max_col = max(cell.position[1] for cell in grid.cells.values())

	# Create a display buffer
	display_rows = []
	for r in range(min_row, max_row + 1):
		row = []
		for c in range(min_col, max_col + 1):
			cell = grid.get_cell((r, c))
			if cell:
				try:
					level = cell.Level()  # Display fixed level
					row.append(f"{level:^3}")
				except ValueError:
					row.append(" ??? ")  # Indicate unresolved cell
			else:
				row.append("     ")  # Empty space for missing cells
		display_rows.append(row)

	# Print the grid row by row
	for row in display_rows:
		print(" ".join(row))


def main():
	triangular_grid = create_grid(5, 5, size=40, shape="triangular")
	triangular_grid.display()
	visual_grid(triangular_grid)
	triangular_grid.visual()

	hexagonal_grid = create_grid(8, 8, size=30, shape="hexagonal")
	hexagonal_grid.display()
	visual_grid(hexagonal_grid)

	hexagonal_grid.visual()

	octagonal_grid = create_grid(3, 3, size=60, shape="octagonal")
	octagonal_grid.display()
	visual_grid(octagonal_grid)

	octagonal_grid.visual()

# main()
