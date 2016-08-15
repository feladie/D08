import random

def intro():
	"""Introduces the player to the game. Asks the player whether or not 
	they would like to choose the number of digits to play with.
	"""
	print("Let's play the mimsmind0 game.")
	# answer = input("Would you like to choose the number of digits you will play with? (yes/no): ")
	# if answer.lower() == 'yes':
	# 	return True
	# elif answer.lower() == 'no':
	# 	return False
	# else: 
	# 	print("Oops! Please only write yes or no.")
	# 	return intro()


def length():
	"""Allows the player to choose the number of digits they play with.
	"""
	while True:
		try:
			length = int(input("Please enter the number of digits you would like to play with: ")) 
			return length
		except:
			print("Oops! Please enter an integer: ")	


def mastermind():
	player_digits = intro()
	digits = 1
	# if player_digits == True:	# Determine the number of digits to guess with
	# 	digits = length()
	# else:
	# 	digits = 1

	count = 1
	max_range = 10 ** digits
	# print("max: ", max_range)
	min_range = 10 ** (digits - 1)
	# print("min: ", min_range)
	answer = random.randint(min_range, max_range)
	# print("Answer: ", answer)
	guess = ''

	while True:
		try:
			guess = int(input('Guess a {}-digit number: '.format(digits)))
			break
		except:
			print('Oops! Please guess an integer. ')

	while guess != answer:
		count += 1
		if guess > answer:
			if guess >= max_range:
				try:
					guess = int(input(('Oops! Guess a {}-digit number. '.format(digits))))
				except:
					print("Warning: please input an integer. ")
			else: 
				try:
					guess = int(input(('Try again. Guess a lower number. ')))
				except: 
					print("Warning: please input an integer. ")
		elif guess < answer:
			if guess < min_range:
				try:
					guess = int(input(('Oops! Guess a {}-digit number. '.format(digits))))
				except:
					print("Warning: please input an integer. ")
			else:
				try:
					guess = int(input(('Try again. Guess a higher number. ')))
				except:
					print("Warning: please input an integer. ")
				
	else:
		print("Congratulations. You guessed the right answer in {} tries.".format(count))


def main():
	# print(intro())
	# digits()
	mastermind()

if __name__ == '__main__':
	main()