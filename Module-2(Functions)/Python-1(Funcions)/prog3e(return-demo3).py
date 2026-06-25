# Find  outputs
def    f1():
        return  10 #  10  is  returned  to  function  call  f1()
        return  20  #  Skipped
        return  30   #  Skipped
# End  of  the  function
print('Begin')  #  Begin
x = f1()  #  Function  returns  10  which  is  assigned  to  'x'
print(x)   #  10
print('End')  #  End
#return   100  # Error :  return is not  permitted  outside  the  function


'''
Begin
10
End



1) return  10 , 20 , 30
    What  is  returned  ?  ---> A  tuple  of  3  elements  i.e. (10 , 20 , 30)

2) return  10
    return  20
    return  30
    What  is  returned ?  --->  Just  10  and  skips  remaining  two  statements  a
	
3) Why  are  statements  following  return  skipped ?  ---> 	 Since  return  statement  moves  the  control  out  of  the  function
'''
