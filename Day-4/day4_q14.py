## Write a recursive function to calculate the power of a number (a^b).
def power(n, m):
    if m == 0:
        return 1
    return n * power(n, m-1)

n = int(input("enter n:"))
m = int(input("enter m:"))
print(f"n^m:{power(n, m)}")