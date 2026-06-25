'''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True = 36.8
ctr = 0 + 1 + 1 + 1 = 3

1) What  is  ctrl + z ?  ---> End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  ---> Throws  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  ---> ctrl + d
'''
try:
	sum =  ctr = 0
	while  True:
		x = eval(input('Enter input  (ctrl + z  to  stop)  :  '))  #   'One'
		sum += x #  sum = 0 + 'One'
		ctr +=1 #  Counts  number  of  inputs
except  EOFError:
	try:
		print(F'Average : {sum / ctr:.2f}')
	except:
		print('Pls  enter  at  least  one  input')
except  NameError , TypeError:
	print('Input  can  not  be  string')