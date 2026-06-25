#  Find  outputs (Home  work)
a = {
		print('Hyd') ,   #  prints  'Hyd'  and  returns  None
		print('Sec') ,  #  prints  'Sec'  and  returns  None
		print('Cyb')   #  prints  'Cyb'  and  returns  None
     }   #  set  of  single  None
print(type(a)) # <class 'set'>
print(a)  # {None}
print(len(a)) #   1

'''
Outputs
---------
Hyd
Sec
Cyb
<class  'set'>
{None}
1
'''


'''
1) {
	  print('Hyd'),
	  print('Sec'),
	  print('Cyb')
    }
    Is  it  a  suite ?  ---> No  due  to  { }

2) What  does  print('Hyd')  do ?   ---> Prints  Hyd  and  Returns  None
     What  does  print('Sec')  do ?  ---> Prints  Sec  and  Returns  None
     What  does  print('Cyb')  do ?   ---> Prints  Cyb  and  Returns  None

3) {
	  print('Hyd'),
	  print('Sec'),
	  print('Cyb')
    }
	Finally  it  is  set  of  a  single  None  as  set  can  not  hold  duplicates
    i.e.  {None , None , None}  --->  {None}

4) a = [
			print('Hyd') ,
			print('Sec') ,
			print('Cyb')
		  ]
    What  is  type(a) ?  ---> <class  'list'>
    What  is  the  result  of  print(a) ?  ---> [None , None , None]

5) a = (
			print('Hyd') ,
			print('Sec') ,
			print('Cyb')
		  )
    What  is  type(a) ?  ---> <class  'tuple'>
    What  is  the  result  of  print(a) ?  ---> (None , None , None)
	
6) a = {
				print('Hyd');
				print('Sec');
				print('Cyb');
		  }
     Is  the  statement  valid ?  ---> No  becoz  suite  can  not  be  in  { }		  
'''
