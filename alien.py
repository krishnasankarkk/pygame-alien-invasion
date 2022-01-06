import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	"""A class to manage the alien."""
	
	def __init__(self, ai_game):
		"""Initialize the alien."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()
		
		# Load alien image and rect.
		self.image = pygame.image.load('images/alien1.png')
		self.rect = self.image.get_rect()

		# Alien starting postion.
		self.rect.x  = self.rect.width
		self.rect.y = self.rect.height
		#self.rect.top = self.screen_rect.top
		# Alien's horizontal position as decimal value.
		self.x = float(self.rect.x)
	
	def check_edges(self):
		"""Checks whether fleet is at the edge of the screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True
	
	def update(self):
	
		# Update decimal postion.
		self.x += self.settings.alien_speed * self.settings.fleet_direction
		# Update the rect.
		self.rect.x = self.x
		
	def draw_star(self):
	
		self.screen.blit(self.image,self.rect)
		
