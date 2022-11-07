s = "hello world"

print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.swapcase())
print(s.casefold())
print(s.count("You"))
print(s.count("a", 3, 5))
print(s.find("m"))
print(s.find("m",1 ,10))
print(s.casefold())


for u in  range(1, 45,1):
    print("*"*u)

    hello = "hello"
    print (hello.ljust(20, '*'))
    print(hello.rjust(20, '*'))
    print(hello.center(20,'*'))

    for i in range(1, 20, 2):
        s = '*' * i
        print(s.rjust(20))