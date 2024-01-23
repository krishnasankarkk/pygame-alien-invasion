import pygame
from pygame.sprite import Sprite


class Stars(Sprite):
	"""A class to manage the alien."""
	
	def __init__(self, ai_game):
		"""Initialize the alien."""
		super().__init__()
		self.screen = ai_game.screen
		#self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()
		
		# Load alien image and rect.
		self.image = pygame.image.load('images/bullet.png')
		self.rect = self.image.get_rect()

		# Alien starting postion.
		self.rect.center = self.screen_rect.center
		# Alien's horizontal position as decimal value.
		self.y = float(self.rect.y)
	
	def update(self):
	
		# Update decimal postion.
		self.y += 1
		# Update the rect.
		self.rect.y = self.y
		
	def draw_star(self):
	
		self.screen.blit(self.image,self.rect)
		
