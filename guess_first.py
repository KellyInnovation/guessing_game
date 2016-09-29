import random


	
	while True:
		for difficulty_level in DIFFICULTIES:


	if difficulty_level == "1":
		return(random.randrange(1,10,1))
	elif difficulty_level == "2":
		return(random.randrange(1,100,1))
	elif difficulty_level == "3":
		return(random.randrange(1,1000,1))
	else:
		print("\n{} Please enter a difficulty level.")
		print(DIFFICULTIES)

	if difficulty_level == "1":
		guess = input("Choose a number between 1 and 10:  ")
	elif difficulty_level == "2":
		guess = input("Choose a number between 1 and 100:  ")
	elif difficulty_level == "3":
		guess = input("Choose a number between 1 and 1000:  ")
	return guess

	if guess == magic_number:
		print("You Win!")
	elif guess < magic_number:
		print("Your guess is too low.")
	elif guess > magic_number:
		print("Your guess is too high.")
	
game()

DIFFICULTIES = (
	"1: Easy",
	"2: Medium",
	"3: Hard",
)

def get_difficulty_level(DIFFICULTIES):
	"""
	Display a menu and return the user's selection
	"""
	print("\n")
	for difficulty in DIFFICULTIES:
		print(dif)



class Game():


	print(DIFFICULTIES)
	difficulty_level = input("Choose your level:  ")

	def

def main():
	pass

if __name__ == '__main__':
	main()
