#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) # 25 <4  spaces> 10.927400 <4  spaces> Hyd
print('%i    %g    %s'    %(a , b , c))  # 25 <4  spaces> 10.9274 <4  spaces> Hyd
print('%s    %s    %s'  %(a , b , c)) # 25 <4  spaces> 10.9274 <4  spaces> Hyd
print('%d    %g    %s'  , a , b , c) # %d    %g    %s  <space> 25  <space> 10.9274  <space> Hyd
#print('%d    %g      %s'   a , b , c) # Error :   comma  is  missing  between  the  format  and  objects  (or)  %  is  missing  for  objects   a ,  b,  c
#print('%d    %g    %s'  ,  %(a , b , c)) #Error  due  to  comma
#print('%d    %g    %s'    %a%b%c) #Error due  to  multiple  %'s
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) # 25 <space> 10.927400 <space> Hyd
