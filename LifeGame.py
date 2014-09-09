#  -*- coding:utf-8 -*-

import math
import random
import os
import time
import pygame

global timepause 
timepause = 10

class cell(object):

	
	"""docstring for cell"""

	
	def __init__(self, nowstate=0, nextstate=0,x=0,y=0):
		super(cell, self).__init__()
		self.nowstate = nowstate
		self.nextstate= nowstate
		self.x = x
		self.y = y
		
	def updatecell(self):
		self.nowstate = self.nextstate
		self.nextstate = 0


class world(object):
	"""docstring for world"""
	
	def __init__(self, scale = 100):
		super(world, self).__init__()
		self.scale = scale
		self.worldmap = [[]]
		self.creatworld
		pygame.init()
		self.py = 5
		self.px = 5
		self.xlen = 400/self.scale
		self.ylen = 400/self.scale

		self.screen = pygame.display.set_mode([2*self.px+self.scale*self.xlen,2*self.py+self.scale*self.ylen])

	def creatworld(self):
		worldmap = []
		for x in range(self.scale):
			raw = []
			for y in range(self.scale):
			 	onecell = cell(random.randint(0,1),0,x,y)
				raw.append(onecell)
			worldmap.append(raw)
		self.worldmap = worldmap

	def outlook(self,x,y):
		
		neighbourstate = 0

		for i in range(3):
			for j in range (3):
				ii = i
				jj = j
				if (x == self.scale-1 and i == 2):
					ii = -self.scale+2
				if (y == self.scale-1 and j ==2):
					jj = -self.scale+2
				neighbourstate += self.worldmap[x+ii-1][y+jj-1].nowstate
		neighbourstate -= self.worldmap[x][y].nowstate

		return neighbourstate


	def evolution(self):
		for i in range(self.scale):
			for j in range(self.scale):
				neighbourstate = self.outlook(i,j)
				if (neighbourstate == 3 ):
					self.worldmap[i][j].nextstate = 1
				elif(neighbourstate == 2 ):
					self.worldmap[i][j].nextstate = self.worldmap[i][j].nowstate
				else:
					self.worldmap[i][j].nextstate = 0
		
	def updateworld(self):
		for i in range(self.scale):
			for j in range(self.scale):
				self.worldmap[i][j].updatecell()


	def display(self):
		
		for i in range(20):
			self.drawupdateworld()
			self.updateworld()
			self.evolution()
			time.sleep(1)
		

	def displaycell(self,x,y):
		for i in range(10):
			print self.worldmap[x][y].nowstate, self.worldmap[x][y].nextstate
			self.updateworld()
			self.evolution()
			time.sleep(0.3)
		pygame.exit()

	def drawupdateworld(self):

		white = (255,255,255)
		black = (0,0,0)

		for i in range(self.scale):
			for j in range(self.scale):
				if self.worldmap[i][j].nowstate == 1:
					pygame.draw.rect(self.screen,white,[i*self.xlen+self.px,j*self.ylen+self.py,self.xlen,self.ylen])
				if self.worldmap[i][j].nowstate == 0:
					pygame.draw.rect(self.screen,black,[i*self.xlen+self.px,j*self.ylen+self.py,self.xlen,self.ylen])

		pygame.display.update()
		


# pygame.init()
# screen = pygame.display.set_mode([sizey,sizex])
# pygame.draw.rect(screen,white,[px,py,xlen,ylen])
# pygame.draw.rect(screen,white,[px+40,py+40,xlen,ylen])

# for i in range(30):
# 	pygame.display.update([px,py,xlen+100,ylen+100])
# 	time.sleep(1)


oneworld = world(30)
oneworld.creatworld()
oneworld.display()


