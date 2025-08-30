## Write a recursive function to count the number of occurrences of a character in a string.
def char_occurrences(text, ch, i=0):
    if i == len(text):
        return 0
    if text[i] == ch:
        return 1 + char_occurrences(text, ch, i+1)
    else:
        return char_occurrences(text, ch, i+1)
    
text = input("enter string:")
char = input("enter character:")
print(f"'{char}' occurs {char_occurrences(text, char)} times!")