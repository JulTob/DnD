
from AtlasOfMapmaking.Map_of_HandDrawing import  add_edge_shading, add_hand_drawn_filter, add_icon_filter

def add_svg_filters(defs):
    """Add all necessary filters to the SVG defs."""
    add_hand_drawn_filter(defs)
    add_icon_filter(defs)
    add_land_distortion_filter(defs)
    add_edge_shading(defs)



def add_land_distortion_filter(defs):
	"""Add a filter for fractal-based smushing of map features."""
	filter_element = SubElement(defs, "filter", {
		"id": "landDistortion",
		"filterUnits": "userSpaceOnUse",
		"x": "-10%", "y": "-10%",
		"width": "120%", "height": "120%"
		})

	baseFrequency = 1 / RADIUS
	# Generate turbulence (fractal noise pattern)
	feTurbulence = SubElement(filter_element, "feTurbulence", {
		"type": "turbulence",
		"baseFrequency": f"{baseFrequency}",
			# Lower values make larger shapes; adjust for more/less fractal effect
		"numOctaves": "4",
			# Higher values add complexity
		"background-repeat": "stitch",
		"result": "noise"
		})

	baseFrequency = 1 / RADIUS
	# Generate turbulence (fractal noise pattern)
	feTurbulence = SubElement(filter_element, "feTurbulence", {
		"type": "fractalNoise",
		"baseFrequency": f"{baseFrequency}",
			# Lower values make larger shapes; adjust for more/less fractal effect
		"numOctaves": f"{RADIUS/min(MapConfig.GRID_WIDTH, MapConfig.GRID_HEIGHT)}",
			# Higher values add complexity
		"background-repeat": "stitch",
		"result": "noise"
		})


	# Displace the land with the fractal noise
	displacement_scale = RADIUS / 5
	feDisplacementMap = SubElement(filter_element, "feDisplacementMap", {
		"in": "SourceGraphic",
		"in2": "noise",
		"scale": f"{displacement_scale}",
			# Higher scale makes the distortion more dramatic
		"xChannelSelector": "R",
			# Use the red channel for x-axis distortion
		"yChannelSelector": "G",
			# Use the green channel for y-axis distortion
		"result": "distorted"
		})

	# Add Morphology to give shapes a more organic, rounded feel
	morphology_radius = RADIUS / 20
	feMorphology = SubElement(filter_element, "feMorphology", {
		"in": "SourceGraphic",         # Apply after distortion
		"operator": "dilate",      # "dilate" makes shapes larger and rounder; "erode" shrinks them
		"radius": f"{morphology_radius}",             # Adjust for the desired rounding/bubbliness
		"result": "morphed"
		})

	feMorphology2 = SubElement(filter_element, "feMorphology", {
		"in": "SourceGraphic",         # Apply after distortion
		"operator": "erode",      # "dilate" makes shapes larger and rounder; "erode" shrinks them
		"radius": f"{morphology_radius}",             # Adjust for the desired rounding/bubbliness
		"result": "morphed"
		})



	# Output the final result
	feMerge = SubElement(filter_element, "feMerge")
	SubElement(feMerge, "feMergeNode", {"in": "SourceGraphic"})
	SubElement(feMerge, "feMergeNode", {"in": "blurred"})
