def breaking_records(scores: list) -> tuple:
    """
    Function that returns the number of times that the highest score
    and lowest score were broken.
    """
    high = low = scores[0]
    high_count = low_count = 0
    for score in scores:
        if score > high:
            high = score
            high_count += 1
        elif score < low:
            low = score
            low_count += 1
    return high_count, low_count


if __name__ == "__main__":
    print(breaking_records([10, 5, 20, 20, 4, 5, 2, 25, 1]))