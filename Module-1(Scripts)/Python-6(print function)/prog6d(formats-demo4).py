# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)  #    <4  spaces>Hyd
print('%-7s'  %a)  #   Hyd <4 spaces>
print('%2s'  %a)  #   Hyd  and  ignores  smaller  width  2
print('%s'  %a) #    Hyd
print('%s' , a) #  %s  <space>  Hyd
#print('%s'  a) # Error : Either  comma is  missing  between  %s  and  object  'a'   (or)   %  is  missing  for  object  'a'
#print('%s' , %a) # Error due to comma
print(a) #Hyd


'''
1) What  is   the  difference  between  %7s   and  %-7s ? ---> %7s  is  string  in  a  width  of  7  characters  with  leading  spaces
																												and
																							      %-7s  is   string  in   a  width  of  7  characters  with  trailing  spaces

2) What  happens  when  the  width  is  smaller ? ---> Ignores  smaller  width  and  prints  whole  string  
'''
