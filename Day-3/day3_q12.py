## Rotate a matrix by 90 degrees.
matrix = [[1, 2, 3],
          [4, 5, 6]]

n = len(matrix[0])

rotated_matrix = []
for i in range(0, n):
    row = []
    m = len(matrix)-1
    while m >= 0:
        row.append(matrix[m][i])
        m -= 1
    rotated_matrix.append(row)
    

print(matrix)
print(rotated_matrix)