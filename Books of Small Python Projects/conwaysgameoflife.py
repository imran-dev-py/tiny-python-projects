import copy, random, time 

# set up the constants
WIDTH = 79
HEIGHT = 20
ALIVE = '0'
DEAD = '_'

# the cells and next_cells are dictionaries for the state of the game. Their keys are (x, y) tuples and their values are one of the ALIVE or DEAD values
next_cells = {}

# put random dead and alive cells into next_cells
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            next_cells[(x, y)] = ALIVE
        else:
            next_cells[(x, y)] = DEAD

while True:
    # each iteration of this loop is a step of the simulation

    # separate each step with newlines
    print('\n' * 5)
    cells = copy.deepcopy(next_cells)

    # print cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[x, y], end='')
        print() # newline at the end of row
    print('Press Ctrl-C to quit')

    # calculate the next step's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x - 1) % WIDTH 
            right = (x + 1) % WIDTH 
            above = (y - 1) % HEIGHT 
            below = (y + 1) % HEIGHT

            # count the number of living neighbors
            num_neighbors = 0
            if cells[(left, above)] == ALIVE:
                num_neighbors += 1 # top-left neighbor is alive
            if cells[(x, above)] == ALIVE:
                num_neighbors += 1 # top neighbor is alive
            if cells[(right, above)] == ALIVE:
                num_neighbors += 1 # top - right neighbor is alive
            if cells[(left, y)] == ALIVE:
                num_neighbors += 1 # left neighbor is alive
            if cells[(right, y)] == ALIVE:
                num_neighbors += 1 # right neighbor is alive
            if cells[(left, below)] == ALIVE:
                num_neighbors += 1 # bottom - left neighbor is alive
            if cells[(x, below)] == ALIVE:
                num_neighbors += 1 # bottom neighbor is alive
            if cells[(right, below)] == ALIVE:
                num_neighbors += 1 # bottom - right neighbor is alive

            # set cell based on conway's game of life rules
            if cells[(x, y)] == ALIVE and (num_neighbors == 2 or num_neighbors == 3):
                #living cells with 2 or 3 neighbors stay alive
                next_cells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and num_neighbors == 3:
                next_cells[(x, y)] = ALIVE
            else:
                # everything else dies or stay alive
                next_cells[(x, y)] = DEAD
    
    try:
        # pause for reducing flickering
        time.sleep(1)
    except KeyboardInterrupt:
        print("Conway's Game of Life end")
        exit()
