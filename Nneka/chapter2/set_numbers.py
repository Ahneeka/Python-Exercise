# todo 2. Write a Python program to add member(s) in a set. Your program should collect input(5 numbers), validate it (numbers between 2 and 90) and add it to the set.
# todo If the user enters an invalid input, tell the user "Invalid input, try again." Also use a try and except to handle the user entering string values.
count = 1
set_ = set()
print("Enter number between 2 - 90")
while count <= 5:
    try:
        number = int(input(f"number {count} : "))
        if number in set_:
            print("Already added")
            continue
        if 2 <= number <= 90:
            set_.add(number)
            print(set_)
            count += 1
        else:
            print("Invalid input, try again")
    except ValueError:
        print("Invalid input , try again")
