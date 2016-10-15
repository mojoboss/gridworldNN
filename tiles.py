import numpy as np

def rand_pair(s, e):
	return np.random.randint(s, e), np.random.randint(s, e)

#grid 0 for player, 1 for wall, 2 for pit, 3 for goal
def init_grid():
	state = np.zeros((4, 4, 4))
	#players position
	state[0, 0] = np.array([0, 0, 0, 1])
	#wall
	state[1, 1] = np.array([0, 0, 1, 0])
	#pit
	state[2, 2] = np.array([0, 1, 0, 0])
	#goal
	state[3, 3] = np.array([1, 0, 0, 0])
	return state

#find the position of 1's in a grid
def find_pos(grid, x):
	for i in range(4):
		for j in range(4):
			if grid[i][j] == x:
				return i, j

def make_move(state, action):
	player_pos = find_pos(state[0], 1)
	wall_pos = find_pos(state[1], 1)
	pit_pos = find_pos(state[2], 1)
	goal_pos = find_pos(state[3], 1)
	state = np.zeros((4, 4, 4))
	#move_up
	if action == 0:
		new_loc = (player_pos[0]-1, player_pos[1])
		if (np.array(new_loc) <= (3, 3)).all() and new_loc != wall_pos and ((np.array(new_loc) >= (0, 0)).all():
			state[0][new_loc] = 1
	#move down
	elif action == 1:
		new_loc = (player_pos[0]+1, player_pos[1])
		if (np.array(new_loc) <= (3, 3)).all() and new_loc != wall_pos and ((np.array(new_loc) >= (0, 0)).all():
                        state[0][new_loc] = 1
	#move left
	elif action == 2:
		new_loc = (player_pos[0], player_pos[1]-1)
		if (np.array(new_loc) <= (3, 3)).all() and new_loc != wall_pos and ((np.array(new_loc) >= (0, 0)).all():
                        state[0][new_loc] = 1
	#move right
	elif action == 3:
		new_loc = (player_pos[0], player_pos[1]+1)
		if (np.array(new_loc) <= (3, 3)).all() and new_loc != wall_pos and ((np.array(new_loc) >= (0, 0)).all():
                        state[0][new_loc] = 1
	state[1][wall_pos] = 1
	state[2][pit_pos] = 1
	state[3][goal_pos] = 1
	return state
	
if __name__ == "__main__":
	state = init_grid()
	print state

