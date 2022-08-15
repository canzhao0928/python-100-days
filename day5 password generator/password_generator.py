from operator import index
from random import choice, random, shuffle


letters =list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers=list("0123456789")
symbols=list("!@#$%^&*()")

password=[]
# password_random=[]
print("Welcome to the PyPassword Generator!")
letters_num=input("How many letters would you like in your password?")
symbols_num=input("How many sumbols would you like?")
numbers_num=input("How many numbers would you like?")

for i in range(int(letters_num)):
    password.append(choice(letters))
for i in range(int(numbers_num)):
    password.append(choice(numbers))
for i in range(int(symbols_num)):
    password.append(choice(symbols))

# random the sequence
# for i in range(len(password)):
#     element= choice(password)
#     password.pop(password.index(element))
#     password_random.append(element)
shuffle(password)

# print("Your password is:", ''.join(password_random))
print("Your password is:", ''.join(password))