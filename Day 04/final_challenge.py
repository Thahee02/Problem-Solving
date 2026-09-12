numbers = [12, -5, 8, 20, -3, 15, 20, 7, -1]

largest_positive = None
smallest_positive = None
number_of_positive_numbers = 0
number_of_negative_numbers = 0

for number in numbers:
    if number > 0:
        number_of_positive_numbers += 1
        if largest_positive is None or number > largest_positive:
            largest_positive = number
        if smallest_positive is None or number < smallest_positive:
            smallest_positive = number
    elif number < 0:
        number_of_negative_numbers += 1

print("Largest positive number:", largest_positive)
print("Smallest positive number:", smallest_positive)
print("Number of positive numbers:", number_of_positive_numbers)
print("Number of negative numbers:", number_of_negative_numbers)