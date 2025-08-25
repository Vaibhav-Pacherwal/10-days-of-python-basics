## WAP to remove duplicates from the list
nums = [1, 1, 4, 5, 3, 4, 7, 9, 0, 1]

cleanedSet = set()
for i in range(0, len(nums)):
    cleanedSet.add(nums[i])

cleanedList = list(cleanedSet)
for i in range(0, len(cleanedList)):
    print(cleanedList[i], "occurs", nums.count(cleanedList[i]), "times")

