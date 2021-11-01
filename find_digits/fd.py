def find_digits(n:int)->int:
    count = 0
    for digit in str(n):
        if int(digit) == 0:
            continue
        elif n % int(digit) == 0:
            count+=1
    return count

if __name__ == "__main__":
    print(find_digits(12))
    print(find_digits(1012))
