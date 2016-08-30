import random

magic_number = random.randrange(1,100,1)

def game():
	count = 10
	while (count > 0):
		player_number = int(input("Choose a number between 1 and 100:  "))
		if player_number == magic_number:
			print("You Win!")
			break
		elif player_number < magic_number:
			print("Your guess is too low.")
		elif player_number > magic_number:
			print("Your guess is too high.")
		count = count - 1

game()