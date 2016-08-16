import random
import sys

def mastermind():
	digits = 3
	if len(sys.argv) > 1:	# Set the number of digits
		digits = int(sys.argv[1])
	maximum = 10 ** digits
	int_answer = random.randint(0, maximum)
	answer = str(int_answer)
	answer = '0' * (digits - len(answer)) + answer # Left-pad the answer with 0s
	count = 1	# Number of guesses
	max_guesses = 2 ** digits + digits

	guess = input('Guess a {}-digit number: '.format(digits))	# Initial message to guess.
	
	while count < max_guesses:
		count += 1
		try: 
			for n in range(1, digits + 1):
				int(guess[digits - n])
		except:
			guess = input("Invalid input. Try again: ")
		else: 
			bulls = 0	# matching number in correct position
			cows = 0	# matching number in incorrect position
			if len(guess) > digits:
				guess = input("Invalid input. Try again: ")
			elif guess == answer:
				print("Congratulations. You guessed the correct number in {} tries.".format(count))
				break
			else:
				for x, y in zip(guess, answer):
					if x == y:
						bulls += 1
				for chars in guess:
					if chars in answer:
						cows += 1
				cows = cows - bulls
				guess = input("{} bull(s), {} cow(s). Try again: ".format(bulls, cows))

	else:
		print("Sorry. You did not guess the number in {} tries. The correct number is {}.".format(count, answer))


def main():
	mastermind()

if __name__ == '__main__':
	main()