#!/usr/bin/env python3
# HW08_ch11_ex01
# Write a function that reads the words in words.txt and stores them as keys
# in a dictionary (returning the dictionary). It doesn’t matter what the
# values are. Then you can use the in operator as a fast way to check whether
# a string is in the dictionary.
###############################################################################
# Imports


# Body
def store_to_dict():
	""" Reads the words in words.txt and stores them as keys in a dictionary.
	"""
	d = dict()
	with open('words.txt', 'r') as f:
		for each_line in f:
			words = each_line.split()
			for each_word in words:
				d[each_word] = ''
	return d


###############################################################################
def main():  # DO NOT CHANGE BELOW
	words_dict = store_to_dict()
	if "this" in words_dict:
		print("Yup.")
	if "qwertyuiop" in words_dict:
		print("Hmm.")

if __name__ == '__main__':
	main()
