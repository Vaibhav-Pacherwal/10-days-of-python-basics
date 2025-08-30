## Write a recursive function to calculate the sum of digits of a number.
def digiSum(num):
    if num == 0:
        return 0
    digit = num % 10
    return digit + digiSum(num//10)

num = int(input("enter num:"))
print(f"sum of all the digits:{digiSum(num)}")