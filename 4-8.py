n=int(input())
sum=0
for i in range(1,n+1):
    prod=1
    for j in range(1,i+1):
        prod*=j
    sum+=prod
print(sum)


#partial_sum = 0
#current_factorial = 1
#for i in range(1, int(input()) + 1):
  #current_factorial *= i
  #partial_sum += current_factorial
#print(partial_sum)