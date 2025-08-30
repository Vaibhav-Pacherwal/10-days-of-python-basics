## Write a function that takes a list and returns the second largest number.
def sec_large(nums):
    max_val = float("-inf")
    sec_max_val = float("-inf")
    for i in range(0, len(nums)):
        if max_val < nums[i]:
            sec_max_val = max_val
            max_val = nums[i]

    return sec_max_val

nums = [47, 12, 6, 99, 28, 73, 15, 496, 33, 81]
print(f"Second largest value:{sec_large(nums)}")


