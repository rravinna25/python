'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . __dict__

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 10
	y = 20
	z = 15
#  End  of  the  class
a = {}  #  Empty  dictionary
b = c1 . __dict__  #   All  the  static  variables  of  class  c1  and  Ev's  in  the  form  of  dictionary
for  key  in   b:  #  key  is  each  key  of  dict 'b'
	if  not(key . startswith('__')  and  key . endswith('__')):
		a[key] = b[key]
print('static  variables  of  class  c1 :  '  ,  a)  #  {'x' : 1 , 'y' : 2 , 'z' : 3}


'''
a = {'x' : 1 , 'y' : 2 , 'z' : 3}

b = {'__module__': '__main__', 
        '__firstlineno__': 6, 
		'x': 1,
		'y': 2,
		'z': 3,
		'__static_attributes__': (), 
		'__dict__': <attribute '__dict__' of 'c1' objects>,
		'__weakref__': <attribute '__weakref__' of 'c1' objects>, 
		'__doc__': None}



Iteration            key                         if-condition        a[key]  = b[key]        dictionary  'a'
-------------------------------------------------------------------------------------------------------------
																														{}
      1          '__module__'                       False               Not  executed            {}
      2          '__firstlineno__'                 False               Not  executed            {}
	  3                'x'                                  True                a['x'] = b['x'] = 10    {'x' : 10}
	  4                'y'                                  True                a['y'] = b['y'] = 20    {'x' : 10 , 'y' : 20}
	  5                'z'                                  True                a['z'] = b['z'] = 15    {'x' : 10 , 'y' : 20 , 'z' : 15}
      6          '__static_attributes__'      False               Not  executed          {'x' : 10 , 'y' : 20 , 'z' : 15}
      7              '__dict__'                       False                Not  executed          {'x' : 10 , 'y' : 20 , 'z' : 15}
      8              '__weakref__'                False                Not  executed          {'x' : 10 , 'y' : 20 , 'z' : 15}
      9              '__doc__'                        False                Not  executed          {'x' : 10 , 'y' : 20 , 'z' : 15}
'''
