'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''
from  random  import  randint
def   digit():
        return  randint(0 , 9)  #  Any  random  integer  between  0  and  9
def  alpha():
        return  chr(randint(65 , 90))  #  Any  random  alphabet  between  'A'  and   'Z'
for  i  in  range(10): #   10  passwords
        print(alpha() , digit() , alpha() , digit() , alpha() , digit() , sep = '')  #  Each  password  of  6-char  length


'''
What  are  65  and  90 ?  --->  Unicode  values of  'A'  to  'Z'
'''
