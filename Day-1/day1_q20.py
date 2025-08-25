## WAP to sort list without using sort()
nums = [4, 5, 8, 2, 1, 8, 0, 5]

for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        if(nums[i] > nums[j]):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

print(nums)