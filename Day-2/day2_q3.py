text = input("enter text: ")

updatedTextList = []
for i in range(0, len(text)):
    if(48 <= ord(text[i]) <= 57 or 65 <= ord(text[i]) <= 90 or 97 <= ord(text[i]) <= 122):
        updatedTextList.append(text[i])

updatedText = "".join(updatedTextList)
print(updatedText)