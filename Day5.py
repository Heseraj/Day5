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

#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%