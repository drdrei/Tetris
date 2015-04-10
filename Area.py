from random import *
import pygame

class Area:
	"""
	A class that stores the area of the screen
	as well as a few statistic to be displayed
	during the game.
	
	Initialize with the width and height of the
	screen being used
	
	Has functions to build the game area as a
	matrix as well as drawing to the screen.
	"""
	

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.area = []
		self.lines_cleared = 0
		self.score = 0

		# builds the matrix from the width/height input.
		array_builder = []
		for row in range(int(self.height/20)):
			for column in range(int(self.width/20)):
				array_builder.append(0)
			self.area.append(array_builder)
			array_builder = []

	# function to return the current matrix to caller
	def matrix(self):
		return self.area

	# function checks the shape state. If state is 1, it converts the shapes current
	# coordinates to the matrix and redraws the matrix.
	def draw(self, shape, matrix, screen):
		self.check_state(shape, matrix)
		solid_color = (70,70,70) # color used for tetrominos set in the game area
		solid = pygame.image.load("outside.png").convert()
		solid.fill(solid_color,(1,1,18,18))
		# draws the block to matrix
		for row, row_items in enumerate(matrix):
			for column, item in enumerate(row_items):
				x, y = column, row
				if item == 1:
					screen.blit(solid,(x*20, y*20))
	
	# function to draw the upcoming shape.					
	def draw_next_shape(self,shape,screen):
		# uses the x and y locations of shape to draw it
		for index, item in enumerate(shape.x):
			screen.blit(shape.block, ((shape.x[index])*20, shape.y[index]*20))

	# Checks whether the shape needs to become part of the matrix
	# also checks if any lines need to be cleared. records the lines and computes the score
	# finally it updates the score/lines cleared.
	def check_state(self, shape, matrix):
		if shape.state == 1:
			for ind, i in enumerate(shape.x):
				if matrix[shape.y[ind]][shape.x[ind]] == 0:
					matrix[shape.y[ind]][shape.x[ind]] = 1
		
		old_lines_cleared = self.lines_cleared
		count = 0
		update_score = 0
		for row, row_items in enumerate(matrix):
			if sum(row_items) == 10:
				matrix.pop(row)
				matrix.reverse()
				matrix.append([0]*10)
				matrix.reverse()
				self.lines_cleared += 1
				count += 1
				update_score = 1
		
		if update_score == 1:
			self.score += (self.lines_cleared - old_lines_cleared) * count * 100

	# Gives the user updates on the progress of the game
	# by shows the lines cleared and user's score on the right
	def print_game_info(self, screen):
		myfont = pygame.font.SysFont("monospace", 16)
		font_color = (255,255,0)
		# render text
		label_1 = myfont.render("Lines", 1, font_color)
		label_1_rect = label_1.get_rect()
		label_1_rect.center = (250, self.height/8*7 - 20)

		label_2 = myfont.render("Cleared:", 1, font_color)
		label_2_rect = label_2.get_rect()
		label_2_rect.center = (250, self.height/8*7)

		lines = myfont.render("%i" % self.lines_cleared, 1, font_color)
		lines_rect = lines.get_rect()
		lines_rect.center = (250, self.height/8*7 + 20)

		score_1 = myfont.render("Your", 1, font_color)
		score_1_rect = score_1.get_rect()
		score_1_rect.center = (250, self.height/2 - 20)

		score_2 = myfont.render("Score:", 1, font_color)
		score_2_rect = score_2.get_rect()
		score_2_rect.center = (250, self.height/2)

		score = myfont.render("%i" % self.score, 1, font_color)
		score_rect = score.get_rect()
		score_rect.center = (250, self.height/2 + 20)

		screen.blit(label_1, label_1_rect)
		screen.blit(label_2, label_2_rect)
		screen.blit(lines, lines_rect)

		screen.blit(score_1, score_1_rect)
		screen.blit(score_2, score_2_rect)
		screen.blit(score, score_rect)
