def apple_and_orange(s ,t , a , b , apples , oranges):
    count_apple, count_orange = 0, 0
    for apple in apples:
        if (apple+a >= s) and (apple+a <= t):
            count_apple +=1
    for orange in oranges:
        if (orange+b >=s) and (orange+b <= t):
            count_orange += 1
    print(count_apple)
    print(count_orange)


if __name__ == '__main__':
    apple_and_orange(7,10,4,12,[2,3,-4],[3,-2,-4])