n = input()
myList = list(map(int, n.split()))
out =[max(myList), myList.index(max(myList))]
print(str(out).replace('[','').replace(']','').replace(',',''))
# Prints max input value and its index


#a = [int(s) for s in input().split()]
#print(max(a), a.index(max(a)))