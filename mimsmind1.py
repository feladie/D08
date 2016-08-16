import random
import sys

# def intro():
# 	"""Introduces the player to the game. Asks the player whether or not 
# 	they would like to choose the number of digits to play with.
# 	"""
# 	length = input()
# 	print("Let's play the mimsmind1 game.")
# 	return length

def exceptions(s):
	try:
		for n in range(1, digits + 1):
			int(s[digits - n])
	except ValueError:
		print("Invalid input. Try again: ")

def mastermind():
	digits = 3
	if len(sys.argv) > 1:
		digits = int(sys.argv[1])
	maximum = 10 ** digits
	int_answer = random.randint(0, maximum)
	answer = str(int_answer)
	answer = '0' * (digits - len(answer)) + answer
	count = 0
	max_guesses = 2 ** digits + digits

	guess = input('Guess a {}-digit number: '.format(digits))	# Initial message to guess.

	while count < max_guesses - 1:
		count += 1
		guess = input('Guess a {}-digit number: '.format(digits))
		try:
			for n in range(1, digits + 1):
				int(guess[digits - n])
		except ValueError:
				print("Invalid input. Try again: ")
		else:
			if len(input) > digits:
				print("Invalid input. Try again: ")

			elif len(input) < digits:
				print("Invalid input. Try again: ")
		
		bulls = 0
		cows = 0
		if input == answer:
			print("Congratulations. You guessed the right answer in {} tries.".format(count))
			break
		elif len(input) < digits:

		


	# guess = ''
	# player_digits = intro()
	# digits = 3
	# if player_digits == '':	# Determine the number of digits to guess with
	# 	digits = 3
	# else:
	# 	digits = int(player_digits)

	# count = 0
	# max_guess = 2 ** digits + digits
	# max_range = 10 ** digits
	# # print("max: ", max_range)
	# # min_range = 10 ** (digits - 1)
	# # print("min: ", min_range)
	# answer = random.randint(0, max_range)
	# str_answer = str(answer)
	# length_str = len(str_answer)
	# if length_str < digits:
	# 	str_answer = '0' * (digits - length_str) + str_answer

	# while True:
	# 	guess = input('Guess a {}-digit number: '.format(digits))
	# 	try:
	# 		for n in range(1, digits + 1):
	# 			int(guess[digits - n])
	# 		breakt
	# 	except:
	# 		print('Invalid input. Try again: ')

	# while count < max_guess - 1:
	# 	count += 1
	# 	if guess == str_answer:
	# 		print("Congratulations. You guessed the right answer in {} tries.".format(count))
	# 		break
	# 	elif int(guess) > answer:
	# 		if int(guess) >= max_range:
	# 			guess = input(('Invalid input. Try again: ')
	# 			try:
	# 				for n in range(1, digits + 1):
	# 					int(guess[digits - n])
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