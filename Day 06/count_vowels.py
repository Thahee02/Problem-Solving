text = "programming"
count = 0

for char in text:
    if char in "aeiou":
        count += 1

print(f"Total vowels: {count}")