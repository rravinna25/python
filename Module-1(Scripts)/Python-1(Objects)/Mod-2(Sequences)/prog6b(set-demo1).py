#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) #  {25 , 10.8 , 'Hyd' , True , 3+4j , None}  in  any  order
print(type(a)) # <class 'set'>
print(len(a)) # 6
#print(a[2]) #  Error  :  set  is  not  indexed
#print(a[1 : 4])  #  Error  : set   can  not  be  sliced
#a[2] = 'Sec'# Error  :  Element  of  set  can  not  be  modified  as there  is  no  index
#print(a * 2) # Error :  set  can  not  be  repeated  due  to  duplicate  elements
#print(a * a) # Error :  sets  can  not  be  multiplied


'''
1) a = {25 , 10.8 , 'Hyd' , True}
    print(a)
	Is  set  printed  in  same  order  every   time  program  is   executed ?  --->  Not  guranteed

2) In  other  words,  order  may  change  from  run  to  run

3) a = {25 , 10.8 , 'Hyd' , True}
    print(a)
    print(a)
    print(a)
	Is  set  printed  in  same  order  all  the  three  times ?  --->  Yes  becoz  it  is  the  same  set  which  is  printed  thrice
'''
