## check the word exists in which line.
def check_existence(data, word):
    if word in data:
        return True
    
    return False

word = input("enter word:")

with open("practice.txt", "r") as f:
    count = 1
    data = f.readline()
    if check_existence(data, word):
        print(f"{word} first occurs in line {count}")
    else:
        while data != "":
            count += 1
            data = f.readline()
            if check_existence(data, word):
                print(f"{word} first occurs in line {count}")
                break

