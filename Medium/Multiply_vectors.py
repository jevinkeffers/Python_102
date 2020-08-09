# Multiply Vectors
# Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists.

list_1 = [4, 8, 15]
list_2 = [16, 23, 42]
new_list = []
for num1, num2 in zip(list_1, list_2):
    new_list.append(num1 * num2)
print(new_list)

#Had to look up the zip method, but SOLVED#