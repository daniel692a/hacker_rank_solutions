def beautiful_days(i:int, j:int, k:int) -> int:
    count = 0
    for x in range(i, j+1):
        if abs(int(str(x)[::-1])-x) % k == 0:
            count += 1
    return count

if __name__ == "__main__":
    print(beautiful_days(20, 23, 6))