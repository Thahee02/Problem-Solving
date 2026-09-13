numbers = [1, 2, 4, 6, 8, 9]
target_sum = 10

left = 0
right = len(numbers) - 1

while left < right:
    current_sum = numbers[left] + numbers[right]
    
    if current_sum == target_sum:
        print(f"Pair found: ({numbers[left]}, {numbers[right]})")
        break
    elif current_sum < target_sum:
        left += 1
    else:
        right -= 1