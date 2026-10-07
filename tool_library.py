SIZE = get_world_size()

def clear_land():
	
	while True:
		#reset position
		reset_pos()
			
		# Till all and harvest
		harvested = 0
		for x in range(SIZE):
			for y in range(SIZE):
				harvest()
				if get_ground_type() == Grounds.Grassland:
					till()
				harvested += 1
				move(North)
			move(East)
		
		if harvested == SIZE * SIZE:
			break

def harvest_all():
	while True:
		#reset position
		reset_pos()
		
		clear = True
		
		for x in range(SIZE):
			for y in range(SIZE):
				if can_harvest():
					harvest()
					if get_ground_type() != Grounds.Soil:
						till()
				move(North)
			move(East)
		
		if clear:
			print('Done')
			break
			
def reset_pos():
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)