## Check if a number is a perfect number.
num = int(input("enter num:"))

sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print(f"yayy! {num} is a perfect number.")
else: 
    print(f"{num} is not a perfect number.")