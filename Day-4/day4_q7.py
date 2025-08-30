## Write a function that takes a sentence and returns the word with the maximum length.
def max_len(text):
    curr_word = ""
    longest_word = ""
    for i in range(0, len(text)):
        if text[i] != ' ':
            curr_word += text[i]
        else:
            if len(longest_word) < len(curr_word):
                longest_word = ""
                for i in range(0, len(curr_word)):
                    longest_word += curr_word[i]
            curr_word = ""
        
        if len(curr_word) > len(longest_word):
            longest_word = curr_word
        
    return longest_word

text = input("enter text:")
print(f"longest word:{max_len(text)}")
                

        
