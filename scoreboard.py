import pygame.font
from pygame.sprite import Group

from lives import Lives

class Scoreboard:
	"""A class to report scoring information."""
	
	def __init__(self,ai_game):
		"""Initializes the scoreboard attributes."""
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats
		
		# font settings for scoring information.
		self.font_color = (10,200,200)
		self.font = pygame.font.Font('fonts/Agbalumo-Regular.ttf',25)
		
		# prepare the initial score image.
		self.prep_score()
		self.prep_highscore()
		self.prep_level()
		self.prep_lives()
		
	def prep_score(self):
		"""Turn the text into a rendered image."""
		score_str = "Score:"+"{:,}".format(self.stats.score)
		if self.stats.score > self.stats.highscore:
			self.score_image = self.font.render(score_str, True, self.font_color,self.settings.bg_color)
		else:
			self.score_image = self.font.render(score_str, True, (200, 0, 0),self.settings.bg_color)

		# display score at top right position.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
		
	def prep_highscore(self):
		"""Turn the text into a rendered image."""
		highscore = self.stats.highscore
		highscore_str = "Highscore:{:,}".format(highscore)
		self.highscore_image = self.font.render(highscore_str, True, self.font_color, self.settings.bg_color)

		# highscore position in the screen.
		self.highscore_rect = self.highscore_image.get_rect()
		self.highscore_rect.centerx = self.screen_rect.centerx
		self.highscore_rect.top = self.score_rect.top

	def prep_level(self):
		"""Turn the level into a rendered image."""
		level_str = "Level: " + str(self.stats.level)
		self.level_image = self.font.render(level_str, True, self.font_color, self.settings.bg_color)

		# position the level below the score.
		self.level_image_rect = self.level_image.get_rect()
		self.level_image_rect.right = self.score_rect.right
		self.level_image_rect.top = self.score_rect.bottom + 10

	def prep_lives(self):
		"""Show how many ships are left."""
		self.lives = Group()
		for life_number in range(self.stats.ship_left):
			life = Lives(self.ai_game)
			#ships left position.
			life.rect.x = 10 + life_number * life.rect.width
			life.rect.y = 10
			self.lives.add(life)

	def show_score(self):
		"""Draw the score to screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.highscore_image, self.highscore_rect)
		self.screen.blit(self.level_image, self.level_image_rect)
		self.lives.draw(self.screen)

	def check_highscores(self):
		"""Check to see if there's a new highscore."""
		if self.stats.score > self.stats.highscore:
			self.stats.highscore = self.stats.score
			self.prep_highscore()