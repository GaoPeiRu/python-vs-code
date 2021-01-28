month=int(input())
day=int(input())
if  month in [1,3,5,7,8,10] and day==31:
    print(month+1,1)
elif month==12 and day==31:
    print(1,1)
elif month==12:
    print(12,day+1)
elif month in [4,6,9,11] and day==30:
    print(month+1,1)
elif month==2 and day==28:
    print(3,1)
else:
    print(month,day+1)