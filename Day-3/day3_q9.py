## Check if two strings are anagrams.
text1 = input("enter text1:")
text2 = input("enter text2:")

text1_freq = {}
for i in range(0, len(text1)):
    text1_freq[text1[i]] = text1_freq.get(text1[i], 0) + 1

text2_freq = {}
for i in range(0, len(text2)):
    text2_freq[text2[i]] = text2_freq.get(text2[i], 0) + 1

if text1_freq == text2_freq:
    print(f"'{text1}' and '{text2}' are anagrams!")
else:
    print(f"'{text1}' and '{text2}' are not anagrams!")