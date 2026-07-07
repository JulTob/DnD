import app.random as random

class DungeonGenerator:
	def __init__(self, width, height, room_attempts=10):
		self.width = width
		self.height = height
		self.room_attempts = room_attempts
		self.grid = [["#" for _ in range(width)] for _ in range(height)]  # Dungeon starts as solid walls
		self.rooms = []

	def create_room(self, x, y, w, h):
		"""Create a rectangular room in the grid."""
		for i in range(y, y + h):
			for j in range(x, x + w):
				self.grid[i][j] = "."  # Mark as floor

	def is_valid_room(self, x, y, w, h):
		"""Check if a room can fit without overlapping others or boundaries."""
		if x + w >= self.width or y + h >= self.height:
			return False  # Out of bounds
		for i in range(y - 1, y + h + 1):  # Check with padding to avoid overlap
			for j in range(x - 1, x + w + 1):
				if self.grid[i][j] == ".":
					return False  # Overlaps existing room
		return True

	def generate_rooms(self):
		"""Randomly generate rooms in the dungeon."""
		for _ in range(self.room_attempts):
			w = random.randint(3, 8)  # Room width
			h = random.randint(3, 8)  # Room height
			x = random.randint(1, self.width - w - 1)
			y = random.randint(1, self.height - h - 1)
			if self.is_valid_room(x, y, w, h):
				self.create_room(x, y, w, h)
				self.rooms.append((x, y, w, h))

	def connect_rooms(self):
		"""Create corridors between rooms."""
		for i in range(len(self.rooms) - 1):
			x1, y1, _, _ = self.rooms[i]
			x2, y2, _, _ = self.rooms[i + 1]

			if random.choice([True, False]):
				self.create_h_corridor(x1, x2, y1)
				self.create_v_corridor(y1, y2, x2)
			else:
				self.create_v_corridor(y1, y2, x1)
				self.create_h_corridor(x1, x2, y2)

	def create_h_corridor(self, x1, x2, y):
		"""Create a horizontal corridor."""
		for x in range(min(x1, x2), max(x1, x2) + 1):
			self.grid[y][x] = "."

	def create_v_corridor(self, y1, y2, x):
		"""Create a vertical corridor."""
		for y in range(min(y1, y2), max(y1, y2) + 1):
			self.grid[y][x] = "."

	def print_dungeon(self):
		"""Display the dungeon in the console."""
		for row in self.grid:
			print("".join(row))

# Use the generator
dungeon = DungeonGenerator(width=30, height=20, room_attempts=15)
dungeon.generate_rooms()
dungeon.connect_rooms()
dungeon.print_dungeon()
