## Write a program to read a file and count how many times each word occurs.
with open("sample.txt", "r") as f:
    data = f.read()

    word = input("enter word:")
    print(f"{word} occurs {data.count(word)} times!")