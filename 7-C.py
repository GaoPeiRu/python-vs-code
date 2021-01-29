n = 0
coord = {}
myList = []
x_co = []
y_co = []
Rule_vi = None
while n < 16:
    a = input()
    inList = list(map(int, a.split()))
    myList.append(inList[0])
    myList.append(inList[1])
    x_co.append(myList[n]) 
    y_co.append(myList[n+1]) 
    n = n+2
i = 0
for x in x_co:
    for i in range(0,8):
        if x == x_co[i] and x_co.index(x) != i:
            Rule_vi = True 
i = 0
for y in y_co:
    if Rule_vi == True:
      break
    for i in range(0,8):
        if y == y_co[i] and y_co.index(y) != i:
            Rule_vi = True 
            break
n = 0
i = 0
for n in range(0,8):
    if Rule_vi == True:
        break
    for i in range(0,8):
        if  abs(x_co[n] - x_co[i]) == abs(y_co[n] - y_co[i]) and i != n:
            Rule_vi = True
            break
if Rule_vi == True:
  print('YES')
else:
  print('NO')





#x = []
#y = []
#for i in range(8):
  #a = [int(s) for s in input().split()]
  #x.append(a[0])
  #y.append(a[1])
#answer = 'NO'
#for i in range(8):
  #for j in range(i + 1, 8):
    #if ((x[i] == x[j]) or
        #(y[i] == y[j]) or
        #(abs(x[i] - x[j]) == abs(y[i] - y[j]))):
      #answer = 'YES'
#print(answer)