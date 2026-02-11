# MATRIX IN PYTHON @11 Feb DSA
#  METHOD 1
row = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
matrix = []
for i in range(row):
    rows_temp = []
    for j in range(columns):
        rows_temp.append(int(input("Enter values : ")))
    matrix.append(rows_temp)
print(matrix)

for i in range (row):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()