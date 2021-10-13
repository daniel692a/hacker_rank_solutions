def bill_divison(bill:list, k:int, b:int):
    cost = 0
    for i in range(len(bill)):
        if i == k:
            continue
        else:
            cost += bill[i]

    div_bill = cost/2
    if div_bill == b:
        print('Bon Appetit')
    else:
        print(int(b - div_bill))

if __name__ == '__main__':
    bill_divison([3, 10, 2, 9], 1, 12)
    bill_divison([3, 10, 2, 9], 1, 7)