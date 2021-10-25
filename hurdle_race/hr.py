def hurdle_race(k:int, height:list)->int:
    """
    """
    if max(height)-k < 0:
        return 0
    else:
        return max(height)-k


if __name__ == "__main__":
    print(hurdle_race(4, [1, 6, 3, 5, 2]))
    print(hurdle_race(7, [2, 5, 4, 5, 2]))