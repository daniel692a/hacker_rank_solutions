def sock_merchant(n: int, ar:list)->int:
    """
    Function to count the number of matching pairs of socks.
    """
    unique_colors = set(ar)
    count_sock = {sock: ar.count(sock) for sock in unique_colors}
    counter = 0
    for key in count_sock:
        counter += count_sock[key] // 2
    return counter


if __name__ == "__main__":
    print(sock_merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))