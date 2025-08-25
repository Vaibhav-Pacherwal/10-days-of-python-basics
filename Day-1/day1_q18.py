## WAP to check if number is armstrong or not
num = int(input("enter num: "))
original = num

count = 0
while num > 0:
    digit = num % 10
    count += pow(digit, 3)
    num //= 10

if(count == original):
    print("armstrong!")
else: 
    print("not an armstrong!")