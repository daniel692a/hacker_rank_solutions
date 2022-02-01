def solve(s):
    words = s.split(" ")
    new_s = [word.capitalize() for word in words]
    return " ".join(new_s)


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)