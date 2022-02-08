#Password Generator Project: simple password and shuffled password
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#set the list for the complex password 
list = []
#set the string for the simple password
password = ""

for letter in range(nr_letters):
  letter = random.choice(letters)
  list.append(letter)
  password += str(letter)

for symbol in range(nr_symbols):
  symbol = random.choice(symbols)
  list.append(symbol)
  password += str(symbol)

for number in range(nr_numbers):
  number = random.choice(numbers)
  list.append(number)
  password += str(number)

print("Your simple password is: " + password)

#shuffle the list
random.shuffle(list)

password_shuf = ""
for character in range(nr_letters+nr_symbols+nr_numbers):
  password_shuf += str(list[character])
  
print("Your shuffled password is: " + password_shuf)
