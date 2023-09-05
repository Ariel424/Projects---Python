# This Python code is a password generator program. It prompts the user to specify how many letters, numbers, and symbols they want in their password.

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print ("Welcome To Password Generator!")
nr_letters = int(input ("Please choose how many letters your want in your password:\n"))
nr_numbers = int(input ("Please choose how many numbers your want in your password:\n"))
nr_symbols = int(input ("Please choose how many symbols your want in your password:\n"))

your_password = []

for char in range (1, nr_letters + 1):
  your_password += random.choice (letters) 

for char in range (1, nr_numbers + 1):
  your_password.append (random.choice (numbers))

for char in range (1, nr_symbols + 1):
  your_password.append (random.choice (symbols))

random.shuffle (your_password) 

password = " "
for char in your_password:
  password += char

print (f"Your Random password is:{password})")



