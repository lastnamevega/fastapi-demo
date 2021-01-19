def fibonacci(desired_index: int):
    if desired_index < 0:
        raise ValueError(f'{desired_index} is less than 0')

    values = [0, 1]

    for i in range(2, desired_index + 1):
        values.append(values[i - 1] + values[i - 2])

    return values[desired_index]
