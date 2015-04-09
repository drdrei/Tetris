from random import *
import pygame


class Menu:
	
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.demo=0
		self.singlePlayer=1
		self.info=0
		self.gameStart=0
		
	def draw_menu(self,screen):
		
		background_color=(255,255,255)
		font_color = (0,0,0)
		
		pygame.draw.rect(screen, background_color, (50,50,self.width-100,self.height-100),0)
		
		tetris_font=pygame.font.Font("Tetris.TTF",32)
		tetris_font.set_bold(1)
		
		label_1 = tetris_font.render("TETRIS",1, font_color)
		label_1_rect = label_1.get_rect()
		label_1_rect.center = (150, 100)
		
		tetris_font=pygame.font.SysFont("monospace", 10)
		label_5 = tetris_font.render("By Niko Somos & Andrei Usenka",1, font_color)
		label_5_rect = label_5.get_rect()
		label_5_rect.center = (150, 350)
		
		screen.blit(label_1, label_1_rect)
		screen.blit(label_5, label_5_rect)
		
		
	def update_menu(self,screen):
		
		tetris_font=pygame.font.Font("Tetris.TTF",16)
		tetris_font.set_bold(0)
		
		singlePlayerBG=(255*(1-self.singlePlayer),255*(1-self.singlePlayer),255*(1-self.singlePlayer))
		demoBG=(255*(1-self.demo),255*(1-self.demo),255*(1-self.demo))
		infoBG=(255*(1-self.info),255*(1-self.info),255*(1-self.info))
		
		singlePlayerFont=(255*self.singlePlayer,255*self.singlePlayer,255*self.singlePlayer)
		demoFont=(255*self.demo,255*self.demo,255*self.demo)
		infoFont=(255*self.info,255*self.info,255*self.info)
		
		
		pygame.draw.rect(screen, singlePlayerBG, (90,180,120,20),0)
		label_2 = tetris_font.render("Single Player",1, singlePlayerFont)
		label_2_rect = label_2.get_rect()
		label_2_rect.center = (150, 190)
		
		pygame.draw.rect(screen, demoBG, (90,240,120,20),0)
		label_3 = tetris_font.render("Demo",1, demoFont)
		label_3_rect = label_3.get_rect()
		label_3_rect.center = (150, 250)
		
		pygame.draw.rect(screen, infoBG, (90,300,120,20),0)
		label_4 = tetris_font.render("Info",1, infoFont)
		label_4_rect = label_4.get_rect()
		label_4_rect.center = (150, 310)
		
		screen.blit(label_2, label_2_rect)
		screen.blit(label_3, label_3_rect)
		screen.blit(label_4, label_4_rect)

		
	def move_cursor(self,direction):
		if self.demo:
			if direction==1:
				self.demo=0
				self.singlePlayer=1
			elif direction==-1:
				self.demo=0
				self.info=1
		elif self.singlePlayer:
			if direction==1:
				self.singlePlayer=0
				self.info=1
			elif direction==-1:
				self.demo=1
				self.singlePlayer=0
		elif self.info:
			if direction==1:
				self.demo=1
				self.info=0
			elif direction==-1:
				self.singlePlayer=1
				self.info=0
				
	def reset_game(self):
		self.demo=0
		self.singlePlayer=1
		self.info=0
		self.gameStart=0