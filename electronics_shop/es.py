def get_money_spent(keyboards:list, drives:list, b:int)->int:
    """
    :param keyboards: list of ints
    :param drives: list of ints
    :param b: int
    :return: int
    """
    max_price = -1
    for keyboard in keyboards:
        for drive in drives:
            if keyboard + drive <= b and keyboard + drive > max_price:
                max_price = keyboard + drive
    return max_price
    # if (min(keyboards) >= b) or (min(drives)>=b) or ((min(keyboards) + min(drives))>b):
    #     return -1
    # else:
    #     costs = []
    #     for i in range(len(drives)):
    #         for j in range(len(keyboards)):
    #             if drives[i] + keyboards[j] <= b:
    #                 costs.append(drives[i] + keyboards[j])
    #             else:
    #                 break
    #     return max(costs)

if __name__ == '__main__':
    print(get_money_spent([3, 1], [5, 2, 8], 10))