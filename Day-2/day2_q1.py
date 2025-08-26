##  WAP to rotate the list by K rotations
l1 = [1, 2, 3, 4, 5, 6]

def reverse(nums, start, end):
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start+=1
        end-=1

k = int(input("enter no. of rotations:"))
reverse(l1, 0, len(l1)-1)
reverse(l1, 0, k-1)
reverse(l1, k, len(l1)-1)

print(l1)
