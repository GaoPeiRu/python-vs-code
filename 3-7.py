a=int(input())
b=a//100%10
c=a//10%10
if a//1000==a%10 and b==c:
    print("YES")
else:
    print("NO")


#x = int(input())
#thousands = x // 1000
#hundreds = x // 100 % 10
#tens = x // 10 % 10
#units = x % 10
#if thousands == units and hundreds == tens:
  #print('YES')
#else:
  #print('NO')