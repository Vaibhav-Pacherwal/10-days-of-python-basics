## WAP to find maximum and Minimum element without using max/min
nums = [13, 7, 25, 42, 9, 31, 18, 5]

max = float('-inf')
min = float('inf')

for i in range(0, len(nums)):
    if(nums[i] > max):
        max = nums[i]

    if(nums[i] < min):
        min = nums[i]

print("Max:", max)
print("Min", min)