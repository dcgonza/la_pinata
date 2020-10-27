import pygame
from pygame.sprite import Sprite

class Stick(Sprite):
	"""A class to manage the stick that hits the pinata."""

	def __init__(self, ai_game):
		"""Create a stick at the striker's current position."""
		super(Stick).__init__()

		self.images = []

		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.stick_color

		self.images.append(pygame.image.load('images/stick01.png'))
		self.images.append(pygame.image.load('images/stick01.png'))
		self.images.append(pygame.image.load('images/stick01.png'))
		self.images.append(pygame.image.load('images/stick01.png'))
		self.images.append(pygame.image.load('images/stick01.png'))
		self.images.append(pygame.image.load('images/stick01.png'))
		self.images.append(pygame.image.load('images/stick02.png'))
		self.images.append(pygame.image.load('images/stick02.png'))
		self.images.append(pygame.image.load('images/stick02.png'))
		self.images.append(pygame.image.load('images/stick02.png'))
		self.images.append(pygame.image.load('images/stick02.png'))
		self.images.append(pygame.image.load('images/stick03.png'))
		self.images.append(pygame.image.load('images/stick03.png'))
		self.images.append(pygame.image.load('images/stick03.png'))
		self.images.append(pygame.image.load('images/stick03.png'))
		self.images.append(pygame.image.load('images/stick03.png'))
		self.images.append(pygame.image.load('images/stick03.png'))
		self.images.append(pygame.image.load('images/stick04.png'))
		self.images.append(pygame.image.load('images/stick04.png'))
		self.images.append(pygame.image.load('images/stick04.png'))
		self.images.append(pygame.image.load('images/stick04.png'))
		self.images.append(pygame.image.load('images/stick04.png'))
		self.images.append(pygame.image.load('images/stick05.png'))
		self.images.append(pygame.image.load('images/stick05.png'))
		self.images.append(pygame.image.load('images/stick05.png'))
		self.images.append(pygame.image.load('images/stick05.png'))
		self.images.append(pygame.image.load('images/stick05.png'))
		self.images.append(pygame.image.load('images/stick05.png'))
		self.images.append(pygame.image.load('images/stick06.png'))
		self.images.append(pygame.image.load('images/stick06.png'))
		self.images.append(pygame.image.load('images/stick06.png'))
		self.images.append(pygame.image.load('images/stick06.png'))
		self.images.append(pygame.image.load('images/stick06.png'))
		self.images.append(pygame.image.load('images/stick07.png'))
		self.images.append(pygame.image.load('images/stick07.png'))
		self.images.append(pygame.image.load('images/stick07.png'))
		self.images.append(pygame.image.load('images/stick07.png'))
		self.images.append(pygame.image.load('images/stick07.png'))
		self.images.append(pygame.image.load('images/stick08.png'))
		self.images.append(pygame.image.load('images/stick08.png'))
		self.images.append(pygame.image.load('images/stick08.png'))
		self.images.append(pygame.image.load('images/stick08.png'))
		self.images.append(pygame.image.load('images/stick08.png'))
		self.images.append(pygame.image.load('images/stick08.png'))
		self.images.append(pygame.image.load('images/stick09.png'))
		self.images.append(pygame.image.load('images/stick09.png'))
		self.images.append(pygame.image.load('images/stick09.png'))
		self.images.append(pygame.image.load('images/stick09.png'))
		self.images.append(pygame.image.load('images/stick09.png'))
		self.images.append(pygame.image.load('images/stick10.png'))
		self.images.append(pygame.image.load('images/stick10.png'))
		self.images.append(pygame.image.load('images/stick10.png'))
		self.images.append(pygame.image.load('images/stick10.png'))
		self.images.append(pygame.image.load('images/stick10.png'))
		self.images.append(pygame.image.load('images/stick10.png'))
		self.images.append(pygame.image.load('images/stick11.png'))
		self.images.append(pygame.image.load('images/stick11.png'))
		self.images.append(pygame.image.load('images/stick11.png'))
		self.images.append(pygame.image.load('images/stick11.png'))
		self.images.append(pygame.image.load('images/stick11.png'))
		self.images.append(pygame.image.load('images/stick12.png'))
		self.images.append(pygame.image.load('images/stick12.png'))
		self.images.append(pygame.image.load('images/stick12.png'))
		self.images.append(pygame.image.load('images/stick12.png'))
		self.images.append(pygame.image.load('images/stick12.png'))
		self.images.append(pygame.image.load('images/stick13.png'))
		self.images.append(pygame.image.load('images/stick13.png'))
		self.images.append(pygame.image.load('images/stick13.png'))
		self.images.append(pygame.image.load('images/stick13.png'))
		self.images.append(pygame.image.load('images/stick13.png'))
		self.images.append(pygame.image.load('images/stick13.png'))
		self.images.append(pygame.image.load('images/stick14.png'))
		self.images.append(pygame.image.load('images/stick14.png'))
		self.images.append(pygame.image.load('images/stick14.png'))
		self.images.append(pygame.image.load('images/stick14.png'))
		self.images.append(pygame.image.load('images/stick14.png'))
		self.images.append(pygame.image.load('images/stick14.png'))
		self.images.append(pygame.image.load('images/stick15.png'))
		self.images.append(pygame.image.load('images/stick15.png'))
		self.images.append(pygame.image.load('images/stick15.png'))
		self.images.append(pygame.image.load('images/stick15.png'))
		self.images.append(pygame.image.load('images/stick15.png'))
		self.images.append(pygame.image.load('images/stick15.png'))
		self.images.append(pygame.image.load('images/stick16.png'))
		self.images.append(pygame.image.load('images/stick16.png'))
		self.images.append(pygame.image.load('images/stick16.png'))
		self.images.append(pygame.image.load('images/stick16.png'))
		self.images.append(pygame.image.load('images/stick16.png'))
		self.images.append(pygame.image.load('images/stick16.png'))
		self.images.append(pygame.image.load('images/stick17.png'))
		self.images.append(pygame.image.load('images/stick17.png'))
		self.images.append(pygame.image.load('images/stick17.png'))
		self.images.append(pygame.image.load('images/stick17.png'))
		self.images.append(pygame.image.load('images/stick17.png'))
		self.images.append(pygame.image.load('images/stick17.png'))
		self.images.append(pygame.image.load('images/stick18.png'))
		self.images.append(pygame.image.load('images/stick18.png'))
		self.images.append(pygame.image.load('images/stick18.png'))
		self.images.append(pygame.image.load('images/stick18.png'))
		self.images.append(pygame.image.load('images/stick18.png'))
		self.images.append(pygame.image.load('images/stick18.png'))
		self.images.append(pygame.image.load('images/stick19.png'))
		self.images.append(pygame.image.load('images/stick19.png'))
		self.images.append(pygame.image.load('images/stick19.png'))
		self.images.append(pygame.image.load('images/stick19.png'))
		self.images.append(pygame.image.load('images/stick19.png'))
		self.images.append(pygame.image.load('images/stick19.png'))
		self.images.append(pygame.image.load('images/stick20.png'))
		self.images.append(pygame.image.load('images/stick20.png'))
		self.images.append(pygame.image.load('images/stick20.png'))
		self.images.append(pygame.image.load('images/stick20.png'))
		self.images.append(pygame.image.load('images/stick20.png'))
		self.images.append(pygame.image.load('images/stick20.png'))
		self.images.append(pygame.image.load('images/stick21.png'))
		self.images.append(pygame.image.load('images/stick21.png'))
		self.images.append(pygame.image.load('images/stick21.png'))
		self.images.append(pygame.image.load('images/stick21.png'))
		self.images.append(pygame.image.load('images/stick21.png'))
		self.images.append(pygame.image.load('images/stick21.png'))
		self.images.append(pygame.image.load('images/stick22.png'))
		self.images.append(pygame.image.load('images/stick22.png'))
		self.images.append(pygame.image.load('images/stick22.png'))
		self.images.append(pygame.image.load('images/stick22.png'))
		self.images.append(pygame.image.load('images/stick22.png'))
		self.images.append(pygame.image.load('images/stick22.png'))
		self.images.append(pygame.image.load('images/stick23.png'))
		self.images.append(pygame.image.load('images/stick23.png'))
		self.images.append(pygame.image.load('images/stick23.png'))
		self.images.append(pygame.image.load('images/stick23.png'))
		self.images.append(pygame.image.load('images/stick23.png'))
		self.images.append(pygame.image.load('images/stick24.png'))
		self.images.append(pygame.image.load('images/stick24.png'))
		self.images.append(pygame.image.load('images/stick24.png'))
		self.images.append(pygame.image.load('images/stick24.png'))
		self.images.append(pygame.image.load('images/stick24.png'))

		self.index = 0
		self.image = self.images[self.index]
#  		self.image = pygame.image.load('images/stick.png')
		self.rotated_image = self.image
		self.rect = self.image.get_rect()
		self.rect.center = ai_game.striker.rect.center

		self.settings.stick_x = self.rect.x
		self.settings.stick_y = self.rect.y
		self.w, self.h = self.image.get_size()
# 		self.settings.stick_x = ai_game.striker.rect.x + ai_game.striker.w // 4
# 		self.settings.stick_y = ai_game.striker.rect.y + ai_game.striker.h // 4
		self.striker_w = ai_game.striker.w

		# Store the stick's position as a decimal value
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.swinging = False
		self.stick_swung = False
# 		self.clock = pygame.time.Clock()

	def update(self):
		if self.swinging:
			self.index += 1

			if self.index >= len(self.images):
				self.index = 0
				self.stick_swung = True
	
			self.rotated_image = self.images[self.index]

		if self.stick_swung:
			self.stick_swung = False
			self.swinging = False

	def blitme(self):
		"""Draw the stick at its current location."""
		self.rect.x = self.settings.stick_x
		self.rect.y = self.settings.stick_y

		self.blitRotate()

		self.screen.blit(self.rotated_image, self.rect)

#	def blitRotate(self, surf, image, pos, originPos, angle, ccw_or_cw):
	def blitRotate(self):
	    # calcaulate the axis aligned bounding box of the rotated image

		w, h       = self.w, self.h
		originPos  = (w//2, h//2)
		pos        = (self.rect.x//2, self.rect.y//2)
# 		pos        = (self.settings.screen_width//2, 
# 				self.settings.screen_height//2)
		angle      = self.settings.stick_theta # self.cur_theta * ccw_or_cw
		box        = [pygame.math.Vector2(p) for p in [(0, 0),
				(w, 0), (w, -h), (0, -h)]]
		box_rotate = [p.rotate(angle) for p in box]
		min_box    = (min(box_rotate, key=lambda p: p[0])[0],
				min(box_rotate, key=lambda p: p[1])[1])
		max_box    = (max(box_rotate, key=lambda p: p[0])[0],
				max(box_rotate, key=lambda p: p[1])[1])

		# calculate the translation of the pivot 
		pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
		pivot_rotate = pivot.rotate(angle)
		pivot_move   = pivot_rotate - pivot

		# calculate the upper left origin of the rotated image
		self.origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0],
				pos[1] - originPos[1] - max_box[1] + pivot_move[1])

		# get a rotated image
		self.rotated_image = pygame.transform.rotate(self.images[self.index], angle)
		self.w, self.h = self.rotated_image.get_size()
# 		temp_rect =  self.rotated_image.get_rect()
# 		self.rect.x, self.rect.y = (temp_rect.x, temp_rect.y)
		
		# rotate and blit the image
# 		self.screen.blit(self.image, origin)