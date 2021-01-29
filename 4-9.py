answer=0
N=int(input())
N_org=N 
for i in range(N-1):
  N=int(input())
  answer+=N
for i in range(N_org):
  N_org+=i
  i+=N
N_org-=answer
print(N_org)


#n = int(input())

#cards_sum = 0
#for i in range(1, n + 1):
  #cards_sum += i

#for i in range(n - 1):
  #cards_sum -= int(input())

#print(cards_sum)