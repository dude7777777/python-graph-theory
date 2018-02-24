###########################################################################
#                                 Node                                    #
#                                                                         #
#  Programmed by Dean Zeller                                              #
#  Modified by Jacob Preston                                              #
#                                                                         #
#  Description:  The file contains the attributes and methods necessary   #
#                to represent a node within a graph.                      #
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

class Node:

    #######################################################################
    # __init__ -- Initialize attributes to given parameters               #
    #######################################################################
    def __init__ (self, canvas, ID=0, label="A",coordinates=[100,100],
                  color="red", size=5, textsize=9,
                  width=3, outline="black"):
        self.ID = ID 
        self.c = canvas
        self.coordinates = coordinates
        self.color = color
        self.size = size
        self.ID = str(ID)
        self.label = label
        self.textsize = textsize
        self.width = width
        self.outline = outline
        
    #######################################################################
    # draw -- Draw the node                                               #
    #######################################################################
    def draw(self):
        left = self.coordinates[0]-self.size
        right = self.coordinates[0]+self.size
        top = self.coordinates[1]-self.size
        bottom = self.coordinates[1]+self.size
        self.c.create_oval(left, top, right, bottom, fill=self.color,
                           width=self.width, outline=self.outline)
        self.c.create_text(self.coordinates, text=self.label,
                           font=("Times",self.textsize))
        idoffset = 5
        self.c.create_text(self.coordinates[0]+7, self.coordinates[1]+7,
                           font=("Helvetica",6),
                           text=self.ID)

    #######################################################################
    # getCoordinates -- Get the node coordinates (x,y)                    #
    #######################################################################
    def getCoordinates(self):
        return self.coordinates

    #######################################################################
    # setColor -- Set the node color                                      #
    #######################################################################
    def setColor(self, color):
        self.color = color
        self.draw()

    #######################################################################
    # setWidth -- Set the node outline width                              #
    #######################################################################
    def setWidth(self, width):
        self.width = width
        self.draw()

    #######################################################################
    # setOutline -- Set the node outline color                            #
    #######################################################################
    def setOutline(self, outline):
        self.outline = outline
        self.draw()

    #######################################################################
    # getID -- Get the node ID                                            #
    #######################################################################
    def getID(self):
        return self.ID

    #######################################################################
    # getLabel -- Get the node Label                                      #
    #######################################################################
    def getLabel(self):
        return self.label
