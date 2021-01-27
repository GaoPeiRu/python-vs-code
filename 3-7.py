a=int(input())
b=a//100%10
c=a//10%10
if a//1000==a%10 and b==c:
    print("YES")
else:
    print("NO")