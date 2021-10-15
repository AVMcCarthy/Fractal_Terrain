#!/usr/bin/env python

from Tkinter import *
import random
import math

master = Tk()
coords = []

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        
        self.width = 1200
        self.height = 800
        self.sea = self.height - 150
        self.hillRoughness = 0.5
        self.wideLongRatio = 0.09
        self.sunSize = 50
        self.w = Canvas(master, width=self.width, height=self.height)
        self.w.pack()
        self.button = Button(
            frame, text="Regen", fg="green", command=self.paint
            )
        self.button.pack(side=LEFT)
        
        self.paint()

    def fractal(self, low, high, delta):
        global coords
        if (low + 1 < high):
            midX = (low + high + 1) / 2
            midY = (coords[low] + coords[high] + 1) / 2
            if delta == 0:
                disp = 0
            else:
                disp = random.randrange(-delta, +delta)
            coords[midX] = midY + disp
            newDelta = int(delta * self.hillRoughness)
            self.fractal(low, midX, newDelta)
            self.fractal(midX, high, newDelta)

    def degreeToRad(self, angle):
        return (angle / 180.0) * math.pi
    
    def fixY(self, y):
        return self.height - y
    
    def tree(self, x1, y1, length, angle):
        x2 = x1 + length * math.cos(self.degreeToRad(angle))
        y2 = y1 + length * math.sin(self.degreeToRad(angle))
        thick = max(self.wideLongRatio * length, 1.0)
        self.w.create_line(x1,self.fixY(y1),x2,(self.fixY(y2)), fill = "#7c3712", width = int(thick))
        if(length >= 4):
            newL = int(length * (0.5 + random.random() * 0.49))
            newR = int(length * (0.5 + random.random() * 0.49))
            self.tree(x2,y2, newR, angle - random.randrange(10, 30))
            self.tree(x2,y2, newL, angle + random.randrange(10, 30))
        else:
            self.w.create_oval(x2 + 2, self.fixY(y2 + 2), x2 - 2, self.fixY(y2 - 2), fill = "SpringGreen4", outline = "SpringGreen4")

    # def cloud(self, x1, y1, height, width, angle):
    #     self.w.create_oval(x1, y1, x1 + width, y1 + height, fill = "gray", outline = "DarkGray")
    #     if(height > 15 and width > 15):
    #         x2 = x1 + width * math.cos(self.degreeToRad(angle))
    #         y2 = y1 + height * math.sin(self.degreeToRad(angle))
    #         x3 = x1 + width * math.cos(self.degreeToRad(angle))
    #         y3 = y1 + height * math.sin(self.degreeToRad(angle))
    #         newHighL = int(height * (0.4 + random.random() * 0.59))
    #         newHighR = int(height * (0.4 + random.random() * 0.59))
    #         newWideL = int(width * (0.4 + random.random() * 0.59))
    #         newWideR = int(width * (0.4 + random.random() * 0.59))
    #         self.cloud(x2, y2, newHighR, newWideR, angle - random.randrange(10, 90))
    #         self.cloud(x3, y3, newHighL, newWideL, random.randrange(10, 90) - angle)

    def paint(self):
        global coords
        self.w.create_rectangle(0, 0, self.width, self.sea, fill='#4fbfff', outline = "blue")
        sunX = random.randrange(0, self.width - self.sunSize)
        sunY = random.randrange(0, self.sea - self.sunSize)
        self.w.create_oval(sunX, sunY, sunX + (sunY / 30) + self.sunSize, sunY + self.sunSize, fill = "orange", outline = "red")
        # for x in range(random.randrange(0, 5)):
#   		  	self.cloud(random.randrange(0, self.width - 100), random.randrange(0, self.height - 250), 150, 200, 180)
        coords = [self.sea - 50 for i in range(0,self.width)]
        self.fractal(0, self.width - 1, 100)
        for x,y in enumerate(coords):
            self.w.create_line(x,y,x,self.height, fill = "#2c0a03")
            if (y < self.sea):
                self.w.create_line(x,y,x,self.sea, fill = "#227700")
                if random.randrange(0,self.width / 2) == 0:
                    self.tree(x, self.fixY(y),self.sea / 6, 90.0)
            else:
                self.w.create_line(x,y,x,self.sea - 1, fill = "blue")
        
app = App(master)

master.mainloop()