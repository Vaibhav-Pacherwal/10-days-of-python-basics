## check if "learning" exists in file or not.
def check_existence(data, word):
    if word in data:
        return True
    
    return False

word = input("enter word:")

with open("practice.txt", "r") as f:
    data = f.read()
    if check_existence(data, word):
        print(f"'{word}' do exists in practice.txt")
    else:
        print(f"'{word}' do not exists in practice.txt")