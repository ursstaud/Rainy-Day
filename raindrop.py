import pygame
from pygame.sprite import Sprite
from random import randint

class Raindrop(Sprite):
	"""a class to represent a SINGLE drop """

	def __init__(self, ai_game):
		super().__init__() #inherits characteristics from sprite class
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		#load the drop image and set its rect attribute
		self.image = pygame.image.load('raindrops.bmp')
		self.rect = self.image.get_rect()

		#start each new drop near the top left of the screen width's and height's away from 0,0
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height 

		#store the drop's exact horizontal position
		self.y = float(self.rect.y)


	def update(self):
		"""move the drops down the screen"""
		self.y += self.settings.rain_drop_speed
		self.rect.y = self.y