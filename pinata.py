import pygame
from pygame.sprite import Sprite
from random import randint

class Pinata(Sprite):
	"""A class to represent a single pinata."""

	def __init__(self, ai_game):
		"""Initialize the pinata and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the pinata image and set its rect attribute.
		self.image = pygame.image.load('images/la_pinata.png')
		self.rect = self.image.get_rect()
		self.zoomed_image = self.image

		# Start each new pinata at the center of the screen
		self.rect.x = randint(100, self.settings.max_width_placement)
		self.rect.y = randint(100, self.settings.max_height_placement)

		# Store the pinata's exact x, and y position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		self.going_up = 1

		self.hits_required = randint(1, self.settings.MAX_HITS_REQUIRED)
		self.times_hit = 0
		self.currently_hit = False
		self.settings.release_candy = False
		self.pinata_burst = False

	def update(self, stick, collision):
		"""Move the pinata around."""
		if (stick.swinging and collision and self.settings.pinata_height < 1.2
				and not stick.stick_swung and not self.currently_hit):
			self._pinata_hit()
			self.currently_hit = True
		elif (stick.swinging and self.settings.pinata_height >= 1.5):
			self.currently_hit = False

	def blitme(self):
		"""Draw the striker at its current location."""
		if self.going_up == 1:
			self.settings.pinata_height += self.settings.pinata_zoom_factor
			if self.settings.pinata_height > self.settings.max_pinata_zoom:
				self.going_up = 0
		elif self.going_up == 0:
			self.settings.pinata_height -= self.settings.pinata_zoom_factor
			if self.settings.pinata_height < 1:
				self.going_up = 1
		self.zoomed_image = pygame.transform.rotozoom(
			self.image, 0, self.settings.pinata_height)

		self.settings.pinata_speed += .1

		if self.settings.pinata_speed > 1:
			self.x += ((-1) ** randint(0, 1) *
					randint(1, self.settings.pinata_random_motion))
			self.y += ((-1) ** randint(0, 1) *
					randint(1, self.settings.pinata_random_motion))
			self.settings.pinata_speed = 0
			self.check_bounds()


		if not self.pinata_burst:
			self.screen.blit(self.zoomed_image, self.rect)

	def _pinata_hit(self):
		self.times_hit += 1
		print(f"Hits required: {self.hits_required}")
		print(f"Times Hit: {self.times_hit}")
		if self.times_hit == self.hits_required:
			self.settings.release_candy = True
			self.pinata_burst = True
			pygame.mixer.music.stop()
		
	def check_bounds(self):
		"""This checks that the character is within the bounds of the screen."""
		if self.y <= (self.settings.max_height_placement) and self.y > 0:
			self.rect.y = self.y
		else:
			self.y = self.rect.y
		if self.x <= (self.settings.max_width_placement) and self.x > 0:
			self.rect.x = self.x
		else:
			self.x = self.rect.x