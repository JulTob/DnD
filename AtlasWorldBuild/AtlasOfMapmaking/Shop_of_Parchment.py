# SVG Initialization

from xml.etree.ElementTree import Element, SubElement, tostring
from AtlasOfMapmaking.Compass_of_MapConfiguration import MapConfig


def create_svg_root():
    """Create the root SVG element."""
    width, height = Compass_of_MapConfig.calculate_svg_dimensions()
    svg = Element("svg", xmlns="http://www.w3.org/2000/svg", width=str(width), height=str(height))
    SubElement(svg, "rect", {
        "x": "0", "y": "0",
        "width": str(width), "height": str(height),
        "fill": str(PARCHMENT_COLOR)  # Parchment background
    })
    return svg


def add_parchment_texture(defs):
	# Create a filter for the paper texture
	filter_element = SubElement(defs, "filter", {
		"id": "paperTexture",
		"x": "0%", "y": "0%",
		"width": "100%", "height": "100%"
	})
	feTurbulence = SubElement(filter_element, "feTurbulence", {
		"type": "fractalNoise",
		"baseFrequency": "0.8",
		"numOctaves": "5",
		"result": "noise"
	})
	feColorMatrix = SubElement(filter_element, "feColorMatrix", {
		"in": "noise",
		"type": "saturate",
		"values": "0"
	})
	feComposite = SubElement(filter_element, "feComposite", {
		"in": "SourceGraphic",
		"in2": "noise",
		"operator": "arithmetic",
		"k1": "0", "k2": "1", "k3": "1", "k4": "0"
	})


def add_compass_rose(parent_group):
	"""Add a compass rose to the map."""
	compass_group = SubElement(parent_group, "g", attrib={"transform": f"translate({MapConfig.width() - 150}, 150)"})
	# Outer circle
	# Directions
	directions = [
		("N", 0, -40), ("E",  40, 0),
		("S", 0,  20), ("W", -40, 0)]
	for label, x, y in directions:
		SubElement(compass_group, "text", {
			"x": str(x), "y": str(y),
			"text-anchor": "middle",
			"dominant-baseline": "middle",
			"font-size": "20",
			"font-family": "Merriweather",
			"fill": "black"
		}).text = label
	# Compass rose
	SubElement(compass_group, "text", {
		"x": "0", "y": "0",
		"text-anchor": "middle",
		"dominant-baseline": "middle",
		"font-size": "75",
		"font-family": "Merriweather",
		"fill": "black"
	}).text = Rose()

def add_scale_bar(parent_group):
	"""Add a scale bar to the map."""
	scale_group = SubElement(parent_group, "g", attrib={"transform": f"translate(100, {MapConfig.height() - 100})"})
	# Scale line
	SubElement(scale_group, "line", {
		"x1": "0", "y1": "0", "x2": "200", "y2": "0",
		"stroke": "black", "stroke-width": "4"
	})
	# Tick marks
	for i in range(5):
		x = i * 50
		SubElement(scale_group, "line", {
			"x1": str(x), "y1": "-10", "x2": str(x), "y2": "10",
			"stroke": "black", "stroke-width": "4"
		})
	# Label
	SubElement(scale_group, "text", {
		"x": "100", "y": "30",
		"text-anchor": "middle",
		"font-size": "20",
		"font-family": "Merriweather",
		"fill": "black"
	}).text = "200 miles"
