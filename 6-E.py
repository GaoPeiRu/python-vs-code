x = int(input())
prev = x
count = 1
mcount = count

while x != 0:
  x = int(input())
  if x == prev:
    count += 1
    prev = x
  else:
    if count > mcount:
      mcount = count
    count = 1
    prev = x

print(mcount)


#next = int(input())
#length = 1
#max_length = 1
#while next != 0:
  #prev, next = next, int(input())
  #if prev == next:
    #length += 1
  #else:
    #length = 1
  #max_length = max(length, max_length)
#print(max_length)
