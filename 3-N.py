x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
x3=int(input())
y3=int(input())
x4=0
y4=0
if x1==x2 or x1==x3:
    if x1==x2:
        x4=x3
    else:
        x4=x2
else:
    x4=x1
if y1==y2 or y1==y3:
    if y1==y2:
        y4=y3
    else:
        y4=y2
else:
    y4=y1