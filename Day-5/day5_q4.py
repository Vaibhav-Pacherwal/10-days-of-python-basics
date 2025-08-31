## create a new file that doesn't exist already.

f = open("sample.txt", "a")
f.write("just testing the file creation using append!")
f.close()