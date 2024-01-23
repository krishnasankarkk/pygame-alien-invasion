import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage the bullet."""
	
	def __init__(self, ai_game):
		"""Initialize the bullet."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()
		
		# Load bullet image and rect.
		self.image = pygame.image.load('images/bullet.png')
		self.rect = self.image.get_rect()
		
		# Bullet starting postion.
		self.rect.midtop  = ai_game.ship.rect.midtop
		
		# Bullet's positon as decimal value.
		self.y = float(self.rect.y)
		
	def update(self):
		"""Move the bullet vertically."""
		# Update decimal postion.
		self.y -= self.settings.bullet_speed
		# Update the rect.
		self.rect.y = self.y
		
	def draw_bullet(self):
		"""Draw the bullet to screen."""
		self.screen.blit(self.image,self.rect)
