#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20)) #  'a'  is  10 , 'b'  is  20 , Result  is   30
print(add('Hyder' , 'abad')) # 'a' is 'Hyder' , 'b' is 'abad' ,  Result  is  'Hyderabad'
print(add(10.8 , 20.6)) # a is  10.8 , b is 20.6 ,  Result  is  31.4
print(add(True , False)) #  'a'  is  True , 'b'  is  False , Result  is   True + False = 1 + 0 = 1
print(add(3 + 4j , 5 + 6j)) #  'a'  is  3 + 4j , 'b'  is  5 + 6j  , Result  is   3 + 4j + 5 + 6j = 8 + 10j
print(add(25 , 10.8)) #  'a'  is   25 , 'b'  is   10.8 , Result  is   25 + 10.8 = 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec'])) # [25 , 10.8 , 'Hyd',True , None , 3+4j , 'Sec']
#print(add(10 , '20')) # Error :  int  and  str  can  not  be  added


'''
1) What  are  the  three  events  in  execution  of  add(10 , 20) ?  --->
	a) Executes  add()  function  and  passes  10  and  20  to  the  function
	b) Copies  10  and  20  to  formal  parameters  'a'  and   'b'
	c) Function  returns  30  which  is  returned  to  the  function  call  add(10 , 20)

2) Finally  add(10 , 20)  is  30

3) int  add(int  a , int  b)
     {
     		return  a +  b;
     }
	 add(10 , 20)  is  30
     What  is  the  drawback  of   'c'  language  function  ?  --->  Only  integers  can  be  passed  to  add()  function  as
																								   'a'  and  'b'  are  integers

4) def   add(a , b):
             return  a + b
    What  is  the  advantage  of  python  function ?  --->  Any  object  can  be  passed  to  the  function
'''
