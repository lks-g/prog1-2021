def matrix_add(a, b):
  
  if len(a) != len(b) or len(a[0]) != len(b[0]):
    raise ArithmeticError("Zadane matice nie je mozne scitat")
  matrix = [[0]*len(a[0]) for _ in range(len(a))]
  for i_row in range(len(a)):
    for i_col in range(len(a[0])):
      matrix[i_row][i_col] = a[i_row][i_col] + b[i_row][i_col] 
  return matrix

a_matrix = [
  [1, 1, 2],
  [3, 5, 8],
  [3, 1, 4]
]

b_matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

c_matrix = [
  [5, 2],
  [2, 4],
  [7, 8]
]

print(matrix_add(a_matrix, b_matrix))
# print(matrix_add(a_matrix, c_matrix))  # Nescita