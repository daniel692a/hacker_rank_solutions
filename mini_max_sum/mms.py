def mini_max_sum(arr):
    """
    Given an array of 5 integers, find the minimum and maximum values
    that can be calculated by summing exactly 4 of the 5 integers.
    Then print the respective minimum and maximum values as a single
    line of two space-separated long integers.
    """
    # max_val, min_val = max(arr), min(arr)
    # min_sum, max_sum = 0, 0
    # for num in arr:
    #     if min_val == max_val:
    #         min_sum = min_val * 4
    #         max_sum = max_val * 4
    #     else:
    #         if num<max_val:
    #             min_sum += num

    #         if num>min_val:
    #             max_sum += num

    # print(min_sum, max_sum)
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    print(min_sum, max_sum)

if __name__ == "__main__":
    arr = [5, 5, 5, 5, 5]
    arr_2 = [5, 7, 9, 2, 1]
    mini_max_sum(arr)
    mini_max_sum(arr_2)