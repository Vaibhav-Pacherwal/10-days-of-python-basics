## Replace every space in a string with -
text = input("enter text:")

updated_text_list = []
for i in range(0, len(text)):
    if text[i] == ' ':
        updated_text_list.append('-')
    else:
        updated_text_list.append(text[i])

updated_text = "".join(updated_text_list)
print(f"Actual Value:{text}")
print(f"Updated Value:{updated_text}")