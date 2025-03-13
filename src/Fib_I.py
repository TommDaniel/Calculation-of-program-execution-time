def fib_i(position):
    if position == 1:
        return 0
    elif position == 2:
        return 1
    else:
        first = 0
        second = 1
        value = 0
        for i in range(3, position + 1):
            value = first + second
            first = second
            second = value
        return value

