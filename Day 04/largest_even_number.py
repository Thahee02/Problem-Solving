numbers = [15, 8, 23, 42, 17, 30, 11]

largest_even = None

for number in numbers:
    if number % 2 == 0:
        if largest_even is None or number > largest_even:
            largest_even = number

print(largest_even)