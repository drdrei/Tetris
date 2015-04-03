from random import *
import pygame

######### Main ##########
def shapes(type, rotation):
	if type == 0 and rotation % 2 == 0:
		shape = ["0020",
				 "0020",
				 "0020",
				 "0020"]
	elif type == 0 and rotation % 2 == 1: 
		shape = ["0000",
				 "0000",
				 "2222",
				 "0000"]
	return shape

def array_builder(height, width):
	area = []
	array_builder = []
	for x in range(int(width/20)):
		for i in range(int(height/20)):
			array_builder.append(0)
		area.append(array_builder)
		array_builder = []
	return area

def input(shape, block_data):
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				block_data[1] += 1
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
	return block_data

def draw_shape(shape_list, blockrect, area):
	prev_area = area
	for row, row_items in enumerate(shape_list):
		for column, item in enumerate(row_items):
			if int(item) == 2:
				x, y = column - 3, row
				xx, yy = int((blockrect.x + x*20)/20), int((blockrect.y + y*20)/20)
				# check for collisions
				# if xx >= 0 and yy >= 21
				screen.blit(block,(blockrect.x + x*20, blockrect.y + y*20))
	return area

def draw_matrix(blockrect, area):
	trans_coords = []
	new_area = area
	for row, row_items in enumerate(new_area):
		for column, item in enumerate(row_items):
			if item == 2:
				x, y = column - 3, row
				xx, yy = int((blockrect.x + x*20)/20), int((blockrect.y + y*20)/20)
	
################### MAIN ####################
pygame.init()
size = width, height = 200, 440

black = (0, 0, 0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('TETRIS')

color = (randint(1,255), randint(1,255), randint(1,255))
block = pygame.image.load("outside.png").convert()

block.fill(color, (1,1,18,18))
blockrect = block.get_rect()
area = array_builder(width, height)

blockrect.x = int(width/2)
blockrect.y = -40

a = blockrect


block_data = [0,0]
init = 1000


while 1:
	time = pygame.time.get_ticks()
	block_data = input(blockrect, block_data)
	if init < time:
		if blockrect.bottom <= height:
			blockrect.y += 20
		init += 300
	
	screen.fill(black)
	area = draw_shape(shapes(block_data[0],block_data[1]), blockrect,area)
	pygame.display.flip()


