numbers = [12, 5, 8, 20, 3, 15]

smallest_number = float('inf')  # Initialize to a very large number

for number in numbers:
    if number < smallest_number:
        smallest_number = number

print("The smallest number is:", smallest_number)