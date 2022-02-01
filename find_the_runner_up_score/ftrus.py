if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    convert = list(arr)
    max_val = max(convert)
    while max(convert) == max_val:
        convert.remove(max_val)
    print(max(convert))