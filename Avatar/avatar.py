import svgwrite
	# This library creates SVG vector images
import numpy as np
	# Mathematical utilities
import random as random
	# Random numbers
from PIL import ImageColor
	# Coloring utilities, such as names of colors to hex

base = 250
outline_width = int(0.07*base)  # Define the outline width

x0 = 3*base
y0 = 3*base

head_center = ( x0,     # x
				y0 )    # y

head_radius = int(0.7*base)

'''
Coloring
'''
def Skin_Color(race = None):
	if "Elf" in race:
		skin_colors = [
			"ivory", "floralwhite", "mintcream", "honeydew", "lavenderblush", "seashell",
			"darkslategray", "slategray", "black", "dimgray" # Drow
			]
	elif "Orc" in race:
		skin_colors = [
			"darkolivegreen", "olivedrab", "forestgreen", "yellowgreen"
			]
	elif "Tiefling" in race:
		skin_colors = [
			"lightcoral", "indianred", "crimson", "firebrick", "maroon"
			]
	elif "Dragonborn" in race:
		skin_colors = [
			"gold", "darkred", "midnightblue", "darkslateblue", "steelblue", "sienna"
			]
	elif "Dwarf" in race:
		skin_colors = [
			"rosybrown", "sienna", "chocolate", "maroon", "saddlebrown"
			]
	elif "Aasimar" in race:
		skin_colors = [
			"azure", "aliceblue", "ghostwhite", "lightyellow"
			]
	else: #	"Human", "Gnome", "Halfling" ...:
			skin_colors = [
				"peachpuff", "bisque", "navajowhite", "wheat", "tan", "peru", "saddlebrown", "rosybrown",
				"peachpuff", "mistyrose", "linen",
				"wheat", "burlywood", "tan", "peru",
				]
	return named_color_to_rgb(random.choice(skin_colors))

def Hair_Color(race = None):
	hair_colors = [
		# Natural shades
		"Black", "Brown", "Gold", "Red", "DarkSlateGray", "Indigo", "Gray", "White",
		# Exotic shades for fantasy characters
		"Blue", "Green", "Purple", "Pink", "Turquoise", "Magenta", "Lavender",
		# Dark elf and orc specific shades
		"Silver", "SlateGray", "Navy", "Emerald", "MysticPurple",
		"PaleGoldenrod", "DarkRed", "DarkSlateBlue", "DarkRed",
		"Sienna", "DarkGreen",
		"Lavender",
		# Additional magical and metallic shades
		"Gold", "SandyBrown", "FireBrick", "Sapphire", "Ruby", "Amethyst", "OrangeRed",
		]
	return named_color_to_rgb(random.choice(hair_colors))

def Blade_Color():
	blade_color = named_color_to_rgb(random.choice([
			"Grey", "Gold", "Silver", "Black",    "Grey", "Gold", "Silver",
			"Black", "SteelBlue", "DarkSlateGray",
			"LightGrey", "DarkGrey", "SlateGray", "DimGray", "MidnightBlue",
			"Cornsilk", "PaleGoldenRod", "LightSteelBlue", "DarkSlateBlue",     "FieryRed", "IcyBlue", "MysticPurple", "EtherealWhite", "DarkMagicBlack",
		"ElectricBlue", "SlateGray", "Crimson",
		"RadiantGold", "PoisonGreen", "ShadowGray", "LavaOrange"
			]))
	return blade_color

def Handle_Color():
	handle_color = named_color_to_rgb(random.choice([
			"Grey", "Gold", "Silver", "Brown", "saddlebrown",    "Grey", "Gold", "Silver", "Brown", "SaddleBrown", "DarkRed", "DarkGreen",
			"DarkBlue", "Black", "Tan", "DarkSlateGrey", "RosyBrown", "DarkGoldenRod",
			"DimGrey", "Peru", "Chocolate", "FireBrick", "OliveDrab",     "Ruby", "Emerald", "Sapphire", "Amethyst", "Topaz", "Opal", "Pearl", "Diamond",
		"Turquoise", "Garnet", "Aquamarine", "Citrine", "Peridot", "Onyx", "Jade"
			]))
	return handle_color

def named_color_to_rgb(color_name):
	custom_colors = {
		"Ruby": (224, 17, 95),
		"Emerald": (80, 200, 120),
		"Sapphire": (15, 82, 186),
		"Amethyst": (153, 102, 204),
		"Topaz": (255, 200, 124),
		"Opal": (168, 195, 188),
		"Pearl": (234, 224, 200),
		"Diamond": (185, 242, 255),
		"Turquoise": (64, 224, 208),
		"Garnet": (115, 54, 53),
		"Aquamarine": (127, 255, 212),
		"Citrine": (228, 208, 10),
		"Peridot": (230, 226, 0),
		"Onyx": (53, 56, 57),
		"Jade": (0, 168, 107),
		"FieryRed": (255, 69, 0),
		"IcyBlue": (135, 206, 250),
		"MysticPurple": (138, 43, 226),
		"EtherealWhite": (245, 245, 245),
		"DarkMagicBlack": (12, 12, 12),
		"ElectricBlue": (0, 191, 255),
		"RadiantGold": (255, 223, 0),
		"PoisonGreen": (60, 179, 113),
		"ShadowGray": (105, 105, 105),
		"LavaOrange": (255, 140, 0)
		}
	if color_name in custom_colors:
		return custom_colors[color_name]
	else:
		return ImageColor.getrgb(color_name)  # Use PIL for standard color names

def create_salt_and_pepper_pattern(dwg, pattern_id, size, color, ratio=0.2):
	pattern = dwg.pattern(
		id=pattern_id, size=(size, size), patternUnits="userSpaceOnUse"
		)

	# Create a rectangle for the background color
	pattern.add(dwg.rect(
			insert=(0, 0),
			size=(size, size),
			fill = color
			))

	num_dots = int(size * size * ratio)
	for i in range(num_dots):
		x = random.randint(0, size)
		y = random.randint(0, size)
		dot_size = random.randint(1, 4)
		factor = random.uniform(0.0, 0.40)
		dot_color = lighter(color, factor) if (i%2 == 0) else darker(color, factor)
		r, g, b = dot_color
		pattern.add(dwg.circle(
			center=(x, y),
			r=dot_size,
			fill= svgwrite.rgb(r, g, b)
			))

	dwg.defs.add(pattern)
	return pattern.get_funciri()

def parse_rgb(color_str):
	import re
	match = re.match(r'rgb\((\d+),(\d+),(\d+)\)', color_str)
	if match:
		return tuple(map(int, match.groups()))
	raise ValueError("Invalid color format")

def darker(color, factor=0.5):
	if factor >= 1: return color
	if isinstance(color, str):
		color = parse_rgb(color)
	r, g, b = color
	r, g, b = r - int(r * factor), g - int(g * factor), b - int(b * factor)
	return (r, g, b)

def lighter(color, factor=0.5):
	if isinstance(color, str):
		color = parse_rgb(color)
	r, g, b = color
	r = r + factor * (255 - r)
	g = g + factor * (255 - g)
	b = b + factor * (255 - b)

	return (int(r), int(g), int(b))

def add_transparency(color, alpha=0.5):
	"""Add transparency to an RGB color"""
	if isinstance(color, str):
		color = parse_rgb(color)
	r, g, b = color
	return (r, g, b, int(alpha * 255))

def Color():
	# random color
	return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def hex(rgb):
	return '#{:02x}{:02x}{:02x}'.format(*rgb)

def create_gradient(dwg,gradient_id, color1, color2, color3, direction = 0):
	gradient = dwg.linearGradient(id=gradient_id, gradientTransform=f"rotate({direction})")
	gradient.add_stop_color(offset='0%', color=hex(color1), opacity=1)
	gradient.add_stop_color(offset='50%', color=hex(color2), opacity=1)
	gradient.add_stop_color(offset='100%', color=hex(color3), opacity=1)
	dwg.defs.add(gradient)
	return gradient.get_funciri()

def create_eye_pattern(dwg, pattern_id, color, eye_size, center):
	pattern_size = eye_size * 2
	pattern_center = (pattern_size // 2, pattern_size // 2)
	shine_position = (int(pattern_size* 0.9 / 2),  int(pattern_size* 0.9 / 2))
		# Create a larger pattern to ensure coverage
	pattern = dwg.pattern(
		id=pattern_id,
		size=(pattern_size, pattern_size),
		patternUnits="userSpaceOnUse",
		insert=(center[0] - pattern_size // 2, center[1] - pattern_size // 2)
		)

	random.seed(hex(color))

	# Calculate the offset for the concentric circles with displacement
	offset_x = 0
	offset_y = 0

	radius = pattern_size
	pattern.add(dwg.circle(
			center=pattern_center,
			r=radius,
			fill=svgwrite.rgb(*lighter(color, random.uniform(0,1)))
			))

	radius = eye_size//2
	pattern.add(dwg.circle(
			center=pattern_center,
			r=radius,
			fill=svgwrite.rgb(*color)
			))
	pattern.add(dwg.circle(
			center=pattern_center,
			r=radius//2,
			fill=svgwrite.rgb(*lighter(color, 0.2))
			))

	radius = eye_size//7
	pattern.add(dwg.circle(
			center=pattern_center,
			r=radius,
			fill=svgwrite.rgb(*darker(color, 0.3))
			))


	# anime eye-shine
	shine = lighter(color, 0.8)
	shine = add_transparency(shine, 0.5)
	shine = svgwrite.rgb(shine[0], shine[1], shine[2], '%')

	pattern.add(dwg.circle(
			center=shine_position,
			r=radius//2,
			fill=shine
			))

	dwg.defs.add(pattern)
	return pattern.get_funciri()

'''
Shaping
'''
def add_eyelid_blink(dwg, eye_center, eye_width, eye_height, skin_color, dur="5s"):
	rect = dwg.rect(
		insert=(eye_center[0] - eye_width, eye_center[1] - eye_height),
		size=(eye_width, eye_height),
		fill=svgwrite.rgb(*skin_color),
		opacity=1
	)
	h = int(eye_height)
	values_str = f"0;0;{h};0;{h}"
	keytimes_str = "0;0.8;0.85;0.9;1"

	rect.add(dwg.animate(
		attributeName="height",
		values=values_str,
		keyTimes=keytimes_str,
		dur="4s",
		repeatCount="indefinite"
	))
	dwg.add(rect)

def draw_eyes(dwg, eye_color, skin_color):
	# Parameters for the eyes
	width_factor = random.uniform(0.4, 0.8)
		# Size in x of the eye's base [percentage of head's radius]
	height_factor = random.uniform(0.2, 0.55)
		# Size in y of the eye's base [percentage of head's radius]
	offset_x_factor = random.uniform(0.1, 0.7 -width_factor)
		# Separation in x to the axis [percentage of head's radius]
	offset_y_factor = random.uniform(-0.2, 0.21)
		# Separation in y to the axis [percentage of head's radius]

	eye_width = head_radius * width_factor
	eye_height = head_radius * height_factor
	eye_offset_x = head_radius * offset_x_factor
	eye_offset_y =  head_radius * offset_y_factor
		# Factors scaled to head's proportion

	angle = np.pi * 2 * (random.randint(-15,65))/ 360
		# Angle of the eye's paralelogram shape to the horizontal

	angle_left = -angle
		# For left eye
	angle_right = angle
		# For right eye


	def calculate_parallelogram_vertices(center, width, height, angle):
		dy = height  * np.cos(angle)
		dx = width   * np.sin(angle)
		vertices = [
			(center[0] - width / 2, center[1] + height/2 ),  # Bottom-left
			(center[0] + width / 2, center[1] + height/2 ),  # Bottom-right
			(center[0] + (dx + width) / 2 , center[1]  - height/2),  # Top-right
			(center[0] + (dx - width) / 2 , center[1]  - height/2)   # Top-left
			]
		return vertices

	def create_rounded_path(points, tension=0.5):
		if len(points) < 2:
			raise ValueError("At least two points are required")

		path_data = f"M {points[0][0]},{points[0][1]} "
		for i in range(1, len(points)):
			path_data += f"L {points[i][0]},{points[i][1]} "
		path_data += "Z"  # Close the path
		return path_data

	corner_radius = random.uniform(0, 1)

	# Left eye
	left_eye_center = (x0 - eye_offset_x - eye_width/2, y0 + eye_offset_y)
	left_eye_vertices = calculate_parallelogram_vertices(left_eye_center, eye_width, eye_height, angle_left)
	left_eye_path = create_rounded_path(left_eye_vertices, corner_radius)

	pattern_id_left = "eye_pattern_left"
	pattern_uri_left = create_eye_pattern(dwg, pattern_id_left, eye_color,
										  eye_width, left_eye_center)

	# Right eye
	right_eye_center = (x0 + eye_offset_x + eye_width/2, y0 + eye_offset_y)
	right_eye_vertices = calculate_parallelogram_vertices(right_eye_center, eye_width, eye_height, angle_right)
	right_eye_path = create_rounded_path(right_eye_vertices, corner_radius)


	# Create eye pattern centered on the right eye
	pattern_id_right = "eye_pattern_right"
	pattern_uri_right = create_eye_pattern(
							dwg,
							pattern_id_right,
							eye_color,
							eye_width,
							right_eye_center
							)

	values="url(#eye_pattern); dark_color; url(#eye_pattern)"

	Leye = dwg.path(
		d=left_eye_path,
		fill=pattern_uri_left,
		stroke=svgwrite.rgb(*darker(eye_color)),
		stroke_width=outline_width / 2
		)
	Reye = dwg.path(
		d=right_eye_path,
		fill=pattern_uri_right,
		stroke=svgwrite.rgb(*darker(eye_color)),
		stroke_width=outline_width / 2
		)

	blink_values = "1;1;0;1;0;1;1"
	blink_times = "0;0.84;0.85;0.86;0.87;0.88;1"
	blink_duration= "4s"
	Reye.add(dwg.animate(
			attributeName="opacity",
			values=blink_values,
			keyTimes=blink_times,
			dur=blink_duration,
			repeatCount="indefinite"
			))
	Leye.add(dwg.animate(
			attributeName="opacity",
			values=blink_values,
			keyTimes=blink_times,
			dur=blink_duration,
			repeatCount="indefinite"
			))

	dwg.add(Leye)

	dwg.add(Reye)


def draw_body(dwg, color):
	# Draw body (rectangle with rounded corners)
	body_top_left = (
		int(x0 - 0.5 * base),
		int(y0 + 0.3 * base)
		)
	body_bottom_right = (
		int(x0 + 0.5 * base),
		int(y0 - 0.3 * base)
		)
	body_radius = int(0.20*base)

	pattern_id = "body_texture"
	pattern_uri = create_salt_and_pepper_pattern(
					dwg,
					pattern_id,
					base*2,
					svgwrite.rgb(*color))

	dwg.add(dwg.rect(
		insert=body_top_left,
		size=(base, base),
		rx=body_radius,
		ry=body_radius,
		fill = pattern_uri,
		stroke=svgwrite.rgb(*darker(color)),
		stroke_width=outline_width
		))

def draw_legs(dwg, skin_color):
	# Draw left leg (rectangle with rounded corners)
	leg_width =  random.uniform(0.3,0.5)
	separation = random.uniform(leg_width,0.75) * base
	leg_width = leg_width * base
	left_leg_top_left =  (x0 - separation, y0 + 1.2 * base)
	right_leg_top_left = (x0 + separation - leg_width, y0 + 1.2 * base)

	size=(leg_width, 0.85 * leg_width)

	leg_radius = random.uniform(0.05,0.2)*base

	# Draw left leg
	dwg.add(dwg.rect(
		insert=left_leg_top_left,
		size= size,
		rx=leg_radius,
		ry=leg_radius,
		fill=svgwrite.rgb(*skin_color),
		stroke=svgwrite.rgb(*darker(skin_color)),
		stroke_width=outline_width
		))

	# Draw right leg
	dwg.add(dwg.rect(
		insert=right_leg_top_left,
		size=size,
		rx=leg_radius,
		ry=leg_radius,
		fill=svgwrite.rgb(*skin_color),
		stroke=svgwrite.rgb(*darker(skin_color)),
		stroke_width=outline_width
		))

def draw_cape(dwg, color):

	#draw_hoodie(dwg, color)

	# Get a darker color for the cape
	cape_color = darker(color)

	cape_hight =  int(random.uniform(0,head_radius*2 ) )
	cape_width = int(random.uniform(0,cape_hight) )

	# Define the cape shape (rounded triangle)
	cape_points = [	(x0, y0),
					(x0-cape_width, y0+cape_hight),
					(x0+cape_width, y0+cape_hight)]

	# Draw the cape
	dwg.add(dwg.polygon(
		points=cape_points,
		fill=svgwrite.rgb(*cape_color),
		stroke=svgwrite.rgb(*color),
		stroke_width=outline_width
		))

def draw_belt(dwg, belt_color, buckle_color):
	belt_color = darker(belt_color)

	# Define the belt position
	belt_top_left = (	x0 - 0.51*base,
						y0 + 0.85*base	)
	belt_bottom_right = (	x0 + 0.51*base,
							y0 + 0.95*base	)

	# Draw the belt (horizontal line)
	dwg.add(dwg.rect(
		insert=belt_top_left,
		size=(belt_bottom_right[0] - belt_top_left[0], belt_bottom_right[1] - belt_top_left[1]),
		fill=svgwrite.rgb(*belt_color),
		stroke=svgwrite.rgb(*darker(belt_color)),
		stroke_width=outline_width // 2
		))

	# Define the buckle position and randomize the curvature of the corners
	buckle_top_left = (	x0 - 0.10*base,
						y0 + 0.80*base	)

	buckle_bottom_right = (	x0 + 0.10*base,
							y0 + 1.00*base	)
	buckle_radius = random.randint(0, 15) * base // 100

	# Draw the buckle (rectangle with random corner curvature)
	dwg.add(dwg.rect(
		insert=buckle_top_left,
		size=(buckle_bottom_right[0] - buckle_top_left[0], buckle_bottom_right[1] - buckle_top_left[1]),
		rx=buckle_radius,
		ry=buckle_radius,
		fill=svgwrite.rgb(*buckle_color),
		stroke=svgwrite.rgb(*lighter(buckle_color)),
		stroke_width=outline_width // 2
		))

def draw_head(dwg, skin_color, race="Human"):
	# Halo for aasimar
	if "aasimar" in race:
		halo_radius = head_radius + 10
		halo_color = svgwrite.rgb(255, 255, 153)
		dwg.add(dwg.circle(
			center=(head_center[0], head_center[1] - head_radius - 10),
			r=halo_radius,
			fill="none",
			stroke=halo_color,
			stroke_width=10
		))

	# Draw head (circle)
	head = dwg.circle(
		center=head_center,
		r=head_radius,
		fill=svgwrite.rgb(*skin_color),
		stroke=svgwrite.rgb(*darker(skin_color)),
		stroke_width=outline_width
		)
	dwg.add(head)

	race = race.lower()

	if "elf" in race or "orc" in race or "goblin" in race:
		ear_length = 100
		ear_offset_y = 40
		ear_color = svgwrite.rgb(*skin_color)

		# Left ear
		dwg.add(dwg.polygon(
			points=[
				(head_center[0] - head_radius, head_center[1]),  # base
				(head_center[0] - head_radius - ear_length, head_center[1] - ear_offset_y),
				(head_center[0] - head_radius, head_center[1] - ear_offset_y)
			],
			fill=ear_color,
			stroke=svgwrite.rgb(*darker(skin_color)),
			stroke_width=outline_width
		))
		# Right ear
		dwg.add(dwg.polygon(
			points=[
				(head_center[0] + head_radius, head_center[1]),
				(head_center[0] + head_radius + ear_length, head_center[1] - ear_offset_y),
				(head_center[0] + head_radius, head_center[1] - ear_offset_y)
			],
			fill=ear_color,
			stroke=svgwrite.rgb(*darker(skin_color)),
			stroke_width=outline_width
		))
	# Horns for tieflings and orcs
	if "tiefling" in race or "orc" in race:
		horn_size = 15
		horn_color = svgwrite.rgb(50, 0, 0)
		top_x = head_center[0]
		top_y = head_center[1] - head_radius

		dwg.add(dwg.path(
			d=f"M {top_x-60},{top_y+20} "
				f"C {top_x- 100},{top_y }, {top_x- 120},{top_y - 60}, {top_x- 80},{top_y - 80}",
			fill="none",
			stroke=horn_color,
			stroke_width=outline_width
		))
		dwg.add(dwg.path(
			d=f"M {top_x+60},{top_y+20} "
				f"C {top_x+ 100},{top_y }, {top_x+ 120},{top_y - 60}, {top_x+ 80},{top_y - 80}",
			fill="none",
			stroke=horn_color,
			stroke_width=outline_width
		))

def draw_hoodie(dwg, hoodie_color):

	# Draw the hood (large circle behind the head)
	head_center = (2.00*base, 1.00*base)
	hood_radius = int(head_radius + (random.randint(-10, 20))*base//100)
	hood_box = [head_center[0] - hood_radius,
				head_center[1] - hood_radius,
				head_center[0] + hood_radius,
				head_center[1] + hood_radius]
	dwg.add(dwg.circle(
		center=head_center,
		r=hood_radius,
		fill=svgwrite.rgb(*hoodie_color),
		stroke=svgwrite.rgb(*darker(hoodie_color)),
		stroke_width=outline_width
		))

def draw_crown(dwg, crown_color, jewel_color):
	crown_base_top_left = ( 	x0 - 0.8 * head_radius ,
								y0 - 0.65 * head_radius)
	crown_base_bottom_right = ( x0 + 0.8 * head_radius,
								y0 - 0.60 * head_radius)
	crown_width = crown_base_bottom_right[0] - crown_base_top_left[0]

	dwg.add(dwg.rect(
		insert=crown_base_top_left,
		size=(crown_width, 15),
		fill=svgwrite.rgb(*crown_color),
		stroke=svgwrite.rgb(*darker(crown_color)),
		stroke_width=outline_width // 3
	))

	num_jewels = random.randint(1, 4)
	jewel_width = crown_width // (num_jewels)
	jewel_sides = random.randint(4, 6)  # Randomly choose number of sides for all jewels
	jewel_radius = 0.05 * base

	center_y = crown_base_top_left[1] + random.randint(0, int(crown_base_bottom_right[1] - crown_base_top_left[1]) // 2 )

	for i in range(num_jewels):
		center_x = crown_base_top_left[0] + (i + 1) * jewel_width - jewel_width // 2

		jewel_vertices = [
			(
				center_x + jewel_radius * np.cos(2 * np.pi * j / jewel_sides),
				center_y + jewel_radius * np.sin(2 * np.pi * j / jewel_sides)
			)
			for j in range(jewel_sides)
		]

		dwg.add(dwg.polygon(
			points=jewel_vertices,
			fill=svgwrite.rgb(*jewel_color),
			stroke=svgwrite.rgb(*lighter(jewel_color)),
			stroke_width=outline_width // 3
		))

def draw_hair(dwg, hair_color):
	# Center and radius for the hair (same as the head)
	hair_center = head_center[0], head_center[1]
	hair_radius = head_radius * 1.15

	angle = 2 * np.pi *  (random.randint(10, 270)) / 360

	# Calculate start and end angles based on the specified angle
	start_angle = -angle / 2 + np.pi/2 # Start angle in radians
	end_angle = angle / 2  + np.pi/2   # End angle in radians

	# Create a path for the hair shape
	path_data = []
	steps = 100  # Number of points to create the arc

	# Move to the center
	path_data.append(f'M {hair_center[0]},{hair_center[1]-random.uniform(0.1,0.5)*hair_radius}')

	# Draw line to the starting point of the arc
	start_x = hair_center[0] + hair_radius * np.cos(start_angle)
	start_y = hair_center[1] - hair_radius * np.sin(start_angle)
	path_data.append(f'L {start_x},{start_y}')

	hair_radius0 = hair_radius

	# Create the arc
	for i in range(steps + 1):
		hair_radius = (hair_radius0 + hair_radius0 * random.randint(-5, 5) / 100)
		angle = start_angle + (end_angle - start_angle) * (i / steps)
		x = hair_center[0] + hair_radius * np.cos(angle)
		y = hair_center[1] - hair_radius * np.sin(angle)
		path_data.append(f'L {x},{y}')

	# Close the path to form a "pizza slice"
	path_data.append('Z')

	dwg.add(dwg.path(
		d=" ".join(path_data),
		fill=svgwrite.rgb(*hair_color),
		stroke=svgwrite.rgb(*darker(hair_color)),
		stroke_width=outline_width//2
	))

def draw_axe(dwg, group, position, size, right = True):
	handle_width = 0.1 * base
	handle_height = 1.2 * base
	blade_width = random.uniform(0.2,0.9) * base
	blade_height = random.uniform(0.1,0.9) * base
	blade_curve_radius = random.uniform(-0.2,2) * base

	side = "right" if right else "left"

	blade_color = Blade_Color()
	handle_color = Handle_Color()

	# Create a group for the axe with an identifiable ID
	axe_group = svgwrite.container.Group(id='axeGroup')

	gradient_fill = create_gradient(dwg, f'axeGradient{side}', blade_color, Blade_Color(), blade_color)

	# Draw handle
	handle_top_left = (position[0] - handle_width / 2, position[1] - handle_height /2 )
	handle_bottom_right = (position[0] + handle_width / 2, position[1] + handle_height /2)

	handle_rect = svgwrite.shapes.Rect(
		insert=handle_top_left,
		size=(handle_width, handle_height),
		fill=svgwrite.rgb(*handle_color),
		stroke=svgwrite.rgb(*darker(handle_color)),
		stroke_width=outline_width
		)

	# Define the blade shape with curves
	blade_top_left = (position[0] - blade_width / 2, position[1] - handle_height*(1/3) )
	blade_top_right = (position[0] + blade_width / 2, position[1] - handle_height*(1/3) )
	blade_bottom_left = (position[0] - blade_width / 2, position[1] - handle_height *(1/3)  - blade_height)
	blade_bottom_right = (position[0] + blade_width / 2, position[1] - handle_height *(1/3)  - blade_height)
	blade_center_top = (position[0], blade_top_left[1] )
	blade_center_bottom = (position[0], blade_bottom_left[1])

	blade_path = (
		f"M {blade_top_left[0]} {blade_top_left[1]} "
		f"A {blade_curve_radius} {blade_curve_radius*2} 0 0 1 {blade_center_top[0]} {blade_center_top[1]} "
		f"A {blade_curve_radius} {blade_curve_radius*2} 0 0 1 {blade_top_right[0]} {blade_top_right[1]} "
		f"A {blade_curve_radius} {blade_curve_radius} 0 0 0 {blade_bottom_right[0]} {blade_bottom_right[1]} "
		f"A {blade_curve_radius} {blade_curve_radius*2} 0 0 1 {blade_center_bottom[0]} {blade_center_bottom[1]} "
		f"A {blade_curve_radius} {blade_curve_radius*2} 0 0 1 {blade_bottom_left[0]} {blade_bottom_left[1]} "
		f"A {blade_curve_radius} {blade_curve_radius} 0 0 0 {blade_top_left[0]} {blade_top_left[1]} "
		"Z"
		)

	blade = svgwrite.path.Path(
		d=blade_path,
		fill=gradient_fill,
		stroke=svgwrite.rgb(*darker(blade_color)),
		stroke_width=outline_width,
		)

	axe_group.add(handle_rect)
	axe_group.add(blade)
	# Add the axe group to the main group
	group.add(axe_group)

def draw_sword(dwg, group, position, size, right = True):

	guard_size = base * random.uniform(0.25,0.55)  # Size of the cross guard arms
	x_radius = random.uniform(0,guard_size)
	y_radius = random.uniform(0,guard_size)
	blade_width = base * random.uniform(0.05,0.15)
	blade_height = base * random.uniform(0.5,1.75)
	side = "right" if right else "left"
	blade_color = Blade_Color()
	handle_color = Handle_Color()
	# Create gradient fill for the blade with 90-degree rotation
	gradient_fill = create_gradient(dwg, f'swordGradient{side}', Blade_Color(), blade_color, blade_color, direction=90)
	# Draw cross guard
	guard_top_left = (	position[0] - guard_size / 2,
						position[1] - guard_size / 2)
	guard_bottom_right = (position[0] + guard_size / 2, position[1] + guard_size / 2)
	guard_rect = svgwrite.shapes.Rect(
		insert=guard_top_left,
		rx=x_radius,
		ry=y_radius,
		size=(guard_size,guard_size),
		fill=svgwrite.rgb(*handle_color),
		stroke=svgwrite.rgb(*darker(handle_color)),
		stroke_width=outline_width
	)
	group.add(guard_rect)

	# Draw blade
	blade_points = [
		(position[0] - blade_width / 2, position[1]),
		(position[0] + blade_width / 2, position[1]),
		(position[0] + blade_width / 2, position[1] - blade_height),
		(position[0], position[1] - blade_height * 1.1),
		(position[0] - blade_width / 2, position[1] - blade_height),

	]
	blade_polygon = svgwrite.shapes.Polygon(
		points=blade_points,
		fill=gradient_fill,
		stroke=svgwrite.rgb(*darker(blade_color)),
		stroke_width=outline_width//2
	)
	group.add(blade_polygon)

def draw_shield(dwg,group, position, size):
	x, y = position
	proportion = size / 3  # Ensure size is a single value (not a tuple)
	high = random.uniform(proportion, size)
	width = random.uniform(proportion, size)
	x += proportion

	stroke_color = Blade_Color()
	fill_color = Handle_Color()

	gradient_fill = create_gradient(dwg, 'shieldGradient', fill_color, lighter(fill_color,0.7), fill_color, direction=0)

	# Define control points based on the size and position
	control_points = [
		(x - width,  y),                        # Start point (top left)
		(x + width,  y),                        # Top right
		(x + width,  y + high),            # Top right corner
		(x + width,  y + high),   # Control point for top right curve
		(x + width,  y + high),   # Control point for top right curve
		(x + 1,  		 y + high * 2),        # Bottom right corner
		(x - 1,  		 y + high * 2),        # Bottom left corner
		(x - width,  y + high),   # Control point for bottom left curve
		(x - width,  y + high),   # Control point for bottom left curve
		(x - width,  y + high)             # Top left corner
	]

	path_commands = []
	path_commands.append(f"M {control_points[0][0]} {control_points[0][1]}")  # Move to start point
	path_commands.append(f"L {control_points[1][0]} {control_points[1][1]}")  # Line to top right
	path_commands.append(f"L {control_points[2][0]} {control_points[2][1]}")  # Line to top right corner
	path_commands.append(f"C {control_points[3][0]} {control_points[3][1]}, "
						 f"{control_points[4][0]} {control_points[4][1]}, "
						 f"{control_points[5][0]} {control_points[5][1]}")    # Cubic Bézier curve to bottom right corner
	path_commands.append(f"L {control_points[6][0]} {control_points[6][1]}")  # Line to bottom left corner
	path_commands.append(f"C {control_points[7][0]} {control_points[7][1]}, "
						 f"{control_points[8][0]} {control_points[8][1]}, "
						 f"{control_points[9][0]} {control_points[9][1]}")    # Cubic Bézier curve to top left corner
	path_commands.append(f"L {control_points[0][0]} {control_points[0][1]}")  # Line to close path
	path_commands.append(f"Z")  # Line to close path

	# Joining all commands into a single path string
	path_string = " ".join(path_commands)

	# Create a Path object
	shape = svgwrite.path.Path(d=path_string,
		fill=gradient_fill,
		stroke=svgwrite.rgb(*stroke_color),
		stroke_width=outline_width)

	# Create a new group for rotation
	shield_group = svgwrite.container.Group(transform=f"rotate(-90, {x}, {y})")

	# Add the Path object to the group
	shield_group.add(shape)

	unicode_char= random.choice("§§ƱϘϗψϕΞΣΧΨθϞϕϑ★☆☪☥☪☼☽☾♍♎♇♃☿♀♁♂♃♄♅♆♇♈♉♊♋♌♍♎♏♐♑♒♓♔⛤⛥⛦⛧⛫❀⭐⭑Ⱞⱞⴚⴜⵥ𐀏𐀚𐀣𐀲𐀶𐁀𐁄𐁊𐁑𐁔𐁙𐂃𐂄𐂅𐂎𐂥𐂡𐂢𐂲𐂴𐂵𐃆𐃈𐃋𐃏𐃞𐃘𐃡𐃢𐃣𐃤𐃥𐃦𐃧𐃨𐃩𐃫𐃯𐃰𐆖𐆔𐆒𐆓𐆗𐆙𐋃𐋐𐏕𐘃𐘨𐙈𐙡𐙢𐙣𐙤𐙥𐙧𐙦𐙩𐙪𐙫𐙾𐙿𐙹𐙴𐙲𐙱𐚀𐚄𐚅𐚕𐚪𐚫𐚬𐚭𐚮𐚿𐚰𐛞𐛗𐛢𐛭𐜝𐜢𐠃𐠄𐠅𐠠𐠐𐠲𐡠𐤷𐦀𐦝𐦞𐦟𐦃𐦐𐩢𐩣𐩦𐩻𐩸𐩰𐩯𐪎𐪏𐫱𐮛𐮜𐮚𐮙𐰡𐰑𐰒𐰋𐰌𐰍𐰎𐰧𐰵𐱁𐱃𐲃𑁍𑁣𑁢𑀣𑄇𑄟𑄣𑆑𑆇𑌲𑖂𑖌𑖍𑖜𑗁𑗆𑗊𑗌𑗋𑗍𑗎𑗕𑗐𑗗𑗖𑗘𑗙𑗚𑜙𑜎𑜍𑜏𑿒𑿯𒀭ϠϡϢϣϰӁҰԅ֍֎۝۞߷ߡ࠶ࢡࢧࢼऄऐकஐந௹೫༐༄༅༆࿓࿔ᐁ᐀ᐂᐃᐄᐐᐑᗒᗐᗑᗓᗔᗧᗣᗪ ᚁᚂᚃᚄᚅᚆᚇᚖᚇᚈᚉᚊᚋᚌᚍᚎᚏᚐᚑᚒᚓᚔᚕᚖᚗᚘᚙᚚ᚛᚜ᚠᚡᚢᚣᚤᚥᚦᚧᚨᚩᚪᚫᚬᚭᚮᚯᚰᚱᚲᚳᚴᚵᚶᚷᚸᚹᚺᚻᚼᚽᚾᚿᛏᛎᛍᛌᛋᛊᛉᛈᛇᛆᛅᛄᛃᛂᛁᛀᛐᛑᛒᛓᛔᛕᛖᛗᛘᛙᛚᛛᛜᛝᛞᛟᛯᛮ᛭᛬᛫ᛪᛩᛨᛧᛦᛥᛤᛣᛢᛡᛠᛰᜁᜢᝌᝎᝏᝢᝣᝤᝪឃញនបយរលហឡអឦឧឫឬឭ។៕៖៙៚៛ៜ០១៣᠀᠂᠃᠄᠅ᣀᣁᣫᤀᤂᤁᤃᤅᤎᤐᤑᤕᤗᤘᤜᤞ᥀᥄᥅᥆᥇᥈᥉᥊᥋᥌᥍᥎᥏ᥖᥕᥗᨀᨁᨂᨃᨄᨅᨆᨇᨈᨉᨊᨋᨌᨍᨎᨎᨏ᨟᨞ᨖᨕᨔᨓᨒᨑᨐᨫ᪠᪤᪥ᮃᮎᯣᯙᯤᯥ᯼᯽᯾ᰄᰇᰉᰊᰋᰌᰍᰎᰟᰞᰝᰜᰛᰙᰔᰓᰣᱵ᳀᳁᳂ᳲᳳᳵ†‡⁐⁂⁕⁘⁙⁚⁛⁜⁝⁞Ω℧℣ℤ℥ℰℱ⅌⌀⌁⌂⌅⌆⌇⌑⌒⌓⌔⌖⌘⌛⌱⌲⌵⌶⌺⌻⌼⌽⌾⍉⍊⍋⍟⍚⍙⍣⍦⍺⍹⍶⍵⍴⎔⎖⏣⏾⏼⏻⏳⑂⑃▀▁▂▃▄▅▆▇▢■□▣▲◐◑◒◓◉◈◎☀☁☄★☆☉☓☘☙☝☜☞☟☠☠☠☠☠☠☣☢☤☥☥☥☥☦☧☨☩☪☫☬☭☭☮☯☸☼☽☾☿♀♁♂♃♄♅♆♇♈♉♊♋♌♍♎♏♐♑♒♓♔♕♖♗♘♙♚♛♜♝♞♟♠♡♢♣♤♥♦♧♨♮♰♱♾⚀⚆⚇☰☱☲☳☴☵☶☷⚊⚋⚌⚍⚎⚏⚒⚓⚔⚕⚖⚗⚘⚙⚚⚛⚜⚝⚡⚬⚭⚰⚱⚲⚳⚴⚵⚶⚷⚸⚹⚺⚻⛈⛌⛎⛏⛓⛚⛛⛢⛤⛥⛦⛧⛨⛩⛫⛪⛬⛭⛮⛯⛰⛲⛺⛻⛼✙✚✛✝✞✟✠✡✢✣✤✥✦✧✩✪✫✬✭✮✯✱✲✳✴✵✶✷✸✹✺✻✼✽✾✿❀❁❂❃❄❅❆❇❈❉❊❋❖❡❤❥❦❧➳➴➵➶➷➸➹⟁⟃⟄⟐⟠⟡⦶⧊⨁⨀⨂⭐⭑⭒Ɱ𝜋𝜑𝜃𝜗𝑈𝑉𝑊𝑘𝄡𝄢𐡷𐡸⚜️⚜⚜︎𓀡𓀠𓀿𓀾𓁀𓁜𓁝𓁛𓁢𓁭𓁮𓁿𓁾𓁽𓁼𓁻𓁺𓁹𓁷𓁶𓁲𓂀𓂃𓂅𓂍𓂞𓂟𓂝𓂜𓂘𓂗𓂖𓂓𓂑𓂒𓂡𓂢𓂣𓂩𓂬𓂿𓂾𓂻𓃀𓃁𓃆𓃇𓃉𓃊𓃋𓃌𓃍𓃎𓃏𓃐𓃑𓃒𓃓𓃗𓃠𓃢𓃣𓃤𓃥𓃦𓃬𓃭𓃮𓃯𓃰𓃱𓃹𓃷𓃺𓃻𓃾𓄀𓄂𓄃𓄄𓄆𓄇𓄉𓄊𓄋𓄌𓄍𓄒𓄙𓄚𓄠𓄩𓄬𓄯𓄰𓄱𓄲𓄳𓄴𓄵𓄶𓄷𓄸𓄹𓄺𓄻𓄼𓄽𓄿𓅀𓅂𓅃𓅄𓅅𓅇𓅊𓅌𓅐𓅑𓅒𓅓𓅔𓅖𓅕𓅗𓅘𓅙𓅚𓅛𓅞𓅟𓅠𓅢𓅣𓅥𓅧𓅨𓅩𓅪𓅫𓅬𓅭𓅮𓅯𓅰𓅱𓅲𓅳𓅴𓅺𓅻𓅼𓆏𓆏𓆍𓆌𓆋𓆊𓆉𓆈𓆃𓆂𓆁𓆀𓆐𓆑𓆓𓆕𓆖𓆗𓆘𓆙𓆚𓇢𓇡𓇬𓇾𓇽𓇼𓈊𓈉𓇺𓇹𓇳𓈌𓉑𓉱𓉳𓉶𓉷𓊗𓊝𓊤𓊠𓊱𓋊𓋉𓋈𓋇𓋐𓋪𓋹𓌏𓌕𓌖𓌖𓌜𓌛𓌨𓌣𓌢𓌳𓌴𓌵𓍌𓍊𓍑𓍕𓍝𓍩𓍨𓍧𓍦𓍥𓍤𓍣𓍢𓍰𓍱𓍲𓍳𓍴𓍵𓎏𓎆𓎇𓎂𓎖𓎫𓎱𓎲𓏒𓏴𓏲𓐀𓐂𓐭𓐬𓐩𖠀𖠁𖠂𖠃𖠄𖠅𖠆𖠇𖠈𖠉𖠊𖠋𖠞𖠝𖠛𖠙𖠕𖠔𖠪𖠭𖠮𖠯𖠿𖠾𖠻𖠹𖠷𖠳𖠲𖠰𖡃𖡄𖡆𖡌𖡍𖡟𖡜𖡛𖡗𖡒𖡢𖡣𖡦𖡨𖡩𖡪𖡭𖡿𖡽𖡼𖡻𖡺𖡹𖡷𖡶𖡰𖢄𖢆𖢌𖢏𖢞𖢙𖢗𖢖𖢐𖢢𖢣𖢥𖢨𖢪𖢬𖢭𖢾𖢻𖢺𖢹𖢲𖣀𖣊𖣎𖣙𖣔𖣓𖣐𖣠𖣢𖣨𖣬𖣴𖣲𖣰𖤀𖤁𖤂𖤄𖤈𖤉𖤍𖤟𖤝𖤜𖤓𖤑𖤐𖤣𖤲𖥂𖥉𖥍𖥎𖥟𖥞𖥜𖥘𖥗𖥕𖥔𖥒𖥐𖥠𖥡𖥣𖥤𖥧𖥸𖥷𖥳𖥲𖥱𖦁𖦞𖦝𖦜𖦙𖦖𖦺𖦹𖦸𖦷𖧈𖧟𖧞𖧓𖧑𖧐𖧡𖧦𖧧𖧾𖧻𖧷𖧵𖨠𖨢𖨦𖨫𖨭𖨲𖨳𖩏𝄐𝄑𝄢𝄪𝄞𝌀𝌁𝌂𝌃𝌄𝌅𝌆𝌇𝌈𝌉𝌊𝌋𝌌𝌍𝌎𝌏𝌐𝌑𝌒𝌓𝌔𝌕𝌖𝌗𝌘𝌙𝌚𝌛𝌜𝌝𝌞𝌟𝌯𝌮𝌭𝌬𝌫𝌪𝌩𝌨𝌧𝌦𝌥𝌤𝌣𝌢𝌡𝌠𝌰𝌱𝌲𝌳𝌴𝌵𝌶𝌷𝌸𝌹𝌺𝌻𝌼𝌽𝌾𝌿𝍏𝍎𝍍𝍌𝍋𝍊𝍉𝍈𝍇𝍆𝍅𝍄𝍃𝍂𝍁𝍀𝍐𝍑𝍒𝍓𝍔𝍕𝍖𝛹𝛸𝛷𝛴𝛳𝛱𝜁𝛥𝛗𝛙𝛚𝛡𝛀𝛺𝛻𝜛𝜙𝜘𝜗𝜕𝜔𞢆🌑🌒🌓🌔🌕🌖🌗🌘🐇🐈🐉🐊🐍🐟🐘🐙🐗🐕🐪🐬🐿🐺🐲🐲🐲🐺🐺🐴👁👁👹💎💀💀💀💀💧💢💠🔰🔱🔶🔷🔸🔹🔴🔵🕰🖤💙💚💜💛🗝🗡🛡🛠🜁🜂🜃🜄🜅🜆🜇🜈🜉🜊🜋🜌🜍🜎🜏🜐🜑🜒🜓🜔🜕🜖🜗🜘🜙🜚🜛🜜🜝🜞🜟🜯🜮🜭🜬🜫🜪🜩🜨🜧🜦🜥🜤🜣🜢🜡🜠🜰🜱🜲🜳🜴🜵🜶🜷🜸🜹🜺🜻🜼🜽🜾🜿🝏🝎🝍🝌🝋🝊🝉🝈🝇🝆🝅🝄🝃🝂🝁🝀🝐🝑🝒🝓🝔🝕🝖🝗🝘🝞🝟🝡🝢🝣🝤🝧🝩🝪🝮🝯🝰🝲🝳🟠🟡🟢🟣🟤🟥🟦🟧🟨🟩🟪🟫🟰🤍🤎🥀🦀🦁🦂🦄🦅🦆🦇🦈🦉🦊🦋🦌🦍🦎🦏🦞🦚🦖🦑🦢🦩🦴🧄🧭🩵🩶🩸🪓🪬🪬🪬🪞🪲🪷🪽🫎𓆣𓆼𓆽𓇇𓇈𓇉𓇊𓇚𓇙𓇗𓇖𓇕𓇓𓇒𓇑𓅿☘️☘☘︎🪷࿆🏵𑁍❁❀✿⚡⚝⛦⛥⛤✪𖤐⛧★✭✰✮✯✬✫✩⭒⭐︎☆⭑✡✶⚖𓍝𐁄⚔𖣓🕸⚙︎⚙☯☯︎☮࿊࿋࿌☣𖦲۩𐦝𓂀☠🜏⧝𖣨𐮛🜹᯽𖧷𓇬𖧵⌘𖣘𖦷✠🜊🜋🜌☩𖣴𞢈𐫰𑇍𖣊⌖𖥠𖥟𖥤♱♰𐦞☥𓋹⚚⚕☤𖤍⚒☭𓆃⚰𓊿𐃯𐃏𐀚𓆈𓆉𓆊𓆌𓆓𓆗𓆘𓆙𓆚𐦐𓄇𓄂𓃬𓃭𓃮𓃠𓃒𓃓𓄀𓃽𐦃𓃵𓄄𓄃𓃻𓃗𓃹𓃺𓃟𓃥𓃦𓄁𓃱𓃰𐦖𐦉𓆂𓅿𓅩𓅪𓅫𓅬𓅨𓅠𓅟𓅞𓅛𓅚𓅔𓅓𓅐𓅊𓅃𓅂𓄿𓆦𓆧𓆣𓁳𓁴𓁢𓁣𓁐𓀿𓀾𓀏𓀗𓀆𓀂𐦂𐦀𓋖𓋔𓆛𓆜𓆝𓆞𓆟𓆡𓇗⚔️⚒️🪲🕷️🗡️⚓️🦇💀🔮🌬️🌧️🌤️🌥️🌩️꧞☁️ϗϏϰ⛫⛩⛈🝪🝫🝩🝧🝳🝲🝮🝬🝤🝢🝗🝑🝋🝈🝁🜾🜱🜳🜒🜎🜇𝛟𝛡𝛚𝛙𝛘𝛗𝛍𝛃𝛂𝚿𝛀Ʊ𖤛𖤎𖤌𖤄𖤉𖥗𖥔𖥘𖥚𖥱𖥯𖥹𖧐𖧑𖦜𖧟𖧦𖧻𖧾𖨆𖨠𖨡𖨟𖨢𖫪𖫡𖭷𖮆𖣰𖣸𖣽⚳⚴⚵⚶⚷𖧶⚸♆♅♄♃♁☿🜻🜯🜮🜭🜬🜫🜪🜩🜧🜦🜥🜤🜣🜢🜡🜟🜞𐃩𐃨𐃣𐃶𐆚𓉳🪦🏹👁️🛡️🐘𖤞𖤝𝒜𝐀𝐃𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐖𝐗𝐘𝐙𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𞢾𞢗𞣄🐮🐃🦚🦢🐇𓅜𓅙☠️⚓︎Ħ𝟊꧁꧂꥟✊🏾✋🏼⚖️⨇⨈⩕⩖⩓⩔⌛⏳⌛️⏿⌛︎𞢩꩸ꪝ🩸💧🌧🌩🌨🌦🌥🌤🌑🌒🌓🌔🌕🌖🌗🌘🌙🌚🌛🌜☽☾🌝⏾☪🔥🜚🌞☉❂☀☀︎☀️🔆🔅☼𖤓✵✷✸✹✺❇✳✴︎✴𝛬𝜆𝝀🔱༊དᙡᙏᙎᙢᙓᙣᙦᙩᙫᙪ𖣔𖣲ᚕᚖ𑗊𑗋𑗌𑗍𑗎𑗖𑗗𑜏𑜒𑜀𑜌𑜍𑜙𑣯𝒵𝒴𝒳𝒲𝒱𝒰𝒮𝒯𝒬🏵️𞠀𞋏𞋎𞡯𞡚𞠻𞡛𞡜𞢆𞡯𞢘⚕︎⚖︎☸︎⚔︎🪽")
	text = svgwrite.text.Text(unicode_char,
							  insert=(x - width / 2, y + (high*0.75) ),
							  font_size= 5+min(width,high),
							  fill=svgwrite.rgb(*stroke_color))
	shield_group.add(text)
	group.add(shield_group)

def draw_arms(dwg, skin_color):
	arm_radius = int(0.20 * base)

	arm_length = random.uniform(0.25 * base, 0.50 * base)

	left_arm_center = (
		x0 - (2 * arm_length) + int(base * random.uniform(-0.4, 0.10)),
		y0 + base + int(base * random.uniform(-0.4, 0.10))
		)

	right_arm_center = (
		x0 + (2 * arm_length) + int(base * random.uniform(-0.1, 0.175)),
		y0 + base // 2 + int(base * random.uniform(-0.1, 0.20))
		)

	left_weapon_angle = random.uniform(-90, -45)
	right_weapon_angle = random.uniform(45, 90)

	left_arm_and_weapon_group = dwg.g(
		id="left_arm_and_weapon",
		transform=f"rotate({left_weapon_angle}, {left_arm_center[0]}, {left_arm_center[1]})"
		)

	right_arm_and_weapon_group = dwg.g(
		id="right_arm_and_weapon",
		transform=f"rotate({right_weapon_angle}, {right_arm_center[0]}, {right_arm_center[1]})"
		)

	# Draw left arm and add animation
	left_arm_rect = svgwrite.shapes.Rect(
		insert=left_arm_center,
		size=(arm_length, arm_length),
		rx=arm_radius,
		ry=arm_radius,
		fill=svgwrite.rgb(*skin_color),
		stroke=svgwrite.rgb(*darker(skin_color)),
		stroke_width=outline_width
		)
	left_arm_and_weapon_group.add(left_arm_rect)

	# Draw right arm and add animation
	right_arm_rect = svgwrite.shapes.Rect(
		insert=right_arm_center,
		size=(arm_length, arm_length),
		rx=arm_radius,
		ry=arm_radius,
		fill=svgwrite.rgb(*skin_color),
		stroke=svgwrite.rgb(*darker(skin_color)),
		stroke_width=outline_width
		)
	right_arm_and_weapon_group.add(right_arm_rect)

	# Add weapons to arms
	draw_weapon(dwg, right_arm_and_weapon_group, right_arm_center, right = True)
	draw_weapon(dwg, left_arm_and_weapon_group, left_arm_center, right = False)

	# Add arms to the SVG drawing
	dwg.add(left_arm_and_weapon_group)
	dwg.add(right_arm_and_weapon_group)

def draw_weapon(dwg, group, position, right = True):
	if not right: # My right and their right is reversed
		weapons = ["axe", "sword"]
	else:
		weapons = ["axe", "sword", "shield"]
	weapon = random.choice(weapons)

	if weapon == "axe":
		draw_axe(dwg,group,
				 position,
				 (head_radius, head_radius),
				 right
				 )
	elif weapon == "sword":
		draw_sword(dwg, group,
			   position,
			   (head_radius, head_radius),
			   right
			   )
	elif weapon == "shield":

		draw_shield(dwg,group,
			position, head_radius)

def draw_chibi():
	# Create a svg dwg with no background
	dwg = svgwrite.Drawing('chibi_dwg.svg', profile='full', size=(2*x0, 3*y0))
	race =  random.choice(["Human", "Goblin", "Dwarf", "Elf", "Orc", "Tiefling",
		"Dragonborn", "Aasimar"])
	skin_color = Skin_Color(race)
	draw_cape(dwg, Color())
	draw_body(dwg, Color())
	draw_legs(dwg, Color())
	draw_belt(dwg, Color(), Color())
	draw_head(dwg, skin_color, race)
	draw_hair(dwg, Hair_Color())
	draw_crown(dwg, Color(), Color())
	draw_eyes(dwg, Color(), skin_color)
	draw_arms(dwg, skin_color)


	return dwg

# Example usage
chibi_dwg = draw_chibi()
chibi_dwg.save("chibi_dwg.svg")
print("Chibi image created and saved as chibi_dwg.svg")
