## Find the sum of all even numbers up to N.
num = int(input("enter num: "))

evenSum = 0
for i in range(0, num+1):
    if i % 2 == 0:
        evenSum += i

print(f"Even Sum:{evenSum}")