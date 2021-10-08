def birthday(s:list, d:int, m:int):
    """
    >>> birthday([4, 2, 1, 3, 5], 4, 2)
    3
    >>> birthday([1, 1, 1, 1, 1, 1], 3, 5)
    0
    >>> birthday([4], 4, 1)
    1
    >>> birthday([4], 4, 0)
    0
    >>> birthday([], 4, 0)
    0
    """
    count = 0
    for i in range(len(s)):
        if sum(s[i:i+m]) == d:
            count += 1
    return count


if __name__ == "__main__":
    print(birthday([4, 2, 1, 3, 5], 4, 2))