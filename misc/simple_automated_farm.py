SIZE = get_world_size()

while True:
	for i in range(SIZE):

		x = get_pos_x()
		y = get_pos_y()
	
		if x == 15:
			harvest()
			if get_ground_type() == Grounds.Soil:
				till()
			plant(Entities.Grass)
		
		# 🎃 PUMPKIN
		# 9x9 = 81 tiles
		elif x < 9 and y < 9:
			harvest()

			if get_ground_type() != Grounds.Soil:
				till()

			plant(Entities.Pumpkin)

		# 🥕 CARROT
		# 4x9 = 36 tiles
		elif x < 13 and y < 9:
			harvest()

			if get_ground_type() != Grounds.Soil:
				till()

			plant(Entities.Carrot)

		# 🌳 WOOD
		# Most of the remaining area
		elif x >= 13 or y >= 9:
			harvest()

			if get_ground_type() == Grounds.Soil:
				till()

			plant(Entities.Bush)

		# 🌱 GRASS
		else:
			harvest()

			if get_ground_type() == Grounds.Soil:
				till()

			plant(Entities.Grass)

		move(North)

	move(East)