numbers = [10, 20, 30, 40, 50, 60]

left = 0
right = len(numbers) - 1

while left < right:
    # Swap the elements at left and right indices
    numbers[left], numbers[right] = numbers[right], numbers[left]
    
    # Move towards the middle
    left += 1
    right -= 1

print("Reversed array:", numbers)