def reverse_lookup(d, value):
	res = []
	for item in d:
		if d[item] == value:
			res.append(item)
	return res

def main():
	d = {"Daniel" : "blue", "SomeoneOne" : "blue", "SomeoneTwo" : "red"}
	print(reverse_lookup(d, "blue"))
	print(reverse_lookup(d, "red"))

if __name__ == '__main__':
	main()

