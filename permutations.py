import itertools
import pandas as pd
import math 

aux = []
n = math.factorial(5)
matrix = [[list() for i in range(n)] for j in range(n)]
permutations = list(itertools.permutations([1, 2, 3, 4, 5]))

for i in range(n):
  for j in range(n):
    aux = []
    for k in range(5):
      a = permutations[i][k]
      b = a - 1 
      aux.append(permutations[j][b])
    matrix[i][j] = aux

table = pd.DataFrame(matrix, index = permutations,columns = permutations )
table.to_csv('permutations.csv',index=True, encoding='utf-8')

