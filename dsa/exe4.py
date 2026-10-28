def count_even(numbers):
    least = 0

    for number in numbers:
        if number % 2 == 0:
            least += 1
    return least
print(count_even([1, 2, 3, 4, 6]))
print(count_even([1, 3, 5, 7]))