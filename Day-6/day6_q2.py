## Write a recursive function to flatten a nested list.
def flatten(nested_nums, flatten_nums=[], i=0):
    if flatten_nums is None:  
        flatten_nums = []

    if i == len(nested_nums):
        return flatten_nums

    if isinstance(nested_nums[i], int):  
        flatten_nums.append(nested_nums[i])
    else:
        flatten(nested_nums[i], flatten_nums, 0) 
    
    return flatten(nested_nums, flatten_nums, i+1)  
        

nested_nums = [1,[2,[3,4]],5]
print(flatten(nested_nums))