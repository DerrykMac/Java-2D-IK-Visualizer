import os, sys, time, random, math, json
import pygame as pg
import STDF

# Define some colors\
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

#initialize pygame
pg.init()
size = (800, 600)
screen = pg.display.set_mode(size)
pg.display.set_caption("IK Visualizer")
clock = pg.time.Clock()

#Draw 5 rectangles
pg.draw.rect(screen, BLACK, [0, 0, 800, 600], 2) #Base
pg.draw.rect(screen, BLUE, [0, 0, 100, 100], 2) #Joint 1
pg.draw.rect(screen, BLUE, [0, 0, 100, 100], 2) #Joint 2
pg.draw.rect(screen, RED, [0, 0, 100, 100], 2) #Hand
pg.draw.rect(screen, GREEN, [0, 0, 100, 100], 2) #waight
#Draw 1 circle
pg.draw.circle(screen, ORANGE, [0, 0], 50, 2) #point

#Pygame loop
done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    
    

    screen.fill(WHITE)
    pg.display.flip()
    clock.tick(60)

pg.quit()