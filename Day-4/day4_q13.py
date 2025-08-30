## Write a recursive function to find the length of a string.
def str_len(text, n=0):
    if n == len(text):
        return 0
    return 1 + str_len(text, n+1)

text = input("enter string:")
print(f"length of string:{str_len(text)}")