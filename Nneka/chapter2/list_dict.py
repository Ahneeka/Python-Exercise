# todo 3. Write a program to convert two lists into a dictionary.
# todo list1(values) = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred']
# todo list2(key) = [10, 20, 30, 40,  50, 60, 70, 80, 90, 100]
# todo use a loop to iterate through and print the values of the dictionary.

if __name__ == '__main__':
    test1_values = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety", "Hundred"]
    test2_key = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print("original values list is: " + str(test1_values))
    print("original key  list is: " + str(test2_key))

    dictionary = dict()
    for i in range(len(test1_values)):
        dictionary[test2_key[i]] = test1_values[i]

    print(dictionary)
