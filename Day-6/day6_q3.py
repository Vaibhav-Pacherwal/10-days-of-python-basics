## Write a function to read a file and print only the lines that contain a given keyword.
with open("sample.txt", "r") as f:
    data = f.read()
    line_wise_data = data.split("\n")

    word = input("enter word:")
    for i in range(0, len(line_wise_data)):
        if word in line_wise_data[i]:
            print(line_wise_data[i])
            