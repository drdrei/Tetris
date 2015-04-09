from random import *
from Shapes import Shape
from Area import Area
from Display import Hud
from Menu import Menu
from Gameover import Gameover
from Bot import Bot
import pygame
import sys

def check_input():
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				shape.rotate(area.matrix())
			if event.key == pygame.K_DOWN:
				shape.test_y(area.matrix())
				if shape.collision != 1:
					shape.move_down(area.matrix())
			if event.key == pygame.K_LEFT:
				shape.move_left(area.matrix())
			if event.key == pygame.K_RIGHT:
				shape.move_right(area.matrix())
			if event.key == pygame.K_SPACE:
				shape.test_y(area.matrix())
				while shape.collision != 1:
					shape.move_down(area.matrix())
					shape.draw_shape(area.matrix(), screen)
					area.draw(shape, area.matrix(), screen)
	return area

################### MAIN ####################
# some initialization procedures
pygame.init()

bot = Bot()
size = width, height = 300, 440
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('TETRIS')
pygame.key.set_repeat(75)
shape_queue = []

	
while 1:
	for i in range(5):
		shape_queue.append(randint(0,6))
	
	shape_color=(randint(1,255), randint(1,255), randint(1,255))
	# build a matrix for from the width and height
	area = Area(width - 100, height)

	# creates a new shape: 0 is the shape id
	shape = Shape(shape_queue[0])

	# init Heads up Display
	hud = Hud(width, height)

	screen.fill((0,0,0))
	hud.draw(screen)

	menu=Menu(width,height)
	menu.draw_menu(screen)
	menu.update_menu(screen)
	pygame.display.flip()

	while not menu.gameStart:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				
				if event.key == pygame.K_DOWN:
					menu.move_cursor(-1)
					menu.update_menu(screen)
					pygame.display.flip()
				
				if event.key == pygame.K_UP:
					menu.move_cursor(1)
					menu.update_menu(screen)
					pygame.display.flip()
		
				if event.key == pygame.K_RETURN:
					menu.gameStart=1	


	init = 1000
	start_time = pygame.time.get_ticks()
	shape_color=(randint(1,255), randint(1,255), randint(1,255))
	while menu.singlePlayer and shape.game_state:
		check_input()
		time = pygame.time.get_ticks() - start_time

		# deactivate shape if state become one, pop shape off the queue and
		# add a new shape to the list and 		
		if shape.state == 1:
			next_shape.deactivate()
			shape_queue.pop(0)
			shape_queue.append(randint(0,6))
			shape = Shape(shape_color,shape_queue[0], 0,5,0)
			shape_color=(randint(1,255), randint(1,255), randint(1,255))

		
		# Delay
		if init < time:			
			shape.move_down(area.matrix())
			init += 500

		screen.fill((0,0,0))
		shape.draw_shape(area.matrix(), screen)
		area.draw(shape, area.matrix(), screen)
		area.print_game_info(screen)
		next_shape=Shape(shape_color,shape_queue[1],0,12,0)
		next_shape.bot_update_shape()
		area.draw_next_shape(next_shape,screen)
		hud.draw(screen)
		pygame.display.flip()
		
	while menu.demo and shape.game_state:
		check_input()
		time = pygame.time.get_ticks() - start_time

		if shape.state == 1:
			next_shape.deactivate()
			shape_queue.pop(0)
			shape_queue.append(randint(0,6))
			shape = Shape(shape_color, shape_queue[0])
			shape_color=(randint(1,255), randint(1,255), randint(1,255))

			
		# Delay
		if init < time:
			shape.move_down(area.matrix())
			location = bot.check_spot_score(shape, area.matrix())
			shape.track_x = location[1]
			shape.rotation = location[2]
			init += 300

		screen.fill((0,0,0))
		shape.draw_shape(area.matrix(), screen)
		area.draw(shape, area.matrix(), screen)
		area.print_game_info(screen)
		next_shape=Shape(shape_color,shape_queue[1],0,12,0)
		next_shape.bot_update_shape()
		area.draw_next_shape(next_shape,screen)
		hud.draw(screen)
		pygame.display.flip()

	gameOver=Gameover(width,height,area.score)
	gameOver.draw_Gameover(screen)
	gameOver.press_continue(screen)
	pygame.display.flip()

	while not gameOver.pressContinue:
		gameOver.press_continue(screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit()
				sys.exit()
				
			if event.type == pygame.KEYDOWN:
				gameOver.pressContinue=1
			
	menu.reset_game()
	
