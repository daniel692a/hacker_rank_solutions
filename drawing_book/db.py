def page_count(n, p):
    """"
    n: an integer, the number of pages in the book
    p: an integer, the page number to turn to
    """
    turn_beginning, turn_end = 0, 0
    page_beginning, page_end = 0, 0
    for i in range(1, n+1, 2):
        page_beginning = i
        if (page_beginning == p) or (page_beginning-1 ==p):
            break
        else:
            turn_beginning+=1
    for j in range(n, 1, -2):
        page_end = j
        if n % 2 == 0:
            if (page_end == p) or (page_end+1 ==p):
                break
            else:
                turn_end+=1
        else:
            if (page_end == p) or (page_end-1 ==p):
                break
            else:
                turn_end+=1

    if turn_beginning <= turn_end:
        return turn_beginning
    else:
        return turn_end


if __name__ == '__main__':
    print(page_count(6, 5))
    print(page_count(6, 2))