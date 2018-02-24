###########################################################################
#                                 Graph                                   #
#                                                                         #
#  Programmed by Dean Zeller                                              #
#  Modified by Jacob Preston                                              #
#                                                                         #
#  Description:  The file contains the attributes and methods necessary   #
#                to represent a graph, with nodes and edges.              #
#                                                                         #
#  Methods:                                                               #
#          __init__        Initialize attributes to given parameters      #
#          draw            Draw the node                                  #
#          getCoordinates  Get the node coordinates (x,y)                 #
#          setColor        Set the node color                             #
#          setWidth        Set the node outline width                     #
#          setOutline      Set the node outline color                     #
#          getID           Get the node ID (numeric)                      #
#          getLabel        Get the node label (alphabetic)                #
#                                                                         #
#  This program is copyright (c) 2016 Dean Zeller.                        #
#  All rights reserved.  Permission granted to use for educational        #
#  purposes only.  Any modifications must be documented, and commercial   #
#  use of this code must receive permission from the author(s).           #
###########################################################################
from tkinter import *
from Node import Node
from Edge import Edge
import random

class Graph:

    #######################################################################
    # __init__ -- Initialize attributes to given parameters               #
    #######################################################################
    def __init__ (self, canvas, matrix=[], nodeCoords=[], nodeColors=[],
                  nodeSize=15, nodeLabelSize=14, edgeColor="black",
                  edgeLabelSize=12, labels=[]):
        self.c = canvas
        self.matrix = matrix
        self.nodeColors = nodeColors
        self.nodeCoords = nodeCoords
        self.nodeSize = nodeSize
        self.nodeLabelSize = nodeLabelSize
        self.n = len(matrix)
        self.nodes = []
        for i in range(self.n):
            node = Node(self.c, ID=i, coordinates=nodeCoords[i],
                        color=nodeColors[i],
                        size=nodeSize, textsize=nodeLabelSize,
                        label=labels[i])
            self.nodes.append(node)
        self.edgeColor = edgeColor
        self.edgeLabelSize = edgeLabelSize
        self.edges = []
        for i in range(self.n):
            for j in range(i+1,self.n):
                if self.matrix[i][j]>0:
                    edge = Edge(self.c, i,j,nodeCoords[i],nodeCoords[j],
                                color=edgeColor, width=2,
                                cost=self.matrix[i][j],
                                textsize = self.edgeLabelSize)
                    self.edges.append(edge)
        self.checkMatrix()
        
    #######################################################################
    # checkMatrix -- Ensure matrix is symmetric diagonally.               #
    #######################################################################
    def checkMatrix(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] != self.matrix[j][i]:
                    print("Error in matrix symmetry:",i,j)
                    return

    #######################################################################
    # getN -- return the number of nodes in the graph.                    #
    #######################################################################
    def getN(self):
        return self.n

    #######################################################################
    # getNodeLabel -- return the label of node i.                         #
    #######################################################################
    def getNodeLabel(self,i):
        return self.nodes[i].getLabel()
        
    #######################################################################
    # getPathLabels -- return a list of all labels in a path.             #
    #######################################################################
    def getPathLabels(self,path):
        labels = []
        for node in path:
            labels.append(self.getNodeLabel(node))
        return(labels)
        
    #######################################################################
    # draw -- draw the edges and the nodes.                               #
    #######################################################################
    def draw(self):
        for i in range(len(self.edges)):
            self.edges[i].draw()
        for i in range(self.n):
            self.nodes[i].draw()

    #######################################################################
    # checkPath -- Ensure the list of nodes is a path within the graph.   #
    #######################################################################
    def checkPath(self, path):
        for i in range(len(path)-1):
            node1 = path[i]
            node2 = path[i+1]
            if self.matrix[node1][node2] is 0:
                return False
        return True

    #######################################################################
    # pathLength -- Calculate and return the overall length of the path.  #
    #######################################################################
    def pathLength(self, path):
        if self.checkPath(path) is False:
            return -1
        length = 0
        for i in range(len(path)-1):
            node1 = path[i]
            node2 = path[i+1]
            length += self.matrix[node1][node2]
        return length

    #######################################################################
    # generateRandomPath -- Given a start node and a length, generate a   #
    #                       path selecting edges at random.               #
    #                                                                     #
    # The repeatsAllowed parameter allows the user to specify if nodes    #
    # can be repeated.  If, as a result the length cannot be reached, the #
    # path generated up to that point is returned.                        #
    #######################################################################
    def generateRandomPath(self, start, length, repeatsAllowed=True):
        randomPath = [start]
        for i in range(length-1):
            success = True
            badNode = start
            neighbors = self.generateNeighbors(start, randomPath, repeatsAllowed)
            if not neighbors:
                badNode = randomPath.pop
                success = False
            if success is True:
                choice = random.choice(neighbors)
                while choice is badNode:
                    choice = random.choice(neighbors)
                randomPath.append(choice)
                start = choice
        return randomPath

    #######################################################################
    # generateNeighbors -- Given a start node, generate the nodes         #
    #                       connected to it.                              #
    #######################################################################
    def generateNeighbors (self, start, randomPath, repeatsAllowed):
        neighbors = []
        for i in range(len(self.matrix)):
            if self.matrix[start][i] > 0:
                if repeatsAllowed is True:
                    neighbors.append(i)
                else:
                    success = True
                    for j in range(len(randomPath)):
                        if randomPath[j] is i:
                            success = False
                    if success is True:
                        neighbors.append(i)
        return neighbors
    
    #######################################################################
    # distance -- Given start and end nodes, find the distance (shortest  #
    #             path) between the nodes.                                #
    #######################################################################
    def distance(self, start, end):
        #Variables
        shortestPath = []
        nextNode = start
        dist = []
        parents = []
        visited = []

        #Copy of Matrix
        copyMatrix = self.matrix

        #Initializes dist, parents, and visited arrays
        for i in range(self.n):
            dist.append(99999)
            parents.append(0)
            visited.append(0)

        #Replaces 0 with 99999 in matrix
        for i in range(self.n):
            for j in range(self.n):
                if copyMatrix[i][j] == 0:
                    copyMatrix[i][j] = 99999

        #Scans starting node
        dist[start] = 0
        visited[start] = 1
        parents[start] = start

        #Does a scan for each node in list
        for c in range(self.n):
            #Changes distance and parents array
            for i in range(self.n):
                if((dist[nextNode]+copyMatrix[nextNode][i])<dist[i]) and visited[i]==0:
                    dist[i] = dist[nextNode] + copyMatrix[nextNode][i]
                    parents[i] = nextNode

            #Picks next node by smallest distance
            test = 0
            for j in range(len(dist)):
                if visited[j] == 0:
                    if test == 0:
                        nextNode = j
                        test = 1
                    if dist[j] < dist[nextNode]:
                        nextNode = j

            #Prints visited array
            visited[nextNode] = 1

        #Uses parent array to contruct shortest path
        shortestPath.append(end)
        j = end
        while True:
            if start == parents[j]:
                shortestPath.append(start)
                break
            shortestPath.append(parents[j])
            j = parents[j]

        #Reverses shortest path
        shortestPath = shortestPath[::-1]

        #Gets path length
        totalPathLength = self.pathLength(shortestPath)

        #Returns shortest path and its path length
        return (shortestPath, totalPathLength)

    #######################################################################
    # diameter -- Find the two nodes with the greatest distance.          #
    #######################################################################
    def diameter(self):
        #Variables
        diam = []
        longestPath = []
        longestLength = 0

        #Initializes the diameter array with zeros
        for i in range(self.n):
            diam.append(0)

        #checks each distance if it is the longest
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    d = self.distance(i,j)[1]
                    if d > longestLength:
                        #if the currently tested distance is longer it stores it and its path
                        longestLength = d
                        longestPath = [i,j]

        #Returns the longest path and its length
        return (longestPath, longestLength)

    #######################################################################
    # center -- Find the node with the smallest average distance to all   #
    #           other nodes.                                              #
    #######################################################################
    def center(self):
        #Variables
        totalDist = []

        #Initializes total distance with zeros
        for i in range(self.n):
            totalDist.append(0)

        #checks shortest distance for each path
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    d = self.distance(i,j)[1]
                    totalDist[i] = totalDist[i] + d

        #Linear search for shortest total distance
        center = totalDist[0]
        for c in range(len(totalDist)):
            if totalDist[c] < center:
                center = c

        #Returns the center node index
        return center
