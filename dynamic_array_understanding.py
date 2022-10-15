from sys import getsizeof

numbers = []
print(getsizeof(numbers))

# numbers.append(1)
# print(getsizeof(numbers))
# numbers.append(2)
# numbers.append(3)
# numbers.append(4)
# print(getsizeof(numbers))

# numbers.append(5)
# print(getsizeof(numbers))

for index in range(25):
    numbers.append(index)
    print(getsizeof(numbers))