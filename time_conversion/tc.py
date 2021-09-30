import re
def time_conversion(s):
    """
    This function convert a time in 12-hour AM/PM format, to military (24-hour) time.
    >>> time_conversion('07:05:45PM')
    '19:05:45'
    """
    # schedule = re.search('[A-Z]+', s).group(0)
    # s = re.sub(schedule, '', s)
    # hour = re.split('[:]', s)
    # c_h = int(hour[0])
    # if schedule == 'PM':
    #     if c_h == 12:
    #         c_h = str(c_h)
    #     else:
    #         c_h = str(c_h+12)
    #     print(f'{c_h}:{hour[1]}:{hour[2]}')
    #     return f'{c_h}:{hour[1]}:{hour[2]}'
    # else:
    #     if c_h == 12:
    #         c_h = '00'
    #         return f'{c_h}:{hour[1]}:{hour[2]}'
    #     else:
    #         return s
    if s[-2:] == 'AM':
        if s[:2] == '12':
            return '00' + s[2:-2]
        else:
            return s[:-2]
    else:
        if s[:2] == '12':
            return s[:-2]
        else:
            return str(int(s[:2]) + 12) + s[2:-2]

if __name__ == '__main__':
    print(time_conversion('12:00:00AM'))
    print(time_conversion('12:00:00PM'))