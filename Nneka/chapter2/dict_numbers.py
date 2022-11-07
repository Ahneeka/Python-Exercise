# todo 1. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# todo Sample Dictionary ( n = 5) :
# todo Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


if __name__ == '__main__':
    numbers = int(input("Enter a number"))
    d = dict()

    for x in range(1, 1 + numbers):
        d[x] = x * x
    print(d)


