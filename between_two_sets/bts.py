import functools

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

def get_total_x(a, b):
    counter = 0
    gcd_value =  functools.reduce(gcd, b)
    lcm_value = functools.reduce(lcm, a)
    multiple_of_lcm = lcm_value
    while multiple_of_lcm <= gcd_value:
        if gcd_value % multiple_of_lcm == 0:
            counter += 1
        multiple_of_lcm += lcm_value
    return counter
    # counter = 0
    # for i in range(max(a), min(b)+1):
    #     if all(i % j == 0 for j in a) and all(j % i == 0 for j in b):
    #         counter += 1
    # return counter

if __name__ == '__main__':
    print(get_total_x([2, 4], [16, 32, 96]))
    print(get_total_x([2, 3, 6], [42, 84]))