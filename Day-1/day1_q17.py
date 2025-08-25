## WAP to generate a pascal's trinagle
row = int(input("enter row: "))

def fact(n):
    pro = 1
    for i in range(1, n+1):
        pro *= i
    return pro

for i in range(1, row+1):
    for j in range(1, i+1):
        print(fact(i-1) // (fact(j-1) * fact(i-j)), end=" ")
    print()
    