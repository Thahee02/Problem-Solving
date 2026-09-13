text = "aabbcdde"

frequency = {}

# First pass: count characters
for char in text:

    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1


# Second pass: find first unique character
# for char in text:

#     if frequency[char] == 1:
#         print("First non-repeating character:", char)
#         break

            # or

for char in frequency:
    if frequency[char] == 1:
        print("First non-repeating character:", char)
        break