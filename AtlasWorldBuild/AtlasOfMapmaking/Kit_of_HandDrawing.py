
from AtlasOfMapmaking.Shop_of_Parchment import create_svg_root, add_parchment_texture, add_compass_rose
from xml.etree.ElementTree import Element, SubElement, tostring
from AtlasOfMapmaking.Compass_of_MapConfiguration import MapConfig
from random import randint

BACKGROUND_COLOR = "#ad5f0b"
PARCHMENT_COLOR = "#f5deb3"
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
		'Caveat', 'Tangerine',
		'cursive',
			]

def Font():
	from random import sample, seed, choice
	from time import time_ns
	seed(time_ns())
	result = choice(FONT_FAMILY)
	return result

def Place_Color():
	from random import choice, seed
	from time import time_ns
	seed(time_ns())
	INK_COLORS = [
		"#070D0D",
		"black",
		"#081910",
		"#242E16",
		"#041322",
		"#0D0332",
		"#67032D",
		"#350719",
		"#0A001C",
		"#4D0135",
		"#004040",
		"#2B0202",
		"#100C08",
		"#1B2431",
		"#00035B",
		"#341C02",
		"#013220",
		"#000435",
		]
	result= choice(INK_COLORS)
	return result

def set_emoji_filter():
	result = '''
<filter id="outline-indigo">
<feMorphology in="SourceAlpha" result="expanded"
operator="dilate" radius="3"/>
<feFlood flood-color="indigo" result="indi" />
<feComposite in ="indi" in2="expanded" operator="in" />
<feComposite in="SourceGraphic"/>
</filter>

'''
	return result

def draw_emoji(emoji):
	result = f''' <clipPath id='emojiClipPath'>
		  <text filter="url(#filter)" x="0" y="80" font-family="Helvetica" font-weight="bold"
		  font-size="7em" fill="#000000">
		  {emoji}
		  </text>
	</clipPath>'''
	return result

def add_edge_shading(defs):
	gradient = SubElement(defs, "radialGradient", {
		"id": "edge_shading",
		"cx": "50%",
		"cy": "50%",
		"r": "70%",
		"fx": "50%",
		"fy": "50%"
	})
	SubElement(gradient, "stop", {
		"offset": "70%",
		"stop-color": f"{BACKGROUND_COLOR}",
	})
	SubElement(gradient, "stop", {
		"offset": "100%",
		"stop-color": "rgba(0,0,0,0.7)",
	})

def add_parchment_background(svg, defs):
	# Add the parchment texture pattern
	add_parchment_texture(defs)
	# Add the edge shading gradient
	add_edge_shading(defs)

	# Group to hold background elements
	background_group = SubElement(svg, "g")

	# Base parchment color rectangle
	SubElement(background_group, "rect", {
		"x": "0",
		"y": "0",
		"width": str(MapConfig.width()),
		"height": str(MapConfig.height()),
		"fill": PARCHMENT_COLOR
	})

	# Overlay the noise pattern
	SubElement(background_group, "rect", {
		"x": "0",
		"y": "0",
		"width": str(MapConfig.width()),
		"height": str(MapConfig.height()),
		"fill": "url(#parchment_texture)"
	})

	# Overlay the edge shading
	SubElement(background_group, "rect", {
		"x": "0",
		"y": "0",
		"width": str(MapConfig.width()),
		"height": str(MapConfig.height()),
		"fill": "url(#edge_shading)"
	})

def add_hand_drawn_filter(defs):
	# Create a filter for the hand-drawn effect
	filter_element = SubElement(defs, "filter", {
		"id": "handDrawnFilter",
		"filterUnits": "objectBoundingBox",
		"x": "0%", "y": "0%",
		"width": "200%", "height": "200%"
		})

	# Generate turbulence (noise pattern)
	feTurbulence = SubElement(filter_element, "feTurbulence", {
		"type": "fractalNoise",
		"baseFrequency": "0.05",  # Adjust for more or less distortion
		"numOctaves": "4",
		"result": "noise",
		"seed": "2"
		})

	# Displace the image using the noise
	feDisplacementMap = SubElement(filter_element, "feDisplacementMap", {
		"in": "SourceGraphic",
		"in2": "noise",
		"scale": "5",  # Adjust for more or less distortion
		"xChannelSelector": "R",
		"yChannelSelector": "G",
		"result": "displaced"
		})

	# Output the final image
	feMerge = SubElement(filter_element, "feMerge")
	SubElement(feMerge, "feMergeNode", {"in": "blurred"})

def place_icon( parent_group, center_x, center_y, icon, icon_size ):
	"""Place an icon with a hand-drawn filter."""
	SubElement(
		parent_group,
		"text",
		x = str( center_x ),
		y = str( center_y ),
		attrib = {
			"text-anchor": "middle",
			"dominant-baseline": "middle",
			"font-size": f"{icon_size*2 }",  # Icon size
			"font-family": Font() ,  # Hand-drawn style font
			"style": "filter: url(#handDrawnFilter);",
			"fill": "black",
			},
		).text = icon

def name_place( parent_group, center_x, center_y, landmark , icon_size):
	"""Place an icon with a hand-drawn filter."""
	SubElement(
		parent_group,
		"text",
		x = str( center_x + MapConfig.RADIUS ),
		y = str( center_y + randint(MapConfig.RADIUS, MapConfig.RADIUS*2 )) ,
		attrib = {
			"text-anchor": "middle",
			"dominant-baseline": "middle",
			"font-size": f"{icon_size}",  # Name size
			"font-family": Font() ,  # Hand-drawn style font
			"style": "filter: url(#handDrawnFilter);",
			"fill": Place_Color(),
			"fill-opacity": "1"
			},
		).text = landmark

def place_icon_into_svg(svg_elements, cell, icon):
	"""
	Add an icon to the SVG elements list for a specific cell.
	<svg_elements> List of SVG strings.
	<cell> Cell object where the icon will be placed.
	<icon> The icon (string) to display.
	"""
	cx = sum(x for x, y in cell.points) / len(cell.points)
	cy = sum(y for x, y in cell.points) / len(cell.points)

	svg_elements.append(
		f'<text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="middle" '
		f'font-size="{MapConfig.RADIUS * 1.5}" font-family="Patrick Hand, sans-serif" '
		f'fill="black" style="filter: url(#icon_filter);">{icon}</text>'
		)


def add_icon_filter(defs):
	"""Add a filter to make icons appear hand-drawn."""
	filter_element = SubElement(defs, "filter", {
		"id": "iconHandDrawn",
		"filterUnits": "userSpaceOnUse",
		"x": "0%", "y": "0%",
		"width": "200%", "height": "200%",  # Adjust bounds to include nearby distortions
		})
	hand_emoji(filter_element)
	feBlend = SubElement(filter_element, "feBlend", {
		"in": "grayscale",
		"in2": "noise",
		"mode": "multiply",
		"result": "inkedEdges"
		})

	# Step 3: Add some hand-drawn imperfections
	feDisplacementMap = SubElement(filter_element, "feDisplacementMap", {
		"in": "inkedEdges",
		"in2": "noise",
		"scale": "3",
		"xChannelSelector": "R",
		"yChannelSelector": "G",
		"result": "displaced"
	})

	# Extract edges using morphology
	feMorphology = SubElement(filter_element, "feMorphology", {
		"in": "grayscale",
		"operator": "dilate",  # Enhance edges
		"radius": "1",
		"result": "edges"
		})

	# brightness to invisible
	feColorMatrix = SubElement(filter_element, "feColorMatrix", {
		"in": "SourceGraphic",
		"type": "matrix",
		"values": "0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0.8 0.8 0.8 1 0",
		"result": "grayscale"
		})


	# Step 4: Merge back into the final result
	feMerge = SubElement(filter_element, "feMerge")


	SubElement(feMerge, "feMergeNode", {"in": "displaced"})

def hand_emoji(defs):
		# Create a filter element
	flt = SubElement(defs, "filter", {
		"id": "handdrawnOutline",
		"filterUnits": "objectBoundingBox",
		"x": "0%",
		"y": "0%",
		"width": "100%",
		"height": "100%"
	})

	# Step 1: Convert to grayscale
	# This simplifies edge detection by removing color complexity.
	SubElement(flt, "feColorMatrix", {
		"in": "SourceGraphic",
		"type": "saturate",
		"values": "0",
		"result": "grayscale"
	})

	# Step 2: Detect edges using a Laplacian kernel
	# The kernel below finds edges by comparing each pixel's luminance to its neighbors.
	SubElement(flt, "feConvolveMatrix", {
		"in": "grayscale",
		"result": "edges",
		"order": "5",
		"kernelMatrix": '''"
			 1   1    1  1
			 1  -3   -3  1
			 1  -3   -3  1
			 1   1    1  1"''',
		"edgeMode": "duplicate"
	})

	# Step 3: Thresholding the result
	# Use feComponentTransfer to force pixels above a certain luminance to remain opaque
	# and everything else to become transparent.
	comp = SubElement(flt, "feComponentTransfer", {
		"in": "edges",
		"result": "thresholded"
	})
	# The alpha channel is adjusted: slope and intercept values chosen to emphasize edges.
	# Increase slope and negative intercept can push dim edges to full opacity.
	SubElement(comp, "feFuncA", {
		"type": "linear",
		"slope": "10",
		"intercept": "-9"
	})

	# Step 4: Set the final line color to black
	# We ensure the visible outlines are black by zeroing out RGB and leaving alpha as is.
	SubElement(flt, "feColorMatrix", {
		"in": "thresholded",
		"type": "matrix",
		# R   G   B   A   Offset
		"values": 	"0 0 0 0 0 "
					"0 0 0 0 0 "
					"0 0 0 0 0 "
					"0.5 0.5 0.5 1 0.12",
		"result": "finalEdges"
	})

import xml.etree.ElementTree as ET

def handdrawn_emoji(emoji: str) -> str:
	# Create the main SVG element
	svg = ET.Element("svg", {
		"xmlns": "http://www.w3.org/2000/svg",
		"width": "200",
		"height": "200",
		"viewBox": "0 0 200 200"
	})

	# Define the filter in <defs>
	defs = ET.SubElement(svg, "defs")
	flt = ET.SubElement(defs, "filter", {
		"id": "handdrawnOutline",
		"filterUnits": "objectBoundingBox",
		"x": "0%",
		"y": "0%",
		"width": "100%",
		"height": "100%"
	})
	ET.SubElement(flt, "feColorMatrix", {
		"in": "SourceGraphic",
		"type": "saturate",
		"values": "0",
		"result": "grayscale"
	})
	ET.SubElement(flt, "feConvolveMatrix", {
		"in": "grayscale",
		"result": "edges",
		"order": "3",
		"kernelMatrix": "-1 -1 -1 -1 8 -1 -1 -1 -1",
		"edgeMode": "duplicate"
	})
	comp = ET.SubElement(flt, "feComponentTransfer", {
		"in": "edges",
		"result": "thresholded"
	})
	ET.SubElement(comp, "feFuncA", {
		"type": "linear",
		"slope": "10",
		"intercept": "-9"
	})
	ET.SubElement(flt, "feColorMatrix", {
		"in": "thresholded",
		"type": "matrix",
		"values": "0 0 0 0 0 "
				  "0 0 0 0 0 "
				  "0 0 0 0 0 "
				  "0 0 0 1 0",
		"result": "finalEdges"
	})

	# Add the emoji text element and apply the filter
	# The text is centered with large font-size to show the outline clearly.
	text = ET.SubElement(svg, "text", {
		"x": "100",
		"y": "100",
		"font-size": "100",
		"text-anchor": "middle",
		"dominant-baseline": "central",
		"filter": "url(#handdrawnOutline)"
	})
	text.text = emoji

	# Return the SVG as a string
	return ET.tostring(svg, encoding="unicode")

# Example usage:
# svg_code = handdrawn_emoji("🙂")
# print(svg_code)
