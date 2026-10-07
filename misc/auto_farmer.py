plants = Entities.Sunflower

while True:
	for i in range(get_world_size()):
		harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(plants)
		move(North)
	move(East)