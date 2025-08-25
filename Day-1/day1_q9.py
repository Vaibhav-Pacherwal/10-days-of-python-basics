## WAP to print fibonacci series on N numbers
num = int(input("enter number: "))

fTerm = 0
print(fTerm)
sTerm = 1
print(sTerm)
for i in range(2, num):
    nextTerm = fTerm + sTerm
    print(nextTerm)
    fTerm = sTerm
    sTerm = nextTerm
