a=int(input())
b=int(input())
if a==0:
    print("many solutions")
elif b==0:
    print(b)
elif a!=0:
    c=int(b/a)
    if c!=0:
        print(c)
    elif c==0:
        print("no solution")

