'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  ---> ba**le
'''
a = input('Enter  any  string :  ')  #   Reads  input  string
b = a[0] + a[1:] . replace(a[0] , '*')  #  b = 'b' + 'abble' . replace('b' , '*')  --->  b = 'b' + 'a**le' = 'ba**le'
print('Result :  '  ,  b)


'''
What  does  a[1:]  do ?  --->  String  without  first  character
'''
