import random

def intro():
	"""Introduces the player to the game. Asks the player whether or not 
	they would like to choose the number of digits to play with.
	"""
	length = input()
	print("Let's play the mimsmind1 game.")
	return length


def mastermind():
	guess = ''
	player_digits = intro()
	digits = 3
	if player_digits == '':	# Determine the number of digits to guess with
		digits = 3
	else:
		digits = int(player_digits)

	count = 0
	max_guess = 2 ** digits + digits
	max_range = 10 ** digits
	# print("max: ", max_range)
	# min_range = 10 ** (digits - 1)
	# print("min: ", min_range)
	answer = random.randint(0, max_range)
	str_answer = str(answer)
	length_str = len(str_answer)
	if length_str < digits:
		str_answer = '0' * (digits - length_str) + str_answer

	while True:
		guess = input('Guess a {}-digit number: '.format(digits))
		try:
			for n in range(1, digits + 1):
				int(guess[digits - n])
			break
		except:
			print('Invalid input. Try again: ')

	while count < max_guess - 1:
		count += 1
		if guess == str_answer:
			print("Congratulations. You guessed the right answer in {} tries.".format(count))
			break
		elif int(guess) > answer:
			if int(guess) >= max_range:
				guess = input(('Invalid input. Try again: ')
				try:
					for n in range(1, digits + 1):
						int(guess[digits - n])
	# 			except: 
	# 				print('Invalid input. Try again: ')
	# 		else: 
	# 			guess = input(('Invalid input. Try again: ')
	# 			try:
	# 				for n in range(1, digits + 1):
	# 					int(guess[digits - n])
	# 			except: 
	# 				print('Invalid input. Try again: ')
	# 	elif int(guess) < answer:
	# 		if guess < 0:
	# 			guess = input(('Invalid input. Try again: ')
	# 				try:
	# 					for n in range(1, digits + 1):
	# 						int(guess[digits - n])
	# 				except: 
	# 					print('Invalid input. Try again: ')
	# 		else:
	# 			guess = input(('Invalid input. Try again: ')
	# 			try:
	# 				for n in range(1, digits + 1):
	# 					int(guess[digits - n])				
	# 			except:
	# 				print('Invalid input. Try again: ')
				
	# else:
	# 	print('Sorry. You did not guess the number in {} tries. The correct number is {}.'.format(max_guess, answer))
		


def main():
	# print(intro())
	# length()
	mastermind()

if __name__ == '__main__':
	main()