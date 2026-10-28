def second_largest(numbers):
    large = None
    second = None

    for number in numbers:
        if large is None or number > large:
            second = large
            large = number
        elif number < large and (second is None or number > second): 
            second=number
    return second
print(second_largest([10, 5, 8, 10, 3] ))