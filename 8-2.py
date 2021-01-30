m,n = [int(s) for s in input().split()]
for i in range(0,m):
    myList = list(map(int, input().split()))
    if i == 0:
        max_el = max(myList)
        maxList = [0,myList.index(max(myList))]
    elif max(myList) > max_el:
        max_el = max(myList)
        maxList = [i,myList.index(max(myList))]
print(*maxList, sep =' ')


#m, n = [int(s) for s in input().split()]
#a = [[int(j) for j in input().split()] for i in range(m)]
#max_value, max_i, max_j = a[0][0], 0, 0
#for i in range(m):
  #for j in range(n):
    #if a[i][j] > max_value:
      #max_value, max_i, max_j = a[i][j], i, j
#print(max_i, max_j)