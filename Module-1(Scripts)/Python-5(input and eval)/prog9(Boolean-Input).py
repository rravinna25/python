#  Find  outputs  (Home  work)
print(bool('False')) #  True :  'False'  is   a  non-empty  string
print(eval('False')) # converts  'False'  to  False
print(bool('')) #   Converts  ''  to   False
print(eval('  ""  ')) #  Converts  '   ""   '  to   ""  i.e.  Empty  string
#print(eval('')) # Error  :  Converts  ''  to   nothing
print(eval('  " "   '))  #  Converts  '   " "   '  to   " "  i.e.   space
#print(eval(' ')) # Error :  Converts  ' '  to   nothing


'''
1) What  is  the  result  of  eval('  ""  ')  ?   ---> Empty string  i.e.  ""

2) What  is  the  result  of  eval('  " "  ')  ?   ---> Space  i.e.  " "

3) What  is  the  result  of  eval('')  ?   --->  Error  becoz  result  is  nothing

4) What  is  the  result  of  eval(' ')  ?   --->  Error  becoz  result  is  nothing

5) How  to  convert  'False'  to  False ?  ---> eval('False')  but  not  bool('False')
'''
