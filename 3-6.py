a=int(input())
b=a//100
c=a//10%10
d=a%10
if b<c<d:
    print("YES")
else:
    print("No")