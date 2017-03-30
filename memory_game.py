#! usr/bin/env python
import time

from game import Game

"author == Ash"
class Main:
	def __init__(self):
		
		self.elapsed = 0.0
		self.game_instance = Game()
	
	def initialize(self):
		
		level = "Welcome to Memory: This game is about memorizing and re-displaying the grid" \
		        " in the same way it appears.\n" \
		        "Press Enter to continue.......or (q) to exit.\n"
		
		print level
		user_prompt = raw_input()
		if user_prompt == "q":
			self.game_instance.stop()
		else:
			self.capture_user_selection()
			
	def capture_user_selection(self):
		print "Press (h) for help, (q) to quit the game \n " \
		      "Select game level to proceed\n1) Easy\n2) Medium\n3) Hard"
		while True:
			
			user_prompt = raw_input()
			
			if user_prompt == "q":
				return self.stop()
			elif user_prompt == "h":
				print self.game_instance.help()
			elif int(user_prompt) == 1:
				game_level = "easy"
				return self.game_instance.play(game_level)
			elif int(user_prompt) == 2:
				game_level = "medium"
				return self.game_instance.play(game_level)
			elif int(user_prompt) == 3:
				game_level = "hard"
				return self.game_instance.play(game_level)
			else:
				continue
if __name__ == '__main__':
	
	main_object = Main()
	main_object.initialize()
