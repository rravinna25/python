# How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno']) #   Value  of  key  'Empno'  i.e. 25
print(a['Ename']) #   Value  of  key  'Ename'  i.e. Rama Rao
print(a['Sal'])  #   Value  of  key  'Sal'  i.e. 1000.65


'''
1) a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
    Is  a['Gender']  valid ?  ---> No  becoz  dictionary  'a'  does  not  have  key  'Gender'
    Is  a[25]  valid ?  --->  No  becoz  dictionary  'a'  does  not  have  key  25

2) What  does  dict[key]  do ?  --->  Returns  value  of  the  key  in  dictionary

3) What  does  dict[value]  do ?  --->  Raises  error
'''
