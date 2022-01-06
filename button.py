import pygame.font

class Button:
	"""A class to manage play button."""
	def __init__(self, ai_game, msg):
		"""Initializes button attributes."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		
		# Set dimensions and properties of the button.
		self.width, self.height = 200, 50
		self.button_color = (10,100,159)
		self.text_color = (255,255,255)
		self.font = pygame.font.SysFont(None, 48)
		
		# Button rect and center the position.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		
		# The button msg is to be prepped.
		self._prep_msg(msg)
		
	def _prep_msg(self, msg):
		"""Returns msg as image."""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
	
	def draw_button(self):
		# Draw button and text image over the button.
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)