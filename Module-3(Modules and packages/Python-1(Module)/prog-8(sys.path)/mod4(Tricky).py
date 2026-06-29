# Find  outputs
import   sys
print(len(sys . path))  #   6  but  not  7
for  dir   in   sys . path:    #  Executed  6  times
	print(dir)   #  dir  is  each  directory  of  sys.path


'''
1) sairam  directory  which  is   added  to  sys . path  in  mod3(modify-path) . py  is  not  visible  to  current  module

2) In  general, if  sys . path  is  modified  in  a  program, changes  are  not  visible  to  other  programs

3) sys . path  is  reset  to  default  list  for  every  program
'''
