import math

def findNearestCandy(self):
	x1, y1 = self.rect.x, self.rect.y

# 	r = math.sqrt(x**2 + y**2)
# 	theta = math.atan(y/x)

	nearest_candy_x = float('inf')
	nearest_candy_y = float('inf')

	d_old = dist(nearest_candy_x, nearest_candy_y, x1, y1)

	num_points = len(self.settings.candy_x)

	for n in range(num_points):
		x2 = self.settings.candy_x[n]
		y2 = self.settings.candy_y[n]

		d_cur = dist(x1, y1, x2, y2)
 
		if d_cur < d_old and d_cur > 10:
			d_old = d_cur
			nearest_candy_x = x2
			nearest_candy_y = y2

# 	nearest_candy_r = math.sqrt( nearest_candy_x ** 2 + nearest_candy_y ** 2 )
# 	nearest_candy_theta = math.atan( nearest_candy_y / nearest_candy_x )

	if (nearest_candy_x - x1 != 0):
		nearest_theta = math.atan(
				abs((nearest_candy_y - y1) / (nearest_candy_x - x1)) )
		nearest_theta = nearest_theta * 180 / math.pi
	elif (nearest_candy_y - y1) > 0:
		nearest_theta = 90
	else:
		nearest_theta = 180

	return nearest_theta

def dist(x1, y1, x2, y2):
	return math.sqrt( (x1 - x2)**2 + (y1 - y2)**2)