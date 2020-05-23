class Settings:
	"""a class to store all the settings for the Alien Invasion game"""

	def __init__(self):
		"""initialize the game's settings"""
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (124, 185, 232) 

		#alien settings
		self.rain_drop_speed = 1
		#fleet direction of 1 represents right, -1 represents left
		self.fleet_direction = 1