#!/usr/bin/env python3
# HW08_ch11_ex02c.py
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
###############################################################################
# Imports


# Body
def reverse_lookup_old(d, v):
	for k in d:
		if d[k] == v:
			return k
	raise ValueError


def reverse_lookup_new(d, v):
	result = []
	for k in d:
		if d[k] == v:
			result.append(k)
	return result


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
pledge_histogram = {}

def histogram_old(s):
	d = dict()
	for c in s:
		count = d.get(c, 0)
		d[c] = count + 1
	return d


def histogram_new(s):
	return histogram_old(s)


def get_pledge_list():
	""" Opens pledge.txt and converts to a list, each item is a word in
	the order it appears in the original file. returns the list.
	"""
	# Your code here.
	pledge_list = []
	with open('pledge.txt', 'r') as f:
		for each_line in f:
			words = each_line.split()
			for each_word in words:
				pledge_list.append(each_word)
	return pledge_list

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():   # DO NOT CHANGE BELOW
	pledge_histogram = histogram_new(get_pledge_list())
	print(reverse_lookup_new(pledge_histogram, 1))
	print(reverse_lookup_new(pledge_histogram, 9))
	print(reverse_lookup_new(pledge_histogram, "Python"))

if __name__ == '__main__':
	main()
