import pygame.font

class Button:
	"""A class to manage play button."""
	def __init__(self, ai_game, msg):
		"""Initializes button attributes."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		
		# Set dimensions and properties of the button.
		self.width, self.height = 200, 50
		self.button_color = (10,150,159)
		self.text_color = (255,255,255)
		self.font = pygame.font.Font('fonts/Agbalumo-Regular.ttf', 20)
		
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

	def _rounded_rect(self, rect, color, radius):
		"""Draws a rectangle with rounded corners."""
		pygame.draw.rect(self.screen, color, rect, border_radius=radius)
  
	def draw_button(self):
		# Draw button and text image over the button.
		self._rounded_rect(self.rect, self.button_color, 20)  
		self.screen.blit(self.msg_image, self.msg_image_rect)
  
	

  