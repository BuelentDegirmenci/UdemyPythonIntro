
num_rows = 3
num_cols = 2


matrix = [[((j * num_cols + 1) + i) for j in range(num_cols)] for i in range(num_rows)]
print(matrix)
