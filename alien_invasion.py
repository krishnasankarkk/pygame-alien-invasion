import sys

from time import sleep
import pygame


from alien import Alien
from bullet import Bullet
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
 	
class AlienInvasion:
	"""Class to manage game assets and behaviour."""
	
	def __init__(self):
		"""Initialize the game, and create the game resources."""
		pygame.init()
		self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)		
		self.settings = Settings()
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self.bg = pygame.image.load('images/space.png')
		# Instance to create game stats.
		# and the scoreboard.
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)
		
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")
		
		self.ship = Ship(self)
		self._create_fleet()

		#make a button instance.
		self.play_button = Button(self, "Play")
		#self.count = 0
	def run_game(self):
		"""Start main loop for the game."""
		while True:
			self._check_events()
	
			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()
			
			self._update_screen()

	def _update_bullets(self):
		"""Updates bullet's positions."""
		self.bullets.update()
		# Delete the disappeared bullets.
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		self._bullet_alien_collisions()
		
	def _bullet_alien_collisions(self):
		""" Deletes aliens and bullets collided."""
		#check for bullet and alien collision.
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
		
		if collisions:
			for aliens in collisions.values():
				self.stats.score += self.settings.alien_point * len(aliens)
			self.sb.prep_score()
			self.sb.check_highscores()
		
		if not self.aliens:
			# Destroy existing bullets and create a new fleet.
			self.bullets.empty()
			self._create_fleet()	
			self.settings.increase_speed()
			
			#increase level.
			self.stats.level += 1
			self.sb.prep_level()

	def _update_aliens(self):
		"""Updates alien's positions."""
		self._check_fleet_edges()
		self.aliens.update()
	
		# Alien-ship collisions.
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
	
		self._check_aliens_bottom()
	
	def _ship_hit(self):
		"""Respond when alien hits the ship."""
		if self.stats.ship_left > 1:
			# Remaining ships.
			
			self.stats.ship_left -= 1
			self.sb.prep_lives()

			#get rid of bullets and aliens.
			self.aliens.empty()
			self.bullets.empty()

			# Create a new fleet and center the ship.
			self._create_fleet()
			self.ship.center_ship()
		
			#pause
			sleep(0.5)
				
		else:
			self.sb.lives.empty()
			self.play_button = Button(self, "Play again!")
			self.stats.game_active = False
			pygame.mouse.set_visible(True)
	
	def _check_aliens_bottom(self):
		"""Respond when aliens reached bottom of the screen."""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				self._ship_hit()
				break
	
	def _check_events(self):
		"""Responds to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				with open(self.stats.highscore_file, 'w') as file:
					highscore = int(self.stats.highscore)
					file.write(highscore)
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)
	
	def _check_play_button(self, mouse_pos):
		"""Start new game on play button click."""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			# Reset the game statistics.
			self.settings.initialize_dynamic_settings()
			self.stats.reset_stats()
			self.stats.game_active = True
			self.sb.prep_score()
			self.sb.prep_level()
			self.sb.prep_lives()
			
			# Get rid of the aliens and bullets.
			self.aliens.empty()
			self.bullets.empty()
			
			# Create a new fleet and center the ship.
			self._create_fleet()
			self.ship.center_ship()
			
			# Hide mouse cursor.
			pygame.mouse.set_visible(False)
			
				
	def _check_keydown_events(self, event):
		"""Responds to keydown events."""
		if event.key == pygame.K_RIGHT:
			# Move the ship to right.
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			# Move the ship to left.
			self.ship.moving_left = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_SPACE:
			if self.stats.game_active:
				self._fire_bullet()
		
		elif event.key == pygame.K_q:
			# Quit the game.
			with open(self.stats.highscore_file, 'w') as file:
				highscore = str(self.stats.highscore)
				file.write(highscore)
			sys.exit()
			
	def _check_keyup_events(self, event):
		"""Responds to keyup events."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:		
			self.ship.moving_left = False	
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False
	def _fire_bullet(self):
		"""Creates new bullet and add it to bullets group."""
		if len(self.bullets) < self.settings.bullet_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)	
			
	def _create_fleet(self):
		"""Creates a fleet of aliens."""
		# Make an alien.
		alien = Alien(self)
		
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_of_aliens_x= available_space_x // alien_width
		
		# Determine the number of rows of aliens that will fit on the screen.
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
		number_rows = available_space_y // alien_height
		
		#Create the full fleet of aliens.
		for row_number in range(number_rows):
			for alien_number in range(number_of_aliens_x):
				self._create_alien(alien_number, row_number)
			
	def _create_alien(self, alien_number, row_number):
		#Create an alien and place it in the row.
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + alien_height * row_number
		# Add alien to the group.	
		self.aliens.add(alien)
			
	def _check_fleet_edges(self):
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break
				
	def _change_fleet_direction(self):
		"""Drop entire fleet and change direction."""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.drop_speed
		self.settings.fleet_direction *= -1 
			
	def _update_screen(self):
		"""Redraw the screen in each loop."""
		self.screen.fill(self.settings.bg_color)
		self.screen.blit(self.bg,(0, 0))
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)
		
		# draw the score board.
		self.sb.show_score()
		
		
		
		#draw the play button
		if not self.stats.game_active:
			self.play_button.draw_button()
		# make the recently created screen visible.
		pygame.display.flip()
			
if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()
