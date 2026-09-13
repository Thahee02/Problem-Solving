text = "python"

# change to list because the string is immutable
char_text = list(text)

left = 0
right = len(char_text) - 1

while left < right:
    char_text[left], char_text[right] = (char_text[right], char_text[left])
    left += 1
    right -= 1

result = "".join(char_text)

print(result)
