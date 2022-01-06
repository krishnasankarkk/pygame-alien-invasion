class GameStats:
	"""A class to track game's statistics."""
	def __init__(self, ai_game):
		"""Initialize stats."""
		self.settings = ai_game.settings
		self.reset_stats()
		self.game_active = False
		# Highscore never reset.
		self.highscore_file = "Highscore.txt"
		with open(self.highscore_file, 'r') as file:
			self.highscore = int(file.read())
	def reset_stats(self):
		"""Stats which change during game."""
		self.ship_left = self.settings.ship_limit
		self.score = 0
		self.level = 1