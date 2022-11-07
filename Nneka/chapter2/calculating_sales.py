total = 0
price = 0
while True:
    product = int(input("Enter product number: "))
    quantity = int(input("Enter quantity sold: "))
    match product:
        case 1:
            price = 2.98 * quantity
        case 2:
            price = 4.50 * quantity
        case 3:
            price = 9.98 * quantity
        case 4:
            price = 4.49 * quantity
        case 5:
            price = 6.87 * quantity
    total = total + price
    more = input("More product ?: ")
    if more != 'yes':
        print(f'Total value of all product sold: ${total: .2f}')
        break
