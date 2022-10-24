# set comprehension
num_list = [1, 32, 5, 0, -4]
num_set = {num ** 3 for num in num_list if num >= 0}
print(num_set)

num_set = {num for num in range(0, 30, 3) }
print(num_set)