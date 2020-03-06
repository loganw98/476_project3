#!/usr/bin/env python

# Created by Logan Williams

from rrtNoObstacles import *
import random, math, pygame
from pygame.locals import *
from graph import *

# constants
WINSIZE = [600, 200]
STEPSIZE = .005
RADIUS = 1 - .02
LARGE_INTEGER = 1000000000


# initialize and prepare screen, then run the RRT. Note that everything is shifted by 3 and scaled by 100 to be
# visible
def main():
    name = "path.txt"
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('Rapidly Exploring Random Trees with Collision Detection')
    white = 255, 240, 200
    black = 20, 20, 40
    RED = (255, 0, 0)
    screen.fill(black)
    pygame.draw.circle(screen, white, (300, 0), 98, 1)
    pygame.draw.circle(screen, white, (300, 200), 98, 1)
    pygame.display.update()

    graph = Graph(Vertex(-2, -0.5))
    rrtObstacles(graph, Vertex(-2, -0.5), 2000, screen, RED)

    done = 0
    while not done:
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                print("\nLeaving because you said so\n")
                done = 1
                break


# runs the rapidly exploring tree on a space with two circular objects
def rrtObstacles(graph, start, iterations, screen, color):
    graph.addVertex(start)
    while iterations is not 0:
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


# finds the closest point to the obstacle. If it finds a point that isn't itself, it adds that point into the
# graph, then returns true. If it finds a point that is itself, it just returns true. If none of the above, return
# false. Returning false tells the main algorithm to go ahead and add the originally sampled vertex into the graph
def ClosesttoCollision(graph, vertex, nearest):
    vector = calcDistanceMetric(vertex, nearest)
    temp = nearest
    while checkIfPast(nearest, temp, vertex) is not True:
        prev = temp
        temp = Vertex(temp.x + vector[0] * STEPSIZE, temp.y + vector[1] * STEPSIZE)
        if distanceFromObstacles(temp, 0, 1, 0, -1)[0] <= RADIUS or distanceFromObstacles(temp, 0, 1, 0, -1)[
            1] <= RADIUS:
            if prev is not nearest:
                graph.addVertex(prev)
                graph.addEdge(prev, nearest)
                return True
            else:
                return True

    return False


# checks if the point has gone past the goal
def checkIfPast(original, collV, goal):
    if collV.x >= goal.x > original.x:
        return True
    elif collV.x < goal.x < original.x:
        return True
    elif collV.y >= goal.y > original.y:
        return True
    elif collV.y < goal.y < original.y:
        return True
    return False


# calculates the x and y values that should be multiplied by the step value in order to find x and y values
# that decrease the distance between two points by 0.05
def calcDistanceMetric(vertex, nearest):
    vectorForm = vertex.x - nearest.x, vertex.y - nearest.y
    magnitude = math.sqrt(vectorForm[0] ** 2 + vectorForm[1] ** 2)
    return vectorForm[0] / magnitude, vectorForm[1] / magnitude


# Calculates the distance of a point from both obstacles
def distanceFromObstacles(vertex, obs1x, obs1y, obs2x, obs2y):
    return vertex.distanceToPoint(obs1x, obs1y), vertex.distanceToPoint(obs2x, obs2y)



# if python says run, then we should run
if __name__ == '__main__':
    main()
