def migratory_birds(arr):
    """"
    Given an array of integers, find the most common element.
    """
    bird_count = [0] * 6
    for i in arr:
        bird_count[i] += 1
    return bird_count.index(max(bird_count))

if __name__ == '__main__':
    arr = [1, 4, 4, 4, 5, 3]
    print(migratory_birds(arr))
    print(migratory_birds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))