def repeated_string(s:str, n:int)->int:
    if s == 'a':
        return n
    else:
        count_a = s.count('a')
        repeat_str = n//len(s)
        repeat_a = repeat_str * count_a + s[:(n%len(s))].count('a')
        return repeat_a

if __name__ == '__main__':
    print(repeated_string('aba', 10))
    print(repeated_string('a', 1000000000000))
