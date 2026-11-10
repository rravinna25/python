#  Difference  between  init()    and  __init__()   methods (Home  work)
class c1:
    def  __init__(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')
        self . x = 30
        self . y = 40
a = c1() #  Constructor  initializes  object  with  x = 10 , y = 20
print(a . __dict__) # {'x' : 10 , 'y' : 20}
b = c2()  #  Empty  object
print(b . __dict__) # { }
b . init()  #  Method  initializes  object  with  x = 30 , y = 40
print(b . __dict__) # {'x' : 30 , 'y' : 40}


'''
Object  'a'  --->  x = 10 , y = 20 

Object  'b'  ---> x = 30 , y = 40
'''


'''
1) Is  method  init()  executed  automatically  ?  ---> No  and  it  needs  to  be  called  explicitly

2) What  is  the  advantage  of  constructor ?  --->  It  is  automatically  executed  as  soon  as   object  is  created

3) What  is  recommended  for  object  initialization  and  why ?  --->  Constructor  due  to  automatic  initialization
'''
