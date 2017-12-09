#! /usr/bin/env python3.6
import os
from game.game import Game

"author == Ash"


class Main:
	def __init__(self):
		
		self.elapsed = 0.0
		self.game_instance = Game()
	
	def initialize(self):
		
		print(
			"Welcome to the Memory Game: Test your memorizing skills by re-displaying the grid"
			" after it's contents are hidden.\n\nPress Enter to continue... or (q) to exit.\n"
		)
		
		initial_input = input()
		if initial_input == "q":
			self.game_instance.stop()
		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			print(
				"Press (h) for help, (q) to quit the game.\nSelect game "
				"level to proceed\n1) Easy\n2) Medium\n3) Expert"
			)
			while True:
				user_prompt = input()
				if user_prompt == "q":
					return self.game_instance.stop()
				elif user_prompt == "h":
					self.game_instance.help()
				elif int(user_prompt) == 1:
					game_level = "easy"
					return self.game_instance.play(game_level)
				elif int(user_prompt) == 2:
					game_level = "medium"
					return self.game_instance.play(game_level)
				elif int(user_prompt) == 3:

					game_level = "expert"
					return self.game_instance.play(game_level)
				else:
					continue
	

if __name__ == '__main__':
	main_object = Main()
	main_object.initialize()
