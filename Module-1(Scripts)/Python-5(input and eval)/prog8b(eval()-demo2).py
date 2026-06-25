# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) #   Converts   "   'hyd'  "  to   'hyd'
hyd = 'Sec'
print(eval('hyd')) #  Converts  'hyd'  to  object  hyd   which  is  'Sec'
sec = '25'
print(eval('sec')) #   Converts  'sec'  to  object   sec  which  is  '25'
print(eval(sec)) #   Converts   object  sec  which  has   '25'  to  integer  25
cyb = 10.8
print(eval('cyb')) #   Converts  'cyb'  to  object   cyb   which  is   10.8
#print(eval(cyb)) #  Error :  cyb  is  neither  a  string  nor  a  str  object


'''
1) hyd = 'Sec'
    print(eval('hyd'))
    What  does  eval('hyd')  do  ?  ---> Converts  'hyd'  to  object  hyd
     How  is  the  print()  reduced  to ?  ---> print(hyd)
     What  does  print(hyd)  do  ?  ---> Prints  value  of  object  hyd  i.e.  'Sec'

2) sec = '25'
    print(eval('sec'))
    What  does  eval('sec')  do  ?   ---> Converts  'sec'  to  object  sec
     How  is  the  print()  reduced  to ?  ---> print(sec)
     What  does  print(sec)  do ?  ---> Prints  value  of  object  sec  i.e.  '25'

3) sec = '25'
    print(eval(sec))
    What  does  eval(sec)  do ?  ---> Converts  object  sec  which  contains  '25'  to  integer  25
     How  is  the  print()  reduced  to ?  ---> print(25)
     What  does  print(25)  do  ?  ---> Prints  25

4) cyb = 10.8
    print(eval('cyb'))
    What  does  eval('cyb')  do ?  ---> Converts  'cyb'  to  object  cyb
    How  is  the  print()  reduced  to ?  --->  print(cyb)
    What  does  print(cyb)  do ?  ---> Prints  value  of  object  cyb  i.e.  10.8

5) cyb = 10.8
    What  is  the  issue  with  eval(cyb)  ?  --->  cyb  is   neither  a  string  nor  a  str  object
'''
