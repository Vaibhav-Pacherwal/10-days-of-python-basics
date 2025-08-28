## WAP to generate all substrings of a string
text = input("enter text: ")

for i in range(0, len(text)):
    for j in range(i, len(text)):
        for k in range(i, j+1):
            print(text[k], end="")
        print()