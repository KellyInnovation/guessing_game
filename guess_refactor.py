import random

class Game():
	def __init__(self):
		self.difficulty_choice = 0
		self.magic_number = 0
		self.guesses = 0
	
	def get_magic_number(self):
		self.difficulty_choice = int(input("Please choose a difficulty range \n  10\n  100\n  1000\n  :  "))

		self.magic_number = random.randrange(1,self.difficulty_choice,1)

		self.guesses_number()

	def guesses_number(self):
		self.guesses = int(input("How many guesses would you like?   "))

		self.game()

	def game(self):
		print("Guess the magic number.")

		while (self.guesses >= 0):
			player_number = int(input("Choose a number between 1 and {}:  ".format(self.difficulty_choice)))
			if player_number == self.magic_number:
				print("You Win!")
				break
			elif player_number < self.magic_number:
				print("Your guess is too low.")
			elif player_number > self.magic_number:
				print("Your guess is too high.")

			self.guesses -= 1

		print("You lost. \nThe number was {}".format(self.magic_number))			

game_play = Game()
game_play.get_magic_number()