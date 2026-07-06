# Save  in    cwd \ p1 \ __init__ . py file
__all__  =  ['mod1' , 'mod3']


'''
__all__  list
-----------------
1) What  is  __all__   list ?  --->  List  of  those  modules  of  the  package  which  are  imported  when  *   is  used

2) Where  is  __all__   list  defined ?  --->  In  __init__   module  of  the  package

3) from  package  import   *
    Which  modules  are  imported  ?  --->  Those  modules  which  are   in  __all__  list  of  __init__  module  of  the  package

4) from  package  import   *
    Which  modules  are  imported  without  __all__  list  in  the  package ?  --->																	
																		No  module  would  be  imported  becoz  default  __all__  is  empty  list

5) What  is  the  issue  when  __all__  list  has  an  invalid  module ?  ---> from  package  import  *  raises  an  error

6) import   package
    Which  modules  are  imported ?  --->																		
									No  module  is  imported  becoz  import  statement  imports  package  but  not  modules  of  package

7) from  package  import  mod2
    Which  modules  are  imported  ? --->  Only  mod2  but  not  the  modules  of  __all__  list   becoz  *  is  not  used

8) from  p1 . mod1  import  *
    Which  modules  are  imported  ?  --->  None  becoz  *  indicates  all  the  members  of   p1 . mod1

9) In  general,  when  is  __all__  list  taken  into  consideration ?  --->  When  from  package   import  *   is   used
'''
