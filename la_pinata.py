import sys
from time import sleep
from random import randint

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from striker import Striker
from stick import Stick
from pinata import Pinata
from kid import Kid
from candy import Candy

class LaPinata:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and create game resources."""
		self.filename = 'txt_files/high_score.txt'
		self.song_fn  = 'audio/la_pinata_song.wav'
		self.candy_fn = 'audio/candy_wrapper.wav'
		self.cry_fn   = 'audio/cry_baby.wav'

		pygame.init()

		self.SONG_END = pygame.USEREVENT + 1

		pygame.mixer.music.set_endevent(self.SONG_END)
		pygame.mixer.music.load(self.song_fn)
		pygame.mixer.music.play(-1)

		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width,
				self.settings.screen_height)) #(0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("La Piñata")

		# Create an instance to store game statistics,
		#	and create a scoreboard.
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)

		self.striker = Striker(self)
		self.pinata = Pinata(self)
		self.kids = pygame.sprite.Group()
		self.candies = pygame.sprite.Group()
		self.stick = Stick(self)

		self.load_high_score()

		# Create a gang of kids
		self._create_gang()

		# Create bunch of candies
		self._create_candies()

		# Make the play button.
		self.play_button = Button(self, "Play")

	def load_high_score(self):
		"""Load the highest score saved if there is one."""
		high_score = 0

		try:
			with open(self.filename, encoding='utf-8') as f:
				contents = f.read()
		except FileNotFoundError:
			with open(self.filename, 'w') as f:
				f.write(str(high_score))
			pass
		else:
			if not contents == '':
				self.stats.score = int(contents)
				self.sb.prep_score()
				self.sb.check_high_score()
				self.stats.score = 0
				self.sb.prep_score()

	def _quit_game(self):
# 		filename = 'txt_files/high_score.txt'

		with open(self.filename, 'w') as f:
			f.write(str(self.sb.stats.high_score))
		sys.exit()

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()

			if self.stats.game_active and not self.stick.swinging:
				self.striker.update()
				self.stick.update()
				self._update_candies()
				self._update_gang()
			elif self.stats.game_active and self.stick.swinging:
				self.stick.update()
				stick_pinata_collide = pygame.sprite.collide_rect(
						self.pinata, self.stick)
				self.pinata.update(self.stick, stick_pinata_collide)

			if not self.candies:
				self.kids.empty()
				self._create_gang()
				self._create_candies()

				self.pinata = Pinata(self)
				self.pinata.burst = False
				self.settings.release_candy = False

				self.settings.increase_difficulty()
				self.stats.level += 1
				self.sb.prep_level()
				pygame.mixer.music.set_endevent(self.SONG_END)
				pygame.mixer.music.load(self.song_fn)
				pygame.mixer.music.play()

			self._update_screen()

	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self._quit_game()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == self.SONG_END and self.stats.game_active and not self.settings.release_candy:
				self._striker_hit()

	def _check_play_button(self, mouse_pos):
		"""Start a new game when the player clicks Play."""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			# Reset the game
			self._start_game()

	def _check_keydown_events(self, event):
		"""Respond to keypresses."""
		if event.key == pygame.K_q:
			self._quit_game()
		elif event.key == pygame.K_UP:
			self.striker.moving_fwd = True
		elif event.key == pygame.K_DOWN:
			self.striker.moving_bwd = True
		elif event.key == pygame.K_LEFT:
			self.striker.rotating_ccw = True
		elif event.key == pygame.K_RIGHT:
			self.striker.rotating_cw = True
		elif event.key == pygame.K_SPACE and not self.stick.swinging:
			self.stick.swinging = True
		elif event.key == pygame.K_c:
			self.striker.collect_candy = True
			self._check_for_candy()
		elif event.key == pygame.K_p:
			if not self.stats.game_active:
				# Reset the game
				self._start_game()

	def _start_game(self):
		"""Start the game and initialize everything."""
		self.settings.initialize_dynamic_settings()

		# Reset the game statistics
		self.stats.reset_stats()
		self.stats.game_active = True
		self.sb.prep_score()
		self.sb.prep_level()
		self.sb.prep_strikers()

		# Get rid of any remaining kids and candy.
# 		self.kids.empty()
# 		self.candies.empty()

		# Hide the mouse cursor.
		pygame.mouse.set_visible(False)

		pygame.mixer.music.set_endevent(self.SONG_END)
		pygame.mixer.music.load(self.song_fn)
		pygame.mixer.music.play()			

	def _check_keyup_events(self, event):
		"""Respond to key releases."""
		if event.key == pygame.K_UP:
			self.striker.moving_fwd = False
		elif event.key == pygame.K_DOWN:
			self.striker.moving_bwd = False
		elif event.key == pygame.K_RIGHT:
			self.striker.rotating_cw = False
		elif event.key == pygame.K_LEFT:
			self.striker.rotating_ccw = False
		elif event.key == pygame.K_SPACE:
			self.stick.swinging = False

	def _create_gang(self):
		""" Create the gang of kids."""
		kid = Kid(self)

		for kid_index in range(randint(1, self.settings.num_kids)):
			kid = Kid(self)
			self.kids.add(kid)

	def _create_candies(self):
		""" Create the gang of kids."""
		candy = Candy(self)
		candy_width, candy_height = candy.rect.size

		for candy_index in range(self.settings.max_num_candies):
			self._create_candy()

	def _create_candy(self):
		"""Create a kid and place it in the frame."""
		candy = Candy(self)
		candy_width, candy_height = candy.rect.size
		self.candies.add(candy)

	def _update_gang(self):
		"""Update position of kids."""
# 		self._check_for_candy()
		self.kids.update()

		# Look for striker-kid collisions.
#		if pygame.sprite.spritecollideany(self.striker, self.kids):
		for kid in self.kids.sprites():
			if pygame.sprite.collide_rect(self.striker, kid):
				if self.stats.game_active:
					self.kids.remove(kid)
					self._striker_hit()
				else:
					self.kids.remove(kid)

		# Look for kids collecting candy.
		self._check_kids_candy()

	def _check_for_candy(self):
		for candy in self.candies.sprites():
			if (pygame.sprite.collide_rect(self.striker, candy)
					and self.striker.collect_candy and
					self.settings.release_candy):
				pygame.mixer.music.load(self.candy_fn)
				pygame.mixer.music.play(0)

				self.candies.remove(candy)
				self.stats.score += self.settings.candy_points
				self.sb.prep_score()
				self.sb.check_high_score()

	def _update_candies(self):
		for candy in self.candies:
			candy.update()

	def _striker_hit(self):
		pygame.mixer.music.load(self.cry_fn)
		pygame.mixer.music.play(0)

		if self.stats.strikers_left > 0:
			self.stats.strikers_left -= 1
			self.sb.prep_strikers()
			self.striker.rect.x = self.settings.screen_width // 2
			self.striker.rect.y = self.settings.screen_height // 2
			self.striker.x = float(self.striker.rect.x)
			self.striker.y = float(self.striker.rect.y)
			sleep(0.5)
			if not self.settings.release_candy:
				pygame.mixer.music.set_endevent(self.SONG_END)
				pygame.mixer.music.load(self.song_fn)
				pygame.mixer.music.play()
		else:
			self.striker.kill()
			self.stats.game_active = False
			pygame.mouse.set_visible(True)

	def _check_kids_candy(self):
		for candy in self.candies:
			if (pygame.sprite.spritecollideany(candy, self.kids)
					and self.settings.release_candy):
				pygame.mixer.music.load(self.candy_fn)
				pygame.mixer.music.play(0)

				self.candies.remove(candy)
				self.stats.score -= self.settings.candy_points
				self.sb.prep_score()
				self.sb.check_high_score()

# 	def _kids_collect_candy():
# 		if self.stats.candy_left > 0:
# 			# Decrement candy left, and update

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		
		self.screen.fill(self.settings.bg_color)
		for candy in self.candies.sprites():
			candy.update()

		self.striker.blitme()
		for kid in self.kids.sprites():
			kid.blitme()
# 		self.kids.draw(self.screen)
		self.stick.blitme()
		if not self.pinata.pinata_burst:
			self.pinata.blitme()
		else:
			self.pinata.kill()
		# Draw the score information.
		self.sb.show_score()

		# Draw the play button if the game is inactive.
		if not self.stats.game_active:
			self.play_button.draw_button()

		pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance, and run the game.
	ai = LaPinata()
	ai.run_game()
		
