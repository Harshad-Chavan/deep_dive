"""

Transpose for matrix

"""

A = [[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3],
     [4, 4, 4, 4]]

C = [[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3],
     [4, 4, 4, 4]]

len_row = len(A[0])

B = []
for num_row in range(len_row):
    temp_list = []
    for digits in range(len_row):
        temp_list.append(0)
    B.append(temp_list)

for row in range(len_row):
    for column in range(len_row):
        B[column][row] = A[row][column]

print(A)
print(B)
"""
Tranpose in constant space
"""

for row in range(len_row):
    for column in range(row, len_row):
       print((row,column),(column,row))
       temp = C[row][column]
       C[row][column] = C[column][row]
       C[column][row] = temp

print(C)