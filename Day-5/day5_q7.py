## create function to replace python with java in practice.txt.
def replaceVal(data, old, new):
    new_text = data.replace(old, new)
    return new_text

with open("practice.txt", "r") as f:
    data = f.read()
    new_data = replaceVal(data, "java", "python")
    with open("practice.txt", "w") as l:
        l.write(new_data)