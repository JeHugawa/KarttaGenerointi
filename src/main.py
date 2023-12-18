import perlin, floodfill, river
import pygame
import random


p_siz = 5
map_size = 8*12
seed = 0.6311718905382234
threshold = -2
height_map = perlin.main(seed,map_size)


#simple bruteforce to find single point in threshold
random_coord=(0,0)
for x in range(len(height_map)):
    for y in range(len(height_map)):
        if height_map[y][x] <= threshold:
            random_coord=(x,y)
            break
#random_coord=(20,60)


flood_map = floodfill.floodfill(threshold,random_coord,height_map,map_size)
river_point = river.randomize_river_point(map_size-1)
river_path = river.generate_river(river_point,random_coord,map_size)

pygame.init()
screen = pygame.display.set_mode((map_size*p_siz,map_size*p_siz))
#Colours for the map, used in height order:
h3 = pygame.Color(96,96,96)
h2 = pygame.Color(0,204,0)
h1 = pygame.Color(244,164,96)
h0 = pygame.Color(0,0,255)
hsub0 = pygame.Color(0,0,128)


def draw_map():
    y = 0
    for row in height_map:
        x = 0
        for value in row:
            if flood_map[int(x/p_siz)][int(y/p_siz)] == 1: pygame.draw.rect(screen,hsub0,(x,y,p_siz,p_siz))
            elif river_path[int(x/p_siz)][int(y/p_siz)] == 1: pygame.draw.rect(screen,h0,(x,y,p_siz,p_siz))
            elif value >= 4: pygame.draw.rect(screen,h3,(x,y,p_siz,p_siz))
            elif value >= 0: pygame.draw.rect(screen,h2,(x,y,p_siz,p_siz))
            elif value > -2.00: pygame.draw.rect(screen,h1,(x,y,p_siz,p_siz))
            #else: pygame.draw.rect(screen,h0,(x,y,20,20))
            x+=p_siz
        y+=p_siz
    pygame.display.update()


draw_map()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()   
