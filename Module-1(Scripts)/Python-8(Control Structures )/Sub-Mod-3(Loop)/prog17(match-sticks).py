'''
Gift

There  are  21  matchsticks.
User  can  pick  1 , 2 , 3  or  4  matchsticks.
Computer  picks  after  user  and  whoever  picks  the  last  matchstick, they  lose  the  game.
Write  a  program  such  that  computer  wins

Logic:  Total  should  be  5

Hint: Use while  loop

								n = 21
   Iteration     user         computer             n
-------------------------------------------------------------
          1             4                 1                     n = 21 - 5 = 16   
          
		  2             2                 3                    n = 16 - 5 = 11
		  
		  3             1                  4                   n = 11 - 5 = 6
		  
		  4             3                  2                   n = 6 - 5 = 1
		  
		  5             1                  ----                     -----
---------------------------------------------------------------
'''
n = 21
while  n > 1:
	pick = int(input('How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  '))  #   0
	while  pick < 1  or  pick > 4:
		pick = int(input('Input  can  not  be >  4  nor  <  1,  Reenter  :  '))			#   3
	# End  of  inner  loop
	print(F'Computer  picks  {5 - pick}  matchsticks')
	n = n - 5  #  1
# End  of  while  loop	
print('You  have  lost  the  game  and  Computer  wins')
