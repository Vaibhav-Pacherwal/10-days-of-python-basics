## find the count of even numbers in nums.txt.
with open("nums.txt", "r") as f:
    data = f.read()
    nums = []
    nums_str = data.split(',')
    for i in range(0, len(nums_str)):
        nums.append(int(nums_str[i]))

    count = 0
    for i in range(0, len(nums)):
        if nums[i] % 2 == 0:
            count += 1
    
    print(f"there are {count} even numbers in nums.txt")