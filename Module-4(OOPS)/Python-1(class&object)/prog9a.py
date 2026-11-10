'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   student:
	def   get(self):  #  self  is  object  's'
		self . rno = int(input('Enter  roll  number : ')) #  Adds  variable  rno  to  object  's'  with  user  input
		self . sname = input('Enter  student  name :  ')  #  Adds  variable  sname  to  object  's'  with  user  input
		self . gender = input(('Enter  gender (m/f) : '))   #  Adds  variable  gender  to  object  's'  with  user  input
		self . m = []  #  Adds  empty  list   'm'   to  object  's'
		for  i  in  range(3):  #  Marks  of  3  subjects
			marks = int(input(F'Enter  marks  of  subject  {i + 1}  :  '))  #  Reads  input  to  local  variable
			self . m . append(marks)  #  Appends  value  of  Lv  to  list  s . m
	def   compute(self):  #  self  is  object  's'
		self . tot = sum(self . m)  #  Adds  variable  tot  to  object  's'  with  sum  of  marks
		self . avg = self . tot / 3  #  Adds  variable  avg  to  object  's'  with  average  marks
		if  min(self . m) < 40:   #  At  least  one  subject  is  below  40  marks
				self . grade = 'Fail'  #  Adds  variable  grade  to  object  's'  with  'Fail'
		elif  self . avg >= 70:
				self . grade = 'Distinction'  #  Adds  variable  grade  to  object  's'  with  'Distinction'
		elif  self . avg >= 60:
				self . grade = 'First  class'  #  Adds  variable  grade  to  object  's'  with  'First  class'
		elif  self . avg  >= 50:
				self . grade = 'Second  class'   #  Adds  variable  grade  to  object  's'  with  'Second  class'
		else:
				self . grade = 'Third  class'   #  Adds  variable  grade  to  object  's'  with  'Third  class'
	def  disp(self):  #  self  is  object  's'
		print('Roll  Number  :  ' ,  self . rno)
		print('Student  Name  :  ' , self . sname)
		print('Gender  :  ' ,  self . gender)
		print('Total  Marks  :  ' , self . tot)
		print(F'Average  :  {self . avg:.2f}')
		print('Grade  :  ' , self . grade)	
	def   __str__(self):
		return  F'{self . rno}  \t {self . sname}  \t  {self . gender}  \t  {self . tot}  \t  {self . avg:.2f}  \t  {self . grade}'  #  Concatenates  all  the  value  of  object  self  to  form  a  string	
#End  of  the  class
if  __name__  ==  '__main__':
	s = student() #  Creates  an  empty  student class object
	s . get() #   Reads  inputs  to  object  's'
	s . compute()  #  Stores  results  in  object  's'
	s . disp()  #  Prints  values  of  object  's'
	print(s)  #  Executes  __str__()  method  of  student  class  which  returns  all  the  values  of  object  's'  in  the  form  of  string


#  Object  's'  --->  rno = 25 , sname = 'Rama Rao' , gender = 'm' , m = [52 , 48 , 55] , total = 155 , average = 51.66 , grade = '2nd  class'


'''
Can  Fail  be  handled  at  the  end ?  --->  No  and  it  should  be  handled  only  at  the  begining
'''
