###########################################################################
#                                 Edge                                    #
#                                                                         #
#  Programmed by Dean Zeller                                              #
#  Modified by Jacob Preston                                              #
#                                                                         #
#  Description:  The file contains the attributes and methods necessary   #
#                to represent an edge within a graph.                     #
#                                                                         #
#  Methods:                                                               #
#          __init__    Initialize attributes to given parameters          #
#          draw        Draw the edge, with an appropriately placed cost   #
#                                                                         #
#  This program is copyright (c) 2016 Dean Zeller.                        #
#  All rights reserved.  Permission granted to use for educational        #
#  purposes only.  Any modifications must be documented, and commercial   #
#  use of this code must receive permission from the author(s).           #
###########################################################################
import math
from tkinter import *

class Edge:

    #######################################################################
    # __init__ -- Initialize attributes to given parameters               #
    #######################################################################
    def __init__ (self, canvas, node1ID, node2ID, coords1, coords2, color="red",
                  width=5, cost=1, textsize=9):
        self.c = canvas
        self.node1ID = node1ID
        self.node2ID = node2ID
        self.color = color
        self.width = width
        self.cost  = cost
        self.textsize = textsize

        self.coords1 = coords1
        self.coords2 = coords2
        
    #######################################################################
    # draw -- Draw the edge, with an appropriately placed cost            #
    #######################################################################
    def draw(self):
        self.c.create_line(self.coords1, self.coords2,
                           fill=self.color, width=self.width)
        xdist = self.coords1[0]-self.coords2[0]
        ydist = self.coords2[1]-self.coords1[1]
        amt1 = 9
        amt2 = amt1*.666
        if xdist != 0:
            ratio = ydist / xdist
        else:
            ratio = 1000
        if   ratio > 4.0:    #vertical up
            offset=(amt1,0)
        elif ratio > 2.0 : #near-vertical up-right
            offset=(amt1,amt2)
        elif ratio > 0.5:  #diagonal up-right
            offset=(amt2,amt2)
        elif ratio > 0.25: #near-horizontal up-right
            offset=(amt2,amt1)
        elif ratio > -.25: #horizontal right
            offset=(0,amt1)
        elif ratio > -0.5: #near-horizontal down-right
            offset=(-amt2,amt1)
        elif ratio > -2.0: #diagonal down-right
            offset=(-amt2,amt2)
        elif ratio > -4.0: #near-vertical down-right
            offset=(-amt2,0)
            
        xMid = (self.coords1[0]+self.coords2[0])/2
        yMid = (self.coords1[1]+self.coords2[1])/2
        xMid = (self.coords1[0]+self.coords2[0])/2+offset[0]
        yMid = (self.coords1[1]+self.coords2[1])/2+offset[1]
        if self.cost != 1:            
            self.c.create_text(xMid,yMid, text=self.cost,
                               font=("Times",self.textsize))

        
