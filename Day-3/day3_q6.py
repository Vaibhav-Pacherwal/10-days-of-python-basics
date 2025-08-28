## Remove all vowels from a string.
vowels = "aeiouAEIOU"
text = input("enter text:")

list_without_vowels = []
for i in range(0, len(text)):
    if text[i] not in vowels:
        list_without_vowels.append(text[i])

text_without_vowels = "".join(list_without_vowels)
print(f"Text without vowels:{text_without_vowels}")