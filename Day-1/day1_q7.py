## WAP to print factorial of given number n
num = int(input("enter number: "))

fact = 1
for i in range(1, num+1) :
    fact *= i
    i = i+1

print(fact)
