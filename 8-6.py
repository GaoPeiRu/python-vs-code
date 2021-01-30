n=int(input())
a=[['.']*n for i in range(n)]
for j in range(n):
    for k in range(n):
        if j==k:
            a[k][j]='*'
        elif k==(n-1)/2:
            a[k][j]='*'
        elif j+k==6:
            a[k][j]='*'
        elif j==(n-1)/2:
            a[k][j]='*'

for line in a:
    print(*line)