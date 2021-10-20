def angry_professor(k:int, a:list) -> str:
    """
    Given an array of integers representing the arrival times of each student,
    determine if the class is cancelled.
    """
    return "YES" if sum(map(lambda x: x<=0, a)) < k else "NO"


if __name__ == "__main__":
    print(angry_professor(3, [-1, -3, 4, 2]))
    print(angry_professor(2, [0, -1, 2, 1]))

