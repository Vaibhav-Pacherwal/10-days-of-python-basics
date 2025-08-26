## WAP to find first non repeating chracter in a string
text = input("enter text: ")

freq = {}
for i in range(0, len(text)):
    freq[text[i]] = freq.get(text[i], 0) + 1

for key in freq:
    if(freq[key] == 1):
        print(key, freq.get(key))
        break