import sys

import pygame

from settings_raining import Settings
from raindrop import Raindrop
from game_stats_raining import GameStats


class Raining:
	"""Overall class to manage raindrops"""
	def __init__(self):
		"""initialize the game and create game resources"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width 
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Raining")
		#self.stats = GameStats(self)
		self.raindrops = pygame.sprite.Group() #want to group because it will automatically draw all elements 
		#of a group to the screen
		self._create_raindrop_grid() #this creates a group to hold the fleet of aliens

	def run_game(self):
		"""start the main loop for the game"""
		while True:
			self._check_events() #calls another method from within the class, simplifies the main method
			self._update_raindrops() #another helper method for updating the 
			self._update_screen() #another helper method for updating the screen, continuous updating until exit



	def _update_raindrops(self):
		"""check if the fleet is at an edge, """
		self.raindrops.update() #pulling the method from the raindrop class and adding it to raining class
		self._check_raindrops_bottom()

	def _create_one_row_raindrops(self):
		"""create one row of raindrops for each raindrop lost"""
		for raindrop_number in range(self.number_raindrop_x):
			self._create_raindrop(raindrop_number, 0)

	def _check_raindrops_bottom(self):
		"""check if any aliens have reached the bottom of the screen"""
		screen_rect = self.screen.get_rect()
		for raindrop in self.raindrops.copy():
			if raindrop.rect.top >= self.settings.screen_height:
				self.raindrops.remove(raindrop)
				self._create_one_row_raindrops()


	def _check_events(self): #THIS IS THE HELPER METHOD, it helps the main method
		"""respond to keyboard/mouse events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN: #if the event does not evaluate to quit
				self._check_keydown_events(event)

	def _check_keydown_events(self, event): #this is a helper method
		"""respond to keypresses"""
		if event.key == pygame.K_q:
			sys.exit()

	def _create_raindrop_grid(self):
		"""create the grid of drops"""
		raindrop = Raindrop(self)
		raindrop_width, raindrop_height = raindrop.rect.size
		available_space_x = self.settings.screen_width - (2 * raindrop_width)
		self.number_raindrop_x = available_space_x // (2 * raindrop_width) #note, 2 variable can only be an int, not float

		#determine the number of rows of aliens that fit on the screen
		raindrop_start_height = raindrop_height
		available_space_y = (self.settings.screen_height -
								 (3 * raindrop_height) - raindrop_start_height)
		number_rows = available_space_y // (3 * raindrop_height)

		#create the first row of aliens
		for row_number in range(number_rows):
			for raindrop_number in range(self.number_raindrop_x):
				self._create_raindrop(raindrop_number, row_number)
				#print(row_number)

	def _create_raindrop(self, raindrop_number, row_number):
		#create an alien and place it in the row
		raindrop = Raindrop(self)
		raindrop_width, raindrop_height = raindrop.rect.size
		raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
		raindrop.rect.x = raindrop.x 
		raindrop.rect.y = raindrop.y = raindrop.rect.height + 2 * raindrop.rect.height * row_number
		self.raindrops.add(raindrop)


	def _update_screen(self): #this is another helper method!
		"""update images on screen, flip to new screen"""
		self.screen.fill(self.settings.bg_color)#redraw the screen during each pass through the loop

		self.raindrops.draw(self.screen) #draws the alien on the screen, draw method requires one argument:

		
		pygame.display.flip()#make the most recently drawn screen visible, keeps playing smooth



if __name__ == '__main__': #if the file is being run directly, run this if block
	#make the game instance and run the game
	ai = Raining()
	ai.run_game()