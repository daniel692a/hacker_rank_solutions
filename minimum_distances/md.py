def minimum_distance(a:list)->int:
    for d in range(1, len(a)):
        for i in range(len(a)-d):
            if a[i] == a[i+d]:
                return d
    return -1


if __name__ == '__main__':
    print(minimum_distance([7, 1, 3, 4, 1, 7]))
    print(minimum_distance([1, 2, 1, 2, 1, 2, 1]))