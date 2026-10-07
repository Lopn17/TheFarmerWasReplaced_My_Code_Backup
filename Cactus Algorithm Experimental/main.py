from tool_library import reset_pos

SIZE = 4

def clear_land():
	# <<<^
	# v<^^
	# v>>^
	# >>>>
	pass

def clear_land_temp():
	
	reset_pos()
	
	pairs = SIZE // 2
	
	for x in range(pairs):
		for y in range(SIZE):
			harvest()
			if get_pos_x() < SIZE and get_pos_y() < SIZE:
				if get_ground_type() != Grounds.Grassland: 
					till()
			if y < SIZE-1:
				move(North)
		if get_pos_x() < SIZE-1:
			move(East)
			for y in range(SIZE):
				harvest()
				if get_pos_x() < SIZE and get_pos_y() < SIZE:
					if get_ground_type() != Grounds.Grassland: 
						till()
				if get_pos_y() > 0:
					move(South)
				elif get_pos_y() == 0 and get_pos_x() < SIZE:
					move(East)
	if SIZE % 2 == 1:
		for y in range(SIZE):
			harvest()
			if get_pos_x() < SIZE and get_pos_y() < SIZE:
				if get_ground_type() != Grounds.Grassland: 
					till()
			move(North)

	reset_pos()

def plant_cactus():
	
	reset_pos()
	
	for x in range(SIZE):
		for y in range(SIZE):
			harvest()
			if get_pos_x() < SIZE and get_pos_y() < SIZE:
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Cactus)
				
			if y < SIZE - 1:
				move(North)
		if x < SIZE - 1:
			move(East)
			for y in range(SIZE-1):
				move(South)
	reset_pos()


def plant_cactus2():
	
	reset_pos()
	
	pairs = SIZE // 2
	
	for x in range(pairs):
		for y in range(SIZE):
			harvest()
			if get_pos_x() < SIZE and get_pos_y() < SIZE:
				if get_ground_type() == Grounds.Grassland: 
					till()
				plant(Entities.Cactus)
			if y < SIZE-1:
				move(North)
		if get_pos_x() < SIZE-1:
			move(East)
			for y in range(SIZE):
				harvest()
				if get_pos_x() < SIZE and get_pos_y() < SIZE:
					if get_ground_type() == Grounds.Grassland: 
						till()
					plant(Entities.Cactus)
				if get_pos_y() > 0:
					move(South)
				elif get_pos_y() == 0 and get_pos_x() < SIZE:
					move(East)
	if SIZE % 2 == 1:
		for y in range(SIZE):
			harvest()
			if get_pos_x() < SIZE and get_pos_y() < SIZE:
				if get_ground_type() == Grounds.Grassland: 
					till()
			plant(Entities.Cactus)
			move(North)
	
	reset_pos()

#clear_land_temp()
#plant_cactus() # 23.16 , 48.75
#plant_cactus2() # 14.51 , 52.19
	
			
			
	
	
		
		