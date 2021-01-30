x = input()
list_x = list(map(int, x.split()))
tally = 0
# To check if any values are greater than the values on either side.
for n in range(1,len(list_x)-1):
  if list_x[n-1] < list_x[n] and list_x[n] > list_x[n+1]:
    tally = tally + 1
print(tally)


#a = [int(s) for s in input().split()]
#counter = 0
#for i in range(1, len(a) - 1):
  #if a[i - 1] < a[i] > a[i + 1]:
    #counter += 1
#print(counter)
