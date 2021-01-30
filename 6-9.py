p=0
z=0
s=0
while True:
  a=int(input())
  if a==0:
    break
  while z<a:
    z=a
    print(z)
    p+=1
    print(p,'***')
    if p==p:
      break
  while z>a:
    print(z)
    p+=1
    if p==p:
      break