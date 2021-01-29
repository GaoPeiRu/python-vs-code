a=input()
exp1 =a.find('h')
exp2 =a.rfind('h')
print(a[:exp1] + a[exp2:exp1:-1] + a[exp2:])


#s = input()
#first_pos, last_pos = s.find('h') + 1, s.rfind('h')
#left, middle, right = s[:first_pos], s[first_pos:last_pos], s[last_pos:]
#print(left + middle[::-1] + right)