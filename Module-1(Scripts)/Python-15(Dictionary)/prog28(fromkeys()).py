# fromkeys()  method  demo  program
tpl = ('R' , 'G' , 'R' , 'B')
a = dict . fromkeys(tpl)  # Converts  tuple  to  dictionary 
print(a)  # {'R' : None , 'G' : None , 'B' : None}
print(type(a))  #   <class  'dict'>
set = {'R' , 'G' , 'R' , 'B'}  
b = dict . fromkeys(set , 25)  # Converts  set  to  dictionary 
print(b) # {'R' : 25 , 'G' :  25 , 'B' :  25}  in  any  order


'''
fromkeys()   method
------------------------
1) What  does  fromkeys(sequence)  do ? --->  Converts  sequence  to  dictionary  and  returns  dictionary

2) What  are  the  keys  of  dictionary ?  --->  Elements  of  sequence  
    What  are  the  values  of  dictionary ?  --->  None's

3) fromkeys(sequence , x)  
    What  are  the  keys  of  dictionary ?  --->  Elements  of  sequence  
    What  are  the  values  of  dictionary ?  --->  x's
											
4) dict . fromkeys(sequence)
    Why  is  fromkeys()  method  called  thru  classname  dict ?  ---> Since  it  is  a  static  method  of  dict  class

5) {10 : 'A' , 20 : 'B'} . fromkeys(sequence)
    Can  fromkeys()  method  be  called  thru  dictionary  object ?  --->  Yes  but  not  recommended
	
6) Every  method  of  dict  class  is  non-static  except  fromkeys()  method
'''
