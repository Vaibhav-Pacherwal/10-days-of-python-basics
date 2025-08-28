## Print the cube of first N natural numbers.
num = int(input("enter n:"))

sum = 0
for i in range(0, num+1):
    sum += pow(i, 3)

print(f"sum:{sum}")