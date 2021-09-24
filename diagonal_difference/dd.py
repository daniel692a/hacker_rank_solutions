def diagonal_diference(arr:list):
    """
    Function that returns the absolute difference between the sums of the
    right and left diagonals in a square matrix.
    """
    right_sum, left_sum = 0, 0
    for i in range(len(arr)):
        left_sum += arr[i][i]
        right_sum += arr[i][len(arr)-i-1]
    return abs(right_sum - left_sum)

if __name__ == "__main__":
    print(diagonal_diference([
        [3,2,3],
        [4,5,6],
        [7,8,9]]))