from random import *
import pygame
import sys

class Shape:
	"""
	Class used to build and keep track of
	shapes used in our game.
	
	Initialize with a color and optional
	shape_id, rotation, x location, and 
	y location.
	"""
	def __init__(self, color, shape_id = 0, rotation = 0, track_x = 5, track_y = 0):
		self.x = []
		self.y = []
		self.shape_id = shape_id		
		self.rotation = rotation
		self.state = 0
		self.collision = 0
		self.game_state = 1
		self.track_x = track_x
		self.track_y = track_y

		# building block details
		self.color = color
		self.block = pygame.image.load("outside.png").convert()
		self.block.fill(self.color, (1,1,18,18))
		self.blockrect = self.block.get_rect()

	# Changes shape and orientation based on shape_id and rotation
	def shape_types(self):
		# I
		if self.shape_id == 0 and self.rotation % 2 == 0:
			self.shape =["00200",
						"00200",
						"00200",
						"00200",
						"00000"]
		elif self.shape_id == 0 and self.rotation % 2 == 1:
			self.shape =["00000",
				 		 "00000",
				 		 "22220",
				 		 "00000",
				 		 "00000"]

		# Cube
		if self.shape_id == 1:
			self.shape =["00000",
						"02200",
						"02200",
						"00000",
						"00000"]

		# Backwards L
		if self.shape_id == 2 and self.rotation % 4 == 0:
			self.shape =["00000",
						"00200",
						"00200",
						"02200",
						"00000"]
		elif self.shape_id == 2 and self.rotation % 4 == 1:
			self.shape =["00000",
						"02000",
						"02220",
						"00000",
						"00000"]
		elif self.shape_id == 2 and self.rotation % 4 == 2:
			self.shape =["00000",
						"00220",
						"00200",
						"00200",
						"00000"]
		elif self.shape_id == 2 and self.rotation % 4 == 3:
			self.shape =["00000",
						"00000",
						"02220",
						"00020",
						"00000"]

		# L
		if self.shape_id == 3 and self.rotation % 4 == 0:
			self.shape =["00000",
						"00200",
						"00200",
						"00220",
						"00000"]
		elif self.shape_id == 3 and self.rotation % 4 == 1:
			self.shape =["00000",
						"00020",
						"02220",
						"00000",
						"00000"]
		elif self.shape_id == 3 and self.rotation % 4 == 2:
			self.shape =["00000",
						"02200",
						"00200",
						"00200",
						"00000"]
		elif self.shape_id == 3 and self.rotation % 4 == 3:
			self.shape =["00000",
						"00000",
						"02220",
						"02000",
						"00000"]

		# Z
		if self.shape_id == 4 and self.rotation % 2 == 0:
			self.shape =["00000",
						"02200",
						"00220",
						"00000",
						"00000"]
		elif self.shape_id == 4 and self.rotation % 2 == 1:
			self.shape =["00000",
						"00020",
						"00220",
						"00200",
						"00000"]

		# S
		if self.shape_id == 5 and self.rotation % 2 == 0:
			self.shape =["00000",
						"00220",
						"02200",
						"00000",
						"00000"]
		elif self.shape_id == 5 and self.rotation % 2 == 1:
			self.shape =["00000",
						"00200",
						"00220",
						"00020",
						"00000"]

		# T
		if self.shape_id == 6 and self.rotation % 4 == 0:
			self.shape =["00000",
						"00200",
						"02220",
						"00000",
						"00000"]
		elif self.shape_id == 6 and self.rotation % 4 == 1:
			self.shape =["00000",
						"00200",
						"02200",
						"00200",
						"00000"]
		elif self.shape_id == 6 and self.rotation % 4 == 2:
			self.shape =["00000",
						"00000",
						"02220",
						"00200",
						"00000"]
		elif self.shape_id == 6 and self.rotation % 4 == 3:
			self.shape =["00000",
						"00200",
						"00220",
						"00200",
						"00000"]


	# creates two arrays of x and y coordinates of the shapes blocks
	def update_shape(self, matrix):
		self.shape_types()
		# clear x and y locations before adding new coordinates
		self.x = []
		self.y = []
		for row_ind, row in enumerate(self.shape):
			for col_ind, item in enumerate(row):
				if int(item) == 2:
					self.y.append(row_ind + self.track_y)
					self.x.append(col_ind-2 + self.track_x)
		try:
			for ind, y in enumerate(self.y):
				if y > 1 and matrix[self.y[ind]][self.x[ind]] == 1 and self.track_x == 5 and self.track_y == 0:
					self.game_state = 0
			for i in range(3):
				if sum(matrix[i]) > 0:
					self.game_state = 0
		except IndexError:
			pass

	# Updates the shape, checks is rotation is possible, checks if out of bounds,
	# then draws the shape to the screen
	def draw_shape(self, matrix, screen):
		self.update_shape(matrix)
		self.rotation_test(matrix)
		self.check_bounds()
		for index, item in enumerate(self.x):
			screen.blit(self.block, (self.x[index]*20, self.y[index]*20))

	# increments the rotation
	def rotate(self, matrix):
		self.rotation += 1

	# attempt to move shape down by one. run test_y.
	# if collision detected, move the shape back by one
	def move_down(self, matrix):
		self.test_y(matrix)
		if self.collision == 1:
			self.track_y -= 1
			self.y = [i-1 for i in self.y]
			self.deactivate()
		self.y = [i+1 for i in self.y]
		self.track_y += 1
		

	# moves shape left if all the tests pass and not collision detected
	def move_left(self, matrix):
		self.test_left(matrix)
		self.track_x -= 1
		self.x = [i-1 for i in self.x]
		if self.collision == 1:
			self.track_x += 1
			self.x = [i+1 for i in self.x]
			self.collision = 0

	# moves shape right if all the tests pass and not collision detected
	def move_right(self, matrix):
		self.test_right(matrix)
		self.track_x += 1
		for index, x_pos in enumerate(self.x):
			self.x[index] += 1
		if self.collision == 1:
			self.track_x -= 1
			self.x = [i-1 for i in self.x]
			self.collision = 0

	# checks if the shape is out of bounds of the matrix,
	# if out of bounds is detected, it moves it back
	# if out of bounds on the y coordinate detected, it deactivates the shape
	def check_bounds(self):
		max_y = max(self.y)
		min_x = min(self.x)
		max_x = max(self.x)
		if max_y > 21:
			self.y = [i-(max_y - 21) for i in self.y]
			self.track_y += max_y - 21
			self.deactivate()
		if min_x < 0:
			self.x = [i-min_x for i in self.x]
			self.track_x -= min_x
		if max_x > 9:
			self.x = [i-(max_x - 9) for i in self.x]
			self.track_x -= (max_x - 9)

	# deactivates the shape
	def deactivate(self):
		self.state = 1		

	# tries to move the shape down by one, then checks there's a collision
	def test_y(self, matrix):
		try:
			y_test = [i+1 for i in self.y]
			for ind, i in enumerate(y_test):
				if matrix[y_test[ind]][self.x[ind]] == 1:
					self.collision = 1
		except IndexError:
			self.collision = 1
			pass

	# tries to move the shape left by 1 then checks if there's a collision
	def test_left(self, matrix):
		try:
			x_test = [i-1 for i in self.x]
			for ind, i in enumerate(x_test):
				if matrix[self.y[ind]][x_test[ind]] == 1:
					self.collision = 1
		except IndexError:
			pass

	# tries to move the shape right by 1 then checks if there's a collision
	def test_right(self, matrix):
		try:
			x_test = [i+1 for i in self.x]
			for ind, i in enumerate(x_test):
				if matrix[self.y[ind]][x_test[ind]] == 1:
					self.collision = 1
		except IndexError:
			pass

	# tries to rotate the shape, if there's an overlap, it prevents the rotation
	def rotation_test(self, matrix):
		try:
			rotation_error = 0
			for ind, coord in enumerate(self.x):
				if matrix[self.y[ind]][self.x[ind]] == 1:
					rotation_error = 1
			if rotation_error == 1:
				self.rotation -= 1
				self.update_shape(matrix)
		except IndexError:
			pass
