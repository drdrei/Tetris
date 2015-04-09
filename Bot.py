import pygame
import math
import copy
from Shapes import Shape
from operator import itemgetter

class Bot:
	def __init__(self):
		self.heightMod = -0.66569 
		self.lineMod = 0.99275
		self.holeMod = -0.46544
		self.bumpyMod = -0.24077
	
	def check_spot_score(self, shape, matrix):
		self.score = []
		for rotation in range(0,4):
			for column in range(0,10):
				test_matrix = copy.deepcopy(matrix)
				test_shape = copy.deepcopy(shape)
				test_shape.rotation = rotation
				test_shape.track_x = column
				test_shape.bot_update_shape(test_matrix)
				
				test_x = 0
				for x in test_shape.x:
					if x < 0 or x > 9:
						test_x = 1

				if test_x == 0:
					try:
						max_y = max(test_shape.y)
						while not test_shape.collision and max_y < 22:
							test_shape.test_y(test_matrix)
							test_shape.y = [(y+1) for y in test_shape.y]
					except IndexError:
						pass
					try:
						for ind, i in enumerate(test_shape.x):
							test_matrix[test_shape.y[ind]-1][test_shape.x[ind]] = 1
					except IndexError:
						pass

					height = self.heightMod * self.test_height(test_matrix)
					holes = self.holeMod * self.test_holes(test_matrix)
					lines = self.lineMod * self.test_lines(test_matrix)
					bumpy = self.bumpyMod * self.test_bumpy()
					self.score.append((height + holes + lines + bumpy , column , rotation))

		return max(self.score)
		
				
	def test_height(self,matrix):
		test_matrix = copy.deepcopy(matrix)
		test_matrix.reverse()

		self.col=[0]*10
		for row in range(0, 22):
			for column in range(0, 10):
				if test_matrix[row][column] == 1:
					self.col[column]=row+1
					
		return sum(self.col)

	
	def test_holes(self,matrix):
		holes=0
		try:
			for row, row_items in enumerate(matrix):
				for column, item in enumerate(row_items):
					x, y = column, row
					if item == 1 and not matrix[y+1][x]:
						holes += 1
						# while matrix[row-i][column] and row-i>0:
						# 	holes+=1
						# 	i+=1
		except IndexError:
			pass
	
		return holes
		
	def test_bumpy(self):
		self.bumpy=0
		for i in range(9):
			self.bumpy+=abs(self.col[i]-self.col[i+1])
		return self.bumpy

	def test_lines(self,matrix):
		lines = 0
		for row in matrix:
			if sum(row)==10:
				lines += 1
		return lines
	

		


			
			
			
			
			
		