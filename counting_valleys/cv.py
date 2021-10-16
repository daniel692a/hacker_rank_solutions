def countig_valleys(steps: int, path: str) -> int:
    """
    Counting Valleys
    """
    valleys = 0
    level = 0
    for step in path:
        if step == 'U':
            level += 1
        elif step == 'D':
            level -= 1
        if level == 0 and step == 'U':
            valleys += 1
    return valleys

if __name__ == '__main__':
    print(countig_valleys(8, 'UDDDUDUU'))
    print(countig_valleys(12, 'DDUUDDUDUUUD'))