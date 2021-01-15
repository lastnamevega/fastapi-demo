def fibonacci(num: int):
    if num < 0:
        raise ValueError(f'{num} less than min of 0')
    elif num > 20:
        raise ValueError(f'{num} greater than max of 20')
    elif num < 3:
        return 1

    return (fibonacci(num - 1) + fibonacci(num - 2))
