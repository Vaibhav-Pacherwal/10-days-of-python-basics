## Write a program that reads a file and prints the top 5 most common words.
with open("sample.txt", "r") as f:
    data = f.read()
    words = data.split(' ')

    freq = {}
    for i in range(0, len(words)):
        freq[words[i]] = freq.get(words[i], 0) + 1
    
    frequent_words = []
    while len(frequent_words) != 5:
        word = []
        max_appearences = 0
        for key in freq:
            if max_appearences < freq[key]:
                max_appearences = freq[key]
                word.clear()
                word.append(key)
        
        frequent_words.append(word[0])
        freq.pop(word[0])

    print(f"top 5 words:{frequent_words}")