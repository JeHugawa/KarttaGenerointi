import copy
from math import sqrt

def jump_flood(points: list, size: int):
    

    diagram = []
    for i in range(size):
        diagram.append([0]*size)
    step = size//2
    visited = copy.deepcopy(points)
    seed_points = {}
    
    #populate seed points and associated unique number with each seed
    seednum = 1
    for seed in points:
        seed_points[seed] = seed
        diagram[seed[0]][seed[1]] = seednum
        seednum += 1
        
    while step > 0:
        for point in visited:
            for i in [step,0,-(step)]:
                for j in [step,0,-(step)]:
                    neighbour = (point[0]+i,point[1]+j)
                    #check out of bounds
                    if neighbour[1] >= size or neighbour[1] < 0: continue
                    if neighbour[0] >= size or neighbour[0] < 0: continue

                    if diagram[neighbour[0]][neighbour[1]] <= 0:
                        diagram[neighbour[0]][neighbour[1]] = diagram[point[0]][point[1]]
                        visited.append(neighbour)
                        seed_points[neighbour] = seed_points[point]
                    else:
                        og_seed = seed_points[neighbour]
                        new_seed = seed_points[point]

                        original_distance = sqrt( ((og_seed[0]-neighbour[0])**2) + ((og_seed[1]-neighbour[1])**2) )
                        new_distance = sqrt( ((new_seed[0]-neighbour[0])**2) + ((new_seed[1]-neighbour[1])**2) )

                        if new_distance < original_distance:
                            diagram[neighbour[0]][neighbour[1]] = diagram[point[0]][point[1]]
                            seed_points[neighbour] = seed_points[point]
        step = step //2
    return diagram

