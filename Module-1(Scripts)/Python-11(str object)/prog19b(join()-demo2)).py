#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))  #  Joins  strings  of  list  'a'  with  ':'  to  form   a  string  i.e.  '15:36:48'
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))  #  Joins  strings  of  tuple  'b'  with  ' '  to  form   a  string  i.e.  'Hyd is green city'
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))  #  Joins  strings  of  set  'c'  with  ','  to  form   a  string  i.e.  '10,20,15,25,52'  in  any  order  (as  set  is  unordered)
d = ['www' , 'gmail', 'com']
print('.' . join(d))  #  Joins  strings  of  list  'd'  with  '.'  to  form   a  string  i.e.  'www.gmail.com'
e = [15 , 36 , 48]
#print(':' . join(e))  #  Error :  List  of  integers  can  not  be  joined
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))  #  Joins  strings  of  list  'f'  with  ''  to  form   a  string  i.e.  'SankarDayalSarma'
g = range(5)
#print('-' . join(g)) #  Error :   range  of  integers  can  not  be  joined
