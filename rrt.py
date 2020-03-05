#!/usr/bin/env python

# Created by Logan Williams

import random, math, pygame, graph
from pygame.locals import *
from graph import Graph, Vertex, Edge
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
    pygame.draw.circle(screen, white, (300, 0), 98, 1)
    pygame.draw.circle(screen, white, (300, 200), 98, 1)
    pygame.display.update()
    
    count = 0
    graph = Graph(Vertex(-2, -0.5))
    while count < 200:    
        x2 = random.uniform(-3, 3)
        y2 = random.uniform(-1, 1)
        graph.addVertex(Vertex(x2, y2))
        for edge in graph.edges:
            vertex1xAdj = (edge.vertex1.x + 3) * 100
            vertex1yAdj = (edge.vertex1.y + 1) * 100
            vertex2xAdj = (edge.vertex2.x + 3) * 100
            vertex2yAdj = (edge.vertex2.y + 1) * 100
            pygame.draw.line(screen, RED, (vertex1xAdj, vertex1yAdj), (vertex2xAdj, vertex2yAdj), 1)
            pygame.display.update()
        count += 1

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

