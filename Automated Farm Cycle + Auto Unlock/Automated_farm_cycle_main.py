from tool_library import reset_pos

# farm settings
state = 0
cycle = 5

first_cycle_reps = 0
sec_cycle_reps = 0
third_cycle_reps = 0
fourth_cycle_reps = 0
fifth_cycle_reps = 0

first_cycle = 3
second_cycle = 10
third_cycle = 10
fourth_cycle = 2
fifth_cycle = 1

# Entities
Bush = Entities.Bush
Carrot = Entities.Carrot
Grass = Entities.Grass
Pumpkin = Entities.Pumpkin
Sunflower = Entities.Sunflower
Cactus = Entities.Cactus
Trees = Entities.Tree

# Cycle information
cycle_info = {
	'cycle_1': 'Grass & Trees',
	'cycle_2': 'Carrot',
	'cycle_3': 'Pumpkin',
	'cycle_4': 'Sunflower',
	'cycle_5': 'Cactus'
}

# Grounds
Soil = Grounds.Soil
Grassland = Grounds.Grassland


reset_pos()

while True:
	
	#Auto unlock
		# Pumpkin Cost
	if unlock(Unlocks.Expand):
		unlock(Unlocks.Expand)
		print('')
		quick_print('----- The Expand Upgraded -----')
	if unlock(Unlocks.Cactus):
		unlock(Unlocks.Cactus)
		print('')
		quick_print('----- The Cactus Upgraded -----')
		#Cactus Cost	
	if unlock(Unlocks.Dinosaurs):
		unlock(Unlocks.Dinosaurs)
		print('')
		quick_print('----- The Dinosaurs Upgraded -----')
		# Wood Cost
	if unlock(Unlocks.Grass):
		unlock(Unlocks.Grass)
		print('')
		quick_print('----- The Grass Upgraded -----')
	if unlock(Unlocks.Carrots):
		unlock(Unlocks.Carrots)
		print('')
		quick_print('----- The Carrots Upgraded -----')
		# Hay Cost
	if unlock(Unlocks.Trees):
		unlock(Unlocks.Trees)
		print('')
		quick_print('----- The Tree Upgraded -----')
		# Carrot Cost
	if unlock(Unlocks.Pumpkins):
		unlock(Unlocks.Pumpkins)
		print('')
		quick_print('----- The Pumpkin Upgraded -----')
		
	first_cycle_reps = 0
	sec_cycle_reps = 0
	third_cycle_reps = 0
	fourth_cycle_reps = 0
	fifth_cycle_reps = 0
	SIZE = get_world_size()
	GRASS_AREA = SIZE * 0.3

	# =========================
	# First cycle = Trees & Grass
	# =========================
	if state % cycle == 0:

		quick_print('')
		quick_print('===== Cycle', state + 1, '=====')
		quick_print('Plant:', cycle_info['cycle_1'])
		quick_print('Current State:', state)
		quick_print('===================')

		while first_cycle_reps < first_cycle:

			for j in range(SIZE):
				x = get_pos_x()

				harvest()

				if x % 2 == 1:
					if j % 2 == 1:
						plant(Trees)
					else:
						plant(Grass)
				elif x % 2 == 0:
					if j % 2 == 0:
						plant(Trees)
					else:
						plant(Grass)

				move(North)

				if get_pos_x() == SIZE - 1 and get_pos_y() == SIZE - 1:
					first_cycle_reps += 1

					quick_print(
						'Cycle', state + 1, ':',
						first_cycle_reps,
						'reps done out of',
						first_cycle
					)

			move(East)

		state += 1

		quick_print('Cycle', state, 'done')
		quick_print('New State:', state, '| Cycle', state + 1, 'Starts')


	# =========================
	# Second cycle = Carrot
	# =========================
	elif state % cycle == 1:

		quick_print('')
		quick_print('===== Cycle', state + 1, '=====')
		quick_print('Plant:', cycle_info['cycle_2'])
		quick_print('Current State:', state)
		quick_print('===================')

		while sec_cycle_reps < second_cycle:

			for j in range(SIZE):

				harvest()

				if get_ground_type() != Soil:
					till()

				plant(Carrot)

				move(North)

				if get_pos_x() == SIZE - 1 and get_pos_y() == SIZE - 1:
					sec_cycle_reps += 1

					quick_print(
						'Cycle', state + 1, ':',
						sec_cycle_reps,
						'reps done out of',
						second_cycle
					)

			move(East)

		state += 1

		quick_print('Cycle', state, 'done')
		quick_print('New State:', state, '| Cycle', state + 1, 'Starts')


	# =========================
	# Third cycle = Pumpkin
	# =========================
	elif state % cycle == 2:

		quick_print('')
		quick_print('===== Cycle', state + 1, '=====')
		quick_print('Plant:', cycle_info['cycle_3'])
		quick_print('Current State:', state)
		quick_print('===================')

		while third_cycle_reps < third_cycle:

			for j in range(SIZE):

				harvest()

				if get_ground_type() != Soil:
					till()

				plant(Pumpkin)

				move(North)

				if get_pos_x() == SIZE - 1 and get_pos_y() == SIZE - 1:
					third_cycle_reps += 1

					quick_print(
						'Cycle', state + 1, ':',
						third_cycle_reps,
						'reps done out of',
						third_cycle
					)

			move(East)

		state += 1

		quick_print('Cycle', state, 'done')
		quick_print('New State:', state, '| Cycle', state + 1, 'Starts')


	# =========================
	# Fourth cycle = Sunflower
	# =========================
	elif state % cycle == 3:

		quick_print('')
		quick_print('===== Cycle', state + 1, '=====')
		quick_print('Plant:', cycle_info['cycle_4'])
		quick_print('Current State:', state)
		quick_print('===================')

		while fourth_cycle_reps < fourth_cycle:

			for j in range(SIZE):

				harvest()

				if get_ground_type() != Soil:
					till()

				plant(Sunflower)

				move(North)

				if get_pos_x() == SIZE - 1 and get_pos_y() == SIZE - 1:
					fourth_cycle_reps += 1

					quick_print(
						'Cycle', state + 1, ':',
						fourth_cycle_reps,
						'reps done out of',
						fourth_cycle
					)

			move(East)

		state += 1

		quick_print('Cycle', state, 'done')
		quick_print('New State:', state, '| Cycle', state + 1, 'Starts')


	# =========================
	# Fifth cycle = Cactus
	# =========================
	elif state % cycle == 4:

		quick_print('')
		quick_print('===== Cycle', state + 1, '=====')
		quick_print('Plant:', cycle_info['cycle_5'])
		quick_print('Current State:', state)
		quick_print('===================')

		while fifth_cycle_reps < fifth_cycle:

			for j in range(SIZE):

				harvest()

				if get_ground_type() != Soil:
					till()

				plant(Cactus)

				move(North)

				if get_pos_x() == SIZE - 1 and get_pos_y() == SIZE - 1:
					fifth_cycle_reps += 1

					quick_print(
						'Cycle', state + 1, ':',
						fifth_cycle_reps,
						'reps done out of',
						fifth_cycle
					)

			move(East)

		state += 1

		quick_print('Cycle', state, 'done')
		quick_print('New State:', state, '| Cycle', state + 1, 'Starts')

