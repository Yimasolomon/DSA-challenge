def move_zeros(numbers):
    encountered = []
    zero = 0

    for number in numbers:
        if number == 0:
            zero += 1
        else:
            encountered.append(number)
    encountered.extend([0] * zero)
    return encountered
print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([1, 2, 3]))
print(move_zeros([0, 0, 5]))