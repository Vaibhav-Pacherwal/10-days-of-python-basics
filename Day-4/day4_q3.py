## WARF to print all the elememts of a list.
def list_print(nums, n=0):
    if n == len(nums):
        return
    print(nums[n], end=' ')
    list_print(nums, n+1)

nums = [47, 12, 6, 99, 28, 73, 15, 496, 33, 81]
list_print(nums)
print()