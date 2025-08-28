## Count uppercase and lowercase letters in a string.
text = input("enter text:")

upper_count = 0
lower_count = 0
for i in range(0, len(text)):
    if text[i].isupper():
        upper_count += 1
    else:
        lower_count += 1

print(f"There are {upper_count} uppercase chracters in this text.")
print(f"There are {lower_count} lowercase chracters in this text.")