def compare_triplets(a:list, b:list) -> list:
    """
    Compare two lists and return a score of how many times each element
    in a is greater than the corresponding element in b.
    """
    score = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            score[0] += 1
        elif a[i] < b[i]:
            score[1] += 1
    return score


if __name__ == '__main__':
    a = [1, 90, 39]
    b = [2, 90, 40]
    print(compare_triplets(a, b))