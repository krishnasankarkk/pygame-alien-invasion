class Settings:
	"""A class to store all settings for Alien Invasion."""
	
	def __init__(self):
		"""Iniatilize the static settings."""
		# screen settings
		self.screen_width = 1200
		self.screen_height = 600	
		self.bg_color = (0,0,0)
			
		# Ship settings

		self.ship_limit = 5
		
		

		
		# ALien settings

		self.drop_speed = 30
		# 1 means right -1 means left.
		self.fleet_direction = 1
		
		# How quickly game speed increases.
		self.game_speed = 1

		# How quickly alien point value increases.
		self.score_scale = 2
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		"""Initializes the settings that change during the game."""
		self.ship_speed = 10
		self.bullet_speed = 10
		self.alien_speed = 1.0

		# Bullet settings.
		self.bullet_allowed = 10

		#scoring
		self.alien_point = 50
		
		self.fleet_direction = 1 #right
		
	def increase_speed(self):
		"""Increase speed settings and alien point values."""
		self.ship_speed += self.game_speed
		self.bullet_speed += self.game_speed
		self.alien_speed += self.game_speed

		self.bullet_allowed += 1
		
		self.alien_point = int(self.alien_point * self.score_scale)