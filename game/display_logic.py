import os


class DisplayGrid:
	def __init__(self):
		self.box_initials = "*"
		
	def show_grid(self, grid_type, grid_size):
		os.system('cls' if os.name == 'nt' else 'clear')
		
		for n in range(grid_size):
			index = n+1
			print(
				str(index)+Colors.OKBLUE+' | ' +Colors.ENDC+'  '.join(grid_type[n]) +
				Colors.OKBLUE+' | '+Colors.ENDC+str(index)
			)
		
	def hide_grid(self, grid_size):
		os.system("clear")
		for n in range(grid_size):
			index = n + 1
			print(
				str(index) + Colors.OKBLUE + ' | ' + Colors.ENDC + self.box_initials*grid_size +
				Colors.OKBLUE + ' | ' + Colors.ENDC + str(index)
			)
			
	def random_grid(self):
		pass
	

class Colors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
