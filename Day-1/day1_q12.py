## WAP to reverse a string without slicing
string = input("enter a string: ")
listed_str = list(string)

i = 0
j = len(listed_str)-1
while i <= j :
    temp = listed_str[i]
    listed_str[i] = listed_str[j]
    listed_str[j] = temp
    i+=1
    j-=1

print("string", string)
new_str = "".join(listed_str)
print("reversed string:", new_str)

