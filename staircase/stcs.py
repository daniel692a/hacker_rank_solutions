def staircase(n:int):
    """
    Print a staircase of size n.
    """
    # for i in range(n, 0, -1):
    #     white_spaces = i -1
    #     if i == 1:
    #         print('#'*(n))
    #     else:
    #         print(' '* white_spaces + '#'*(n-white_spaces))
    for i in range(1, n+1):
        print(' '*(n-i) + '#'*i)

if __name__ == '__main__':
    n = 6
    staircase(n)
