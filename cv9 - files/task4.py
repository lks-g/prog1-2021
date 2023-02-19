from task3 import *

def matrix_mul(a, b):
  if len(a[0]) != len(b):
    raise ArithmeticError("Zadane matice nie je mozne vynasobit")
  matrix = [[0]*len(b[0]) for _ in range(len(a))]
  for i_row in range(len(matrix)):
    for i_col in range(len(matrix[0])):
      sum = 0
      for k in range(len(a[0])):
        sum += a[i_row][k] * b[k][i_col]
      matrix[i_row][i_col] = sum
  return matrix

print(matrix_mul(a_matrix, b_matrix))