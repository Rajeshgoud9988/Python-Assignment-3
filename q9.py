def drop_minimum(*args):
    numbers = list(args)
    numbers.remove(min(numbers))
    return numbers

print(drop_minimum(5, -2, 8, 4, -5, 7, 10))