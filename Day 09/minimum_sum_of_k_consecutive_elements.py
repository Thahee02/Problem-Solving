numbers = [4, 2, 1, 7, 8, 1, 2]
k = 3

window_sum = 0

# find the sum of first window
for i in range(k):
    window_sum += numbers[i]

min_sum = window_sum

# slide
for i in range(k, len(numbers)):
    window_sum = window_sum - numbers[i-k] + numbers[i]
    if window_sum < min_sum:
        min_sum = window_sum

print("Minimum sum:", min_sum)