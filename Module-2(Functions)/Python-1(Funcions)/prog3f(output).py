#  Find  outputs
#f1() # Error :  Function  f1()  is  not  yet  defined
def   f1():
        print('Hello')
print(f1()) #  f1  function  prints  Hello  and   returns  None  by  default
print(f1) # Type and address of function f1()

'''
Hello
None
Type  and  address  of  function  f1



1) Can  a  function  be  called  before  it  is  defined  ?  ---> No

2) In  other  words,  define  the  function  first  and  then  call  the  function

3) print(f1())
    print(f1)
	What  is  the   difference  between  the  two  statements ?  --->
												print(f1())  executes  f1()  function  and  prints  the  result  of  f1()  function
												but  print(f1)  prints  type  and  address  of  function  f1
'''
