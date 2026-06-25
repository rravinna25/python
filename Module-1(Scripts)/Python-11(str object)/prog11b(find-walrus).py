# Same  as  prog11a  but  walrus  operator  is  used
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = -1  #  Initial  value
while  (index :=  a . find('is' , index + 1))  !=  -1:  #  Execute  loop  until  'is'  is  not  found
	print(index)  #   4  <next  line>  23   <next  line>  42  <next  line>   46  <next  line>
print('End')  #  End  <next  line>



'''
while   index  :=   a . find('is' , index + 1)   !=   -1:
What  is  the  issue  without  () ? --->  Executes  !=  before  :=   due  to  higher  priority  which  leads  to  infinite  loop
What  is  printed ?  --->  True  infinite  times
'''
