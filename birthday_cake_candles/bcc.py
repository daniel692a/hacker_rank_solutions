def count(arr, item):
    count = 0
    for i in arr:
        if i == item:
            count += 1
    return count

def tallest_candle(ar):
    max_height = 0
    for i in ar:
        if i > max_height:
            max_height = i
    return max_height

def birthday_cake_candles(ar):
    tallest = tallest_candle(ar)
    return count(ar, tallest)

if __name__ == '__main__':
    ar_test = [3, 2, 1, 3]
    print(birthday_cake_candles(ar_test))
    print(birthday_cake_candles([4, 2, 1, 3]))