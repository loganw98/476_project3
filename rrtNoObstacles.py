#!/usr/bin/env python

# Created by Logan Williams

import random, math, pygame
from pygame.locals import *
from array import *
from math import sin, cos, pi

#constants
WINSIZE = [600, 200]
SIZE = 360




def main():
    #initialize and prepare screen
            
    name = "path.txt"
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('Linked Chains with Obstacles: G. Song, 2019s')
    white = 255, 240, 200
    black = 20, 20, 40
    RED =   (255,   0,   0)
    screen.fill(black)
    #pygame.draw.circle(screen, white, (300, 0), 98)
    #pygame.draw.circle(screen, white, (300, 200), 98)
    pygame.display.update()

    done = 0
    while not done:
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
              print("\nLeaving because you said so\n")
              done = 1
              break



# if python says run, then we should run
if __name__ == '__main__':
    main()
