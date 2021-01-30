a=1
b=0
c=1
while a!=0:
    a=int(input())
    if a>b:
        b=a
        c=1
    elif a==b:
        c+=1
print(c)

#maximum = int(input())
#counter = 1
#a = -1
#while a != 0:
  #a = int(input())
  #if a > maximum:
    #maximum, counter = a, 1
  #elif a == maximum:
    #counter += 1
#print(counter)