if __name__ == '__main__':
    # how to write dictionary
    paragon = {
        "name_one": "John Doe",
        "name_two": "Peter Dry",
        "name_three": "Jim Berlin",
        "name_four": "Lee min hu",
        "name_five": "Kahane Pinky",
        "name_six": "Catalina Hank",
    }
    print(paragon)

    # how to print a particular name
    print(paragon["name_four"])

    # how to replace a particular name
    paragon["name_four"] = "oladele"
    print(paragon.values())

    # how to add key
    paragon["name_seven"] = "oppa"
    print(paragon)

    # pop remove both the key and value
    paragon.pop("name_six")
    print(paragon)

    val = paragon.get("name_one")
    print(val)

    # the turple
    maa = ("oppa", "Hii", "Say Hi")

    # the form covert tuple to dictionary
    _dixt = paragon.fromkeys(maa)

    _dixt["Oppa"] = "Anky pankie"
    _dixt["Hii"] = "Jude Family"
    _dixt["Say Hii"] = "Youth Pastor Family"
