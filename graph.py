#!/usr/bin/env python

#Created by Logan Williams

import random, math

class Vertex:
    neighbors = []
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distanceTo(self, vertex):
        return (math.exp(vertex.x - self.x) + math.exp(vertex.y - self.y))
        
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
    def distanceToPoint(self, vertex):
        closestVertex = self.getClosestPoint(vertex)
        return vertex.distanceTo(closestVertex)
    def getClosestPoint(self, vertex):
    
        APx = vertex.x - self.vertex1.x
        APy = vertex.y - self.vertex1.y
        ABx = self.vertex2.x - self.vertex1.x
        ABy = self.vertex2.y - self.vertex1.y
        magAB2 = ABx * ABx + ABy * ABy
        ABdotAP = ABx * APx + ABy * APy
        t = ABdotAP / magAB2
        
        if t < -0.005:
            return self.vertex1
        elif t > 1.005:
            return self.vertex2
        else:
            return Vertex(self.vertex1.x + ABx * t, self.vertex1.y + ABy * t)
        
        
class Graph:
    edges = []
    vertices = []
    def __init__(self, startVertice):
        self.vertices.append(startVertice)
    def addVertex(self, vertex):
        temp = 10000000000
        tempVertex = None
        newVertex = None
        tempEdge = None
        for item in self.vertices:
            distance = vertex.distanceTo(item)
            if(distance < temp):
                temp = distance
                tempVertex = item
        for i in self.edges:
            distance = i.distanceToPoint(vertex)
            if(distance < temp):
                temp = distance
                newVertex = i.getClosestPoint(vertex)
                tempEdge = i
        self.vertices.append(vertex)
        if newVertex != None:
            tempVert2 = tempEdge.vertex2
            newVertex.neighbors.append(tempVert2)
            tempEdge.vertex2 = newVertex
            newVertex.neighbors.append(tempEdge.vertex1)
            self.vertices.append(newVertex)
            self.edges.append(Edge(newVertex, tempVert2))
            edge = Edge(vertex, newVertex)
            vertex.neighbors.append(newVertex)
            newVertex.neighbors.append(vertex)
        else:
            edge = Edge(vertex, tempVertex)
            vertex.neighbors.append(tempVertex)
            tempVertex.neighbors.append(vertex)
        self.edges.append(edge)
    def addRandomVertex(self):
        x = random.uniform(-3, 3)
        y = random.uniform(-1, 1)
        vertex = Vertex(x, y)
        self.addVertex(vertex)
