from random import *
from Shapes import Shape
from Area import Area
from Display import Hud
from Menu import Menu
from Gameover import Gameover
from Bot import Bot
import pygame
import sys

# checks the user input and implements proper tests and movements in correspondance
# with the user's input
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

# updates the menu screen based on user inputs
def menu_input():
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


################### MAIN ####################
# some initialization procedures
pygame.init()
bot = Bot()

# initializes the screen, window name and the key repeater
# if the key is held the key is repeated
size = width, height = 300, 440
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('TETRIS')
pygame.key.set_repeat(75)

while 1:
	# build a matrix for from the width and height
	area = Area(width - 100, height)

	# initializes the shape queue (first number is current shape, second is upcoming)
	# randomizes the shape color
	shape_queue = []	
	for i in range(5):
		shape_queue.append(randint(0,6))
	shape_color=(randint(1,255), randint(1,255), randint(1,255))

	# creates a new shape: 0 is the shape id
	shape = Shape(shape_color, shape_queue[0])

	# init Heads up Display
	hud = Hud(width, height)
	gameOver=Gameover(width,height,area.score)

	# redraws the screen with the black background hud and menu
	screen.fill((0,0,0))
	hud.draw(screen)
	menu=Menu(width,height)
	menu.draw_menu(screen)
	menu.update_menu(screen)
	pygame.display.flip()

	# moves the selector box around the menu
	menu_input()

	# initializes the ticker and starts moving the blocks after ~1s elapsed.
	init = 1000 
	start_time = pygame.time.get_ticks()

	# Single Player Looop
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

		# Delay (increase to increase the shape drop delay)
		if init < time:			
			shape.move_down(area.matrix())
			init += 300
		
		# redraws the screen to update everything
		screen.fill((0,0,0))
		shape.draw_shape(area.matrix(), screen)
		area.draw(shape, area.matrix(), screen)
		area.print_game_info(screen)
		next_shape = Shape(shape_color,shape_queue[1],0,12,0)
		next_shape.update_shape(area.matrix())
		area.draw_next_shape(next_shape,screen)
		hud.draw(screen)
		pygame.display.flip()

	# first loop helps bot with the first iteration of the bot loop
	first_loop = 1
	# Main Bot loop
	while menu.demo and shape.game_state:
		check_input()
		time = pygame.time.get_ticks() - start_time

		next_shape = Shape(shape_color,shape_queue[1],0,12,0)

		if shape.state == 1 or first_loop == 1:
			next_shape.deactivate()
			shape_queue.pop(0)
			shape_queue.append(randint(0,6))
			shape = Shape(shape_color, shape_queue[0])
			shape_color=(randint(1,255), randint(1,255), randint(1,255))

			location = bot.check_spot_score(shape, area.matrix())
			shape.track_x = location[1]
			shape.rotation = location[2]
			first_loop = 0

		# Delay (increase to increase the shape drop delay)
		if init < time:
			shape.move_down(area.matrix())
			init += 0

		# redraws the screen to update everything
		screen.fill((0,0,0))
		shape.draw_shape(area.matrix(), screen)
		area.draw(shape, area.matrix(), screen)
		area.print_game_info(screen)
		next_shape.update_shape(area.matrix())
		area.draw_next_shape(next_shape,screen)
		hud.draw(screen)
		pygame.display.flip()


	# display the info screen
	while menu.info and not menu.infoDone:
		menu.draw_info(screen)
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit()
				sys.exit()
				
			if event.type == pygame.KEYDOWN:
				menu.infoDone=1
	
	# displays the loss screen			
	while not menu.info and not gameOver.pressContinue:
		gameOver.draw_Gameover(screen)
		gameOver.press_continue(screen)
		pygame.display.flip()

		# waits for a keystroke to move to main menu
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit()
				sys.exit()
				
			if event.type == pygame.KEYDOWN:
				gameOver.pressContinue=1

	# resets the game variables.
	menu.reset_game()
	
