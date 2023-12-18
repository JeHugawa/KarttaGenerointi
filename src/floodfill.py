def floodfill(threshold: int, point: int, height_map: list, map_size: int):
    #0 täyttämätön ruutu, 1 täytetty
    floodmap = [map_size*[0] for x in range(map_size)]
    que = [point]
    while que:
        x,y = que.pop()
        leftx = x
        while inside( (leftx-1,y), threshold, height_map):
            floodmap[leftx-1][y] = 1
            leftx = leftx -1 
        while inside((x,y),threshold, height_map):
            floodmap[x][y] = 1
            x = x + 1
        find_seed_points(leftx,x,y+1,que,floodmap)
        find_seed_points(leftx,x,y-1,que,floodmap)
    return floodmap

#tarkistaa onko piste kynnysarvon sisällä
def inside(point: tuple, threshold: int,height_map):
    if point[0] < 0 or point[1] < 0:
        return False
    if point[0] >= len(height_map) or point[1] >= len(height_map[0]):
        return False
    return height_map[point[1]][point[0]] <= threshold


def find_seed_points(leftx, rightx, y, que,floodmap):
    if y < 0 or y >= len(floodmap):
        return
    for x in range(leftx, rightx):
        if floodmap[x][y] == 0:
            que.append((x,y))
