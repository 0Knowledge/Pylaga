#2007-04-1 RJ Marsan
#Pylaga
#Original: 2007-02-20 Derek Mcdonald 
#Subclass of pylaga.py
#################################################################################################################
#
#	A few premade menu objects
#
#       Makes it easier on my brain
#
#
#import pygame os and sys libraries
import pygame, os, sys, math, random
import globalvars
from menu import Menu
from display import points

##takes a tuple of menuitem strings as input
#a generic menu class
#very effective
class MenuLists:
            ############the menu functions###########
	def init_menu(self):
                self.clear_screen()
		menu=Menu(("Play!","About","Help","Exit"))
		selection=-1
		while True:
			events=pygame.event.get()
			selection=self.menu_action(events,menu)
			if selection >= 0:
                                if selection == 0:
                                        break
                                if selection == 1:
                                        menu.disp_special(self.about_menu)
                                if selection == 2:
                                        menu.disp_special(self.help_menu)
                                if selection == 3:
                                        sys.exit(0)
			menu.render()
			globalvars.clock.tick(globalvars.FPS)
		self.clear_screen()
		pygame.mouse.set_visible(0)
		pygame.event.set_grab(1)
		
	def exit_menu(self):
                self.clear_screen()
                pygame.mouse.set_visible(1)
		menu=Menu(("Again?","About","Help","Exit","Score: %s"%points.get_points()))
		selection=-1
		while True:
			events=pygame.event.get()
			selection=self.menu_action(events,menu)
			if selection >= 0:
                                if selection == 0:
                                        break
                                if selection == 1:
                                        menu.disp_special(self.about_menu)
                                if selection == 2:
                                        menu.disp_special(self.help_menu)
                                if selection == 3:
                                        return False
			menu.render()
			globalvars.clock.tick(globalvars.FPS)
		self.clear_screen()
		pygame.mouse.set_visible(0)
		return True


	def pause_menu(self):
                #self.clear_screen()
                pygame.mouse.set_visible(1)
		pygame.event.set_grab(0)
		menu=Menu(("Resume","About","Help","Exit"),45,globalvars.logo)
		selection=-1
		while True:
			events=pygame.event.get()
			selection=self.menu_action(events,menu)
			if selection >= 0:
                                if selection == 0:
                                        break
                                if selection == 1:
                                        menu.disp_special(self.about_menu)
                                if selection == 2:
                                        menu.disp_special(self.help_menu)
                                if selection == 3:
                                        sys.exit(0)
			menu.render()
			globalvars.clock.tick(globalvars.FPS)
		self.clear_screen()
		pygame.mouse.set_visible(0)
		pygame.event.set_grab(1)
		
	def special_menu(self,menuarray):
		#self.clear_screen()
                pygame.mouse.set_visible(1)
		pygame.event.set_grab(0)
		menu=Menu(menuarray,30,globalvars.logo)
		selection=-1
		while True:
			events=pygame.event.get()
			selection=self.menu_action(events,menu)
			if selection >= 0:
                                if selection == len(menuarray)-1:
                                        break
			menu.render()
			globalvars.clock.tick(globalvars.FPS)
		self.clear_screen()
		pygame.mouse.set_visible(0)
		pygame.event.set_grab(1)
		
	def about_menu(self):
		self.special_menu(("!This is a small galaga clone written in Python","!Written By:","!RJ Marsan","!Original:","!Derek Mcdonald","!Version: %s"%globalvars.VERSION,"!","Back"))
	
	def help_menu(self):
		self.special_menu(("!Help:","!     Left: Left Arrow or Mouse","!     Right: Right Arrow or Mouse","!     Shoot: Space or Mouse Left","!     Pause: p","!     Exit: q or esc","!","Back"))
		
	def buy_menu(self,menulist):
                #self.clear_screen()
                pygame.mouse.set_visible(1)
		pygame.event.set_grab(0)
		menuarry=[]
		execarry=[]
		for (a,b) in menulist:
			menuarry.append(a)
			execarry.append(b)
		menu=Menu(menuarry,30,globalvars.logo)
		selection=-1
		goagain=True
		while goagain:
			events=pygame.event.get()
			selection=self.menu_action(events,menu)
			if selection >= 0:
				exec execarry[selection]

			menu.render()
			globalvars.clock.tick(globalvars.FPS)
		self.clear_screen()
		pygame.mouse.set_visible(0)
		pygame.event.set_grab(1)

	def menu_action(self, events, menu):
                selection=-1
                pygame.event.pump()
                for event in events:
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                        sys.exit(0)
				if event.key == pygame.K_ESCAPE:
					sys.exit(0)
                                if event.key == pygame.K_UP:
                                        menu.change_selection_up()
                                if event.key == pygame.K_DOWN:
                                        menu.change_selection_down()
                                if event.key == pygame.K_RETURN:
                                        selection=menu.get_selection()
                        if event.type == pygame.MOUSEMOTION:
                                menu.change_selection_pos(event.pos)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                menu.change_selection_pos(event.pos)
                                if menu.mouse_is_anywhere(event.pos):
                                        selection=menu.get_selection()
                return selection
        ############the menu functions###########
	
	def clear_screen(self):
                globalvars.surface.fill(globalvars.bgcolor)
		pygame.display.flip()
		
global menulists
menulists=MenuLists()