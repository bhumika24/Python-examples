# Copying the entire list.
value1 = [1]
value2 = value1[:]
value1[0] = 2
print(value2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
