import math

# 1
print(math.pi)
print("pi is {:.4f}".format(math.pi))
print("pi is {:8.4f}".format(math.pi))
print("pi is {:<8.2f}".format(math.pi))

# 2
# what for means
my_str = 'abc'
for char in 'abc':
    print(char)

# 3
# our implementation of the find function. prints the index where
# the target is found ; a failure message, if it isn't found.
# this version  only searches for a single character

river = 'Mississippi'
target = input('input a character to find: ')
for index in range(len(river)):  # for each index
    if river[index] == target:  # check if the target is found
        print("Letter found at index: ", index)  # if so, print the index
        break  # stop searching
else:
    print('letter', 'target', 'not found in', river)

# 4
name = 'John Marwood Cleese'
first, middle, last = name.split()
transformed = last + ',' + first + ' ' + middle
print(transformed)
print(name)
print(first)
print(middle)


# 5
# palindrome tester
def palindrome():
    user_input = input("Enter a word")
    rev = user_input[::-1]
    if rev == user_input:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")


print(palindrome())
