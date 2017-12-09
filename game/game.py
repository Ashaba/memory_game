import os
from time import sleep
import random
from .display_logic import DisplayGrid


class Game:
	def __init__(self):
		self.display_object = DisplayGrid()
		self.levels = {"easy": 6, "medium": 8, "expert": 10}
		self.grid = []
		self.points = 0
		self.help_flag = 3
		
	def play(self, game_level):
		letters = "ABCDEFGHIJKLMNOPQRSTU"
		matching = False
		if game_level in self.levels:
			grid_size = int(self.levels[game_level])
			
			for i in range(grid_size):
				grid_value = random.sample(letters, grid_size)
				self.grid.append(grid_value)
			self.display_object.show_grid(self.grid, grid_size)
			print("Please wait...")
			sleep(10)
			self.display_object.hide_grid(grid_size)
			while True:
				for x_input in range(1):
					
					positionx = input("Enter Coordinate Values: ")
					positiony = input("Enter Coordinate Values: ")
					
				if positiony == "q" or positionx == "q":
					return self.stop()
				
				if positiony == "h" or positionx == "h":
					if self.help_flag < 1:
						self.display_object.show_grid(self.grid, grid_size)
						self.help_flag = self.help_flag - 1
						print("You have (%d) chances left" %self.help_flag)
						sleep(8)
						self.display_object.hide_grid(grid_size)
					else:
						print("You have (%d) chances to view help" % self.help_flag)
						self.display_object.hide_grid(grid_size)
				
				if ',' in positiony and ',' in positionx:
					Row1 = int(positionx.split(',')[0])
					Col1 = int(positionx.split(',')[1])
					Row2 = int(positiony.split(',')[0])
					Col2 = int(positiony.split(',')[1])
				
					for grid_row in range(grid_size):
						for grid_col in range(grid_size):
							if self.grid[Row1-1][Col1-1] == self.grid[Row2-1][Col2-1]:
								matching = True
				if matching:
					self.points = self.points + 2
				print("You have accumulated: (%d) points and unlocked: (%d) keys." % (self.points, self.points))
				
	def pause(self):
		print("Paused: ")
	
	def restart(self):
		
		print("Restarted:")
	
	def stop(self):
		
		print("stopped:")
		
	def help(self):
		os.system('clear')
		print(
			"Memory presents a grid of numbers with (rows and columns).The grid will appear on screen "
			"displaying initial values in it for 3 seconds, your task is to reproduce(unlock) the matching "
			"rows and columns by entering their positions e.g(3,5), (3,3) for A A. At the end of the game, "
			"we calculate the time it takes you to unlock  values and the number of points you have accumulated."
		)
