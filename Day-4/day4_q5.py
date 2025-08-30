## Write a function that accepts a string and returns the number of vowels in it.
def count_vowels(text, vowels="aeiouAEIOU"):
    count = 0
    for i in range(0, len(text)):
        if text[i] in vowels:
            count += 1
        
    return count

text = input("Enter String:")
print(f"Vowel Count:{count_vowels(text)}")