#!/usr/bin/env python

# Created by Logan Williams

from rrtNoObstacles import *
from pygame.locals import *
from graph import Graph, Vertex, Edge

# constants

WINSIZE = [600, 200]
STEPSIZE = .005


# initialize and prepare screen, then run the RRT. Note that everything is shifted by 3 and scaled by 100 to be
# visible
def main():

    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('Rapidly Exploring Random Trees with Solution')
    white = 255, 240, 200
    black = 20, 20, 40
    RED = (255, 0, 0)
    screen.fill(black)
    pygame.draw.circle(screen, white, (300, 0), 98, 1)
    pygame.draw.circle(screen, white, (300, 200), 98, 1)
    pygame.display.update()

    graph = Graph(Vertex(-2, -0.5))
    goal = Vertex(2, -0.5)
    rrtWithSolution(graph, Vertex(-2, -0.5), 2000, screen, RED, goal, .1)

    done = 0
    while not done:
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                print("\nLeaving because you said so\n")
                done = 1
                break


# Runs the raplidly exploring tree with a set probability to find the goal. Modify it above to see different values
def rrtWithSolution(graph, start, iterations, screen, color, goal, probability):
    goalCheck = 0
    graph.addVertex(start)
    while iterations is not 0:
        if goalCheck >= 1:
            nearest = findNearest(graph, goal)
            collisionNode = ClosesttoCollision(graph, goal, nearest)
            if collisionNode is False:
                graph.addVertex(goal)
                graph.addEdge(goal, nearest)
                drawEdges(screen, graph, color)
                break
        x = random.uniform(-3, 3)
        y = random.uniform(-1, 1)
        vertex = Vertex(x, y)
        nearest = findNearest(graph, vertex)
        collisionNode = ClosesttoCollision(graph, vertex, nearest)
        if collisionNode is False:
            graph.addVertex(vertex)
            graph.addEdge(vertex, nearest)
        drawEdges(screen, graph, color)
        iterations -= 1
        goalCheck += probability


# if python says run, then we should run
if __name__ == '__main__':
    main()
