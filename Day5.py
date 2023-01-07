# The concept of loop

fruits = ["apple", "peach", "pear"]
for fruit in fruits:
    print(fruit)

#%% *.mr

height_list = input("print a list of students heights! \n").split(",")
# when typing numbers be sure to not add comma after the last number
print(height_list)
total_h = 0
# print(type(height_list))

for height in range(0, len(height_list)):
    total_h += int(height_list[height])
    print(total_h)
    ave_height = total_h/len(height_list)
    ave_height = round(ave_height)
print(ave_height)

#%%
height_list = input("print a list of students heights! \n").split(",")
# when typing numbers be sure to not add comma after the last number
print(height_list)
total_h = 0
total_s = 0
# print(type(height_list))
for height in height_list:
    total_h += int(height)
print(total_h)

for student in height_list:
    total_s += 1
print(total_s)

ave_height = round(total_h/total_s)
print(f"the average height of studetns is {ave_height}")


#%%
height_list = input("print a list of students heights! \n").split(",")
# when typing numbers be sure to not add comma after the last number
print(height_list)
total_h = 0
total_s = 0
# print(type(height_list))
for height in height_list:
    total_h += int(height)
    total_s += 1
print(total_s)
print(total_h)
ave_height = round(total_h / total_s)
print(f"the average height of studetns is {ave_height}")

#%% Highest score

height_list = input("print a list of students heights! \n").split(",")
# print(height_list[0])
max_height = 0
for height in height_list:
    if int(height) > max_height:
        max_height = int(height)
    else:
        max_height = max_height
print(f"The highest student in the group is {max_height} cm tall! ")

#%%  range function

tot_sum = 0
for number in range(20, 30):
    tot_sum += number
print(tot_sum)

#%%

tot_even = 0
for number in range(1, 101):
    if number % 2 == 0:
        tot_even += number
    else:
        tot_even = tot_even
print(tot_even)

#%% Fizz Buzz Interview coding questions

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
#%% Generating Passwords Will figure this later.
# import random
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# symbols = ["!", "#", "$", "%", "(", ")", "*", "+"]
#
# print(f"len of letters is {len(letters)}, numbers is {len(numbers)} and symbols is {len(symbols)}")
#
# print("Welcome to your password generateor! ")
# nr_letters = int(input("how many letters do you like your password to have? \n"))
# nr_numbers = int(input("how many number do you like your password to have? \n"))
# nr_symbols = int(input("how many symbols do you like your password to have? \n"))
#
# let_list = ""; num_list = ""; sym_list = ""; password_easy = ""
#
# for i in range(0, nr_letters):
#     letter = random.randint(0, len(letters))
#     # print(letters[letter])
#     # let_list += letters[letter]
#     password_easy.append(letter)
#     print(password_easy)
#     # print(let_list)
# for i in range(0, nr_numbers):
#     number = random.randint(0, len(numbers))
#     num_list += str(numbers[number])
# for i in range(0, nr_symbols):
#     symbol = random.randint(0, len(symbols))
#     sym_list += str(symbols[symbol])
# #     print(sym_list)
# print(let_list)
# print(num_list)
# print(sym_list)
#
#
#
# # for i in range(0, nr_letters):
# #     random.randint()

#%%

import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "(", ")", "*", "+"]

print(f"len of letters is {len(letters)}, numbers is {len(numbers)} and symbols is {len(symbols)}")
nr_letters = int(input("how many letters do you like your password to have? \n"))
nr_numbers = int(input("how many number do you like your password to have? \n"))
nr_symbols = int(input("how many symbols do you like your password to have? \n"))

pass_list = []

for letter in range(1, nr_letters + 1):
    pass_list.append(random.choice(letters))
for number in range(1, nr_numbers + 1):
    pass_list.append(random.choice(numbers))
for symbol in range(1, nr_symbols):
    pass_list.append(random.choice(symbols))
print(pass_list)
random.shuffle(pass_list)
print(pass_list)

final_pass = ""
for char in pass_list:
    final_pass += char
print(f"your final strong password is: {final_pass}")

#%%
#%%
#%%