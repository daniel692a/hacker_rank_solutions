def divisible_sum_pairs(n: int, k:int, ar:list) -> int:
    """
    Given an array of integers and a number k,
    find the number of pairs of integers in the array
    whose sum is divisible by k.
    """
    pairs_count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                pairs_count += 1
    return pairs_count

if __name__ == "__main__":
    print(divisible_sum_pairs(6, 3, [1, 3, 2, 6, 1, 2]))
    print(divisible_sum_pairs(5, 2, [5, 9, 10, 7, 4]))