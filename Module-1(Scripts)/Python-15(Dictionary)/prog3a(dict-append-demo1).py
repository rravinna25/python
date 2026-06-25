#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a['Gender'] = 'M'  #  Appends  'Gender' : 'M'  to  dictionary  'a'
a['Married'] = True  #  Appends  'Married' :  True  to  dictionary  'a'
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65,'Gender':'M','Married':True  }


'''
1) dict[valid-key] = value
    What  does  the  statement  do ?  --->  Modifies  value  of  the  key  in  the  dictionary

2) dict[new-key] = value
    What  does  the  statement  do ?  --->  Appends  new  key : value  pair  to  the  dictionary
'''
