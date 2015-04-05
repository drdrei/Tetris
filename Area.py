from random import *
import pygame

class Area:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.area = []
		self.lines_cleared = 0


		array_builder = []
		for row in range(int(self.height/20)):
			for column in range(int(self.width/20)):
				array_builder.append(0)
			self.area.append(array_builder)
			array_builder = []

	def matrix(self):
		return self.area

	def draw(self, shape, matrix, screen):
		self.check_state(shape, matrix)
		solid_color = (50,50,50)
		solid = pygame.image.load("outside.png").convert()
		solid.fill(solid_color,(1,1,18,18))
		for row, row_items in enumerate(matrix):
			for column, item in enumerate(row_items):
				x, y = column, row
				if item == 1:
					screen.blit(solid,(x*20, y*20))

	# Checks whether the shape needs to become part of the matrix
	# also checks if any lines need to be cleared.
	def check_state(self, shape, matrix):
		if shape.state == 1:
			for ind, i in enumerate(shape.x):
				matrix[shape.y[ind]][shape.x[ind]] = 1

		for row, row_items in enumerate(matrix):
			if sum(row_items) == 10:
				matrix.pop(row)
				matrix.reverse()
				matrix.append([0]*10)
				matrix.reverse()
				self.lines_cleared += 1

	def print_game_info(self, screen):
		myfont = pygame.font.SysFont("monospace", 14)

		# render text
		label = myfont.render("test", 1, (255,255,0))
		screen.blit(label, (100, 100))





