def plus_minus(arr:list):
    """
    Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
    """
    positive, negative, zero = 0, 0, 0
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1
    print(format(positive/len(arr), ".6f"))
    print(format(negative/len(arr), ".6f"))
    print(format(zero/len(arr), ".6f"))

if __name__ == '__main__':
    num = [1, 1, 0, -1, -1]
    plus_minus(num)
    num_2 = [-4, 3, -9, 0, 4, 1]
    plus_minus(num_2)