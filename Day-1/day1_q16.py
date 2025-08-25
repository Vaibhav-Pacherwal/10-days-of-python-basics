## WAP to merge two lists without using +
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7, 8, 9]
mergedList = []

i = 0
j = 0
m = len(list1)
n = len(list2)

while i < m and j < n:
    if(list1[i] < list2[j]):
        mergedList.append(list1[i])
        i+=1
    elif(list1[i] > list2[j]):
        mergedList.append(list2[j])
        j+=1
    else:
        mergedList.append(list1[i])
        i+=1
        j+=1
    
if(i < m):
    while i < m:
        mergedList.append(list1[i])
        i+=1

if(j < n):
    while j < n:
        mergedList.append(list2[j])
        j+=1

print(mergedList)