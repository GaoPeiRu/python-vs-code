x = input()
lst = list(map(int, x.split()))
i = 1

for i in range(1, len(lst)):
  if lst[i] * lst[i-1] > 0:
    print(str(lst[i - 1]), str(lst[i]))
    break
  elif i == len(lst)-1:
    print("0")


#a = [int(s) for s in input().split()]
#for i in range(1, len(a)):
  #if a[i - 1] * a[i] > 0:
    #print(a[i - 1], a[i])
    #break
#else:
  #print(0)