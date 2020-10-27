class Settings:
	"""A class to store all settings for La Pinata."""

	def __init__(self):
		"""Initialize the game's static settings."""
		# Screen settings
		self.screen_width  = 1200
		self.screen_height = 800
		self.bg_color = (255, 255, 255)
		self.max_height_placement = self.screen_height - 100
		self.max_width_placement = self.screen_width - 100

		# Pinata settings
		self.max_pinata_zoom = 2
		self.pinata_zoom_factor = 0.001
		self.pinata_random_motion = 20

		# Candy settings
		self.candy_width = 2
		self.candy_height = 5
		self.candy_color = (255, 255, 0)

		# Striker settings
		self.striker_limit = 6
		self.striker_theta = 0

		# Stick settings
		self.stick_width = 50
		self.stick_height = 5
		self.stick_color = (139, 69, 19)

		# How quickly the game speeds up
		self.speedup_scale = 1.5

		# How quickly the candy point values increase
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.striker_speed = 1.5
		self.swing_speed   = 1.0
		self.pinata_speed  = 0.1
		self.candy_speed   = 0.5
		self.candy_radius  = 20.0
		self.candy_direction = 0

		self.num_kids = 5

		# Striker settings
		self.rotation_value = 2.0
		self.striker_x = self.screen_width // 2
		self.striker_y = self.screen_height // 2

		# pinata_vert of 1 represents the pinata is being raised;
		#	-1 being lowered
		self.pinata_height = 1
		self.MAX_HITS_REQUIRED = 4

		# Stick settings
		self.stick_x = self.screen_width // 2
		self.stick_y = self.screen_height // 2
		self.stick_theta = 0

		# Candy settings
		self.max_num_candies = 10
		self.release_candy = False
# 		self.candy_locations_x = []
# 		self.candy_locations_y = []

		# Scoring
		self.candy_points = 50

	def increase_difficulty(self):
		"""Increase the speed settings and candy point valies."""
		self.striker_speed *= self.speedup_scale
		self.swing_speed   *= self.speedup_scale
# 		self.pinata_speed  *= self.speedup_scale
		self.candy_speed   *= self.speedup_scale

		self.pinata_zoom_factor *= self.speedup_scale

# 		self.rotation_value *= self.speedup_scale

		self.candy_points = int(self.candy_points * self.score_scale)
		self.num_kids = int(self.num_kids * self.speedup_scale)
		self.max_num_candies = int(self.max_num_candies * self.speedup_scale)