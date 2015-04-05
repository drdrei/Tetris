from random import *
import pygame
import sys

class Shape:
	def __init__(self, shape_id = 0):
		self.x = []
		self.y = []
		self.shape_id = shape_id		
		self.rotation = 0
		self.reset_tracker()
		self.state = 0
		self.collision = 0

		# building block details
		self.color = (randint(1,255), randint(1,255), randint(1,255))
		self.block = pygame.image.load("outside.png").convert()
		self.block.fill(self.color, (1,1,18,18))
		self.blockrect = self.block.get_rect()

	def update_shape(self):
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
						   "00000",]

		# Backwards L
		if self.shape_id == 2 and self.rotation % 4 == 0:
			self.shape =["00200",
						"00200",
						"02200",
						"00000",
						"00000"]
		elif self.shape_id == 2 and self.rotation % 4 == 1:
			self.shape =["00000",
						"00200",
						"00222",
						"00000",
						"00000"]
		elif self.shape_id == 2 and self.rotation % 4 == 2:
			self.shape =["00000",
						"00000",
						"00220",
						"00200",
						"00200"]
		elif self.shape_id == 2 and self.rotation % 4 == 3:
			self.shape =["00000",
						"00000",
						"22200",
						"00200",
						"00000"]

		# L
		if self.shape_id == 3 and self.rotation % 4 == 0:
			self.shape =["00200",
						"00200",
						"00220",
						"00000",
						"00000"]
		elif self.shape_id == 3 and self.rotation % 4 == 1:
			self.shape =["00000",
						"00200",
						"22200",
						"00000",
						"00000"]
		elif self.shape_id == 3 and self.rotation % 4 == 2:
			self.shape =["00000",
						"00000",
						"02200",
						"00200",
						"00200"]
		elif self.shape_id == 3 and self.rotation % 4 == 3:
			self.shape =["00000",
						"00000",
						"00222",
						"00200",
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

		# 5
		elif self.shape_id == 5 and self.rotation % 2 == 0:
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
						
		# clear x and y locations before adding new coordinates
		self.x = []
		self.y = []
		for row_ind, row in enumerate(self.shape):
			for col_ind, item in enumerate(row):
				if int(item) == 2:
					self.y.append(row_ind + self.track_y)
					self.x.append(col_ind-2 + self.track_x)

	def draw_shape(self, matrix, screen):
		self.update_shape()
		self.rotation_test(matrix)
		self.check_bounds()
		for index, item in enumerate(self.x):
			screen.blit(self.block, (self.x[index]*20, self.y[index]*20))

	def rotate(self, matrix):
		self.rotation += 1

	def move_down(self, matrix):
		self.test_y(matrix)
		if self.collision == 1:
			self.track_y -= 1
			self.y = [i-1 for i in self.y]
			self.deactivate()
		self.y = [i+1 for i in self.y]
		self.track_y += 1

	def move_left(self, matrix):
		self.test_left(matrix)
		self.track_x -= 1
		self.x = [i-1 for i in self.x]
		if self.collision == 1:
			self.track_x += 1
			self.x = [i+1 for i in self.x]
			self.collision = 0

	def move_right(self, matrix):
		self.test_right(matrix)
		self.track_x += 1
		for index, x_pos in enumerate(self.x):
			self.x[index] += 1
		if self.collision == 1:
			self.track_x -= 1
			self.x = [i-1 for i in self.x]
			self.collision = 0

	def reset_tracker(self):
		self.track_x = 5
		self.track_y = 0

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

	def deactivate(self):
		self.state = 1		

	def test_y(self, matrix):
		try:
			y_test = [i+1 for i in self.y]
			for ind, i in enumerate(y_test):
				if matrix[y_test[ind]][self.x[ind]] == 1:
					self.collision = 1
		except IndexError:
			pass

	def test_left(self, matrix):
		try:
			x_test = [i-1 for i in self.x]
			for ind, i in enumerate(x_test):
				if matrix[self.y[ind]][x_test[ind]] == 1:
					self.collision = 1
		except IndexError:
			pass

	def test_right(self, matrix):
		try:
			x_test = [i+1 for i in self.x]
			for ind, i in enumerate(x_test):
				if matrix[self.y[ind]][x_test[ind]] == 1:
					self.collision = 1
		except IndexError:
			pass

	def rotation_test(self, matrix):
		try:
			rotation_error = 0
			for ind, coord in enumerate(self.x):
				if matrix[self.y[ind]][self.x[ind]] == 1:
					rotation_error = 1
			if rotation_error == 1:
				self.rotation -= 1
				self.update_shape()
		except IndexError:
			pass

