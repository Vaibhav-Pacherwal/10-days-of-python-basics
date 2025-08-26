## WAP to transpose 2D matrix
nums = [[1, 2, 4, 6], 
        [4, 7, 3, 9], 
        [8, 32, 4, 7]]

m = len(nums)
n = len(nums[0])

for i in range(m):
    for j in range(i+1, n):
        nums[i][j], nums[j][i] = nums[j][i], nums[i][j]

print(nums)