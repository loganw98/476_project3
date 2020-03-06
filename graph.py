#!/usr/bin/env python

# Created by Logan Williams

import random, math


# a vertex class. Stores an x and y coordinate
class Vertex:
    neighbors = []

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    # gives the distance from this vertex to another
    def distanceTo(self, vertex):
        return math.sqrt(math.pow(vertex.x - self.x, 2) + math.pow(vertex.y - self.y, 2))

    # give the distance from this vertex to an (x, y) coordinate
    def distanceToPoint(self, x, y):
        return math.sqrt(math.pow(x - self.x, 2) + math.pow(y - self.y, 2))


# a class that signifies edges. Stores two vertices
class Edge:
    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2

    def setVertex1(self, vertex1):
        self.vertex1 = vertex1

    def setVertex2(self, vertex2):
        self.vertex2 = vertex2

    def getVertex1(self):
        return self.vertex1

    def getVertex2(self):
        return self.vertex2

    # gives the closest distance from this edge to the given vertex
    def distanceToPoint(self, vertex):
        closestVertex = self.getClosestPoint(vertex)
        return vertex.distanceTo(closestVertex)

    # Gets the closest point on the edge to the given vertex
    def getClosestPoint(self, vertex):

        APx = vertex.x - self.vertex1.x
        APy = vertex.y - self.vertex1.y
        ABx = self.vertex2.x - self.vertex1.x
        ABy = self.vertex2.y - self.vertex1.y
        magAB2 = ABx * ABx + ABy * ABy
        ABdotAP = ABx * APx + ABy * APy
        t = ABdotAP / magAB2

        if t < 0:
            return self.vertex1
        elif t > 1:
            return self.vertex2
        else:
            return Vertex(self.vertex1.x + ABx * t, self.vertex1.y + ABy * t)


# a class to store edges and vertices
class Graph:
    edges = []
    vertices = []

    def __init__(self, startVertice):
        self.vertices.append(startVertice)

    # adds a vertex to the graph
    def addVertex(self, vertex):
        self.vertices.append(vertex)

    # adds an edge to the graph
    def addEdge(self, vertex1, vertex2):
        self.edges.append(Edge(vertex1, vertex2))
        vertex1.neighbors.append(vertex2)
        vertex2.neighbors.append(vertex1)

    # gets the vertices in the graph
    def getVertices(self):
        return self.vertices

    # gets all edges in the graph
    def getEdges(self):
        return self.edges

    # removes an edge from the graph
    def removeEdge(self, edge):
        self.edges.remove(edge)
