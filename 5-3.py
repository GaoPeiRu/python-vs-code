import math
s=input()
print(s[math.ceil(len(s)/2):]+s[:math.ceil(len(s)/2)])


#s = input()
#mid = (len(s) + 1) // 2
#print(s[mid:] + s[:mid])
