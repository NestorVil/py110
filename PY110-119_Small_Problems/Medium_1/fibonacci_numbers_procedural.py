def fibonacci(nth):
    if nth <= 2:
        return 1

    previous, current = 1, 1
    for _ in range(3, nth + 1):
        previous, current = current, previous + current

    return current

print(fibonacci(4))


# Other student
# def fibonacci(sequence_position):
#     sequence = [1, 1]

#     for index in range(2, sequence_position):
#         sequence.append(sequence[index - 1] + sequence[index - 2])


#     return sequence[sequence_position - 1]
