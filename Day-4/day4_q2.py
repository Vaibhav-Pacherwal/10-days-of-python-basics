## WARF to find the sum of first n natural numbers.
def nSum(n):
    if n == 1:
        return 1
    return (n + nSum(n-1))

num = int(input("enter n:"))
print(f"sum of first n nums:{nSum(5)}")


