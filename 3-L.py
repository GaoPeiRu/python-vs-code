a=int(input())
b=int(input())
if a==0:
    print("many solutions")
elif b==0:
    print(b)
elif a!=0:
    solution = b//a
    if solution!=0:
        print(solution)
    elif solution==0:
        print("no solution")
