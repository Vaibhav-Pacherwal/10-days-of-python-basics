## WAP to find the sum and product all elements in a string
nums = [1, 2, 3, 4, 5]

sum = 0
product = 1
for i in range(0, len(nums)):
    sum += nums[i]
    product *= nums[i]

print("Sum:", sum)
print("Product:", product)
