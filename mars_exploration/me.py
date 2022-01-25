def mars_exploration(s:str)->int:
    """
    Función que cuenta los errores en un string
    """
    count_w = 0
    for i in range(len(s)):
        if i % 3 == 1:
            if s[i] != 'O':
                count_w+=1
        elif s[i] != 'S':
            count_w +=1
    return count_w

if __name__ == '__main__':
    print(mars_exploration('SOSSQS'))
    print(mars_exploration('SPQSOSWJG'))