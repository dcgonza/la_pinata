import pygame
from pygame.sprite import Sprite
import math
from blitRotate import blitRotate

class Striker(Sprite):
	"""A class to manage the pinata striker."""

	def __init__(self, ai_game):
		"""Initialize the striker and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the striker image and its rect.
		self.image = pygame.image.load('images/striker_small.png')
		self.rotated_image = self.image
		self.rect = self.image.get_rect()
		self.w, self.h = self.image.get_size()
# 		self.origin = (self.settings.screen_width // 2, 
# 				self.settings.screen_height // 2)
# 		
		# Start each new striker at the center of the screen.
		self.rect.center = self.screen_rect.center

		# Store a decimal value for the striker's horizontal
		#	and vertical position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Movement flags
		self.rotating_cw   = False
		self.rotating_ccw  = False
		self.moving_fwd    = False
		self.moving_bwd    = False
		self.collect_candy = False

	def update(self):
		"""Update the striker's position based on the movement flags."""
		# Update the ship's value, not the rect.
		if self.rotating_cw:
			self.settings.striker_theta -= self.settings.rotation_value
			blitRotate(self)
			self.settings.striker_theta = self.settings.striker_theta % 360
		if self.rotating_ccw:
			self.settings.striker_theta += self.settings.rotation_value
			blitRotate(self)
			self.settings.striker_theta = self.settings.striker_theta % 360
		if self.moving_fwd:
			self.y -= math.cos(self.settings.striker_theta * math.pi / 180)
			self.x -= math.sin(self.settings.striker_theta * math.pi / 180)
			self.check_bounds()
		if self.moving_bwd:
			self.y += math.cos(self.settings.striker_theta * math.pi / 180)
			self.x += math.sin(self.settings.striker_theta * math.pi / 180)
			self.check_bounds()

	def blitme(self):
		"""Draw the striker at its current location."""
		self.settings.striker_x = self.rect.x
		self.settings.striker_y = self.rect.y
		self.settings.stick_x = self.rect.x
		self.settings.stick_y = self.rect.y
		self.settings.stick_theta = self.settings.striker_theta

		self.screen.blit(self.rotated_image, self.rect)

	def check_bounds(self):
		"""This checks that the character is within the bounds of the screen."""
		if self.y <= (self.settings.screen_height - 2*self.h) and self.y > 0:
			self.rect.y = self.y
		if self.x <= (self.settings.screen_width - self.w) and self.x > 0:
			self.rect.x = self.x
