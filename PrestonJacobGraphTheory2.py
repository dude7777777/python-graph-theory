###########################################################################
#                            Graph Tester 2                               #
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
c = Canvas(width=800, height=600, bg='white')
c.pack(expand=YES, fill=BOTH)

# adjacency matrix
    #   #0 #1 #2 #3 #4  #5 #6 #7 #8 #9                                             #25
adj = [[ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],    #0
       [ 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],    #1
       [ 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],    #2
       [ 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],    #3
       [ 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],    #4
       [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [ 0, 0, 0, 0, 0, 0, 0 ,0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [ 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]      #25
       ]

# node coordinates, colors, and labels
coords=[[400,290],#
        [400,210],#
        [450,160],#
        [350,160],#
        [400,110],#
        [300,160],#
        [500,160],#
        [400, 60],#
        [460,375],#
        [525,410],#
        [585,380],#
        [555,470],#11
        [615,440],#
        [610,320],#
        [525,540],#
        [680,475],#15
        [340,375],#
        [275,410],#
        [215,380],#
        [245,470],#19
        [185,440],#
        [190,320],#
        [275,540],#
        [120,475],#
        [365,340],#24
        [435,340] #25
       ]
colors = ["yellow"]*26
labels = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
          'R','S','T','U','V','W','X','Y','Z']

# define and draw the graph
g = Graph(c, matrix=adj, nodeCoords=coords, nodeColors=colors, labels=labels)
g.draw()

#test the distance method
node1 = 0
node2 = 18
shortest = g.distance(node1,node2)
print("The shortest path from",g.getNodeLabel(node1),"to",g.getNodeLabel(node2),"is",shortest[0],"with an overall length of",shortest[1])

node1 = 7
node2 = 23
shortest = g.distance(node1,node2)
print("The shortest path from",g.getNodeLabel(node1),"to",g.getNodeLabel(node2),"is",shortest[0],"with an overall length of",shortest[1])

node1 = 2
node2 = 24
shortest = g.distance(node1,node2)
print("The shortest path from",g.getNodeLabel(node1),"to",g.getNodeLabel(node2),"is",shortest[0],"with an overall length of",shortest[1])

# test the center method
print("\nCenter testing...")
nodeCenter = g.center()
print("The center node is " + str(g.getNodeLabel(nodeCenter)))

# test the diamter method
print("\nDiameter testing...")
longestPath, longestLength = g.diameter()
print("The diameter is",longestLength,"with a path from",g.getNodeLabel(longestPath[0]),"to",g.getNodeLabel(longestPath[1]))
