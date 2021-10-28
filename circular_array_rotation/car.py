def circular_rotation_array(a:list, k:int, queires:list)->list:
    for i in range(k):
        a.insert(0, a.pop())
    return [a[i] for i in queires]

if __name__ == '__main__':
    print(circular_rotation_array([1, 2, 3], 2, [0, 1, 2]))