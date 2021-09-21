import colorama

def simple_array_sum(ar: list)->int:
    """
    Return the sum of the array's elements as a single integer.
    ar = [1, 7, 9, 3]
    simple_array_sum(ar)
    >>> 20
    """
    sum_ar = 0
    for num in ar:
        sum_ar += num
    return sum_ar

if __name__ == "__main__":
    ar = [1, 7, 9, 3]
    ar_2 = [10, 5, 7, 32]
    print(simple_array_sum(ar))
    print(simple_array_sum(ar_2))