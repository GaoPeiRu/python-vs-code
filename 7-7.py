x = input()
lst = list(map(int, x.split()))

for i in range(0, len(lst), 2):
  popval = lst.pop(i)
  lst.insert(i+1, popval)
  
print(lst)


#a = [int(s) for s in input().split()]
#for i in range(0, len(a) - 1, 2):
  #a[i], a[i + 1] = a[i + 1], a[i]
#print(*a)
