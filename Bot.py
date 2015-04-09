import pygame
import math
import copy
from Shapes import Shape
from operator import itemgetter

# Main Bot class
class Bot:
	def __init__(self):
		self.heightMod = -0.66569 
		self.lineMod = 0.99275
		self.holeMod = -0.46544
		self.bumpyMod = -0.24077

	# Main bot testing function
	# Computes a score for each possible place where a block can be places, at every possible
	# orientation and returns a tuple with (best score, location, rotation)
	def check_spot_score(self, shape, matrix):
		self.score = []
		for rotation in range(0,4):
			for column in range(0,10):
				test_matrix = copy.deepcopy(matrix)
				test_shape = copy.deepcopy(shape)
				test_shape.rotation = rotation
				test_shape.track_x = column
				test_shape.update_shape(test_matrix)
				
				# tests the x coordinates of the block to see if it's valid
				test_x = 0
				for x in test_shape.x:
					if x < 0 or x > 9:
						test_x = 1

				# if test_x is valid it will compute the score for that place
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
		
	# function to calculate the total height of all the blocks combined
	# returns the sum of heights
	def test_height(self, matrix):
		test_matrix = copy.deepcopy(matrix)
		test_matrix.reverse()
		self.col = [0]*10
		for row in range(0, 22):
			for column in range(0, 10):
				if test_matrix[row][column] == 1:
					self.col[column] = row+1
					
		return sum(self.col)

	# tests the number of holes in the matrix
	# a hole is a 1 with a zero under it eg:
	# 01111
	# 01101
	# 00111
	# has two holes
	def test_holes(self,matrix):
		holes = 0
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
	
	# function to test the bumpiness of the terrain
	# takes the y height of one block and next block, finds the absolute
	# difference between the two
	# Does this for all the blocks and adds up the bumpiness
	def test_bumpy(self):
		self.bumpy=0
		for i in range(0, 9):
			self.bumpy += abs(self.col[i]-self.col[i+1])
		return self.bumpy

	# tests if any lines are clearable if a block is placed in a spot
	# fetches the row and sums the 1s in the row, if sum is 10, it counts the line
	def test_lines(self,matrix):
		lines = 0
		for row in matrix:
			if sum(row) == 10:
				lines += 1
		return lines

