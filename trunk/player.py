#2007-04-1 RJ Marsan
#Pylaga
#Original: 2007-02-20 Derek Mcdonald 
#Subclass of pylaga.py
#################################################################################################################
#
#	The player class
#
#
#
#
#import pygame os and sys libraries
import pygame, os, sys, math, random
from globalvars import playership,explosion_speed,gamewindow,max_health
from bullet import *
from gun import *

################
#origional program had a few boring player lines, so i made it an object, cuz objects are cool
class Player(pygame.sprite.Sprite):
	health=max_health
	
	def __init__(self,parent,gun):
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.parent=parent
		self.image= playership[0]
		self.rect = self.image.get_rect()
		self.state=0
		self.speed=10
		self.gun=gun
	
	def get_pos(self):
		return self.rect
	
	def move(self, x,y):
		self.rect.topleft=(x,y)
		
	def move_one(self,direction):
		if direction == 1:
			self.rect.move_ip(self.speed,0)
			if not self.in_range(self.rect): #if it goes out of the range, move it back
				self.rect.move_ip((-1)*self.speed,0)
		elif direction == 0:
			self.rect.move_ip((-1)*self.speed,0)
			if not self.in_range(self.rect):
				self.rect.move_ip(self.speed,0)
	
	def in_range(self,rect):
		if gamewindow.contains(rect):
			return True
		return False
	
	def set_pos(self, tempx,tempy):
		self.rect.move_ip(tempx,tempy)
	
	def set_hit(self,health):
		self.state=1
		self.health-=health
		
	def shoot(self):
		self.gun.shoot(self.rect)
		
	def change_gun(self,gun,bullet,slist,damage=1):
		try: 
			a=eval(gun)
			#print "gun is %s"%a
			b=eval(bullet)
			#print "bullet is %s"%b
			c=a(slist,b,damage)
			#print "final gun is %s"%c
			self.gun=c
		except:
			print "GUN COULD NOT BE LOADED"
		
	def update(self):  #yay for update...
		if self.state > 0:
			self.image=playership[self.state/explosion_speed]
			self.state+=1
			if self.state >= len(playership)*explosion_speed:
				self.state=0
				self.image=playership[0]
###################

