## Create a function is_palindrome(word) that checks if a word is a palindrome.
def isPalindrome(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    
    return False

word = input("enter word:")
if isPalindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome!")