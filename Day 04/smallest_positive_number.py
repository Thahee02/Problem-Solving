numbers = [-10, 5, -2, 8, 3, -1, 12]

smallest_positive = None

for number in numbers:
    if number > 0:
        if smallest_positive is None or number < smallest_positive:
            smallest_positive = number

print(smallest_positive)