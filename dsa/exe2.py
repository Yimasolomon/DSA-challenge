def find_smallest(numbers):
    smallest = numbers[0]

    for count in numbers:
        if count < smallest:
            smallest = count
    return smallest
print(find_smallest([8, 3, 12, 1, 7]))