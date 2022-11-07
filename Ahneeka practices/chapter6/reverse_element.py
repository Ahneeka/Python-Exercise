my_str = 'This is a test'
string_element = my_str.split()  # todo lit of words
print(string_element)

reversed_element = []
for element in string_element:  # todo for each word
    reversed_element.append(element[:: -1])  # todo reverse , append

print(reversed_element)
new_str = ' '.join(reversed_element)  # todo join  with space separator
print(new_str)
