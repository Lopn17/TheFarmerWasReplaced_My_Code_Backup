from tool_library import reset_pos

reset_pos()

while True:
	for x in range(get_world_size()):
		harvest()
		if get_ground_type() != Grounds.Grassland:
			till()
		move(North)
	move(East)