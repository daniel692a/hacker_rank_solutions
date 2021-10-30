def save_the_prisioner(n, m, s):
    return ((s-1 + m-1)%n)+1

if __name__ == '__main__':
    print(save_the_prisioner(5, 2, 1))
    print(save_the_prisioner(5, 2, 2))
