import app.random as random
from collections import deque
from random import randint


# Done
def initialize_ranges(grid, min_val, max_val):
	"""
	Initialize the ranges for each cell in the grid.
	"""
	ranges = {cell: list(range(min_val, max_val + 1)) for cell in grid.cells.values()}
	return ranges

# Done
def select_random_cell(grid):
	"""
	Select a random cell from the grid.

	:param grid: The grid object containing cells.
	:return: A randomly selected cell.
	"""
	return random.choice(list(grid.cells.values()))

def propagate_constraints(cell, ranges, grid):
	"""
	Propagate constraints iteratively by updating neighbors' ranges,
	starting from a cell with a fixed value.
	"""
	stack = [cell]  # Start propagation from this cell
	while stack:
		current = stack.pop()
		current_range = ranges[current]
		if len(current_range) == 1:
			min_val, max_val = current_range[0]-1, current_range[0]+1
		else:
			min_val, max_val = min(current_range) - 1, max(current_range) + 1

		for neighbor in current.neighbors:
			neighbor_range = ranges[neighbor]
			new_range = [v for v in neighbor_range if min_val <= v <= max_val]
			if new_range != neighbor_range:
				ranges[neighbor] = new_range
				if not new_range:
					ranges[neighbor] = range(min_val, max_val + 1)
				stack.append(neighbor)  # Revisit the neighbor
				if len(current_range)==1:
					print(f"Processing cell: current range: {current_range}")
					print(f"Updated neighbor: new range: {new_range}")

# Done
def seeding(ranges, grid):
	# Step 1: Filter unlocked cells
	# Select a seed cell
	seed = select_random_cell(grid)
	# Collapse
	ranges[seed] = [random.choice(ranges[seed])]
	# Propagate constraints
	propagate_constraints(seed, ranges, grid)

# Mask
def collapse(ranges, cell, grid):
	return propagate_constraints(cell, ranges, grid)

def collapse_low_entropy_cell(ranges, grid):
	"""
	Collapse the cell with the lowest positive entropy (more than 1 option).
	"""
	# Find the cell with the fewest options greater than 1
	candidate_cells = [cell for cell, range_values in ranges.items() if len(range_values) > 1]
	if not candidate_cells:
		return

	# Select the cell with the smallest range
	target_cell = min(candidate_cells, key=lambda c: len(ranges[c]))

	# Randomly pick a value from the range and collapse
	selector = randint(1,3)
	if selector == 1:
		ranges[target_cell] = ranges[target_cell][0]
	if selector == 3:
		ranges[target_cell] = ranges[target_cell][-1]

	ranges[target_cell] = [random.choice(ranges[target_cell])]
	propagate_constraints(target_cell, ranges, grid)



def wave_function_collapse_legacy(grid):
	"""
	Perform Wave Function Collapse on the grid.
	"""

	# Step 1: Seed the grid by collapsing a random seed cell
	seed_cell = random.choice(list(grid.cells.values()))
	seed_cell.collapse()

	# Step 2: Iterate until all cells are collapsed
	uncollapsed_cells = [cell for cell in grid.cells.values() if not cell.fixed]
	while uncollapsed_cells:
		# Find the cell with the smallest range (lowest entropy)
		target_cell = min(
			uncollapsed_cells,
			key=lambda cell: cell.zenith - cell.nadir
		)

		# Collapse the target cell
		target_cell.collapse()

		# Update the list of uncollapsed cells
		uncollapsed_cells = [cell for cell in grid.cells.values() if not cell.fixed]

	# Step 3: Validate the grid
	for cell in grid.cells.values():
		if not cell.fixed:
			raise ValueError(f"Cell at {cell.position} did not collapse properly.")

	return grid






from random import choice


def wave_function_collapse(grid):
	"""
	Perform Wave Function Collapse on the grid.
	"""
	grid.initialize()
	# Step 1: Seed the grid by collapsing a random seed cell
	seed_cell = choice(list(grid.cells.values()))
	seed_cell.Collapse()

	# Step 2: Iterate until all cells are collapsed
	uncollapsed_cells = [cell for cell in grid.cells.values() if not cell.fixed()]

	while uncollapsed_cells:
		# Find the cell with the lowest entropy (smallest range of levels)
		target_cell = min(
			uncollapsed_cells,
			key=lambda cell: len(cell.levels)
		)

		# Collapse the target cell
		target_cell.Collapse()

		# Update the list of uncollapsed cells
		uncollapsed_cells = [cell for cell in grid.cells.values() if not cell.fixed()]

	# Step 3: Validate the grid
	for cell in grid.cells.values():
		if not cell.fixed():
			raise ValueError(f"Cell at {cell.position} did not collapse properly.")
		if not cell.levels:
			raise ValueError(f"Cell at {cell.position} has invalid levels: {cell.levels}")
		if len(cell.levels) > 1:
			raise ValueError(f"Cell at {cell.position} has more than one level: {cell.levels}")

	return grid
