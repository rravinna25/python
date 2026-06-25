#  replace()  method  demo  program
a = 'Hyd  is  green  city.  Hyd  is  hitec  city.  Hyd  is  his  city'
b = a . replace('is' , 'was') #  Returns  a  string  where  every  'is'  in  object  'a'  is  replaced  with  'was'
print(b)  #  Hyd  was  green  city.  Hyd  was  hitec  city.  Hyd  was  hwas  city
print(a)  #  Hyd  is  green  city.  Hyd  is  hitec  city.  Hyd  is  his  city


'''
replace()  method
---------------------
1) What  does  replace(x , y)  do ?  ---> Returns  a  string  where  every  occurance  of  'x'  is  replaced  with  'y'

2) a . replace(x , y)
    Is  object  'a'  modified ?  --->  No   becoz  str  object  is  immutable

3) a = a . replace(x , y)
    Is  the  statement  valid ?  --->  Yes  and  reference  is  modified  but  not  object
     												  i.e.  Ref  'a'  points  to  the  new  string
'''
