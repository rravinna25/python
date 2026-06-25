# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():  # k  and  v  are  elements  of  each  tuple  in  the  list  of  dict_items  object
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')  #   Dictionary  of  4  key : value  pairs  is  passed  to  the  function
f1()  #  Empty  dictionary  is  passed  to  the   function



'''
Results
Empno...25
Empname...Rama  Rao
Salary...10000.0
Gender...m
Results
'''
