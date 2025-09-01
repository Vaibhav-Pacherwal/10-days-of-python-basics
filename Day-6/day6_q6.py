## Write a function to return the longest word in a text file.
with open("sample.txt", "r") as f:
    data = f.read()

    ch = ""
    count = 0
    max_count = 0
    longestWord = []
    for i in range(0, len(data)):
        if data[i] != ' ':
            count += 1
            ch += data[i]
        else:
            if max_count < count:
                max_count = max(max_count, count)
                longestWord.clear()
                longestWord.append(ch)
            ch = ""
            count = 0

    if count != 0:
        if count > max_count:
            print(f"longest word in sample.txt:{ch}")
        else:
            print(f"longest word in sample.txt:{longestWord[0]}")