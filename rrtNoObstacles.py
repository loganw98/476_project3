#!/usr/bin/env python

# Created by Logan Williams

from rrt import *
import random, math, pygame
from pygame.locals import *
from graph import Graph, Vertex, Edge

# constants
WINSIZE = [600, 200]
SIZE = 360

# initialize and prepare screen, then run the RRT. Note that everything is shifted by 3 and scaled by 100 to be
# visible
def main():
    # initialize and prepare screen

    name = "path.txt"
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('Rapidly Exploring Random Trees')
    white = 255, 240, 200
    black = 20, 20, 40
    RED = (255, 0, 0)
    screen.fill(black)
    pygame.draw.circle(screen, white, (300, 0), 98, 1)
    pygame.draw.circle(screen, white, (300, 200), 98, 1)
    pygame.display.update()

    graph = Graph(Vertex(-2, -0.5))
    rrt(graph, Vertex(-2, -0.5), 300, screen, RED)

    done = 0
    while not done:
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                print("\nLeaving because you said so\n")
                done = 1
                break


def rrt(graph, start, iterations, screen, color):
    graph.addVertex(start)
    while iterations is not 0:
        x = random.uniform(-3, 3)
        y = random.uniform(-1, 1)
        vertex = Vertex(x, y)
        nearest = findNearest(graph, vertex)
        graph.addVertex(vertex)
        graph.addEdge(vertex, nearest)
        drawEdges(screen, graph, color)
        iterations -= 1


# Finds the nearest point on the graph, whether it be a vertex or part of an edge. In the case of an edge, the edge is
# split, which adds two vertices and two edges into the graph instead of 1 each
def findNearest(graph, vertex):
    nearest = findNearestPoint(graph, vertex)
    nearestpoe = findNearestPointOnEdge(graph, vertex)
    if nearestpoe[0] < nearest[0]:
        v1 = nearestpoe[2].vertex1
        v2 = nearestpoe[2].vertex2
        graph.removeEdge(nearestpoe[2])
        graph.addEdge(v1, nearestpoe[1])
        graph.addEdge(nearestpoe[1], v2)
        return nearestpoe[1]
    else:
        return nearest[1]


# Finds the nearest vertex to the one supplied.
# Returns the distance and the node
def findNearestPoint(graph, vertex):
    mindistance = LARGE_INTEGER
    vertexList = graph.getVertices()
    tempV = vertex
    for vertice in vertexList:
        temp = vertice.distanceTo(vertex)
        if temp < mindistance:
            tempV = vertice
            mindistance = temp

    return mindistance, tempV


# Finds the nearest vertex to the one supplied.
# Returns the distance, the node, and the edge it lies on
def findNearestPointOnEdge(graph, vertex):
    mindistance = LARGE_INTEGER
    edgeList = graph.getEdges()
    tempEdge = None
    tempNode = None
    for edge in edgeList:
        temp = edge.getClosestPoint(vertex)
        if vertex.distanceTo(temp) < mindistance:
            mindistance = vertex.distanceTo(temp)
            tempEdge = edge
            tempNode = temp
    return mindistance, tempNode, tempEdge


# Draws the edges on the surface for Pygame
def drawEdges(surface, graph, color):
    for edge in graph.edges:
        vertex1xAdj = (edge.vertex1.x + 3) * 100
        vertex1yAdj = (edge.vertex1.y + 1) * 100
        vertex2xAdj = (edge.vertex2.x + 3) * 100
        vertex2yAdj = (edge.vertex2.y + 1) * 100
        pygame.draw.line(surface, color, (vertex1xAdj, vertex1yAdj), (vertex2xAdj, vertex2yAdj), 1)
        pygame.display.update()

# if python says run, then we should run
if __name__ == '__main__':
    main()
