sam=0.5 
total=0
while sam!=0:
    a=int(input())
    if a>sam:
        total+=1
    sam=a
if total>=1:
    print(total-1)
else:
    print(0)

#prev = next = int(input())
#counter = 0
#while next != 0:
  #if prev < next:
    #counter += 1
  #prev, next = next, int(input())
#print(counter)