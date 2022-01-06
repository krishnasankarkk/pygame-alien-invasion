import pygame

class Ship:
	"""A class to manage the ship."""
	
	def __init__(self, ai_game):
		"""Initialize the ship."""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()
		
		# Load the ship image and get the rect.
		self.image = pygame.image.load('images/ship.png')
		self.rect = self.image.get_rect()
		
		# Start each new  ship at the bottom centre of the screen.
		self.rect.midbottom = self.screen_rect.midbottom
		
		# Store a decimal value for ship's horizontal position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
		# Movement flag.
		self.moving_up = False
		self.moving_down = False
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		"""Update ship's position according to the movement flag."""
		# Horizontal movement of the ship.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
			
		elif self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
			
		# Vertical movement of the ship.
		elif self.moving_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed
			
		elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed
			
		# Update rect object from self.x.
		self.rect.x = self.x
		self.rect.y = self.y
		
	def blitme(self):
		"""Draw the ship at the current loction."""
		self.screen.blit(self.image,self.rect)
		
	def center_ship(self):
		"""Center the ship's position."""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
