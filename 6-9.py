maximum = a = int(input())
index_a, index_max = 1, 1
while a != 0:
  a = int(input())
  index_a += 1
  if a > maximum:
    maximum, index_max = a, index_a
print(index_max)

#maximum = a = int(input())
#maximum_index = 1
#i = 1
#while a != 0:
  #a = int(input())
  #i += 1
  #if a > maximum:
    #maximum = a
    #maximum_index = i
#print(maximum_index)