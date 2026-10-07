plants1 = Entities.Carrot
plants2 = Entities.Grass

while True:
	for i in range(get_world_size()):
		x = get_pos_x()
		if x > 11:
			harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(plants2)
			move(North)
		else:
			harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(plants1)
			move(North)
	move(East)