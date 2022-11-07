import math


def number_of_offenders(current_balance, expected_balance, offenders_balance):
    total_expected_balance = 27500
    current_balance = 4300
    amount_remaining = total_expected_balance - current_balance
    no_of_offenders = amount_remaining / offenders_balance
    return no_of_offenders


if __name__ == '__main__':
    x = number_of_offenders(4300, 27500, 100)
    print(math.ceil(x))
