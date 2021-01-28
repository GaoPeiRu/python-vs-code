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