## WAP to multiply to matrices
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[1, 1, 2],
           [3, 5, 8],
           [1, 1, 1]]

resultMatrix = []
if(len(matrix1) == len(matrix2[0])):
    row = []
    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix1[0])):
            row.append(matrix1[i][j]*matrix2[i][j])
        
