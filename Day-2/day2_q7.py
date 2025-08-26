## WAP to flatten 2D list to 1D
nums = [[1, 2, 4, 6], [4, 7, 3, 9], [8, 32, 4, 7, 8]]

flattenedNums = []
for i in range(0, len(nums)):
    temp = nums[i]
    for j in range(0, len(temp)):
        flattenedNums.append(temp[j])

print(flattenedNums)