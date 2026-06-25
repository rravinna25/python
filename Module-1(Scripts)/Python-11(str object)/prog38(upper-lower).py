'''
Count  number  of  special   chars  i.e.  Both  upper  and  lower
 
Input :  AbcadBED
 
output : 3
'''
s = input('Enter String : ')
count = 0
for ch in set(s.lower()):  
    if ch.lower() in s and ch.upper() in s:
        count += 1 
print(count)