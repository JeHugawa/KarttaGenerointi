import random

def generate_river(start, end, grid):
    #define directions for random walk
    y_dir = end[0] - start[0]
    x_dir =  end[1] - start[1]
    y_dir /= abs(y_dir)
    x_dir /= abs(x_dir)
    y_dir = int(y_dir)
    x_dir = int(x_dir)

    print(x_dir,y_dir)
    moves = [(y_dir,0),(0,x_dir),(y_dir,x_dir)]
    current_y, current_x = start
    grid[current_y][current_x] = 1
    while True:
        if current_y != end[0] and current_x != end[1]:
            move = random.choice(moves)
            current_y += move[0]
            current_x += move[1]
            grid[current_y][current_x] = 1
        elif current_y != end[0]:
            current_y += y_dir
            grid[current_y][current_x] = 1
        elif current_x != end[1]:
            current_x += x_dir
            grid[current_y][current_x] = 1
        else: break
    #returns grid with the path
    return grid
