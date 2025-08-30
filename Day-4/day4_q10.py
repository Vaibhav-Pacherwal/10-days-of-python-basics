## Write a recursive function to calculate factorial of a number.
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

num = int(input("enter n:"))
print(f"Factorial of {num}:{fact(num)}")