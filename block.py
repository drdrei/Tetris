import pygame
import sys
from pygame.sprite import Sprite

class Block(Sprite):
	
	"""
	Basic building block of shapes
	Takes input of color
	"""
	
	active_blocks = pygame.sprite.LayeredUpdates()
	
	def __init__(self, color=None):
		
		self._color=color
		
		self.sprite=pygame.image.load(block_file())
		self._base_image=self.sprite
		
		Sprite.__init__(self)
		
		self._width=1
		self._height=1
		
	def block_color(self):
		return self._color
		
	def block_file(self):
		return {"Blue":"Blocks/blueTetris.png",
				"Gray":"Blocks/grayTetris.png",
				"Green":"Blocks/greenTetris.png",
				"LightBlue":"Blocks/lightblueTetris.png",
				"Orange":"Blocks/orangeTetris.png",
				"Purple":"Blocks/purpleTetris.png",
				"Red":"Blocks/redTetris.png",}[self._color]
		