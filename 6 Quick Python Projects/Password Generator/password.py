import random
from string import ascii_letters, punctuation

def password_generator(NumberOf, length):
	chars = ascii_letters+punctuation

	for i in range(NumberOf):
		passwords = random.sample(chars, length)
		yield passwords


print('Welcome to Password Generator')
NumberOf = int(input('How many password you want to generate? '))
length = int(input("How many characters do you want? "))

for password in password_generator(NumberOf, length):
	print(''.join(password))