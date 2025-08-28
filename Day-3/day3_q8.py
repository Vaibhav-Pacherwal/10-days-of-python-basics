## Find the sum of elements at even indices in a list.
nums = [47, 12, 6, 99, 28, 73, 15, 496, 33, 81]

evenSum = 0
oddSum = 0
for i in range(0, len(nums)):
    if i % 2 == 0:
        evenSum += nums[i]
    else:
        oddSum += nums[i]

print(f"Sum of elements at even indices: {evenSum}")
print(f"Sum of elements at even indices: {oddSum}")