
from AtlasOfMapmaking.Astrolabe_of_Grids import 	create_grid
from AtlasOfMapmaking.Kit_of_WaveFunctionCollapse import wave_function_collapse
from AtlasOfMapmaking.Kit_of_ScalableVectorGraphics import grid_to_svg, save_svg
from AtlasOfMapmaking.Compass_of_MapConfiguration import MapConfig

import app.random as random

# Main Execution
def main():
	# Create a sample triangular grid
	grid = create_grid(
		MapConfig.GRID_HEIGHT,
		MapConfig.GRID_WIDTH,
		size=MapConfig.BASE,
		shape="triangular")
	# Convert the grid to SVG
	wave_function_collapse(grid)
	svg_map = grid_to_svg(grid)

	# Save the SVG to a file or print it
	save_svg(svg_map, "new_map_3.svg")

	# Create a sample hex grid
	grid = create_grid(
		MapConfig.GRID_HEIGHT,
		MapConfig.GRID_WIDTH,
		size=MapConfig.BASE,
		shape="hexagonal")
	# Convert the grid to SVG
	wave_function_collapse(grid)
	svg_map = grid_to_svg(grid)

	# Save the SVG to a file or print it
	save_svg(svg_map, "new_map_6.svg")

	# Create a sample triangular grid
	grid = create_grid(
		MapConfig.GRID_HEIGHT,
		MapConfig.GRID_WIDTH,
		size=MapConfig.BASE,
		shape="octagonal")
	# Convert the grid to SVG
	wave_function_collapse(grid)
	svg_map = grid_to_svg(grid)

	# Save the SVG to a file or print it
	save_svg(svg_map, "new_map_8.svg")

	# Create a sample triangular grid
	grid = create_grid(
		MapConfig.GRID_HEIGHT,
		MapConfig.GRID_WIDTH,
		size=MapConfig.BASE,
		shape=0)
	# Convert the grid to SVG
	wave_function_collapse(grid)
	svg_map = grid_to_svg(grid)

	# Save the SVG to a file or print it
	save_svg(svg_map, "new_map_0.svg")

if __name__ == "__main__":
	main()
