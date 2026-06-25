# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a)) # Address of  dictionary
a['Sal'] = 2000  #  Modifies  value  of  'Sal'  in  dict  'a'  to  2000
a['Ename'] ='Sita' #  Modifies  value  of  'Ename'  in  dict  'a'  to  'Sita'
a['Empno'] = 35   #  Modifies  value  of  'Empno'  in  dict  'a'  to  35
print(a)   # {'Empno'  :  35,  'Ename'  :  'Sita'  ,  'Sal'  :  2000  }
print(id(a)) # Same address


'''
1) Can  key  be  modified  ?  ---> No  becoz  it  is  immutable

2) Can  value  be  modified ?  --->  Yes  with  dict[key] =  value
'''
