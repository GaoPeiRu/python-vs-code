a=int(input())
if a%4==0 and a%100!=0:
    print('LEAP')
elif a%400==0:
    print('LEAP')
else:
    print('COMMON')


#year = int(input())

#if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  #print('LEAP')
#else:
  #print('COMMON')