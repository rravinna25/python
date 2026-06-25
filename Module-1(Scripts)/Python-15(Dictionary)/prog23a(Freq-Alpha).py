'''
(Home  work)
Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order
(ignoring  the  case)

Let  input  be   RamA raO
What  is  the  output ?  --->  {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2}  in  alphabetical  order
'''
str = input('Enter  mixed  case  string : ')
str = str . upper()
d = {}
set = set(str)
for  ch  in  sorted(set):
    if  not  ch . isspace():
        d[ch] = str . count(ch)  #  {'A' : 3 , 'M' : 1 , 
print(d)
