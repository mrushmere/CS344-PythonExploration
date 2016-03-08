# Mark Rushmere
# CS 344
# Description: This program creates three different texts files containing 10 random
# lower case letters and prints the strings. It then prints out two random numbers and their product

import sys
import string
import random

def main():
	for i in range(0, 3):
		filename = "file" + str(i) + ".txt"
		randomString = ""
		target = open(filename, "w")
		for j in range(0, 10):
			# only want the first 26 letters that are lower case
			randomLetter = random.choice(string.letters[:26])
			randomString += randomLetter
		# Print string and write to file, then close file
		print randomString
		target.write(randomString)
		target.close()


	# print out two random integers and their sum
	rand1 = random.randint(1, 42)
	rand2 = random.randint(1, 42)
	print str(rand1) + " * " + str(rand2) + " = " + str(rand1*rand2)

if __name__ == "__main__":
	main()

