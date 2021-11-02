def jumping_on_the_clouds(c:list)->int:
    """
    Function that calculates the minimum number of jumps needed to win the game.
    """
    jumps, i = 0, 0
    while i < len(c) - 1:
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    return jumps


if __name__ == "__main__":
    print(jumping_on_the_clouds([0, 0, 1, 0, 0, 1, 0]))
    print(jumping_on_the_clouds([0, 0, 0, 1, 0, 0]))