## WAP to count number of digits in a number
num = int(input("enter number: "))

count = 0
while num > 0:
    count += 1
    num //= 10

print(count)