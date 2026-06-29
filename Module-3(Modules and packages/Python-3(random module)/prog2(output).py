from  random  import  *
print(random())  #  0.5 : Any  random number between  0 (excluded)   and  1(excluded) 
print(randint(1 , 100)) #  58 :  Any  random  integer  number between  1 (included)   and  100(included) 
print(uniform(1 , 100))  #  72.689 :  Any  random  float   number between  1 (excluded)   and  100(excluded)  
print(randrange(10))  #  5 : Any  random  integer  number between  0 (included)   and   9(included)
print(randrange(1 , 11))  #  8 : Any  random  integer  number between  1 (included)   and  10(included)  
print(randrange(1 , 11 , 2))  #  3 : Any  random  integer  number between  1 (included)   and  10(included)   in  steps  of   2 
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))  #  15 : Any  random  element  of  list
print(choice('RAJESH')) #  J : Any  random  char  of   string  
set  =  {10 , 20 , 30 , 40}
#print(choice(set))   #   Error :  set   is  not  indexed



'''
choice()  function  internally  uses  indexes  but  set  and  dictionary  are  not  indexed
'''
