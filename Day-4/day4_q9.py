## Write a function reverse_words(sentence) that reverses the order of words in a sentence.
def reverse_words(text):
    curr_word = ""
    listed_text = []
    for i in range(0, len(text)):
        if text[i] != ' ':
            curr_word += text[i]
        else:
            listed_text.append(curr_word)
            curr_word = ""
        
    if len(curr_word) != 0:
        listed_text.append(curr_word)
    
    listed_text.reverse()
    return " ".join(listed_text)
    

text = input("enter text:")
print(f"Actual Sentence:{text}")
print(f"Reversed Sentence:{reverse_words(text)}")
