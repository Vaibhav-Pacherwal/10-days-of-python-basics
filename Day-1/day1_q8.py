## WAP to reverse the given number
num = int(input("enter number: "))

new_num = 0
while num > 0:
    digit = num % 10
    new_num = (new_num * 10) + digit
    num //= 10

print(new_num)
