a=int(input())
b=int(input())
c=int(input())
an=min(a,b,c)
cn=max(a,b,c)
bn=(a+b+c)-cn-an
print(an,bn,cn)