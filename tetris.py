from random import *
import pygame

class block:
	def __init__(self, type):
		self.outer_image = pygame.image.load("outside.png")
		self.x = 0
		self.y = 0
		self.x_slave1 = None
		self.x_slave2 = None
		self.x_slave3 = None
		self.y_slave1 = None
		self.y_slave2 = None
		self.y_slave3 = None
		if type == 0:
			self.y_slave1 = self.y - 40
			self.y_slave2 = self.y - 20
			self.y_slave3 = self.y + 20

	def color(self, color = None):
		if color == None:
			self.color = (randint(1,255), randint(1,255), randint(1,255))
		self.color = color

	# contains block type and it's orientation
	def block_data(self, type, orientation):
		self.type = 0
		self.orientation = [0, 1, 2, 3]

	def clear(self):
		self.y_slave1, self.y_slave2, self.y_slave3 = self.y
		self.x_slave1, self.x_slave2, self.x_slave3 = self.x

	def rotate(self):
		if self.type == 0:
			for x in range(3):
				if self.orientation == 0 or self.orientation == 2:
					self.x_slave1 = self.x - 40
					self.x_slave2 = self.x - 20
					self.x_slave3 = self.x + 20
				if self.orientation == 1 or self.orientation == 3:
					self.y_slave1 = self.y - 40
					self.y_slave2 = self.y - 20
					self.y_slave3 = self.y + 20

		self.orientation.append(self.orientation.pop())




def conversion(shape):
	return int(shape.x/20), int(shape.y/20)

def initialize():
	block,blockrect, block_data = load_block()
	blockrect.x = width/2 + 10
	return block, blockrect, block_data

def randomizer():
	return randint(1,6)

def pop_sequence():
	shape_sequence = []
	for x in range(0,10):
		shape_sequence.append(randomizer())
	return shape_sequence

def input(shape, block_data):
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if block_data[1] == 0:
					block_data[1] = 1
				else:
					block_data[1] = 0
			if event.key == pygame.K_DOWN:
				if shape.bottom != 600:
					shape.y += 20
			if event.key == pygame.K_LEFT:
				if shape.left != 0:
					shape.x -= 20
			if event.key == pygame.K_RIGHT:
				if shape.right != 300:
					shape.x += 20
			if event.key == pygame.K_SPACE:
				shape.x = 0

def move_block(blockrect):
	blockrect.y += 20
	return blockrect.y  

def load_block(color = None):
	block_data = [0,0]
	border_color = (255, 255, 255)
	if color == None:
		color = (randint(1,255), randint(1,255), randint(1,255))

	# loads and colors the block
	outside = pygame.image.load("outside.png").convert()
	outside.fill(color, (1,1,18,18))

	return outside, outside.get_rect(), block_data

def draw_shape(block_tuple):
	if block_tuple[0] == 0:	
		shape_L = [-40, -20, 0, 20]
		shape_coords = []

		for index, x in enumerate(shape_L):
			if (block_tuple[1]) == 0:
				newrect = pygame.Rect.union(blockrect)
				shape_coords.append([blockrect.x, blockrect.y + x])
				screen.blit(block, (shape_coords[index][0],shape_coords[index][1]))
		# 	else:
		# 		shape_coords.append([blockrect.x + x, blockrect.y])
		# 		screen.blit(block, (shape_coords[index][0],shape_coords[index][1]))
	return shape_coords


############################################

pygame.init()
size = width, height = 300, 600
area = [[0 for x in range(int(width/20))] for x in range(int(height/20))]

black = (0, 0, 0)

a = block(0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('TETRIS')

block,blockrect, block_data = initialize()
# a.x, a.y = blockrect.x, blockrect.y

print(pygame.Rect)
init = 1000

blocks = set()
while 1:
	input(blockrect,block_data)
	print(blockrect.center)
	time = pygame.time.get_ticks()
	if init < time:
		if blockrect.bottom <= 580:
			blockrect.y += 20
		else:
			blocks.add(blockrect)
			block, blockrect, block_data = initialize()
		init += 500
	
	screen.fill(black)
	draw_shape(block_data)
	pygame.display.flip()

