def fizzbuzz(number: int):
    if number < 1:
        raise ValueError(f'{number} is less than 1')
    elif number % 15 == 0:
        return 'fizzbuzz'
    elif number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'

    return number
