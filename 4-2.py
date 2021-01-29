a = int(input())
b = int(input())
lst=[]
if a < b:
  for x in range(a, b + 1):
    lst.append(x)
elif a >= b:
  for x in range(b, a + 1):
    lst.append(x)
  lst.reverse() 

for x in lst:
  print (x)


#a = int(input())
#b = int(input())

#if a < b:
  #for i in range(a, b + 1):
    #print(i, end=' ')
#else:
  #for i in range(a, b - 1, -1):
    #print(i, end=' ')
