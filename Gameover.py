from random import *
import pygame

class Gameover:
	def __init__(self, width, height, score):
		self.width = width
		self.height = height
		self._score = score
		self.pressContinue=0

	# Draws the Gameover screen	and displays the score
	def draw_Gameover(self,screen):
		background_color = (255,255,255)
		font_color = (0,0,0)
		
		pygame.draw.rect(screen, background_color, (50, 50, self.width-100, self.height-100), 0)
		
		tetris_font = pygame.font.Font("Tetris.TTF",32)
		tetris_font.set_bold(1)
		
		label_1 = tetris_font.render("YOU LOST", 1, font_color)
		label_1_rect = label_1.get_rect()
		label_1_rect.center = (150, 150)
		
		tetris_font = pygame.font.SysFont("monospace", 32)
		tetris_font.set_bold(1)
		label_2 = tetris_font.render("Score:", 1, font_color)
		label_2_rect = label_2.get_rect()
		label_2_rect.center = (150, 230)

		score = tetris_font.render("%i" % self._score, 1, font_color)
		score_rect = score.get_rect()
		score_rect.center = (150, 280)
		
		screen.blit(label_1, label_1_rect)
		screen.blit(label_2, label_2_rect)
		screen.blit(score, score_rect)

	# Prints the continue message
	def press_continue(self,screen):
		tetris_font = pygame.font.SysFont("monospace", 12)
		font_color = (0,0,0)
		
		label_1 = tetris_font.render("Press any button to continue",1, font_color)
		label_1_rect = label_1.get_rect()
		label_1_rect.center = (150, 350)
		
		screen.blit(label_1, label_1_rect)