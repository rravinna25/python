#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) #[10 , 20 , 30 , 40 , 50]   <space>  Address of list
a[1 : 4] = [60 , 70]   #   Modifies  elements  of  list  from  indexes  1  to  3  to  60 , 70
print(a , id(a)) # [10 , 60 , 70 ,  50]   <space>  Same  address
a[2: 4] = [100 , 200 ,  300]  #   Modifies  elements  of  list  from  indexes   2  to  3  to  100 , 200 , 300
print(a , id(a)) #[10,60,100,200,300]  <space> Same  address


'''
1) a[1 : 4] = [60 , 70]
    Is  new  list  generated  when  list  is  sliced ?  ---> No  becoz  slice  is  made  on  leftside  of  =
	What  happens  when  slice  is  made  on  left  side  of  = ?  --->  Modifies  elements  of  list

2) b = a[1 : 4]
    Is  new  list  generated  when  list  is  sliced ?  ---> Yes  becoz  slice  is  made  on  on  right  side  of  =

3) a[1 : 4] = [60 , 70]
    What  is  the  advantage  of  slice ?  --->	Multiple  elements  of  list  are  modified  in  one  go
'''
