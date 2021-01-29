x = int(input())
a = []
while x!=0:
  a.append(x)
  x=int(input())

a= [int(x) for x in a]
a.sort()

print(a[-2])


#maximum = int(input())
#second_maximum = int(input())
#if second_maximum > maximum:
  #second_maximum, maximum = maximum, second_maximum
#a = -1
#while a != 0:
  #a = int(input())
  #if a > maximum:
    #second_maximum, maximum = maximum, a
  #elif a > second_maximum:
    #second_maximum = a
#print(second_maximum)
