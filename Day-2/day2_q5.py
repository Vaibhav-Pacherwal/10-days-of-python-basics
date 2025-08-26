## WAP to count frequency of each chracter in a string
text = input("enter text: ")

freq = {}
for i in range(0, len(text)):
    freq[text[i]] = freq.get(text[i], 0) + 1

print(freq)
