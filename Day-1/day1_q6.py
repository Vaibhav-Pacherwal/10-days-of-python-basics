## WAP to print sum of first N natural numbers
num = int(input("enter number: "))
i = 0
sum = 0
while(i <= num) :
    sum += i
    i = i+1

print(sum)