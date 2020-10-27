import pygame

def blitRotate(self):

    # calcaulate the axis aligned bounding box of the rotated image
	w, h       = self.w, self.h
	originPos  = (w//2, h//2)
	pos        = (self.rect.x//2, self.rect.y//2)
	angle      = self.settings.striker_theta

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

	# get a rotated image
	self.rotated_image = pygame.transform.rotate(self.image, angle)
	self.w, self.h = self.rotated_image.get_size()