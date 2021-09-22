def a_very_big_sum(ar:list)->int:
    result = 0
    for i in ar:
        result += i
    return result

if __name__ == '__main__':
    print(a_very_big_sum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))