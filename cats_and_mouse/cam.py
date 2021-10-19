def cat_and_mouse(x:int, y:int, z:int) -> str:
    if abs(x - z) == abs(y - z):
        return 'Mouse C'
    elif abs(x - z) < abs(y - z):
        return 'Cat A'
    else:
        return 'Cat B'


if __name__ == '__main__':
    print(cat_and_mouse(1, 2, 3))
    print(cat_and_mouse(1, 3, 2))