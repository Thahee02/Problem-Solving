text = "racecar"

left = 0
right = len(text) - 1

is_palindrome = False

while left < right:
    if text[left] != text[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

if is_palindrome:
    print(f"The text {text} is a palindrome.")
else:
    print(f"The text {text} is not a palindrome.")