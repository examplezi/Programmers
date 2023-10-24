from collections import Counter

s = input().lower()
char_count = Counter(s)

max_count = max(char_count.values())
max_chars = [char for char, count in char_count.items() if count == max_count]

if len(max_chars) > 1:
    print("?")
else:
    print(max_chars[0].upper())
