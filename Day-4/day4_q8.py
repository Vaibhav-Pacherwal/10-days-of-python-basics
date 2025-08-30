## Write a function count_occurrences(lst, x) that returns how many times x appears in the list.
def count_occurrences(lst, x):
    count = 0
    for i in range(0, len(lst)):
        if lst[i] == x:
            count += 1
        
    return count

nums = [47, 12, 6, 99, 28, 73, 15, 496, 33, 81, 73, 15, 496, 33, 81]
target = int(input("enter target:"))
if count_occurrences(nums, target) == 1:
    print(f"{target} occurs only {count_occurrences(nums, target)} time!")
else:
    print(f"{target} occurs {count_occurrences(nums, target)} times!")