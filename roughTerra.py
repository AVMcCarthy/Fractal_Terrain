#!/usr/bin/env python

from Tkinter import *
import random

master = Tk()
maxX = 65
maxY = 65
dChange = 0.79 #0.7 is boringly smooth, 0.9 is crazily rough. Change this from 0.8 at your own risk!
coords = [[128 for c in range(0, maxX)] for r in range(0, maxY)]

class App:
	def __init__(self, master):
		global maxX
		global maxY
		frame = Frame(master)
		frame.pack()

		self.w = Canvas(master, width = maxX * 4, height = maxY * 4)
		self.w.pack()
		
		self.button = Button(
			frame, text = "Regen", fg = "Green", command = self.paint
			)
		self.button.pack(side = LEFT)
		self.paint

	def diamond(self, xlow, ylow, xhigh, yhigh, delta):
		global coords
		global maxX
		global maxY
		global dChange
		if(0 <= xlow and xhigh < maxX and ylow >= 0 and yhigh < maxY):
			if(xlow + 1 < xhigh and ylow + 1 < yhigh):
				midX = (xlow + xhigh + 1) / 2
				midY = (ylow + yhigh + 1) / 2
				midZ = (coords[ylow][xlow] + coords[ylow][xhigh] + coords[yhigh][xlow] + coords[yhigh][xhigh] + 3) / 4
				if delta <= 0:
					disp = 0
				else:
					disp = random.randrange(-delta, +delta)
				coords[midY][midX] = midZ + disp
				newDelta = int(delta * dChange)
				dx = midX - xlow
				dy = midY - ylow
				self.square(xlow, ylow - dy, xhigh, midY, newDelta)
				self.square(midX, ylow, xhigh + dx, yhigh, newDelta)
				self.square(xlow, midY, xhigh, yhigh + dy, newDelta)
				self.square(xlow - dx, ylow, midX, yhigh, newDelta)

	def square(self, xlow, ylow, xhigh, yhigh, delta):
		global coords
		global maxX
		global maxY
		global dChange
		if(xlow + 1 < xhigh and ylow + 1 < yhigh):
			midX = (xlow + xhigh + 1) / 2
			midY = (ylow + yhigh + 1) / 2
			zs = []
			if(xlow >= 0):
				zs.append(coords[midY][xlow])
			if(ylow >= 0):
				zs.append(coords[ylow][midX])
			if(xhigh < maxX):
				zs.append(coords[midY][xhigh])
			if(yhigh < maxY):
				zs.append(coords[yhigh][midX])
			midZ = sum(zs)/len(zs)
			if delta <= 0:
				disp = 0
			else:
				disp = random.randrange(-delta, +delta)
			coords[midY][midX] = midZ + disp
			newDelta = int(delta * dChange)
			self.diamond(midX, ylow, xhigh, midY, newDelta)
			self.diamond(midX, midY, xhigh, yhigh, newDelta)
			self.diamond(xlow, midY, midX, yhigh, newDelta)
			self.diamond(xlow, ylow, midX, midY, newDelta)
	
	def paint(self):
		self.diamond(0, 0, maxX - 1, maxY - 1, 127)
		for y,xs in enumerate(coords):
			for x,z in enumerate(xs):
				if(z > 200):
					if(z < 255):
						color = "#%02x%02x%02x" %(z, (z / 7) * 5, (z / 7) * 4)
					else:
						color = "#ffd3af"
				elif(z < 75):
					if(z < 0):
						color = "#000003"
					else:
						color = "#0000%02x" %(z * 3)
				else:
					color = "#%02x%02x%02x" %(z,(z + 1) / 2,(z + 1) / 2)
				self.w.create_rectangle(x * 4,y * 4,(x + 1) * 4,(y + 1) * 4, fill = color)

app = App(master)

master.mainloop()