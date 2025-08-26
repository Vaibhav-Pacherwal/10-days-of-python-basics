## WAP to print sum of all diagnol elements in square matrix
nums = [[1, 2, 3, 4],
        [4, 5, 6, 7],
        [7, 8, 9, 4],
        [2, 6, 6, 3]]

sum = 0
for i in range(0, len(nums)):
    sum += nums[i][i]

print("sum of diagnol elements:", sum)