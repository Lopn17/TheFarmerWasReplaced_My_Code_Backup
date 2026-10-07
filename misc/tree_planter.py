while True:
	for i in range(get_world_size()):
		x = get_pos_x()
		if x % 2 == 0:
			if i % 2 == 0:
				harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Tree)
				move(North)
			else:
				move(North)
		elif x % 2 == 1:
			if i % 2 == 1:
				harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Tree)
				move(North)
			else:
				move(North)
	move(East)
	
	