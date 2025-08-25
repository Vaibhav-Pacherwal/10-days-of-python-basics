## WAP to count vowels in a string
vowels = "aeiouAEIOU"
str = input("enter string: ")

count = 0
for i in range(0, len(str)):
    if(vowels.find(str[i]) != -1):
        count+=1

print(count)