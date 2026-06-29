#  How  to  print  outputs  in  colors
import   os , time
os . system('color   4')  # Changes  text  color  to  red  (4  is   red)
print('Hyd')  #  Prints  Hyd  in  red  color
time . sleep(5)  #   Executes  next  statement  after  5  sec
os . system('color  2')   # Changes  text  color  to   green  (2  is   green)  i.e.  Modifies  color  of  'Hyd'  to  green
print('Sec')   #  Prints  Sec  in   green  color
time . sleep(5)  #   Executes  next  statement  after  5  sec
os . system('color  1')  # Changes  text  color  to  blue  (1   is  blue)  i.e.  Modifies  color  of  'Hyd'  and  'Sec'  to  blue
print('Cyb')  #  Prints   Cyb  in  blue  color

'''
What  does  color  command  do ?  --->  Changes  text  color

0 = Black
1 = Blue
2 = Green
3 = Aqua
4 = Red
5 = Purple
6 = Yellow
7 = White
8 = Gray
9 = Light Blue
A = Light Green
B = Light Aqua
C = Light Red
D = Light Purple
E = Light Yellow
F = Bright White
'''
