m, n = [int(s) for s in input().split()]
matrix = [[int(k) for k in input().split()] for i in range(m)]
a, b =[int(s) for s in input().split()]
for t in range(m):
    matrix[t][b], matrix[t][a] = matrix[t][a], matrix[t][b]
    print(*matrix[t], sep =' ') 


#m, n = [int(s) for s in input().split()]
#a = [[int(j) for j in input().split()] for i in range(m)]
#col1, col2 = [int(s) for s in input().split()]
#for i in range(m):
  #a[i][col1], a[i][col2] = a[i][col2], a[i][col1]
#for line in a:
  #print(*line)