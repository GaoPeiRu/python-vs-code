a = input()
pin_bal = list(map(int, a.split()))
p = pin_bal[0]
b = pin_bal[1]
pos = []
n = 1
while n <= b:
    a =input()
    myList = list(map(int, a.split()))
    pos.append(myList[0])
    pos.append(myList[1])
    n += 1
pins = list(range(1,p+1))
n = 0
for n in range(0,len(pos)-1,2):
    if pos[n+1] > pos[n]:
        dist = list(range(pos[n],pos[n+1]+1))
    elif pos[n+1] < pos[n]:
        dist = list(range(pos[n+1],pos[n]+1))
    else:
        dist =[pos[n]]
    for d in dist:
        if d in pins:
            pins[pins.index(d)] = '.'
for pin in pins:
    if pin == '.':
        continue
    else:
        pins[pins.index(pin)] = 'I'
print(str(pins).replace('[','').replace(']','').replace("'","").replace(",",""))



#n, k = [int(s) for s in input().split()]
#pins = ['I'] * n
#for i in range(k):
  #left, right = [int(s) for s in input().split()]
  #for j in range(left - 1, right):
    #pins[j] = '.'
#print(''.join(pins))