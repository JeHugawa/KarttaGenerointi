def floodfill(threshold: int, point: int, height_map: list,size):
    #0 täyttämätön ruutu, 1 täytetty
    floodmap = [64*[0] for x in range(64)]
    que = [point]
    while que:
        x,y = que.pop()
        leftx = c_coord[0]
        while inside( (leftx-1,y), threshold, height_map):
            floodmap[leftx-1][y] = 1
            leftx = leftx -1 
        while inside(x,y):
            floodmap[x][y] = 1
            x = x + 1
        find_seed_points(leftx,x-1,y+1,que,floodmap)
        find_seed_points(leftx,x-1,y-1,que,floodmap)

    return floodmap

#tarkistaa onko piste kynnysarvon sisällä
def inside(point: tuple, threshold: int):
    return height_map[point[0]][point[1]] < threshold


def find_seed_points(leftx, rightx, y, que,floodmap):
    added = False
    for x in range(leftx, rightx):
        if floodmap[x][y] == 0:
            added = False
        elif not added:
            que.append((x,y))
            added = True
