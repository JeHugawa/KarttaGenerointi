import perlin, floodfill, river, voronoi
import pygame
import random


p_siz = 5
map_size = 8*12
seed = 0.6311718905382234
threshold = -2
voronoi_scale = 4

height_map = perlin.main(seed,map_size)

#simple bruteforce to find single point in threshold
random_coord=(0,0)
for x in range(len(height_map)):
    for y in range(len(height_map)):
        if height_map[y][x] <= threshold:
            random_coord=(x,y)
            break

flood_map = floodfill.floodfill(threshold,random_coord,height_map,map_size)

river_point = river.randomize_river_point(map_size-1)
river_path = river.generate_river(river_point,random_coord,map_size)

voronoi_points = voronoi.randomize_points(voronoi_scale*3, map_size)
biome_map = voronoi.jump_flood(voronoi_points,map_size)

pygame.init()
screen = pygame.display.set_mode((map_size*p_siz,map_size*p_siz))
#Colours for the map, used in height order:
mountain = pygame.Color(96, 96, 96)
grass = pygame.Color(0, 204, 0)
sand = pygame.Color(194, 178, 128)
snow = pygame.Color(240, 240, 240)
water = pygame.Color(0, 0, 255)
deep_water = pygame.Color(0, 0, 128)


def draw_map():
    y = 0
    for row in height_map:
        x = 0
        for value in row:
            if flood_map[int(x/p_siz)][int(y/p_siz)] == 1: 
                pygame.draw.rect(screen, deep_water, (x,y,p_siz,p_siz))
            elif river_path[int(x/p_siz)][int(y/p_siz)] == 1:
                pygame.draw.rect(screen, water, (x,y,p_siz,p_siz))
            elif value >= 4:
                pygame.draw.rect(screen, mountain, (x,y,p_siz,p_siz))
            else:
                if biome_map[int(x/p_siz)][int(y/p_siz)] % 3 == 0:
                    pygame.draw.rect(screen, grass, (x,y,p_siz,p_siz))
                if biome_map[int(x/p_siz)][int(y/p_siz)] % 3 == 1:
                    pygame.draw.rect(screen, sand, (x,y,p_siz,p_siz))
                if biome_map[int(x/p_siz)][int(y/p_siz)] % 3 == 2:
                    pygame.draw.rect(screen, snow, (x,y,p_siz,p_siz))

            x+=p_siz
        y+=p_siz
    pygame.display.update()


draw_map()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()   
