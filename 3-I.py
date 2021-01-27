x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if abs(x2-x1) or abs(y2-y1)==2:
    print("YES")
elif abs(x2-x1) or abs(y2-y1)==1:
    print("YES")
else:
    print("NO")


col = int(input())
row = int(input())
colN = int(input())
rowN = int(input())

if (colN == col + 1 or colN == col - 1) and (rowN == row - 2 or rowN == row + 2):
  print ("YES")
elif (rowN == row + 1 or rowN == row - 1) and (colN == col - 2 or colN == col + 2):
  print ("YES")
else:
  print ("NO")