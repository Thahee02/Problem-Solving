numbers = [10, 5, 20, 8, 15, 20, 3]

second_largest = None
largest = None

for number in numbers:
    if largest is None or number > largest:
        second_largest = largest
        largest = number
    elif second_largest is None or (number > second_largest and number != largest):
        second_largest = number

print(second_largest)