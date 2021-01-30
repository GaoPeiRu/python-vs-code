n,m=[int(s) for s in input().split()]
a=[['.']*m for i in range(n)]
for j in range(n):
    for k in range(m):
        if k%2!=0 and j%2==0:
            a[j][k]='*'
        elif k%2==0 and j%2!=0:
            a[j][k]='*'

for line in a:
    print(*line)


#n, m = [int(s) for s in input().split()]
#a = [['.' if (i + j) % 2 == 0 else '*']
     #for i in range(n)
     #for j in range(m)]
#for line in a:
  #print(*line)
