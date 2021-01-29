a = [int(s) for s in input().split()]
max, min = a.index(max(a)), a.index(min(a))
a[max], a[min] = a[min], a[max]

print(a)


#a = [int(s) for s in input().split()]
#pos_min = a.index(min(a))
#pos_max = a.index(max(a))
#a[pos_min], a[pos_max] = a[pos_max], a[pos_min]
#print(*a)