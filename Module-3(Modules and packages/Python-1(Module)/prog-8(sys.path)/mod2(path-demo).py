# sys . path  demo   program
import  sys   #  sys . path  list   is  automatically  initialized
print('Original  sys.path')
for  x  in   sys . path:  #   'x'  is  each  directory  of  sys . path
	print(x)
print(len(sys . path))  #  6 :  Six  directories  in  sys . path	
#import  rr  #  ModuleNotFoundError :  All  the  directories  of  sys.path  do  not  have  rr  module


'''
What  are  the  six  directories  of  sys.path ?  --->
1) Current  working  directory
2) python314.zip
3) DLLs
4) Lib
5) Python314
6) site-packages
'''