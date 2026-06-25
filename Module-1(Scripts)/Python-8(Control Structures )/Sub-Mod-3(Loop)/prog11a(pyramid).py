'''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>***
<2  spaces>*****
<1  space>*******
<0  spaces>*********

Input  is  number  of  lines
'''
n = int(input("Enter number of lines: "))  
s = n - 1  #  Number  of  spaces  in  1st  line
for i in range(1 , n + 1):    #  Prints  'n'  lines
    print(' ' * s , end = '')  #  's'  spaces  <same  line>
    print('*' * (2 * i - 1))  #   (2 * i - 1)   *'s  <next  line>
    s -= 1  #  Reduces  number  of  spaces  by   1
