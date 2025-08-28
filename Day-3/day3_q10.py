## Find the longest palindrome substring in a given string.
def isPalindrome(text):
    reversed_text = text[::-1]
    if text == reversed_text:
        return True
    else:
        return False
    
text = input("enter text:")
longest_palindrome = {}
for i in range(0, len(text)):
    for j in range(i, len(text)):
        subText_list = []
        for k in range(i, j+1):
            subText_list.append(text[k])
            subText = "".join(subText_list)
        if isPalindrome(subText):
            longest_palindrome[subText] = len(subText)

sub_palindomic_texts = []
max_length_palindrome = max(longest_palindrome.values())
for key in longest_palindrome:
    if longest_palindrome.get(key) == max_length_palindrome:
        sub_palindomic_texts.append(key)
print(f"longest palindromic substring:", end='')
for i in range(0, len(sub_palindomic_texts)):
    print(f"'{sub_palindomic_texts[i]}'", end=' ')
print()