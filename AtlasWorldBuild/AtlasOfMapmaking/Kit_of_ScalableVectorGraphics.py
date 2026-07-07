from AtlasOfMapmaking.Compass_of_Biomes import Biomes, Icons, Color, density
from AtlasOfMapmaking.Astrolabe_of_Grids import *
from AtlasOfMapmaking.Compass_of_MapConfiguration import MapConfig
from AtlasOfMapmaking.Kit_of_WaveFunctionCollapse import wave_function_collapse
from AtlasOfMapmaking.Kit_of_HandDrawing import name_place, draw_emoji, set_emoji_filter, place_icon, add_icon_filter, add_hand_drawn_filter
from xml.etree.ElementTree import Element, SubElement, tostring
from math import atan2
from random import shuffle, randint, gauss
from heapq import heappop, heappush
from math import dist
from math import atan2, pi

MARGIN = MapConfig.MARGIN
GRID_WIDTH = MapConfig.GRID_WIDTH
GRID_HEIGHT = MapConfig.GRID_HEIGHT
BASE = MapConfig.BASE

FONT_FAMILY = [
			"aakar",
			'cmmi10',
			'Chilanka',
			"cmr10",
			"eufm10",
			"Eunjin",
			"'Hadasim CLM'",
			"Karumbi",
			"Purisa",
			"'Pirata One'",
			"rsfs10",
			"Scheherazade",
			"'Times New Roman'",
			"TSCu_Comic"
			"TSCu_Times"
			"'UnPen'",
			"UnPilgi",
			"UnPilgia",
			]

def Font():
	from random import sample, seed, choice
	from time import time_ns
	seed(time_ns())
	result = choice(FONT_FAMILY)
	return result

def cell_to_vector(cell, neighbor):
	dx = neighbor.position[0] - cell.position[0]
	dy = neighbor.position[1] - cell.position[1]
	return atan2(dy, dx)

def angle_difference(angle1, angle2):
	diff = abs(angle1 - angle2)
	return min(diff, 2 * pi - diff)  # Ensure the smallest angle difference is chosen

def calculate_centroid(cell):
	"""Calculate the centroid of a cell based on its corner points."""
	if not hasattr(cell, 'points') or not cell.points:
		cell.calculate_points()

	x_sum = sum(x for x, y in cell.points)
	y_sum = sum(y for x, y in cell.points)
	num_points = len(cell.points)

	return x_sum / num_points, y_sum / num_points

def add_compass_rose(grouping):
	"""Add a compass rose to the map."""
	compass_group = SubElement(grouping, "g", attrib={
		"transform": f"translate({MapConfig.width() - 150}, 150), rotate({randint(-180,180)})"},
		)

	# Circles around the rose
	# Each circle is centered at (0,0), so they share the same center as the rose symbol
	circle_radii = [
		randint(75,100),
		randint(80,120),
		randint(80,120),
		randint(80,120),
		]  # Make as many as you like, set radii here
	for r in circle_radii:
		SubElement(compass_group, "circle", {
			"cx": f"{0}",
			"cy": f"{0}",
			"r":  str(r),
			"fill": "none",
			"stroke": "black",        # Use your preferred color
			"stroke-width": f"{randint(0,3)}"      # Adjust thickness
			})

	# Directions
	directions = [("N", 0, -75), ("E", 75, 0), ("S", 0, 75), ("W", -75, 0), ]
	for label, x, y in directions:
		SubElement(compass_group, "text", {
			"x": str(x), "y": str(y),
			"text-anchor": "middle",
			"dominant-baseline": "middle",
			"font-size": f"{gauss(40,5)}",
			"font-family": "Merriweather",
			"fill": "black"
		}).text = label
	# Compass rose
	SubElement(compass_group, "text", {
		"x": "0", "y": "0",
		"text-anchor": "middle",
		"dominant-baseline": "middle",
		"font-size": f"{gauss(100,20)}",
		"font-family": "Merriweather",
		"fill": "black"
	}).text = Rose()

def Rose():
	from random import choice
	symbol = choice([
	"✵", "✥", "✦", "✧", "✵", "✷", "𑁍", "☸", "𖣓", "☣", "֍", "🜹", "᯽", "𖧷", "𓇬", "𖧵",
	"⁜","⊹","⊹", "⧾", "᛭", "𖦷", "✠", "🜊", "🜋", "☩", "🝊", "𐫰", "𑇍", "𖣊", "⌖", "𖥠", "𖥟", "𖥤",
	"࿇", "𐦟", "𖤍", "۞", "𓌖", "𓆉", "⛯", "𝚿", "𝛀", "᳀", "༒", "ⵥ", "❂", "☀", "☼", "𖤓",
	"✵", "✵", "✵", "✵", "✵", "✵", "✵", "✵", "✵", "✵", "✵", "✵", "✵", "✵", "✵", "✵",
	"✴︎", "𖣔", "𑗊", "𑗋", "𑗌", "𑗍", "𑗎", "ॐ", "☸︎", "⚕︎", "道", "⚔︎", "⚖︎", "𓁽",
	"ᛤ", "Ӿ", "𖡨", "𖠁", "𖢖", "𖢌", "𖢖", "𖢐", "𖢭", "𖡦", "𖦏",
	])
	return symbol

def cell_to_svg(cell):
	if not hasattr(cell, 'points') or not cell.points:
		cell.calculate_points()

	# Calculate centroid
	cx = sum(x for x, y in cell.points) / len(cell.points)
	cy = sum(y for x, y in cell.points) / len(cell.points)

	# Sort points by angle around the centroid
	cell.points.sort(key=lambda p: atan2(p[1] - cy, p[0] - cx))

	# Generate SVG points string
	points = " ".join(
			f"{x+gauss(0,20)},{y+gauss(0,20)}"
			for x, y in cell.points
			)

	altitude = cell.Level()
	biome = Biomes.height_to_biome(altitude)
	fill_color = Color(biome)

	result = f'<polygon points="{points}" '
	result += f'fill="{fill_color}" '
	result += f'stroke="none" stroke-width="0" '
	result += f'fill-opacity="0.{randint(250, 750)}" '
	result += CellFilter()
	result += f' />'
	return result

def add_gradients(defs):
	for biome in Biomes.list_all():
		gradient = SubElement(defs, "linearGradient", id=f"{biome}_gradient")
		SubElement(gradient, "stop", offset="5%", stop_color=Color(biome))
		SubElement(gradient, "stop", offset="95%", stop_color="#FFF")  # White for lightening effect

def canvas_size():
	width = MapConfig.width()
	height = MapConfig.height()
	return width, height

def Position_to_Coordenate(x, y):
	cx = MARGIN + MapConfig.BASE * x
	cy = MARGIN + MapConfig.BASE * y
	return cx, cy

def SetCellFilter():
	expansion = randint(5,MapConfig.BASE)
	frequency = randint(100, 300)
	numOctaves = randint(5,15)
	displacement = randint(150,300)
	return f'''
	<filter id="cell_filter" x="-200%" y="-200%" width="1000%" height="1000%">
	<!-- Turbulence for displacement -->
	<!-- Expand the shapes -->
	<feMorphology in="SourceGraphic"
		operator="dilate"
		radius="{expansion}"
		result="expanded" />

	<feTurbulence type="fractalNoise"
				baseFrequency="{1/frequency}"
				numOctaves="{numOctaves}"
				result="turbulence"/>

	<!-- Displacement to create wavy distortion -->
	<feDisplacementMap 	in="expanded"
						in2="turbulence"
						scale="{displacement}"
						xChannelSelector="R"
						yChannelSelector="G" />
</filter>
'''

def add_window_mask(width, height, margin=50):
	mask = f'''
	<mask id="window_mask">
		<rect x="0" y="0" width="{width}" height="{height}" fill="black"/>
		<rect x="{margin}" y="{margin}" width="{width - 2 * margin}" height="{height - 2 * margin}" fill="white"/>
	</mask>
	'''
	return mask

def CellFilter():
	return ''' style="filter: url(#cell_filter);" '''

def place_name_and_icon(grid):
	placed_cells = {}  # Track cells with icons or names
	grouping = Element("g")

	for cell in grid.cells.values():
		biome = Biomes.height_to_biome(cell.Level())
		icon, landmark = Icons(biome)

		# Skip if neighboring cells already have icons or names
		if any(neighbor in placed_cells for neighbor in cell.neighbors):
			continue

		if icon and randint(1, 1000) <= density(biome):
			cx, cy = calculate_centroid(cell)
			icon_size = min(MapConfig.BASE, dist(cell.points[0], cell.points[1])) * 0.6

			# Place icon at the centroid
			place_icon(grouping, cx, cy - (icon_size / 2), icon, icon_size + 5)

			# Text area and placement
			text_area(grouping, cx, cy + (icon_size / 2) + 5, landmark, icon_size - 2, cell)

			# Mark this cell as occupied
			placed_cells[cell] = True

	return grouping


def text_area(grouping, cx, cy, text, icon_size, cell):
	# Calculate available area within cell
	text_box_width = MapConfig.BASE * 0.8
	text_box_height = MapConfig.BASE * 0.3

	# Create SVG text element that wraps within the calculated area
	text_element = SubElement(grouping, "text", {
		"x": str(cx),
		"y": str(cy),
		"text-anchor": "middle",
		"dominant-baseline": "middle",
		"font-size": f"{gauss(20, 5)}",
		"font-family": "Merriweather",
		"fill": "black"
	})
	text_element.text = text

	# Clip long names or wrap
	if len(text) > 15:
		text_element.set("textLength", f"{text_box_width}")
		text_element.set("lengthAdjust", "spacingAndGlyphs")


def grid_to_svg(grid):
	"""
	Convert a grid into an SVG map.
	<grid> The grid object containing cells.
	<< return: Complete SVG as a string.
	"""
	width, height = canvas_size()
	svg_elements = []
	background_color = MapConfig.BACKGROUND_COLOR

	# Define SVG filters and styles
	defs = Element("defs")
	defs.append(Element("clipPath", id="map_clip"))
	grouping = place_name_and_icon(grid)

	cell_list = list(grid.cells.values())
	for i in range(1,2):
		shuffle(cell_list)
		for cell in cell_list:
			svg_elements.append(cell_to_svg(cell))

	add_hand_drawn_filter(defs)  # This ensures the filter is present in the SVG
	add_icon_filter(defs)
	add_compass_rose(grouping)

	frame_elements = frame(width, height, frame_layers=3, frame_gap=15, frame_color="#000000")
	svg_defs = tostring(defs, encoding="unicode")
	svg_elements.append(tostring(grouping, encoding="unicode"))
	svg_filter = SetCellFilter()

	# Combine all SVG elements into a full SVG document
	svg_content = "\n"
	svg_content += "\n".join(frame_elements + svg_elements)

	window = 50
	svg_header = f'<svg xmlns="http://www.w3.org/2000/svg" '
	svg_header += f'width="{width}" height="{height}" '
	svg_header += f'viewBox="{-(window)} {-(window)} {width + (window) + 1} {height + (window) + 10}" '

	svg_header += f'style="background-color:{background_color};" >'
	svg_header += '''  <style>
	@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&display=swap');
	.handwritten {{
		font-family: 'Caveat', 'Tangerine', cursive;
		}}
	</style>
'''
	svg_footer = "</svg>"

	return f"{svg_header}{svg_filter}{svg_defs}\n{svg_content}\n{svg_footer}"

def frame(map_width, map_height, frame_layers=3, frame_gap=10, frame_color="#000000"):
	"""Generate frame elements that expand outward evenly."""
	frame_elements = []
	for i in range(frame_layers):
		# Adjust position to expand the frame outward equally
		frame_x = (i * frame_gap)  # Move frame outward to the left
		frame_y = (i * frame_gap)  # Move frame outward to the top
		frame_width = map_width - (2 * (i * frame_gap))  # Contract width
		frame_height = map_height - (2 * (i * frame_gap))  # Contract height

		frame_elements.append(
			f'<rect x="{frame_x}" y="{frame_y}" width="{frame_width}" height="{frame_height}" '
			f'stroke="{frame_color}" fill="{MapConfig.PARCHMENT_COLOR}" stroke-width="{4 - i}" />'
			)
	return frame_elements

def generate_map_example():
	# Create a sample triangular grid
	grid = create_grid(MapConfig.GRID_HEIGHT, MapConfig.GRID_WIDTH, size=MapConfig.BASE, shape="triangular")
	# Convert the grid to SVG
	wave_function_collapse(grid)
	svg_map = grid_to_svg(grid)

	# Save the SVG to a file or print it
	save_svg(svg_map, "new_map.svg")

def save_svg(svg, name = "map.svg"):
	with open(name, "w") as file:
		file.write(svg)
	print(f"SVG map created: {name}")
# Call the example
if __name__ == "__main__":
	generate_map_example()
