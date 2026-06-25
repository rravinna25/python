# rindex()  method  demo  program  (Home  work)
try:
	a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
	index = a . rindex('is')  #    Index  of  first  'is'  in  object  'a'  from  the  end  of  object  'a'  i.e.  46
	while  True:
		print(index)   #  Index  of   each  'is'   from  the   end  of  object  'a'  i.e.  46  , 42  , 23  ,  4
		index = a .  rindex('is' , 0 , index)     #    Index  of   next   'is'  in  object  'a'  from  index  -  1  downto  0
except:   #  Executed  when  there  is  no  more  'is'
	print('End')


'''
rindex()  method
--------------------
It  is  same  as   rfind()  method  except  that  it  throws  error  but  not  -1  when  string  is  not  found

Note:
1) Which  methods  search  from  left  to  right ?  ---> find()  and  index()  methods
    Which  methods  search  from  right  to  left  ?  ---> 	rfind()  and  rindex()  methods

2) Which  methods  return  -1  when  string  is  not  found ? ---> find()  and  rfind()
     Which  methods  throw  error  when  string  is  not  found ? ---> index()  and  rindex()
'''
