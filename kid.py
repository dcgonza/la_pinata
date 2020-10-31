import pygame
import math
from random import randint

from pygame.sprite import Sprite
from blitRotate import blitRotate
from findNearestCandy import findNearestCandy

class Kid(Sprite):
	"""A class to represent a single kid in the gang."""

	def __init__(self, ai_game):
		"""Initialize the kid and set its starting position."""
		super().__init__()

		self.images = []

		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the alien image and set its rect attribute.
#		self.image = pygame.image.load('images/kid.png')

		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_07.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_06.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_05.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_04.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_01.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_02.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))
		self.images.append(pygame.image.load('images/kid_03.png'))

		self.index = 0

		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rotated_image = self.image

		# Start each new kid near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the kid's exact horizontal and vertical position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.theta = 0
		self.w, self.h = self.image.get_size()

		self.random_placement()

	def update(self):
		"""Update the striker's position based on the movement flags."""
		# Update the ship's value, not the rect.
		if (self.settings.release_candy):
			self.theta = findNearestCandy(self)
			self.y -= math.cos(self.theta * math.pi / 180)
			self.x -= math.sin(self.theta * math.pi / 180)
			self.index += 1
			if self.index >= len(self.images):
				self.index = 0
			self.image = self.images[self.index]
			self.rotated_image = self.image
			blitRotate(self)
			self.check_bounds()

	def blitme(self):
		"""Draw the striker at its current location."""
		self.screen.blit(self.rotated_image, self.rect)

	def check_bounds(self):
		"""This checks that the character is within the bounds of the screen."""
		if self.y <= (self.settings.screen_height - self.h) and self.y > 0:
			self.rect.y = self.y
		if self.x <= (self.settings.screen_width - self.w) and self.x > 0:
			self.rect.x = self.x

		self.y = self.rect.y
		self.x = self.rect.x

	def random_placement(self):
		"""Initially place the kid at some random location"""
		self.rect.x = randint(100, self.settings.max_width_placement)
		self.rect.y = randint(100, self.settings.max_height_placement)
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)