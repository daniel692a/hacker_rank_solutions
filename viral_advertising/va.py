def viral_advertising(n):
    likes, shares = 2, 5
    for i in range(1, n):
        shares = (shares//2)*3
        likes += (shares//2)
    return likes

if __name__ == "__main__":
    print(viral_advertising(5))
    print(viral_advertising(3))