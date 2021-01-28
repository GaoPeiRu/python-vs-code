month=int(input())
day=int(input())
month<13
if month in [1,3,5,7,8,10,12] and day==31:
    print(month+1,1)
elif month in [4,6,9,11] and day==30:
    print(month+1,1)
else:
    print(month,day+1)