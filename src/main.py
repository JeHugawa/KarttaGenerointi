import perlin
import pygame

seed = 1124321521
height_map = perlin.main(seed)

pygame.init()
screen = pygame.display.set_mode((1280,1280))
#Colours for the map, used in height order:
h4 = pygame.Color(255,255,255)
h3 = pygame.Color(96,96,96)
h2 = pygame.Color(0,204,0)
h1 = pygame.Color(244,164,96)
h0 = pygame.Color(0,0,255)
hsub0 = pygame.Color(0,0,128)


running = True
while running:
    y = 0
    x = 0
    for row in height_map:
        for value in row:
            if x > 1280:
                y += 20
                x = 0
                break
            x+=20
            if value >= 6: pygame.draw.rect(screen,h4,(x,y,20,20))
            elif value >= 4: pygame.draw.rect(screen,h3,(x,y,20,20))
            elif value >= 2: pygame.draw.rect(screen,h2,(x,y,20,20))
            #elif value >= 0: pygame.draw.rect(screen,h1,(x,y,20,20))
            elif value >= 0: pygame.draw.rect(screen,h0,(x,y,20,20))
            else: pygame.draw.rect(screen,hsub0,(x,y,20,20))
        pygame.display.update()
