#  Find  output  (Home  work)
print(eval('print("Hyd")'))   #  print(print("Hyd"))  --->  print(None)  --->  None

'''
Hyd
None
'''

'''
1) print(eval('print("Hyd")'))
    What  does  eval()  function  do ?  ---> Converts  'print("Hyd")'  to  statement  print("Hyd")

2) print(eval('print("Hyd")'))
    How  is  the  statement  reduced  to ?  ---> print(print("Hyd"))

3) print(print("Hyd"))
    What  does   inner  print()  function  do ?  ---> Prints   Hyd  and  returns  None

4) print(print("Hyd"))
    How  is  the  statement  further  reduced  to ?  ---> print(None)

5) What  does  print(None)  do ?  --->  Prints  None  and  returns  None  which  gets  ignored
'''
