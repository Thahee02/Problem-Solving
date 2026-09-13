text = "programming"

frequency = {}

# store char counts
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# print duplicate chars
for char in frequency:
    if frequency[char] > 1:
        print(char)
    