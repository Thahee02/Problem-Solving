numbers = [2, 1, 5, 1, 3, 2]
k = 3

window_max = 0

# first window
for i in range(k):
    window_max += numbers[i]

maximum_sum = window_max

# slide the window
for i in range(k, len(numbers)):
    window_max = window_max - numbers[i-k] + numbers[i]
    if window_max > maximum_sum:
        maximum_sum = window_max

print("Maximum sum:", maximum_sum)


