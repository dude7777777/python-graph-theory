###########################################################################
#                            Graph Tester 1                               #
#                                                                         #
#  Programmed by Dean Zeller                                              #
#  Modified by Jacob Preston                                              #
#                                                                         #
#  Description:  The file draws a graph according to the given adjacency  #
#                matrix, coordinates, and colors.                         #
#                                                                         #
#  External Files:                                                        #
#          Node.py                                                        #
#          Edge.py                                                        #
#          Graph.py                                                       #
#                                                                         #
#  This program is copyright (c) 2016 Dean Zeller.                        #
#  All rights reserved.  Permission granted to use for educational        #
#  purposes only.  Any modifications must be documented, and commercial   #
#  use of this code must receive permission from the author(s).           #
###########################################################################
from tkinter import *
from Node import Node
from Edge import Edge
from Graph import Graph
from random import *

c = Canvas(width=600, height=600, bg='white')
c.pack(expand=YES, fill=BOTH)

# adjacency matrix
          #0  #1  #2  #3  #4  #5 
adj = [ [  0,  4,  0,  0,  0,  7],   #0
        [  4,  0,  2,  0,  5,  0],   #1
        [  0,  2,  0,  5,  3,  0],   #2
        [  0,  0,  5,  0,  9,  6],   #3
        [  0,  5,  3,  9,  0,  0],   #4
        [  7,  0,  0,  6,  0,  0]    #5
      ]

# node coordinates, colors, and labels
coords=[[ 50,300], #0
        [100,200], #1
        [100,100], #2
        [200,100], #3
        [200,200], #4
        [300,250]  #5
       ]
colors = ["yellow"]*6
labels = ['A','B','C','D','E','F']

# define and draw the graph
g = Graph(c, matrix=adj, nodeCoords=coords, nodeColors=colors, labels=labels)
g.draw()

# test the distance method
node1 = 0
node2 = 4
shortest = g.distance(node1, node2)
print("The shortest path from",g.getNodeLabel(node1),"to",g.getNodeLabel(node2),"is",shortest[0],"with an overall length of",shortest[1])

node1 = 5
node2 = 1
shortest = g.distance(node1, node2)
print("The shortest path from",g.getNodeLabel(node1),"to",g.getNodeLabel(node2),"is",shortest[0],"with an overall length of",shortest[1])

node1 = 5
node2 = 4
shortest = g.distance(node1, node2)
print("The shortest path from",g.getNodeLabel(node1),"to",g.getNodeLabel(node2),"is",shortest[0],"with an overall length of",shortest[1])

# test the center method
print("\nCenter testing...")
nodeCenter = g.center()
print("The center node is " + str(g.getNodeLabel(nodeCenter)))

# test the diamter method
print("\nDiameter testing...")
longestPath, longestLength = g.diameter()
print("The diameter is",longestLength,"with a path from",g.getNodeLabel(longestPath[0]),"to",g.getNodeLabel(longestPath[1]))
