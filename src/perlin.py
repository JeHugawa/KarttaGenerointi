import random
import math

# Aloitetaan määrittelemällä 8x8 ristikko, missä jokaisessa ruudussa on 8 arvoa. 
# Kun saamme tämän toimimaan, tehdään yleistetty versio algoritmista joka toimii millä tahansa koolla.

def main():
    grid = []
    for i in range(9):
        a = []
        for j in range(9):
            a.append(random_gradient())
        grid.append(a)
    map_grid = []
    for x_coord in range(64):
        row = []
        for y_coord in range(64):
            row.append(perlin((x_coord, y_coord),grid))
        map_grid.append(row)
    return map_grid


# Luodaan satunnainen vektori
# Voimme myöhemmin nostaa vektorin pituutta parempien tulosten saamiseksi
def random_gradient():
   point_list = [(0,1),(1,1),(1,0),(1,-1),(-1,1),(-1,0),(0,-1),(-1,-1)]
   return random.choice(point_list)


#laskee pistetulon etäisyysvektoreiden ja satunnaisvektorien välillä
def dot_product(point, distances, grid):
    x1 = math.floor(point[0]/8)
    x2 = x1+1
    y1 = math.floor(point[1]/8)
    y2 = y1+1
    products = []
    products.append(single_product(grid[x1][y1],distances[0]))
    products.append(single_product(grid[x2][y1],distances[1]))
    products.append(single_product(grid[x1][y2],distances[2]))
    products.append(single_product(grid[x2][y2],distances[3]))
    return products

def single_product(random_grad,distance_vector):
   return random_grad[0]*distance_vector[0]+ random_grad[1]*distance_vector[1]


# laskee 4 vektoria annetusta pisteestä lähimpiin ristikon pisteisiin.
def calculate_distance(point):
    x1 = math.floor(point[0]/8)*8
    x2 = x1+8
    y1 = math.floor(point[1]/8)*8
    y2 = y1+8
    distances = []
    distances.append((abs(point[0]-x1),abs(point[1]-y1)))
    distances.append((abs(point[0]-x2),abs(point[1]-y1)))
    distances.append((abs(point[0]-x1),abs(point[1]-y2)))
    distances.append((abs(point[0]-x2),abs(point[1]-y2)))
    return distances 

# laskee perlin kohinan annetussa pisteessä
def perlin(point,random_gradient_grid):
    distances = calculate_distance(point)
    dot_products = dot_product(point,distances,random_gradient_grid)
    weight1 = (point[0] - math.floor(point[0]/8)*8)/10
    weight2 = (point[1] - math.floor(point[1]/8)*8)/10
    result = interpolate(dot_products,weight1,weight2)
    return result # palauttaa arvo -8 ja 8 välillä.

# Interpoloi eri pistetulojen välillä
def interpolate(dot_products,w1,w2):
    ip0 = (dot_products[1]-dot_products[0]) * w1+ dot_products[0]
    ip1 = (dot_products[3]-dot_products[2]) * w1 + dot_products[2]
    return (ip1-ip0) *w2 + ip0
