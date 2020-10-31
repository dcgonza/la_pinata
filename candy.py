import pygame
from pygame.sprite import Sprite
from random import randint

class Candy(Sprite):
	""" A class to manage candy falling from the pinata."""

	def __init__(self, ai_game):
		"""Create a candy object at the pinata's current position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.candy_color

		self.image = pygame.image.load('images/candy.png')
		self.rect = self.image.get_rect()
		
		# Create a candy rect at (0, 0) and then set a random position
# 		self.rect = pygame.Rect(0, 0, self.settings.candy_width,
# 			self.settings.candy_height)
# 		self.rect.midtop = ai_game.pinata.rect.midtop
		self.rect.x = randint(120, self.settings.max_width_placement)
		self.rect.y = randint(120, self.settings.max_height_placement)

		# Store the candy's position as a decimal value.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		self.settings.candy_x.append(self.x)
		self.settings.candy_y.append(self.y)

	def update(self):
		"""Do nothing for now"""
		if self.settings.release_candy:
			self.draw_candy()

	def draw_candy(self):
		"""Draw the candy to the screen."""
		self.screen.blit(self.image, self.rect)