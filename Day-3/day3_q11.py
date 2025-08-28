## Find all pairs in a list whose sum equals a target number.
nums = [3, 7, 11, 15, 23, 27]

pair_list = []
target = int(input("enter target number:"))
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        if target == nums[i]+nums[j]:
            pair_list.append([nums[i], nums[j]])

print(pair_list)