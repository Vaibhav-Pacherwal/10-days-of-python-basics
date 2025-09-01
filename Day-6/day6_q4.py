## Write a function that copies the contents of one file into another file.
def copyFileData(file, new_file):
    with open(file, "r") as f:
        data = f.read()
        with open(new_file, "w") as l:
            l.write(data)
        
copyFileData("sample.txt", "sampleCopy.txt")