x = int(input())
t_n = 1
t_prev =1
fib=[1,1]
n = 1
while t_n < x:
  t_n = fib[-1] + fib[-2]
  fib.append(t_n)
  n = n + 1
if t_n == x:
  print(fib.index(fib[-1])+1)
else:
  print(-1)


#prev, next = 1, 1
#index = 2
#possible_fib = int(input())
#while possible_fib > next:
  #prev, next = next, prev + next
  #index += 1
#if possible_fib == next:
  #print(index)
#else:
  #print(-1)