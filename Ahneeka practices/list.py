if __name__ == '__main__':
    _list = ["hi", "paragon", 23, 6.9, ["lowkey", 67, "hello", ["fo", 0.7, "who dey"]]]
    print(_list)

    _list[4][0] = "The value you want to print"
    print(_list)
    _list[4][3][2] = "I want to change it"

    print(_list)