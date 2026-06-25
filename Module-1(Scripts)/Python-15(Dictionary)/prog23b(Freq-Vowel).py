'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}
'''
s = input('Enter String:') #   Reads  a  string
s = s . upper()  #  Returns  uppercase  string
vowels = 'AEIOU'  #  String  of  vowels
a = {}  #  Empty  dictionary
for  v  in  vowels:  #   v  is  each  vowel  of  string  vowels
    ctr = s . count(v)  #  Number  of  times  'v'  is  in  string
    if  ctr  > 0:
        a[v] = ctr  #  Appends  v :  ctr  to  dict  'a'  when  ctr > 0
print(a)
