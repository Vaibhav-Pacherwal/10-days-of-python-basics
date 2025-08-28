## Print all numbers from 1–100 that are divisible by both 3 and 5
count = 0
for i in range(0, 101):
    if i % 3 == 0 or i % 5 == 0:
        count+=1

print(count)