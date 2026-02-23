# MATRIX IN PYTHON @11 Feb DSA
#  METHOD 1

# row = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# matrix = []
# for i in range(row):
#     rows_temp = []
#     for j in range(columns):
#         rows_temp.append(int(input("Enter values : ")))
#     matrix.append(rows_temp)
# print(matrix)

# for i in range (row):
#     for j in range(columns):
#         print(matrix[i][j], end=" ")
#     print()

# @13 Feb DSA 

# rows = int(input("enter no of rows: "))
# colm = int(input("enter the no of columns: "))
# matrix = []
# for i in range(rows):
#     rowArr = []
#     for j in range(colm):
#         rowArr.append(int(input("enter a value: ")))
#     matrix.append(rowArr)
# print(matrix)

# Visiting all the values of array data structure is called traversal.
#  --> Row wise traversal and column wise traversal <--

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     for element in row:
#         print(element, end=" ")

# column wise traversal

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# rows = len(matrix)      # Total rows (3)
# cols = len(matrix[0])   # Total cols (3)

# print("Column-wise Traversal:")

# # 1. Outer loop goes across columns (0 -> 1 -> 2)
# for j in range(cols):
#     print(f"Column {j}:", end=" ")
    
#     # 2. Inner loop goes down the rows (0 -> 1 -> 2)
#     for i in range(rows):
#         # We access [i][j] -> Changing Row 'i', keeping Column 'j' fixed
#         print(matrix[i][j], end=" ")
    
#     print() # New line after finishing one full column

# Diagonal traversal -->

# # In a matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# - [1,5,9] - Primary diagonal
# - [3,5,7] - secondary diagonal

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Primary Diagonal
# n = len(matrix)
# print("Primary diagonal: ", end=" ")
# for i in range(n):
#     print(matrix[i][i], end= " ")
# print()

# # Secondary Diagonal
# print("Secondary diagonal: ", end= "")
# for i in range(n):
#     print(matrix[i][n - 1 - i], end= " ")

# Write a program to calculate the sum of individual rows and columns

# rows = int(input("enter no of rows: "))
# colm = int(input("enter the no of columns: "))
# matrix = []
# for i in range(rows):
#     rowArr = []
#     for j in range(colm):
#         rowArr.append(int(input("enter a value: ")))
#     matrix.append(rowArr)

# for i in range(rows):
#     sum = 0
#     for j in range(colm):
#         sum += matrix[j][i]
#     print("sum of colmuns: ", sum)

# @ 16 feb 

# matrix1 = [
#     [1,2,3,4],
#     [2,3,4,6]
# ]
# matrix2 = [
#     [1,2,3,4],
#     [2,3,4,6]
# ]
# result = []
# for i in range (len(matrix1)):
#     rowsum = []

#     for j in range(len(matrix1[0])):
#         sumval = matrix1[i][j] + matrix2[i][j]
#         rowsum.append(sumval)

#     result.append(rowsum)

# print(result)

# Matrix creation through Py

# rowz = 2
# colz = 2
# mat1 = []
# mat2 = []

# for i in range (rowz):

# @ 17 Feb 
# 1. Printing upper and lower triangular matrix.
#upper triangular matrix
# rows = 3
# columns = 3
# matrix = []
# for i in range(rows):
#     row = []
#     for j in range(columns):
#         value = int(input("Enter the value:"))
#         row.append(value)
#     matrix.append(row)
# print("Matrix")
# for i in range(rows):
#     for j in range(columns):
#         print(matrix[i][j],end=" ")
#     print()

# for r in range(rows-1):
#     for c in range(r+1,columns):
#         print("Upper triangular:",matrix[r][c],end=" ")

# Transpose of a matrix

