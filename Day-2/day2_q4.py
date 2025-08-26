## WAP to find the length of longest word in a string
text = input("enter string: ")

count = 0
max_length = 0
for i in range(0, len(text)):
    if(text[i] != " "):
        count+=1
        max_length = max(count, max_length)
    else:
        count = 0

print("Maximum Length:", max_length)